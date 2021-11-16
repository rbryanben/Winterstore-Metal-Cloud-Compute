from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from virtual_engine.engine import *
import virtualbox
from .serializers import InstanceSerializer
import json
import threading
# Required for channel communication
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

# Returns the frontend application
def Application(request):
    # render template
    return render(request, 'Console.html')


# takes in a request and extracts json values server_name,username and password from the body 
# and returns an http response of 200 if successful and 400 if not
@csrf_exempt
def createInstance(request):
    # get json values
    received_json_data = json.loads(request.body)

    #extract values 
    server_name = received_json_data['server_name']

    #add instance
    new_instance = Instance()
    new_instance.create(server_name,"cloud","password25")

    #create instance in a new thread
    createInstance = threading.Thread(target=createUbuntuLTS2010Instance,args=(f"cloud_{server_name}",))
    createInstance.start()
    
    # return http response
    return HttpResponse("200")


"""
    Returns a list of instances that belong to a user
"""
def getInstances(request):
    #instances 
    instances = Instance.objects.all()
    #serialize 
    instancesSerialized = InstanceSerializer(instances,many=True)

    return JsonResponse(instancesSerialized.data,safe=False)

"""
    Handles requests from virtual machines and assigns them
"""
def handleServerNotification(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    # update server
    servers = Instance.objects.filter(booted=False)[0]
    servers.booted = True
    servers.ip = ip
    servers.save()

    #notify client thier server has booted
    send_channel_message("session_cloud","server-booted")

    return HttpResponse(status=200)

"""
    Sends a message to the client
"""
def send_channel_message(group_name, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        '{}'.format(group_name),
        {
            'type': 'control_message',
            'message': message
        }
    )