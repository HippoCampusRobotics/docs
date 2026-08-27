Usage
#####

Run the xyz Setup
=================

On the Raspberry Pi on the gantry ( :code:`ssh pi@gantry.local` ), run:

.. code-block:: console

   $ ros2 launch gantry xyz_motors.launch.py

This will start the three motors for the x-, y-, and z-axis, respectively.
The configuration files for the motors are found in ``gantry/config/motor_<axis_name>.yaml``.

If you encounter any error messages, e.g. time outs, just keep repeating the launch command... a reboot of the Raspberry Pi ( :code:`sudo reboot` ) or a reboot of the entire setup (see below) can help, too. Eventually, all 3 motors should work. TODO: this needs to be fixed.

Example for timeout errror for x-axis motor:

.. code-block:: console

   pi@gantry ~
   $ ros2 launch gantry xyz_motors.launch.py
   [INFO] [launch]: All log files can be found below /home/pi/.ros/log/2025-06-11-13-28-20-755904-gantry-5649
   [INFO] [launch]: Default logging verbosity is set to INFO
   [INFO] [xyz_motors-1]: process started with pid [5687]
   [xyz_motors-1] [INFO] [1749641301.578167645] [xyz_motor]: Created x axis motor.
   [xyz_motors-1] [INFO] [1749641301.578849939] [xyz_motor]: Created y axis motor.
   [xyz_motors-1] [INFO] [1749641301.579263456] [xyz_motor]: Created z axis motor.
   [xyz_motors-1] [ERROR] [1749641301.944969580] [motor_interface]: Read timed out.
   [xyz_motors-1] [FATAL] [1749641301.945241672] [gantry.motor_x]: Could not read motor position. Are all wires connected properly? Is the motor powered (relay box)?
   [xyz_motors-1] [FATAL] [1749641301.945584319] [gantry.motor_x]: Node will be inactive.
   [xyz_motors-1] [INFO] [1749641302.049688477] [gantry.motor_y]: Initialized.
   [xyz_motors-1] [INFO] [1749641302.053621334] [gantry.motor_z]: Initialized.

Enable the Motors
=================

If the motors are enabled, you should not be able to move the x- and y-axis by hand. Do NOT test this for the z-axis! If you want to move one of the linear axis by hand, you have to turn the power supply off. 

Sometimes, one of the motors is not automatically enabled again after turning the power supply back on. This tends to happen to the y-axis.
You can check the motor status: 

.. code-block:: console

   pi@gantry ~
   $ ros2 topic echo /gantry/motor_y/motor_status          
   header:
     stamp:
       sec: 1787840867
       nanosec: 376819798
     frame_id: ''
   homing: false
   lower_limit_switch_pressed: false
   upper_limit_switch_pressed: false
   enabled: false
   position_reached: true

To manually enable a motor, in this example the y-axis, use: 

.. code-block:: console

   pi@gantry ~
   $ ros2 service call /gantry/motor_y/enable std_srvs/srv/SetBool "{data: True}"
   requester: making request: std_srvs.srv.SetBool_Request(data=True)
   
   response:
   std_srvs.srv.SetBool_Response(success=True, message='')

As a physical check, now the axis should not be movable by hand anymore.


Home the Motors
===============

.. important::

   Always make sure that the motors are homed before sending any setpoints!

.. note::

   The motor position is stored inside the motion controller and not inside any code running on the Raspberry Pi or any ROS node.
   Relaunching any node does **not** make it necessary to rerun the homing procedure 🥳.

.. tab-set::

   .. tab-item:: Homing Using the GUI 

         #. Run the GUI (see :ref:`GUI-label`)

         .. figure:: /res/images/gantry_gui_screenshot.png

         #. Press the "Go Home" Button for each axis. The motors should start homing.

         #. Once each motor has reached its lower limit, press "Set Position" for each axis. 


   .. tab-item:: Homing Using the Command Line

      #. Move the motors to the home position.

         The motors provide a service to move to the home position.

         .. tabs::

            .. code-tab:: console x

               $ ros2 service call /gantry/motor_x/start_homing std_srvs/srv/Trigger{}

            .. code-tab:: console y
               
               $ ros2 service call /gantry/motor_y/start_homing std_srvs/srv/Trigger {}

            .. code-tab:: console z
               
               $ ros2 service call /gantry/motor_z/start_homing std_srvs/srv/Trigger {}

      #. Set the current position.
         Usually this will be 0 but we can also specify arbitrary values either in motor dimensions (i.e. increments) or in physical dimensions ([m]).

         .. tabs::

            .. code-tab:: console x

               $ ros2 service call /gantry/motor_x/set_home_position gantry_msgs/srv/SetHomePosition {} 

            .. code-tab:: console y
               
               $ ros2 service call /gantry/motor_y/set_home_position gantry_msgs/srv/SetHomePosition {} 

            .. code-tab:: console z
               
               $ ros2 service call /gantry/motor_z/set_home_position gantry_msgs/srv/SetHomePosition {} 

         .. todo:: Add an example for non zero values


Smooth Accelerations in Position Mode
=====================================

