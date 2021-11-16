from django.db import models

# Create your models here.
class Instance(models.Model):
    instance_name = models.TextField()
    os = models.TextField(default="Ubuntu Server 20.04 LTS")
    ip = models.TextField(default="Setting Up")
    type = models.TextField(default="E1 Kalahari")
    username = models.TextField()
    password = models.TextField()
    booted = models.BooleanField(default=False)

    def create(self,instance_name,username,password):
        self.instance_name = instance_name
        self.username = username
        self.password = password
        self.save()