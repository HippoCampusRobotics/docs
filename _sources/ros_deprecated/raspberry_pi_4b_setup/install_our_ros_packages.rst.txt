Install Our ROS Packages
########################

Change into the catkin workspace's :file:`src` directory:

.. code-block:: sh

   cd ~/catkin_ws/src

Clone our packages needed for autonomous deployment of HippoCampus:

.. code-block:: sh

   git clone https://github.com/HippoCampusRobotics/hippocampus_common.git
   git clone https://github.com/HippoCampusRobotics/hippocampus_msgs.git
   git clone https://github.com/HippoCampusRobotics/mu_auv_localization.git
   git clone https://github.com/HippoCampusRobotics/control.git
   git clone https://github.com/HippoCampusRobotics/path_planning.git

.. note::

   You don't necessarily need all packages on *both* the **main** and the **buddy** RaspberryPi.