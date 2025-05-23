.. _px4-setup:

PX4 Setup
#########

.. note::
   PX4 is currently used for the real robot exclusively and is not part of the simulation.
   Skip this section if you are **not** preparing for the lab experiments.
   If in doubt ask your supervisor.

Building the Firmware
=====================

If PX4 is used in combination with the onboard computer, make sure the firmware running on the FCU was built with RTPS support.

A tested PX4-Version is the commit :code:`45b390b0bf`.

.. code-block:: console

   $ git clone https://github.com/PX4/PX4-Autopilot.git \
   && cd PX4-Autopilot \
   && git checkout 45b390b0bf \
   && git submodule update --init --recursive

For this version the RTPS support is *not* enabled by default for the :code:`fmu-v4` target (i.e. the PixRacer). One has to modify the file :file:`boards/px4/fmu-v4/default.px4board` and add the line

.. code-block:: sh

   CONFIG_MODULES_MICRODDS_CLIENT=y


Also modify the autostart-line in :file:`src/modules/microdds_client/module.yaml` if you want to have a namespace prepended to the topic names

.. code-block:: sh

   set XRCE_DDS_ARGS "-t serial -d ${SERIAL_DEV} -b p:${BAUD_PARAM} -n uuv00"

Also a good starting point for a minimal set of bridged topics defined in :file:`src/modules/microdds_client/dds_topics.yaml` is

.. code-block:: yaml
   :linenos:
   :caption: src/modules/microdds_client/dds_topics.yaml

   publications:

     - topic: /fmu/out/failsafe_flags
       type: px4_msgs::msg::FailsafeFlags

     - topic: /fmu/out/sensor_combined
       type: px4_msgs::msg::SensorCombined

     - topic: /fmu/out/timesync_status
       type: px4_msgs::msg::TimesyncStatus

     - topic: /fmu/out/vehicle_odometry
       type: px4_msgs::msg::VehicleOdometry

   subscriptions:

     - topic: /fmu/in/vehicle_visual_odometry
       type: px4_msgs::msg::VehicleOdometry


Build the firmware

.. tabs::

   .. code-tab:: sh PixRacer

      make px4_fmu-v4

   .. code-tab:: sh PixRacer Docker
      
      ./Tools/docker_run.sh 'make px4_fmu-v4'
   
   .. code-tab:: sh PixHawk 6C

      make px4_fmu-v6c

   .. code-tab:: sh PixHawk 6C Docker

      ./Tools/docker_run.sh 'make px4_fmu-v6c'

Normally, the :code:`microdds_client` is started automatically, and no further actions are required. Anyhow, to manually start the :code:`microdds_client`, go to the :code:`nsh` terminal and run

.. code-block:: console

   $ microdds_client start -t serial -d /dev/ttyS2 -b 921600 -n uuv00


Configure the Firmware
======================

.. attention:: Make sure you disable the GPS completely by changing its control mode parameter. Otherwise the the vision will be taken as odometry data instead of absolute positions.

Set :code:`XRCE_DDS_0_CFG` to :code:`TELEM2`, i.e. :code:`102`. If you want to, you can change the baudrate of TELEM2 at :code:`SER_TEL2_BAUD`. But the default of 921600 should be just fine.

.. note:: Make sure you disable all MAVLink interfaces on :code:`TELEM2`.


Install px4_msgs
================

.. hint:: Building **and** rebuilding :file:`px4_msgs` takes very long, especially on the Raspberry Pi. Therefore, it is recommended to have an underlying workspace for packages that we are not modifying regularly.


A commit that is tested to be working with the above-mentioned version of PX4 is :code:`8a7f3da`.

Clone it into the ROS workspace

.. code-block:: console

   $ git clone https://github.com/PX4/px4_msgs.git \
   && cd px4_msgs \
   && checkout 8a7f3da

Install Micro-XRCE-DDS-Agent
============================

Clone and build the agent

.. code-block:: console

   $ cd ~/ros2_underlay/src \
   && git clone https://github.com/eProsima/Micro-XRCE-DDS-Agent.git \
   && build_underlay

Running the Micro-XRCE-DDS-Agent
================================

Replace device and baudrate with the correct values.

.. code-block:: console

   $ MicroXRCEAgent serial --dev /dev/fcu_data -b 921600

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


MAVLink Router / QGroundControl
===============================

QGroundControl is very useful to set parameters and to calibrate the sensors of the FCU. The MAVLink Router is needed to connect to the QGroundControl App on your (Desktop) computer.

If not installed on the Raspberry Pi of the vehicle:

.. code-block:: console

   $ git clone https://github.com/mavlink-router/mavlink-router.git \
   && cd mavlink-router \
   && git checkout 3b48da1

Build and install the code following the `official instructions <https://github.com/mavlink-router/mavlink-router>`__.


The configuration file is at :file:`/etc/mavlink-router/main.conf` and can contain the following:

.. code-block:: ini

   [General]

   [UartEndpoint USB]

   # Path to UART device. like `/dev/ttyS0`
   # Mandatory, no default value
   Device =/dev/ttyACM0
   Baud = 921600

   [UdpEndpoint hippo-celsius]
   Mode = normal
   Address = 192.168.0.115
   Port = 14550

Adjust the address to your ground control computer's IP address if you are not using the :file:`hippo-celsius` Desktop computer within the lab.

.. attention:: 

   The UDP Endpoint currently does not work for the very first connection. Manual way of connecting via TCP is described below.


Run the router via

.. code-block:: console

   $ mavlink-routerd


Manual Connection to QGroundControl
===================================

First, the mavlink router needs to be running on the vehicle.

In QGC, click on the top left corner icon -> Application settings -> Comm links -> Add


.. figure:: /res/images/qgc_where_to_find_settings.png

   Where to find the settings.

Add a TCP comm link with standard settings. Add the vehicle's name and IP address. It should look like this:

.. figure:: /res/images/qgc_manually_add_tcp_connection.png

   TCP comm link settings for UUV02.

Now, you should be able to connect. The vehicle setup page should open:

.. figure:: /res/images/qgc_vehicle_setup.png

.. note:: 

   After this first manual connection via TCP from your ground control station to the vehicle, the UDP endpoint should/will start working.


Sensor Calibration 
==================

You might have to calibrate the vehicle's sensors. Click on Sensors:

.. figure:: /res/images/qgc_sensors_setup.png

and follow the instructions.