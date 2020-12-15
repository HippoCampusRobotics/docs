Raspberry Pi 4B Setup
#####################

Pre-Boot Configuration
======================
#. Flash an Raspbian Buster image to an SD card with the tool of your choice (for example `Raspberry Pi Imager <https://www.raspberrypi.org/downloads/>`_).

#. Do not eject the SD card yet. Download the :download:`Boot partition files <https://gist.github.com/lennartalff/5cf69169edcca7bc6bfc7909a567f67d>` and move them to the :file:`boot` partition of the SD card.

   ssh
      Empty file that enables the SSH server on the Raspberry Pi.
   cmdline.txt
      Removed :code:`plymouth.ignore-serial-consoles` to enable output during boot process if connected via serial console.
   config.txt
      Added some lines to enable the serial console, camera, etc.
   wpa_supplicant.conf
      Configuration file for setting up Wifi. Modify or complement, if your Wifi setup requires it.

.. attention:: Please replace the password in the :file:`wpa_supplicant.conf` with the correct one!

Also change your hostname before the first boot, by editing :file:`etc/hosts` and :file:`etc/hostname` on the :file:`rootfs` partition of the SD card. Replace the default hostname :file:`raspberrypi` with the new hostname.

Naming scheme is :file:`hippo-main-nn` for the Raspberry Pi connected with the FCU and :file:`hippo-buddy-nn` if it is the secondary Raspberry Pi. Replace :file:`nn` by a two digit long number with leading zero.

System Configuration
====================

Insert SD card into Raspberry Pi. If your network is configured appropriately you can SSH into the Raspberry Pi. Otherwise connect your computer with the TX/RX pins of the Raspberry Pi via an USB-serial-converter.

Login with default credentials, i.e. :code:`pi:raspberry`. Change the password by typing :code:`passwd`.

Perform a system update:

.. code-block:: bash

   sudo apt update && sudo apt upgrade -y

Reboot the Pi.

.. code-block:: bash

   sudo reboot

ROS Installation
================

In general you can follow the official instruction in the `ROS wiki <http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi>`_ to install ROS under Raspbian Buster on the Raspberry Pi. But the following instructions will use :code:`catkin` instead of :code:`catkin_make` or :code:`catkin_make_isolated`. 

Preparations
************

#. Adding keys

   .. code-block:: bash
        
      sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

   .. code-block:: bash

      sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

#. Update source lists

   .. code-block:: sh

      sudo apt update

#. Install dependencies

   .. code-block:: bash

      sudo apt install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake python-catkin-tools

#. Initialize rosdep

   .. code-block:: bash

      sudo rosdep init

   .. code-block:: bash

      rosdep update

Setup Workspace
***************

#. Create workspace

   .. code-block:: bash

      mkdir ~/ros_catkin_ws && cd ~/ros_catkin_ws

#. Fetch source code

   .. attention:: The following commands will fetch the sources for the :code:`ros_comm` meta package and the :code:`perception` meta package. If you do not need all of them or if you need even more packages feel free to modify the following commands accordingly. Building unnecessary packages might be a waste of time.
   
   .. code-block:: bash

      rosinstall_generator ros_comm perception --rosdistro melodic --deps --wet-only --tar > melodic-ros_comm-perception-wet.rosinstall

   .. code-block:: bash

      wstool init src melodic-ros_comm-perception-wet.rosinstall


#. Resolve dependencies

   .. code-block:: bash

      rosdep install -y --from-paths src --ignore-src --rosdistro melodic -r --os=debian:buster

Build the Code
**************

#. Set the install space

   .. code-block:: bash

      catkin config --install-space /opt/ros/melodic

#. Use the :code:`install` configuration instead of :code:`devel`

   .. code-block:: bash

      catkin config --install

#. Start the build process

   .. note:: Depending on your package configuration the next command may take some time, i.e. a few hours if you want to build many packages.

   .. code-block:: bash

      sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release

Initialize User Workspace
*************************

#. Source your ROS installation

   .. tabs::

      .. code-tab:: sh zsh

         source /opt/ros/melodic/setup.zsh

      .. code-tab:: sh bash

         source /opt/ros/melodic/setup.bash


#. Create workspace

   .. code-block:: sh

      mkdir -p ~/catkin_ws/src && cd ~/catkin_ws

#. Initialize workspace

   .. code-block:: sh

      catkin init

#. Build empty workspace

   .. code-block:: sh

      catkin build


This command created the devel directory inside your catkin workspace. To source your workspace you can either source it manually for each terminal session by executing :code:`source ~/catkin_ws/devel/setup.bash`. A better way to handle this automatically is to append this command to your :file:`.bashrc` file.

.. tabs::

   .. code-tab:: sh zsh

      echo 'source $HOME/catkin_ws/devel/setup.zsh' >> ~/.zshrc
   
   .. code-tab:: sh bash
      
      echo 'source $HOME/catkin_ws/devel/setup.bash' >> ~/.bashrc

For this change of the :file:`.bashrc` to take effect immediately execute:

.. tabs::

   .. code-tab:: sh zsh

      source ~/.zshrc

   .. code-tab:: sh bash

      source ~/.bashrc

