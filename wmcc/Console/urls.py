from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Application), #Login Control
    path('createInstance', views.createInstance), #Create Instance
    path('getInstances',views.getInstances), #Get Instances
    path('notifyBooted',views.handleServerNotification), #Notifications from Server
]
