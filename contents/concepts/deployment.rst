.. _deployment_concept:

Automated Deployment
####################

.. attention::

   This section is (so far) only relevant for the old BlueROV2, :code:`bluerov-01`. On this vehicle, we start all ROS nodes automatically at boot.

Some ROS nodes are required to be running on the on-board Pis for all typical deployment setups and are started automatically.
This mainly refers to nodes representing hardware interfaces.
We use ``systemd`` for starting these nodes.

In many cases no manual interaction with the Raspberry Pis inside the vehicles is required, since all required nodes are started automatically at boot.

Github Repository
=================

The deployment-related files for the robot setup are collected in the
hippo_deployment_ repository. This includes systemd service files, udev rules,
and helper scripts used to start and monitor the ROS 2 nodes on the robot.

.. _hippo_deployment: https://github.com/HippoCampusRobotics/hippo_deployment

Where can I find the services that are starting the nodes?
==========================================================

The system services require the ``VEHICLE_NAME`` variable to be exported in the :file:`~/.zshrc` file.

The files are in :file:`/etc/systemd/system/`

.. code-block:: console

   $ tree /etc/systemd/system
   
   /etc/systemd/system/
   ├── ...
   ├── ros-camera.service
   ├── ros-camera-servo.service
   ├── ros-dvl.service
   ├── ros-esc.service
   ├── ros-spotlight.service
   ├── ros-startup-sequence.service
   ├── ros-xrce-agent.service
   ├── tmux-main.service
   └── tmux-monitoring.service

For all *enabled* services symlinks are created automatically inside :file:`default.target.wants/`.
The term *enabled* means that these services are started automatically.

How can I tell if my services are alright?
==========================================

The respective service's status can be checked via (in this example for ``ros-esc.service``)

.. code-block:: console

   $ systemctl status ros-esc.service
   ● ros-esc.service - ESC Commander
        Loaded: loaded (/etc/systemd/system/ros-esc.service; enabled; vendor preset: enabled)
        Active: active (running) since Tue 2024-07-02 10:07:11 CEST; 19min ago
      Main PID: 669 (ros2)
         Tasks: 17 (limit: 9244)
        Memory: 43.0M
           CPU: 11.888s
        CGroup: /system.slice/ros-esc.service
                ├─ 669 /usr/bin/python3 /opt/ros/iron/bin/ros2 launch esc teensy_esc.launch.py vehicle_name:=bluerov01 use_sim_time:=false
                └─1798 /home/pi/ros2/install/esc/lib/esc/teensy_commander_node --ros-args -r __node:=esc_commander -r __ns:=/bluerov01 --params-file /tmp/launch_params_9m7zs_6r --params-file /home/pi/ros2/install/esc/share/esc/config/teensy_config.yaml

   Jul 02 10:07:28 klopsi-main-01 zsh[669]: [INFO] [launch]: All log files can be found below /home/pi/.ros/log/2024-07-02-10-07-28-093346-klopsi-main-01-669
   Jul 02 10:07:28 klopsi-main-01 zsh[669]: [INFO] [launch]: Default logging verbosity is set to INFO
   Jul 02 10:07:28 klopsi-main-01 zsh[669]: [INFO] [teensy_commander_node-1]: process started with pid [1798]
   Jul 02 10:07:29 klopsi-main-01 zsh[669]: [teensy_commander_node-1] [WARN] [1719907649.872115519] [bluerov01.esc_commander]: '/bluerov01/thruster_command' controls timed out.
   Warning: journal has been rotated since unit was started and some journal files were not opened due to insufficient permissions, output may be incomplete.

We can observe that is is active and running.

For more convenience we have a ``tmux`` monitoring session.
We can switch to another session by :kbd:`ctrl-a s` and choose the desired session from the list.

.. note::

   The monitoring session is not meant for interaction but for reading the logs only.
   Neither enter anything nor hit :kbd:`ctrl-c` there.
   If you you failed to so do it is possible to restart the monitoring session with

   .. code-block:: console

      $ sudo systemctl restart tmux-monitoring.service

Monitoring does not hurt nobody.
It does no harm to the underlying processes that are monitored and restarting the monitoring session will cleanup the old one before starting the new session.
   
What about optional nodes that I want to run occasionally?
==========================================================

If there is already a service available we can start it without enabling it.
It will run until

* it finishes/crashes
* it is stopped via ``sudo systemctl stop my-service.service``
* the Raspberry Pi is rebooted

If we require a certain setup for a certain period and do not want to start it manually each time, we can enable the service for this period for sure!

.. code-block:: console

   $ sudo systemctl enable --now my-newly-enabled-service.service

We can disable it on some future date.
A problem for future-you!

.. code-block:: console

   $ sudo systemctl disable --now my-newly-enabled-service.service

How do I write such a service?
==============================

The following example might be already self-explanatory.
Simply change ``Description`` and ``ExecStart``.

.. code-block:: systemd

   [Unit]
   Description=ESC Commander

   [Service]
   Type=simple
   ExecStart=/usr/bin/zsh -i -c 'ros2 launch esc teensy_esc.launch.py vehicle_name:="$VEHICLE_NAME" use_sim_time:=false'
   User=pi

   [Install]
   WantedBy=multi-user.target

.. note::

   Do not forget to set the user to ``pi`` with ``User=pi``.
