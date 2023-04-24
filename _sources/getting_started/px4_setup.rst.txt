PX4 Setup
#########

.. note:: PX4 is currently used for the real robot exclusively and is not part of the simulation. Skip this section if you are not preparing for the lab experiments.

Building the Firmware
=====================

If PX4 is used in combination with the onboard computer, make sure the firmware running on the FCU was built with RTPS support.

A tested PX4-Version is the commit :code:`45b390b0bf`.

.. code-block:: sh

   git clone https://github.com/PX4/PX4-Autopilot.git --recursive \
   && cd PX4-Autopilot \
   && git checkout 45b390b0bf \
   && git submodule update --init --recursive

For this version the RTPS support is *not* enabled by default for the :code:`fmu-v4` target (i.e. the PixRacer). One has to modify the file :file:`boards/px4/fmu-v4/default.px4board` and add the line

.. code-block:: sh

   CONFIG_MODULES_MICRODDS_CLIENT=y


Also modify the autostart-line in :file:`src/modules/microdds_client/module.yaml` if you want to have a namespace prepended to the topic names

.. code-block:: sh

   set XRCE_DDS_ARGS "-t serial -d ${SERIAL_DEV} -b p:${BAUD_PARAM} -n uuv00"

Build the firmware

.. code-block:: sh

   make px4_fmu-v4

Normally, the :code:`microdds_client` is started automatically, and no further actions are required. Anyhow, to manually start the :code:`microdds_client`, go to the :code:`nsh` terminal and run

.. code-block:: sh

   microdds_client start -t serial -d /dev/ttyS2 -b 921600 -n uvv00


Configure the Firmware
======================

.. attention:: Make sure you disable the GPS completely by changing its control mode parameter. Otherwise the the vision will be taken as odometry data instead of absolute positions.

Set :code:`XRCE_DDS_0_CFG` to :code:`TELEM2`, i.e. :code:`102`. If you want to, you can change the baudrate of TELEM2 at :code:`SER_TEL2_BAUD`. But the default of 921600 should be just fine.

Install px4_msgs
================

.. hint:: Building **and** rebuilding :file:`px4_msgs` takes very long, especially on the Raspberry Pi. Therefore, it is recommended to have an underlying workspace for packages that we are not modifying regularly.


A commit that is tested to be working with the above-mentioned version of PX4 is :code:`8a7f3da`.

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

   /uuv00/fmu/in/obstacle_distance [px4_msgs/msg/ObstacleDistance]
   /uuv00/fmu/in/offboard_control_mode [px4_msgs/msg/OffboardControlMode]
   /uuv00/fmu/in/onboard_computer_status [px4_msgs/msg/OnboardComputerStatus]
   /uuv00/fmu/in/sensor_optical_flow [px4_msgs/msg/SensorOpticalFlow]
   /uuv00/fmu/in/telemetry_status [px4_msgs/msg/TelemetryStatus]
   /uuv00/fmu/in/trajectory_setpoint [px4_msgs/msg/TrajectorySetpoint]
   /uuv00/fmu/in/vehicle_attitude_setpoint [px4_msgs/msg/VehicleAttitudeSetpoint]
   /uuv00/fmu/in/vehicle_command [px4_msgs/msg/VehicleCommand]
   /uuv00/fmu/in/vehicle_mocap_odometry [px4_msgs/msg/VehicleOdometry]
   /uuv00/fmu/in/vehicle_rates_setpoint [px4_msgs/msg/VehicleRatesSetpoint]
   /uuv00/fmu/in/vehicle_trajectory_bezier [px4_msgs/msg/VehicleTrajectoryBezier]
   /uuv00/fmu/in/vehicle_trajectory_waypoint [px4_msgs/msg/VehicleTrajectoryWaypoint]
   /uuv00/fmu/in/vehicle_visual_odometry [px4_msgs/msg/VehicleOdometry]
   /uuv00/fmu/out/failsafe_flags [px4_msgs/msg/FailsafeFlags]
   /uuv00/fmu/out/sensor_combined [px4_msgs/msg/SensorCombined]
   /uuv00/fmu/out/timesync_status [px4_msgs/msg/TimesyncStatus]
   /uuv00/fmu/out/vehicle_attitude [px4_msgs/msg/VehicleAttitude]
   /uuv00/fmu/out/vehicle_control_mode [px4_msgs/msg/VehicleControlMode]
   /uuv00/fmu/out/vehicle_local_position [px4_msgs/msg/VehicleLocalPosition]
   /uuv00/fmu/out/vehicle_odometry [px4_msgs/msg/VehicleOdometry]
   /uuv00/fmu/out/vehicle_status [px4_msgs/msg/VehicleStatus]


