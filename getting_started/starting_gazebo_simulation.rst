Starting Simulation
###################

General Launch Setup
====================

Vehicle-specific nodes in namespace "vehicle_name", for example :code:`uuv00` - :code:`uuv99`.

Each camera node in namespace "camera_name", which can be: :code:`vertical_camera` for HippoCampus, and :code:`vertical_camera` and :code:`front_camera` for the BlueROV's two cameras.



Spawning HippoCampus
====================

.. code-block:: sh

   roslaunch hippocampus_sim single_vehicle_complete.launch


Path Following example
======================

As an example, we will let the HippoCampus follow an Infinity-shaped path in Gazebo.

Here is the launch file code :file:`path_following_example.launch` explained: 



... Let's start it!

.. code-block:: sh

   roslaunch hippocampus_sim path_following_example.launch

Arming the Vehicle
==================

Open QGC

