Workspace Setup
===============

In the following, we describe our ROS2 system setup.

.. note::
   This guide assumes `Ubuntu 22.04 <https://releases.ubuntu.com/22.04/>`_ is used as OS. We use ROS2 `Humble <https://docs.ros.org/en/humble/index.html>`_.


Our Workspace Setup
-------------------

There are a few packages that we will need to build from source, but probably will not touch (or at least not too much). In order to keep the compilation time of our workspace as short as possible during development, we will use a setup with two overlayed workspaces. 
We use :file:`ros2` as development workspace und :file:`ros2_underlay` for larger manually compiled non-development packages that take a lot of time to compile/recompile.
Typical packages for :file:`ros2_underlay` are :code:`px4_msgs` and a ROS2 version of :code:`apriltag_ros` (since there has not been an official release at this point of time).
In :file:`ros2`, we will keep all of our own packages.

To create this directory structure, execute:

.. code-block:: sh

   mkdir -p ~/ros2/src
   mkdir -p ~/ros2_underlay/src


Getting the external packages
-----------------------------

We will need the following external packages that we will put into :file:`ros2_underlay`:

PX4-msg
*******

.. code:: sh

   cd ~/ros2_underlay/src && git clone https://github.com/PX4/px4_msgs.git

AprilTag-ROS
************
There is a `PR <https://github.com/AprilRobotics/apriltag_ros/pull/114>`__ for porting the good old :code:`apriltag_ros` package to ROS2. 

.. code:: sh

   cd ~/ros2_underlay/src && git clone https://github.com/wep21/apriltag_ros.git
   cd ~/ros2_underlay/src/apriltag_ros && git checkout ros2-port

.. note::
   
   There is an alternative `package <https://github.com/christianrauch/apriltag_ros>`__ by Christian Rauch, that works somewhat different but has a simpler code base. Unfortunately it does not support tag bundles.

Building the Workspaces
-----------------------

With :code:`colcon`, the new build tool for ROS2, you cannot build your custom workspace when it is sourced. This would mean that you either cannot source your workspace in :file:`.zshrc` (or :file:`.bashrc` if you use bash), or you have to manually make sure to run the build command in an environment where you only source workspaces outside the workspace you want to build. 

Since this is very tedious, we define some aliases. Put these two lines into your :file:`.zshrc`:

.. code:: sh

   echo "alias build_ros=\"env -i HOME=\$HOME USER=\$USER TERM=xterm-256color bash -l -c 'source \$HOME/ros2_underlay/install/setup.bash && cd \$HOME/ros2 && colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON'\"" >> ~/.zshrc
   echo "alias build_underlay=\"env -i HOME=\$HOME USER=\$USER TERM=xterm-256color bash -l -c 'source /opt/ros/humble/setup.bash && cd \$HOME/ros2_underlay && colcon build'\"" >> ~/.zshrc

Make sure to source the :file:`.zshrc` in your terminal when you make changes. 

Underlay Workspace
******************

We can now build the first "under"layed workspace :file:`ros2_underlay`.
But first, let's check for unresolved dependencies.

.. code:: sh

   cd ~/ros2_underlay && rosdep install --from-paths src -y --ignore-src

And to build:

.. code:: sh

   build_underlay

Note that you do not have to be inside the respective workspace directory to build by executing the defined alias. Very convenient!

After a successful build, we can source this workspace in the :file:`.zshrc`, so that our main, overlayed workspace will find it.

.. code:: sh

   echo "source $HOME/ros2_underlay/install/setup.zsh" >> ~/.zshrc

Main Workspace
**************

Now, we can build our main workspace. Let's get our packages:

.. code:: sh

   cd ~/ros2/src
   git clone git@github.com:HippoCampusRobotics/hippo_core.git
   git clone git@github.com:HippoCampusRobotics/hippo_simulation.git
   git clone git@github.com:HippoCampusRobotics/state_estimation.git
   git clone git@github.com:HippoCampusRobotics/vision.git

.. todo:: 

   Add any other relevant packages as we continue our move to ROS2.

These packages have some more dependencies. Let's resolve them by executing

.. code:: sh

   cd ~/ros2 && rosdep install --from-paths src -y --ignore-src

Make sure that the underlay workspace containing external packages is sourced for this.

Then, we can build this workspace using our defined alias.

.. code:: sh

   build_ros

Now, source this workspace in your :file:`.zshrc`, too, using the local setup this time:

.. code:: sh

   echo "source $HOME/ros2/install/local_setup.zsh" >> ~/.zshrc

Note that since this workspace overlays the :file:`ros2_underlay` workspace, this setup file needs to be sourced afterwards.


Auto-Complete
*************

ROS2 command line tools do not autocomplete as of this `GitHub Issue <https://github.com/ros2/ros2cli/issues/534>`_. While this issue has since been closed, the problem still occurs. To fix this

.. code-block::
   :name: test
   
   echo "eval \"\$(register-python-argcomplete3 ros2)\"" >> ~/.zshrc
   echo "eval \"\$(register-python-argcomplete3 colcon)\"" >> ~/.zshrc

Auto-completing topic names seems to work only after an execution of `ros2 topic list`. Before the auto-complete gets stuck and has to be canceled by :kbd:`Ctrl` + :kbd:`C`.

Sourcing :file:`install/setup.zsh` might reset this. Better source :file:`install/local_setup.zsh`.


Final Check
***********

Your :file:`.zshrc` should look similar to this now:

.. code:: sh 
   
   ...


   alias build_ros="env -i HOME=$HOME USER=$USER TERM=xterm-256color bash -l -c 'source $HOME/ros2_underlay/install/setup.bash && cd $HOME/ros2 && colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON'"
   alias build_underlay="env -i HOME=$HOME USER=$USER TERM=xterm-256color bash -l -c 'source /opt/ros/humble/setup.bash && cd $HOME/ros2_underlay && colcon build'"

   source /opt/ros/humble/setup.zsh
   source $HOME/ros2_underlay/install/setup.zsh
   source $HOME/ros2/install/local_setup.zsh

   eval "$(register-python-argcomplete3 ros2)"
   eval "$(register-python-argcomplete3 colcon)"
