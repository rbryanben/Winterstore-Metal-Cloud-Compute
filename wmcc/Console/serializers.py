from rest_framework import serializers
from .models import *

class InstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instance
        fields = ['instance_name', 'type', 'ip', 'booted', 'os']