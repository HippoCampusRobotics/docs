ROS Installation
################

In general you can follow the official instruction in the `ROS wiki <http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi>`_ to install ROS under Raspbian Buster on the Raspberry Pi. But the following instructions will use :code:`catkin tools` instead of :code:`catkin_make` or :code:`catkin_make_isolated`. 

.. note:: If you use the 64bit Raspbian, you can follow the Debian standard `installation guide <http://wiki.ros.org/noetic/Installation/Debian>`_ and skip everything regarding :file:`ros_catkin_ws`.

Workspace Concept
=================

Since ROS is not availabe as binary packages for Raspbian, all the ROS packages have to be installed from source. To not flood our `normal` Catkin workspace, we create two seperate workspaces. 

~/ros_catkin_ws
   This is the workspace, where the source code of the packages we just want to install lives. We will configure Catkin to install these packages in :file:`/opt/ros/melodic`. This is the directory, where the installation via prebuilt packages would also create its files. It is not very likely you get in touch with this workspace often after the initial installation.

~/catkin_ws
   Your normal workspace directory. All the Hippocampus specific packages should be in here. Also other packages that you want to modify should be in this workspace. 


Preparations
============

#. Adding keys

   .. code-block:: bash
        
      sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

   .. code-block:: bash

      curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

#. Update source lists

   .. code-block:: sh

      sudo apt update

#. Install dependencies

   .. code-block:: bash

      sudo apt install -y python3-rosdep python3-rosinstall-generator python3-vcstool python3-rosinstall build-essential cmake python3-catkin-tools

#. Initialize rosdep

   .. code-block:: bash

      sudo rosdep init

   .. code-block:: bash

      rosdep update

Setup Workspace
===============

#. Create workspace

   .. code-block:: bash

      mkdir -p ~/ros_catkin_ws/src && cd ~/ros_catkin_ws

#. Fetch source code

   .. attention:: The following commands will fetch the sources for the :code:`ros_comm` meta package and the :code:`perception` meta package. If you do not need all of them or if you need even more packages feel free to modify the following commands accordingly. Building unnecessary packages might be a waste of time.
   
   .. code-block:: bash

      rosinstall_generator ros_comm perception --rosdistro noetic --deps --wet-only --tar > noetic-ros_comm-perception-wet.rosinstall

   .. code-block:: bash

      vcs import --input noetic-ros_comm-perception-wet.rosinstall ./src


#. Resolve dependencies

   .. code-block:: bash

      rosdep install -y --from-paths src --ignore-src --rosdistro noetic -r --os=debian:buster

Build the Code
==============

#. Set the install space

   .. code-block:: bash

      catkin config --install-space /opt/ros/noetic

#. Use the :code:`install` configuration instead of :code:`devel`

   .. code-block:: bash

      catkin config --install

#. Start the build process

   .. note:: Depending on your package configuration the next command may take some time, i.e. a few hours if you want to build many packages.

   .. code-block:: bash

      sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release -DPYTHON_EXECUTABLE=/usr/bin/python3


Initialize User Workspace
=========================

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

