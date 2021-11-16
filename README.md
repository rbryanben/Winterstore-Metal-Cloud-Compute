# Winterstore-Metal-Cloud-Compute
Metal as a Service that allows user to rent virtual computers on which to run their own computer applications. Based on a Type 2 Hypervisor on the road to Type 1 Bare Metal

# Road To Bare Metal
Popular MaaS providers like AWS and Google Cloud do not use a type 2 hypervisor to run guest operating systems. 
They use Type 1 hypervisors like Xen Hypervisor-Citrix Project to give bare metal perfomance. This repo is the journey to building a MaaS that is based on a Type 1 Hypervisor Xen
, and our first stop is a MaaS platform that is based on a Type 2 hypervisor (VirtualBox) just to get the concept straight.

# Lets See It Work!
https://user-images.githubusercontent.com/63599157/142004581-757f4706-1920-4b0e-bfb0-baf30841175f.mp4
Above starts off by showing existing instances that have Nginx installed. From there we on to create a new virtual instance called "Github".
36 seconds pass and we get the internal IP of the newly spinned up instance. We then test the ip on Chrome, to which we get no response since 
there is nothing of ours installed on the server. We open Putty(SSH Client), paste the IP of the instance and then log into the instance via SSH.
We install Nginx on the instance, and then go back to test out the IP on Chrome. To which we are greeted with the Nginx boiler plate template. Success!
