Deploying HippoCampus
#####################

Flashing the PixRacer
=====================

.. todo::

   Flash the PX4-Autopilot firmware onto the PixRacer. Select correct Airframe.

PixRacer Calibration
====================

Just follow the steps in QGroundControl.
Probably a good idea to step away from the steel water tank.

Camera Calibration
==================

http://wiki.ros.org/camera_calibration/Tutorials/MonocularCalibration

Copy file to :file:`~/catkin_ws/src/camera/config/calib_ov9281_00.yaml` on RaspberryPi.

Launch Setup
============

Tethered Setup
--------------

#. **ROS network setup**

   The ROS master will be running on the *main* RaspberryPi on HippoCampus. Set the ROS_MASTER_URI on your computer to :code:`http://hippo-main-XX.local:11311`.

   In case of errors, checklist to work through. Maybe this should be in a seperate debugging section.


#. **Start this on HippoCampus:**

   .. code-block:: sh

      roslaunch hippocampus_common hardware_hippo.launch vehicle_name:=uuv00

   IP address for QGC computer can be changed by adding

   .. code-block:: sh 

      roslaunch hippocampus_common hardware_hippo.launch vehicle_name:=uuv00 qgc_ip:=123456789

#. **Start this on a computer of your choice:**

   .. code-block:: sh

      roslaunch hippocampus_common offboard_hippo.launch vehicle_name:=uuv00


Autonomous Setup
----------------

Pretty much the same, this time just launch all necessary nodes on HippoCampus. It might be a good idea to make use of the *Buddy* RaspberryPi as well.

.. todo::

   TBD


Offboard Mode
=============

Set mode to Offboard in QGC.

Arming the Vehicle
==================

Now, you can arm the vehicle in QGC. Try not to move the vehicle too much. 
If you absolutely cannot arm due to preflight errors, you can force arm using a rosservice.

Force arming via mavros
-----------------------

.. code-block:: shaped

   rosservice call /uuv00/mavros/cmd/command "{broadcast: false, command: 400,confirmation: 0, param1: 1, param2: 21196, param3: 0.0, param4: 0.0,param5: 0.0, param6: 0.0, param7: 0.0}"

Force disarming
---------------

.. code-block:: shaped

   rosservice call /uuv00/mavros/cmd/command "{broadcast: false, command: 400,confirmation: 0, param1: 0, param2: 21196, param3: 0.0, param4: 0.0,param5: 0.0, param6: 0.0, param7: 0.0}"




Final Steps
===========

Look! It's running just perfectly fine without any trial and error.


.. image:: /res/images/hippo_inf_path.gif
   :align: center
   :width: 500