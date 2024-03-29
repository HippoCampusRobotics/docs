Pre-Boot Configuration
######################



#. Flash an Raspbian Buster image to an SD card with the tool of your choice (for example `Raspberry Pi Imager <https://www.raspberrypi.org/downloads/>`_).

   .. note:: Experimental `64bit images <https://downloads.raspberrypi.org/raspios_arm64/images/>`_ seem to work with Arducam and have the advantage that ROS can be installed via :code:`apt`. No need to build ROS from source! Use ROS Noetic in this case.

#. Do not eject the SD card yet. Download the :download:`Boot partition files <https://gist.github.com/lennartalff/5cf69169edcca7bc6bfc7909a567f67d>` and move them to the :file:`boot` partition of the SD card.

   ssh
      Empty file that enables the SSH server on the Raspberry Pi.
   config.txt
      Added some lines to enable the serial console, camera, etc.
   wpa_supplicant.conf
      Configuration file for setting up Wifi. Modify or complement, if your Wifi setup requires it.

.. attention:: Please replace the password in the :file:`wpa_supplicant.conf` with the correct one!

To enable output during boot process if connected via serial console, disable using a splash screen via the Plymouth module, by editing :file:`boot/cmdline.txt`. Remove :code:`splash` and :code:`plymouth.ignore-serial-consoles`.

Also change your hostname before the first boot, by editing :file:`etc/hosts` and :file:`etc/hostname` on the :file:`rootfs` partition of the SD card. Replace the default hostname :file:`raspberrypi` with the new hostname.
Naming scheme is :file:`hippo-main-nn` for the Raspberry Pi connected with the FCU and :file:`hippo-buddy-nn` if it is the secondary Raspberry Pi. Replace :file:`nn` by a two digit long number with leading zero.