ROS Network
***********

   .. tabs:: 

      .. tab:: hippo-main

         .. tabs::

            .. code-tab:: sh zsh

               echo 'export ROS_MASTER_URI="http://$(hostname --short).local:11311"' >> ~/.zshrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.zshrc

            .. code-tab:: sh bash

               echo 'export ROS_MASTER_URI="http://$(hostname --short).local:11311"' >> ~/.bashrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.bashrc

      .. tab:: hippo-buddy

         .. attention:: Replace the number for hippo-main with the actual one.

         .. tabs::

            .. code-tab:: sh zsh

               HIPPO_MAIN="hippo-main-01"
               echo "export ROS_MASTER_URI=\"http://$HIPPO_MAIN.local:11311\"" >> ~/.zshrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.zshrc

            .. code-tab:: sh bash

               HIPPO_MAIN="hippo-main-01"
               echo "export ROS_MASTER_URI=\"http://$HIPPO_MAIN.local:11311\"" >> ~/.bashrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.bashrc



Install ROS Packages
====================

If you want to install a new package, for example :file:`apriltag_ros` you can generate a new :file:`.rosinstall` file and merge it with your current workspace with :code:`wstool`.

#. Change directory

   .. code-block:: sh

      cd ~/ros_catkin_ws

#. New :file:`.rosinstall` file

   .. code-block:: sh

      rosinstall_generator apriltag apriltag_ros > apriltag_ros.rosinstall

#. Merge

   .. code-block:: sh

      wstool merge -t src apriltag_ros.rosinstall

#. Update

   .. code-block:: sh

      wstool update -t src

#. Install dependencies

   .. code-block:: sh

      rosdep install -y --from-paths src --ignore-src -r

#. Build

   .. code-block:: sh

      sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release

Camera
======

If the Raspberry Pi uses an OV9281 camera, you will have to install the MIPI camera library by Arducam.

.. code-block:: sh

   git clone https://github.com/ArduCAM/MIPI_Camera.git

.. code-block:: sh

   cd ~/MIPI_Camera/RPI && make install

Configure UART
==============

We have made the decision, to use UART5 for the telemetry communication with the FCU and UART4 is connected to the debug port of the FCU.

To keep things simple, you can create a UDEV rule to create more meaningful names than the default :file:`ttyAMAx` naming convention.

First of all identify your KERNELS value for UART4 and UART5 by the following command:

.. code-block:: sh

   udevadm info --name=/dev/ttyAMA1 --attribute-walk


.. code-block:: sh
   :linenos:

   looking at device '/devices/platform/soc/fe201800.serial/tty/ttyAMA1':
   KERNEL=="ttyAMA1"
   SUBSYSTEM=="tty"
   DRIVER==""

   looking at parent device '/devices/ platform/soc/fe201800.serial':
   KERNELS=="fe201800.serial"
   SUBSYSTEMS=="amba"
   DRIVERS=="uart-pl011"
   ATTRS{driver_override}=="(null)"
   ATTRS{id}=="00241011"
   ATTRS{irq0}=="14"

   looking at parent device '/devices/ platform/soc':
   KERNELS=="soc"
   SUBSYSTEMS=="platform"
   DRIVERS==""
   ATTRS{driver_override}=="(null)"

   looking at parent device '/devices/ platform':
   KERNELS=="platform"
   SUBSYSTEMS==""
   DRIVERS==""

.. attention:: The :file:`ttyAMAx` number is not specific for the UART device and depends on how many UARTs are activated. 

* Debug Port
   UART4

   .. code-block:: sh

      Tx/Rx <-> GPIO8/GPIO9 (KERNELS=="fe201800.serial")

* Telemetry
   UART5

   .. code-block:: sh

      Tx/Rx <-> GPIO12/GPIO13 (KERNELS=="fe201a00.serial")

The resulting UDEV rule in :file:`/etc/udev/rules.d/50-serial.rules` is:

.. code-block:: sh
   :linenos:

   KERNEL=="ttyAMA[0-9]*", GROUP="dialout", ENV{MOTOR_SERIAL}="fcu_serial"

   ENV{MOTOR_SERIAL}=="fcu_serial",  SUBSYSTEM=="tty", KERNELS=="fe201800.serial", SYMLINK+="fcu_debug"
   ENV{MOTOR_SERIAL}=="fcu_serial",  SUBSYSTEM=="tty", KERNELS=="fe201a00.serial", SYMLINK+="fcu_tele"

You can apply these changes by

.. code-block:: sh

   sudo udevadm control --reload-rules && sudo udevadm trigger

To check, that the rule is applied correctly, you can execute

.. code-block:: sh

   ls /dev/fcu* -l

The output should show symbolic links for the serial devices:

.. code-block:: sh

   lrwxrwxrwx 1 root root 7 Dec 11 14:57 /dev/fcu_debug -> ttyAMA1               
   lrwxrwxrwx 1 root root 7 Dec 11 14:57 /dev/fcu_tele -> ttyAMA2 

.. note:: The :file:`ttyAMA` numbers might differ.


Ethernet Configuration
======================

The Raspberry Pis are connected with each other via Ethernet. To have a flexible solution, we define a fallback profile in :file:`/etc/dhcpcd.conf`. So in case you connect the Raspberry Pi directly to the Router, it uses DHCP. If no DHCP server is available, the Raspberry Pis use the static IP address defined in the fallback profile.

Either uncomment the existing lines or add them, so :file:`dhcpcd.conf` contains the following:

.. tabs:: 

   .. code-tab:: sh hippo-main

      # It is possible to fall back to a static IP if DHCP fails:
      # define static profile
      profile static_eth0
      static ip_address=10.0.0.1/24

      # fallback to static profile on eth0
      interface eth0
      fallback static_eth0


   .. code-tab:: sh hippo-buddy

      # It is possible to fall back to a static IP if DHCP fails:
      # define static profile
      profile static_eth0
      static ip_address=10.0.0.2/24

      # fallback to static profile on eth0
      interface eth0
      fallback static_eth0

You might want to restart the Raspberry Pis.
