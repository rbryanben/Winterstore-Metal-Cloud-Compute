import subprocess
import os as operating_system
import time 
import virtualbox

def createUbuntuLTS2010Instance(instance_name):    
    #create instance
    cloneCommand=f"VBoxManage clonevm ubuntu --name={instance_name} --register"
    p = subprocess.Popen(cloneCommand, shell=False, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    
    #change the mac address of the instance
    macAddressChangerCommand  = f'VBoxManage modifyvm {instance_name} --macaddress1 auto'
    changeMac = p = subprocess.Popen(macAddressChangerCommand, shell=False,stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()
    

    #change the mac address of the instance
    startInstanceCommand  = f'VBoxManage startvm {instance_name} --type headless'
    startInstance = p = subprocess.Popen(startInstanceCommand, shell=False,stdin = subprocess.PIPE, stdout = subprocess.PIPE)
    stdout, stderr = p.communicate()

    return


