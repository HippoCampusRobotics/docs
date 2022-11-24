PX4
###

Building the Firmware
=====================

If PX4 is used in combination with the onboard computer, make sure the firmware running on the FCU was built with RTPS support.

A tested PX4-Version is the commit :code:`45b390b0bf`.

.. code-block:: sh

   git clone https://github.com/PX4/PX4-Autopilot.git --recursive \
   && cd PX4-Autopilot \
   && git checkout 45b390b0bf \
   && git submodule update --init --recursive

For this version the RTPS support is *not* enabled by default for the :code:`fmu-v4` target. One has to modify the file :file:`boards/px4/fmu-v4/default.px4board` and add the line

.. code-block:: sh

   CONFIG_MODULES_MICRODDS_CLIENT=y


Also modify the autostart line in :file:`src/modules/microdds_client/module.yaml` if you want to have a namespace prepended to the topic names

.. code-block:: sh

   set XRCE_DDS_ARGS "-t serial -d ${SERIAL_DEV} -b p:${BAUD_PARAM} -n uuv00"

Build the firmware

.. code-block:: sh

   make px4_fmu-v4

To manually start the :code:`microdds_client`, go to the nsh terminal and run

.. code-block:: sh

   microdds_client start -t serial -d /dev/ttyS2 -b 921600 -n uvv00


Configure the Firmware
======================

Set :code:`XRCE_DDS_0_CFG` to :code:`TELEM2`, i.e. :code:`102`. If you want to, you can change the baudrate of TELEM2 at :code:`SER_TEL2_BAUD`. But the default of 921600 should be just fine.

Install px4_msgs
================

A commit that is tested to be working with the above mentioned version of PX4 is :code:`cfed39a`.

Clone it into the ROS workspace

.. code-block:: sh

   git clone https://github.com/PX4/px4_msgs.git

Install Micro-ROS
=================

A tested version is commit :code:`cdd082b`. Newer versions might work as well.

Clone the repository into the ROS workspace.

.. code-block:: sh

   git clone https://github.com/micro-ROS/micro_ros_setup.git


and build the :code:`micro-ros-agent`

.. code-block:: sh

   ros2 run micro_ros_setup create_agent_ws.sh
   ros2 run micro_ros_setup build_agent.sh

Running the Micro-ROS-Agent
===========================

Replace device and baudrate with the correct values.

.. code-block:: sh

   ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyUSB0 -b 921600

If the setup is working, :code:`ros2 topic list` should show the FMUs in and out topics.

.. code-block:: sh

   /fmu/in/obstacle_distance
   /fmu/in/offboard_control_mode
   /fmu/in/onboard_computer_status
   /fmu/in/sensor_optical_flow
   /fmu/in/telemetry_status
   /fmu/in/trajectory_setpoint
   /fmu/in/vehicle_attitude_setpoint
   /fmu/in/vehicle_command
   /fmu/in/vehicle_mocap_odometry
   /fmu/in/vehicle_rates_setpoint
   /fmu/in/vehicle_trajectory_bezier
   /fmu/in/vehicle_trajectory_waypoint
   /fmu/in/vehicle_visual_odometry
   /fmu/out/failsafe_flags
   /fmu/out/sensor_combined
   /fmu/out/timesync_status
   /fmu/out/vehicle_attitude
   /fmu/out/vehicle_control_mode
   /fmu/out/vehicle_local_position
   /fmu/out/vehicle_odometry
   /fmu/out/vehicle_status
   /parameter_events
   /rosout

