ROS Installation
################
.. note:: The following installations steps work for a Ubuntu 22.04 amd64 version **and** for the Ubuntu 22.04 server image for the Raspberry Pi.

Preparation
===========

#. Make sure you have a UTF-8 supported locale with
   
   .. code-block:: sh
      
      locale
   
   If not, refer to the `ROS documentation <https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html#set-locale>`__.

#. Enable universe repository
   
   .. code-block:: sh
      
      sudo apt install software-properties-common
      sudo add-apt-repository universe

#. Add the key

   .. code-block:: sh

      sudo apt update && sudo apt install curl -y
      sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

#. Add sources

   .. code-block:: sh

      echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null




#. Update

   .. warning:: This is critial!
   

   .. code-block:: sh

      sudo apt update && sudo apt upgrade -y

Installation
============

.. note:: Choose the installation option depending on your needs. Probably it's **not** reasonable to install :code:`ros-humble-desktop-full` on an Ubuntu server image for the Raspberry Pi.

#. Install ROS

   .. tabs::
      .. code-tab:: sh desktop-full

         sudo apt install ros-humble-desktop-full
      
      .. code-tab:: sh perception (e.g. for Raspberry Pi)

         sudo apt install ros-humble-ros-perception


#. Install development tools

   .. code-block:: sh

      sudo apt install ros-dev-tools python3-pip

rosdep Initialization
=====================

.. code-block:: sh

   sudo apt install python3-rosdep

.. code-block:: sh

   sudo rosdep init && rosdep update

.. note:: Do **not** execute :code:`rosdep update` with root privileges. This would lead to permission issues.
