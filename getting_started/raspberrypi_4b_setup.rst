Raspberry Pi 4B Setup
#####################

Pre-Boot Configuration
**********************
#. Flash an Raspbian Buster image to an SD card with the tool of your choice (for example `Raspberry Pi Imager <https://www.raspberrypi.org/downloads/>`_).

#. Do not eject the SD card yet. Download the :download:`Boot partition files <https://gist.github.com/lennartalff/5cf69169edcca7bc6bfc7909a567f67d/archive/97462d0b6cd6a0e98dcd437f9db0c2aa28134702.zip>` and move them to the :file:`boot` partition of the SD card.

   ssh
      Empty file that enables the SSH server on the Raspberry Pi.
   cmdline.txt
      Removed :code:`plymouth.ignore-serial-consoles` to enable output during boot process if connected via serial console.
   config.txt
      Added some lines to enable the serial console, camera, etc.
   wpa_supplicant.conf
      Configuration file for setting up Wifi. Modify or complement if your Wifi setup requires it.

System Configuration
********************

Insert SD card into Raspberry Pi. If your network is configured appropriately you can SSH into the Raspberry Pi. Otherwise connect your computer with the TX/RX pins of the Raspberry Pi via an USB-serial-converter.

Login with default credentials, i.e. :code:`pi:raspberry`. Change the hostname via :code:`sudo raspi-config` to a meaningful and unique one to avoid hostname resolution conflicts, for instance :code:`visionmodule01`. Also change the password by typing :code:`passwd`.

Perform a system update:

.. code-block:: bash

   sudo apt update && sudo apt upgrade -y

Reboot the Pi.

.. code-block:: bash

   sudo reboot

ROS Installation
****************

In general you can follow the official instruction in the `ROS wiki <http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi>`_ to install ROS under Raspbian Buster on the Raspberry Pi. But the following instructions will use :code:`catkin` instead of :code:`catkin_make` or :code:`catkin_make_isolated`. 

Preparations
============

#. Adding keys

   .. code-block:: bash
        
      sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

   .. code-block:: bash

      sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

#. Install dependencies

   .. code-block:: bash

      sudo apt install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake python-catkin-tools

#. Initialize rosdep

   .. code-block:: bash

      sudo rosdep init

   .. code-block:: bash

      rosdep update

Setup Workspace
===============

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
==============

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
=========================

#. Source your ROS installation

   .. code-block:: bash

      source /opt/ros/melodic/setup.bash

#. Create workspace

   .. code-block:: bash

      mkdir -p ~/catkin_ws/src && cd ~/catkin_ws

#. Initialize workspace

   .. code-block:: bash

      catkin init

#. Build empty workspace

   .. code-block:: bash

      catkin build


This command created the devel directory inside your catkin workspace. To source your workspace you can either source it manually for each terminal session by executing :code:`source ~/catkin_ws/devel/setup.bash`. A better way to handle this automatically is to append this command to your :file:`.bashrc` file.

.. code-block:: bash
   
   echo '$HOME/catkin_ws/devel/setup.bash' >> ~/.bashrc

For this change of the :file:`.bashrc` to take effect immediately execute:

.. code-block:: bash

   source ~/.bashrc
