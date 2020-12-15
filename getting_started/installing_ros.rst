Installing ROS
##############

The following installations steps work for a Ubuntu 18.04 amd64 version **and** for the Ubuntu 18.04 server image for the Raspberry Pi.

Preparation
===========

#. Add sources

   .. code-block:: sh

      sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

#. Add keys

   .. code-block:: sh

      sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

#. Update

   .. code-block:: sh

      sudo apt update && sudo apt upgrade -y

Installation
============

.. note:: Choose the installation option depending on your needs. Probably it's not reasonable to install :code:`ros-melodic-desktop-full` on an Ubuntu server image for the Raspberry Pi.

#. Install ROS

   .. tabs::
      .. code-tab:: sh desktop-full

         sudo apt install ros-melodic-desktop-full
      
      .. code-tab:: sh base (no GUI)

         sudo apt install ros-melodic-ros-base


#. Install build dependencies

   .. code-block:: sh

      sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential

#. Install catkin-tools

   .. code-block:: sh

      sudo apt install python-catkin-tools

rosdep Initialization
=====================

.. code-block:: sh

   sudo rosdep init && rosdep update

.. note:: Do **not** execute :code:`rosdep update` with root privileges. This would lead to permission issues.

Catkin Initialization
=====================

Depending on the shell you use, choose one of the following two options:


.. tabs:: 
   .. code-tab:: sh zsh

      source /opt/ros/melodic/setup.zsh

   .. code-tab:: sh bash

      source /opt/ros/melodic/setup.bash


Create workspace directories

.. code-block:: sh

   mkdir -p ~/catkin_ws/src && cd ~/catkin_ws

Initialize your workspace

.. code-block:: sh

   catkin build

Automatically source your Catkin workspace, choose the option according to your shell:

.. tabs:: 
   .. code-tab:: sh zsh

      echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
      echo "source \$HOME/catkin_ws/devel/setup.zsh" >> ~/.zshrc

   .. code-tab:: sh bash

      echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
      echo "source \$HOME/catkin_ws/devel/setup.bash" >> ~/.bashrc


Installation of HippoCampus Packages
====================================

.. todo:: Adding list of :code:`git clone` commands.