Deploying HippoCampus
#####################

.. todo:: Rework for ROS2 needed.

Start-Everyting-Check-List
==========================

#. **Push Buttons** 
   
   .. code-block:: sh

      ssh pi@buttons-00.local

   Replace the vehicle name with the one of the vehicle we are actually using.

   .. code-block:: sh

      ros2 launch buttons button_1.launch.py vehicle_name:=uuv02

   We can detach the session with :kbd:`F6`, since we do not have to interact with it anymore.

#. **Start the onboard nodes**

   .. code-block:: sh

      ssh pi@hippo-main-02.local

   We run at least two nodes: the :code:`esc_commander` and :code:`micro-ros`

   .. tabs::

      .. code-tab:: sh MicroXRCE

         MicroXRCEAgent serial --dev /dev/fcu_data -b 921600
      
      .. code-tab:: sh micro-ros

         ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/fcu_data -b 921600

   Open a new termianl window with :kbd:`F2` (switch between them with :kbd:`F3` and :kbd:`F4`).

   .. code-block:: sh

      ros2 run esc esc_commander_node --ros-args -r __ns:=/uuv02 

   Open a new terminal once more and start the debug session for the FCU.

   .. code-block:: sh

      screen /dev/fcu_debug 57600

   We use this session to either reboot the vehicle by entering :code:`reboot` (it does not matter if there are messages popping up while entering this) or to reset the state estimtion by entering :code:`ekf2 stop` and :code:`ekf2 start`.

   We leave this session by hitting :kbd:`Ctrl` + :kbd:`A` followed by :kbd:`k`. You have to confirm quitting the session by hitting :kbd:`y`.


#. Launch the Qualisys MoCap-Bridge and replace the vehicle name so it matches our used vehicle.

   .. code-block:: sh

      ros2 launch qualisys_bridge qualisys_bridge.launch.py vehicle_name:=uuv02

   .. note:: Make sure to use the correct IP address of the computer running the Qualisys Tracking Manager in the config file inside the :file:`qualisys_bridge` package. Check the address for the network interface, that connect the computer with the local network (not the one used to connect the cameras).

#. Launch the specific setup we want to run, for example 

   .. code-block:: sh

      ros2 launch hippo_control top_motor_failure_intra_process.launch.py vehicle_name:=uuv02 use_sim_time:=false

   For this specific launch setup also run the following command to set the desired thrust to  non-zero value

   .. code-block:: sh

      ros2 topic pub -r 50 /uuv02/thrust_setpoint hippo_msgs/msg/ActuatorSetpoint 'x: 3.0'

#. Use the the green and red push button to arm/disarm the vehicle.

.. attention:: Always keep an eye on the battery level. There is a indicator light connected to the Raspberry Pi controlloing the buttons. Besides, the `esc_commander` node also publishes the battery voltage measured by the ESCs under :file:`/uuv02/battery_voltage`. Make sure to **not** discharge the battery below 3.5V (it is okay to have short voltage drops under heavy load until 3.3V) per cell. Otherwise tell Lennart and/or Nathalie about it.

Shutting-Down-Check-List
========================

.. note:: In general, please shutdown every Raspberry Pi with :code:`sudo shutdown 0` before disconnecting any power supply.

#. Shutdown at least all battery powered Raspberry Pis (usually this means the one inside the vehicle) with :code:`sudo shutdown 0` (make sure you run this command on the Pi and not on your own device by accident).

#. Disconnect all batteries and use the battery charger to charge the battery to storage voltage if you will not reuse it immediately.

#. If you have any batteries left that are not charged to storage voltage after your experiments are done, charge them to storage voltage. Do not store them at a voltage level above or below it.


Final Steps
===========

Look! It's running just perfectly fine without any trial and error.


.. image:: /res/images/hippo_inf_path.gif
   :align: center
   :width: 500
