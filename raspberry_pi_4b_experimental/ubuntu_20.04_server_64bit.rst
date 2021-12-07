Ubuntu 20.04 Server 64bit
#########################

.. todo:: Probably the Arducam OV9281 is not compatible with Ubuntu.

Modify Cloud-Init
=================

Modify :file:`user-data` on the :file:`system-boot` partition to your liking. An example configuration is provided below:

.. code-block:: yaml
   :caption: user-data

   #cloud-config
   
   hostname: hippo-main-04
   manage_etc_hosts: true
   locale: en_US.UTF-8
   timezone: Europe/Berlin
   
   users:
       - name: pi
         groups: sudo, dialout, video
         sudo: "ALL=(ALL) NOPASSWD:ALL"
         # false -> allow password login
         lock_passwd: false
         shell: /bin/bash
         plain_text_passwd: "hippocampus"
         ssh_authorized_keys:
         - ssh-ed25519    AAAAC3NzaC1lZDI1NTE5AAAAIF0xs6V9Lp2xzh/+hs+S919KpwAj9VHWO5NeHEuTYTpQ thies.lennart.alff@tuhh.de
   
   # allow password ssh login
   ssh_pwauth: true

   power_state: 
       mode: reboot
       delay: now
       condition: True


Modify User Config
==================

.. code-block:: sh
   :caption: usercfg.txt

   dtoverlay=uart4
   dtoverlay=uart5
   enable_uart=1
   start_x=1
   gpu_mem=256
   dtparam=i2c_vc=on

Install Avahi
=============

Boot the system l and install avahi to resolve hostnames.

.. code-block:: sh

   sudo apt install avahi-daemon




   
   