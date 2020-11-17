Installing ROS
##############

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

#. Install ROS

   .. code-block:: sh

      sudo apt install ros-melodic-desktop-full

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

* Bash
   .. code-block:: sh

      source /opt/ros/melodic/setup.bash

* Zsh
   .. code-block:: sh

      source /opt/ros/melodic/setup.zsh

Create workspace directories

.. code-block:: sh

   mkdir -p ~/catkin_ws/src && cd ~/catkin_ws

Initialize your workspace

.. code-block:: sh

   catkin build

Automatically source your Catkin workspace, choose the option according to your shell:

* Bash
   .. code-block:: sh

      echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
      echo "source \$HOME/catkin_ws/devel/setup.bash" >> ~/.bashrc

* Zsh
   .. code-block:: sh

      echo "source /opt/ros/melodic/setup.zsh" >> ~/.zshrc
      echo "source \$HOME/catkin_ws/devel/setup.zsh" >> ~/.zshrc


Installation of HippoCampus Packages
====================================

.. todo:: Adding list of :code:`git clone` commands.