.. container:: toggle, toggle-hidden

   The maximum acceleration can be set via the :file:`~/set_max_accel` service.
   If the maximum acceleration is higher than what the motor can acutally achieve (it has to move quite a bit of mass) it will overshoot the target position.
   For smoother accelerations we can reduce the acceleration to a smaller value.

   To get the currently set value run

   .. tabs::

      .. code-tab:: console x

         $ ros2 service call /gantry_motor_x/get_max_accel gantry_msgs/srv/GetFloatDrive {}

      .. code-tab:: console y

         $ ros2 service call /gantry_motor_y/get_max_accel gantry_msgs/srv/GetFloatDrive {}

      .. code-tab:: console z

         $ ros2 service call /gantry_motor_z/get_max_accel gantry_msgs/srv/GetFloatDrive {}

   To set a new value run

   .. tabs::

      .. code-tab:: console x

         $ ros2 service call /gantry_motor_x/set_max_accel gantry_msgs/srv/SetFloatDrive '{motorside_value: 500}'

      .. code-tab:: console y

         $ ros2 service call /gantry_motor_y/set_max_accel gantry_msgs/srv/SetFloatDrive '{motorside_value: 500}'

      .. code-tab:: console z

         $ ros2 service call /gantry_motor_z/set_max_accel gantry_msgs/srv/SetFloatDrive '{motorside_value: 500}'

   .. note::

      We could also set the ``driveside_value`` in SI units instead of value in motor dimensions.

Limit the Motor Velocity in Position Mode
=========================================

.. container:: toggle, toggle-hidden

   This is equivalent to acceleration limit settings, but the service names are

   * ``~/get_max_speed``
   * ``~/set_max_speed``

Run a Single Motor
==================

.. container:: toggle, toggle-hidden

   .. code-block:: console

      $ ros2 run gantry single_motor --ros-args \
      --params-file <path_to_config_file> \
      -r __node:=<motor_name> \
      -r __ns:=<namespace>

   .. note::

      The path to the config file can be relative or absolute.

   .. attention::

      Keep in mind that namespaces have to start with a leading ``/``.
      Setting the node name and the namespace is optional but recommended.


   Example
      Assuming we are inside the ``gantry`` package directory, we can directly run

      .. code-block:: console

         $ ros2 run gantry single_motor --ros-args \
         --params-file config/motor_x.yaml \
         -r __node:=single_x \
         -r __ns:=gantry
      

.. _GUI-label:

Run (and use) the GUI
=====================

On any computer with a graphical interface (i.e. **not** the Raspberry Pi via SSH), for example your laptop, run our GUI:

.. code-block:: console

   $ ros2 run gantry_gui manual_control

A window should open:

.. figure:: /res/images/gantry_gui_screenshot.png

   Gantry GUI for manual control.

Remember to home the motors before using them.

Before you can use the manual control, you need to set a mode:

.. figure:: /res/images/gantry_mode_selection.png

   Mode selection: manually control either distance travelled or velocity of motors.

Then, you can use the arrows to control the individual axes.

Closing the GUI: :kbd:`Ctrl` + :kbd:`C` + you will need to manually close the window.

Waypoint Grid Control
=====================

For measurements, you might want to position the gantry system at a certain set of waypoints.
We have an example implementation for this within our `gantry ROS2 package <https://github.com/HippoCampusRobotics/gantry>`_. 

Run (preferably on your own laptop):

.. code-block:: console

   $ ros2 launch gantry waypoint_grid_control_node.launch.py 

To start the waypoint controller, call the start service:

.. code-block:: console

   $ ros2 service call /gantry/gantry_grid_control/start std_srvs/srv/Trigger
   requester: making request: std_srvs.srv.Trigger_Request()
   response:
   std_srvs.srv.Trigger_Response(success=False, message='Starting...')

To stop: 

.. code-block:: console

   $ ros2 service call /gantry/gantry_grid_control/stop std_srvs/srv/Trigger
   requester: making request: std_srvs.srv.Trigger_Request()
   response:
   std_srvs.srv.Trigger_Response(success=True, message='Stopping...')

.. important:: The gantry GUI should not be running at the same time!

By default, the waypoints are defined within the file :file:`gantry/config/waypoint_grid.yaml`. Adapt the waypoints by e.g. writing your own script. 

On your own laptop, you can simply edit the default waypoint file. Alternatively, define the path to your waypoint file by using the :code:`waypoint_file` launch argument.


Restart Gantry System
=====================

#. The Raspberry Pi should be shutdown before the power gets removed. Run :code:`sudo shutdown 0` on the pi and wait until its green LED is not blinking anymore.

#. Remove power from gantry system: Press any of the red emergency buttons.

#. To restart, *all* emergency buttons need to be enabled again. For this, they should all look like the button on the left:

   .. image:: /res/images/gantry_emergency_button_not_pressed.jpg
      :width: 45%
   .. image:: /res/images/gantry_emergency_button_pressed.jpg
      :width: 45%

   Not pressed button *(left)* and pressed button *(right)*.

#. To turn on power again, press this button within the gantry power supply box:

   .. figure:: /res/images/gantry_power_button.jpg
      :width: 80%

      Power button for gantry system. 

   When powered, the green LED should be on.

#. .. important:: You need to re-home the motors any time the power has been shut off. **This is crucial!**


.. note:: When the power is off, the x-axis and the y-axis can be moved by hand. 
