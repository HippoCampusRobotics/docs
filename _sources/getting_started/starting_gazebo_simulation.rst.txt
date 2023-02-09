Starting Simulation
###################

.. hint:: If launching gazebo from ROS, ROS is not able to kill the gazebo node without escalating to **SIGTERM**. This happens after a 15s timeout. If you do not have the time to wait for so long, you can modifiy :file:`/opt/ros/noetic/lib/python3/dist-packages/roslaunch/nodeprocess.py` and change :code:`DEFAULT_TIMEOUT_SIGINT` to some value you are willing to wait.


General Launch Setup
====================

Vehicle-specific nodes should be launched in namespace "vehicle_name", for example :code:`uuv00` - :code:`uuv99`.

Each camera node should be launched in namespace "camera_name", which can be: :code:`vertical_camera` for HippoCampus, and :code:`vertical_camera` and :code:`front_camera` for the BlueROV's two cameras.


Parameter Setup
===============

Before continuing on the *hydrobatic-way-of-live*, we need to set some parameters first.

In QGroundControl:

We set *Offboard* as a flight mode in which remote control (RC) loss is ignored. Thus, *fail-safe* actions are not triggered.

.. code-block:: sh

    COM_RCL_EXCEPT=4



Spawning HippoCampus
====================

To start Gazebo with one HippoCampus:

.. code-block:: sh

   roslaunch hippocampus_sim top_single_vehicle_complete.launch


Path Following example
======================

As an example, we will let the HippoCampus follow an Infinity-shaped path in Gazebo.

Here is the launch file code :file:`top_path_following_example.launch` explained: 

.. todo::
   
   ...



... Let's start it!

.. code-block:: sh

   roslaunch hippocampus_sim top_path_following_example.launch

Offboard Mode
=============

The path follower node publishes attitude setpoints. For the uuv_att_control PX4 module to accept externally provided setpoints, the flight mode *Offboard mode* has to be selected. This mode can only be engaged if the vehicle is already receiving a stream of target setpoints (>2Hz). The vehicle will exit the mode if target setpoints are not received at a rate of >2Hz.

The offboard mode can be selected in QGC.

Arming the Vehicle
==================

Arming is also done in QGC.



