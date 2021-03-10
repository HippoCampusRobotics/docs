Deploying HippoCampus
#####################

Step One
========

Flash this.

Step two
========



Calibrating
===========

Probably a good idea to step away from the steel water tank.

Step N
========

Force arming via mavros
-----------------------

.. code-block:: shaped

   rosservice call /uuv00/mavros/cmd/command "{broadcast: false, command: 400,confirmation: 0, param1: 1, param2: 21196, param3: 0.0, param4: 0.0,param5: 0.0, param6: 0.0, param7: 0.0}"

Force disarming
---------------

.. code-block:: shaped

   rosservice call /uuv00/mavros/cmd/command "{broadcast: false, command: 400,confirmation: 0, param1: 0, param2: 21196, param3: 0.0, param4: 0.0,param5: 0.0, param6: 0.0, param7: 0.0}"


Launch Setup
============

Using a tether and running as much code offline as possible
-----------------------------------------------------------

#. ROS network setup

   Set ROS_MASTER_URI correctly.
   In case of errors, checklist to work through. Maybe this should be in a seperate debugging section.

#. **Start this on HippoCampus:**

   .. code-block:: sh

      roslaunch hippocampus_common hardware_hippo.launch

   IP address for QGC computer can be changed by adding

   .. code-block:: sh 

      roslaunch hippocampus_common hardware_hippo.launch qgc_ip:="123456789"

#. **Start this on a computer of your choice:**

   .. code-block:: sh

      roslaunch hippocampus_common offboard_hippo.launch


Running HippoCampus autonomously
--------------------------------

Pretty much the same, this time just launch all necessary nodes on HippoCampus. It might be a good idea to make use of the *Buddy* RaspberryPi as well.

TBD


Final Steps
===========

Look! It's running just perfectly fine without any trial and error.


.. image:: /res/images/hippo_inf_path.gif