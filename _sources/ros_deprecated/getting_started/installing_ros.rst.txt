Installing ROS
##############

The following installations steps work for a Ubuntu 20.04 amd64 version **and** for the Ubuntu 20.04 server image for the Raspberry Pi.

Preparation
===========

#. Add sources

   .. code-block:: sh

      sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

#. Add keys

   .. code-block:: sh

      sudo apt install curl # if you haven't already installed curl
      curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

#. Update

   .. code-block:: sh

      sudo apt update && sudo apt upgrade -y

Installation
============

.. note:: Choose the installation option depending on your needs. Probably it's not reasonable to install :code:`ros-noetic-desktop-full` on an Ubuntu server image for the Raspberry Pi.

#. Install ROS

   .. tabs::
      .. code-tab:: sh desktop-full

         sudo apt install ros-noetic-desktop-full
      
      .. code-tab:: sh base (no GUI)

         sudo apt install ros-noetic-ros-base


#. Install build dependencies

   .. code-block:: sh

      sudo apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

#. Install catkin-tools

   .. code-block:: sh

      sudo apt install python3-catkin-tools python3-osrf-pycommon

rosdep Initialization
=====================

.. code-block:: sh

   sudo apt install python3-rosdep

.. code-block:: sh

   sudo rosdep init && rosdep update

.. note:: Do **not** execute :code:`rosdep update` with root privileges. This would lead to permission issues.

Catkin Initialization
=====================

Depending on the shell you use, choose one of the following two options:


.. tabs:: 
   .. code-tab:: sh zsh

      source /opt/ros/noetic/setup.zsh

   .. code-tab:: sh bash

      source /opt/ros/noetic/setup.bash


Create workspace directories

.. code-block:: sh

   mkdir -p ~/catkin_ws/src && cd ~/catkin_ws

Initialize your workspace

.. code-block:: sh

   catkin build

Automatically source your Catkin workspace, choose the option according to your shell:

.. tabs:: 
   .. code-tab:: sh zsh

      echo "source /opt/ros/noetic/setup.zsh" >> ~/.zshrc
      echo "source \$HOME/catkin_ws/devel/setup.zsh" >> ~/.zshrc

   .. code-tab:: sh bash

      echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
      echo "source \$HOME/catkin_ws/devel/setup.bash" >> ~/.bashrc


Setting up Catkin Workspace
===========================

.. attention:: Make sure you are in your Catkin workspace's :file:`src` directory.

Installation of HippoCampus packages
************************************

This is a collection of usually needed packages on your personal computer. Feel free to skip unwanted packages and visit `GitHub <https://github.com/hippocampusrobotics>`__ to see a full list of our packages.

.. code-block:: sh

   git clone git@github.com:HippoCampusRobotics/hippocampus_common.git
   git clone git@github.com:HippoCampusRobotics/hippocampus_msgs.git
   git clone git@github.com:HippoCampusRobotics/hippocampus_sim.git
   git clone git@github.com:HippoCampusRobotics/mu_auv_localization.git
   git clone git@github.com:HippoCampusRobotics/control.git
   git clone git@github.com:HippoCampusRobotics/path_planning.git

If you want to interact with the gantry you would also want to have the following packages.

.. code-block:: sh

   git clone git@github.com:HippoCampusRobotics/rqt_gantry.git
   git clone git@github.com:HippoCampusRobotics/gantry_control.git

To install dependencies, such as AprilTag and MAVROS:

.. code-block:: sh

   cd ~/catkin_ws && rosdep install --from-path src --ignore-src -r -y

For MAVROS, you also need to install the `GeographicLib <https://geographiclib.sourceforge.io/>`__ datasets:

.. code-block:: sh

   wget https://raw.githubusercontent.com/mavlink/mavros/master/mavros/scripts/install_geographiclib_datasets.sh
   sudo bash ./install_geographiclib_datasets.sh   

Build your Catkin workspace:

.. code-block:: sh

   cd ~/catkin_ws && catkin build

