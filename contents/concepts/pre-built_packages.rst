.. _concept-pre-built-packages:

Pre-built Packages
##################

Why do I need Pre-built Packages?
=================================

Simple answer: you don't. It's mere convenience to be able to install packages we would like to use via a simple ``apt install`` command.
Alternatively, we would need to clone the source code of the packages we would like to use and build them ourselves.

When **not** to install Pre-built Packages?
===========================================

If you want to modify certain packages to your needs, you want to have the source code inside your workspace(s).
Pre-built packages and the installatio from source are not mutually exclusive.
This means, it is perfectly fine to install all the packages from pre-built binaries and *overlay* them with the modified built-from-source version in your workspace.
The last sourced version of a package takes precedence over all prior versions.

.. hint::

   This also implies if you want to work with the pre-built version of a package, make sure you do not have a local version in one of your sourced workspaces.
   Deleting the source files is not sufficient, you need to remove the corresponding files/directories in the :file:`install` directory inside your workspace as well.

Which Packages can I Install via ``apt``?
=========================================

To find out which packages can be installed from our repository, execute

   .. code-block:: console

      $ curl -s https://repositories.hippocampus-robotics.net/ubuntu/dists/noble/main/binary-amd64/Packages \
      | grep "^Package: " \
      | cut -d" " -f2 | sort -u
      ros-jazzy-acoustic-msgs
      ros-jazzy-alpha-msgs
      ros-jazzy-buttons-msgs
      ros-jazzy-dvl
      ros-jazzy-dvl-msgs
      ros-jazzy-esc
      ros-jazzy-gantry-msgs
      ros-jazzy-hardware
      ros-jazzy-hippo-common
      ros-jazzy-hippo-common-msgs
      ros-jazzy-hippo-control
      ros-jazzy-hippo-control-msgs
      ros-jazzy-hippo-msgs
      ros-jazzy-mjpeg-cam
      ros-jazzy-path-planning
      ros-jazzy-px4-msgs
      ros-jazzy-rapid-trajectories-msgs
      ros-jazzy-remote-control
      ros-jazzy-state-estimation-msgs
      ros-jazzy-uvms-msgs

We can install them by

.. code-block:: console

   $ sudo apt install ros-${ROS_DISTRO}-<PACKAGE_NAME>

for example, if we want to install the remote control package the command would be

.. code-block:: console

   $ ros-${ROS_DISTRO}-remote-control

.. tip::

   There are meta-packages such as (not necessarily limited to) ``hippo_full``, ``hippo_robot`` or ``hippo_common_msgs``.
   They do not contain any source code, but depend on other packages to make the installation of bundles of packages more convenient.
   For example, ``hippo_full`` depends on (almost) all our message packages and all the other ``ros2`` packages we provide.
   This way, instead of installing all these packages one by one, the installation just boils down to

   .. code-block:: console

      $ sudo apt install ros-jazzy-hippo-full

   and all the dependencies get installed automatically.

