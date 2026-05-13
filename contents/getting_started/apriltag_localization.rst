Apriltag Localization
#####################


This page explains how to start and check the AprilTag localization setup.

The setup is used to estimate the vehicle pose from AprilTags observed by a camera. For the BlueROV, the usual localization setup uses the ``vertical_camera``. The BlueROV also has a ``front_camera`` that has been mostly used for the Formulas and Vehicles class. HippoCampus only has one ``vertical_camera``.

The image transport pipeline is intentionally split between the robot and the offboard computer:

.. code-block:: text

   robot / camera Pi:
     image_raw/compressed
     camera_info

   offboard PC:
     image_decoder:
       image_raw/compressed -> image_raw

     rectifier:
       image_raw + camera_info -> image_rect

     apriltag_node:
       image_rect + camera_info -> detections + tag_transforms

     vision_ekf_node:
       tag_transforms + known tag poses -> vision_pose_cov

The compressed image is sent over the network. The raw and rectified images should usually only be used on the offboard computer.


Supported Setups
----------------

There are three main launch files.

.. list-table::
   :header-rows: 1

   * - Launch file
     - Use case
     - Default camera
   * - ``top_localization.launch.py``
     - Standard AprilTag localization
     - ``vertical_camera``
   * - ``top_localization_for_sems.launch.py``
     - Class setup. Includes the standard localization launch and additionally starts the vehicle TF publisher.
     - ``vertical_camera``
   * - ``top_ranges.launch.py``
     - BlueROV front-camera range setup
     - ``front_camera``

.. note::

   ``top_ranges.launch.py`` is intended for the BlueROV ``front_camera`` setup. Do not use it as the normal vertical-camera localization launch.

Launch Arguments
----------------

Check the available launch arguments with:

.. code-block:: bash

   ros2 launch visual_localization top_localization.launch.py --show-args
   ros2 launch visual_localization top_localization_for_sems.launch.py --show-args
   ros2 launch visual_localization top_ranges.launch.py --show-args


Start the Robot Camera
----------------------

First, start the normal robot setup. For the BlueROV, use the usual hardware launch on the Raspberry Pi that hosts the selected camera.

For the vertical camera, check that the compressed image and camera info are available:

.. code-block:: bash

   ros2 topic list -t | grep vertical_camera

Expected before starting the localization launch:

.. code-block:: text

   /bluerov01/vertical_camera/camera_info [sensor_msgs/msg/CameraInfo]
   /bluerov01/vertical_camera/image_raw/compressed [sensor_msgs/msg/CompressedImage]

Check the rate and bandwidth:

.. code-block:: bash

   ros2 topic hz /bluerov01/vertical_camera/image_raw/compressed
   ros2 topic bw /bluerov01/vertical_camera/image_raw/compressed
   ros2 topic info /bluerov01/vertical_camera/image_raw/compressed -v

Do not expect ``image_raw`` or ``image_rect`` to exist yet. These are created by the offboard decoder and rectifier.


Launch Setups
-------------

.. tabs::

   .. tab:: Standard Localization

      Use this for the normal AprilTag localization setup.

      .. code-block:: bash

         ros2 launch visual_localization top_localization.launch.py \
            vehicle_name:=bluerov01 \
            use_sim_time:=false

      To enable the AprilTag overlay image:

      .. code-block:: bash

         ros2 launch visual_localization top_localization.launch.py \
            vehicle_name:=bluerov01 \
            use_sim_time:=false \
            use_apriltag_viz:=true

      The standard launch expects the required vehicle TF tree to already be available. It does not start the vehicle TF publisher.

   .. tab:: SEMS/FAV Setup for BlueROV

      .. code-block:: bash

         ros2 launch visual_localization top_localization_for_sems.launch.py \
            vehicle_name:=bluerov01 \
            use_sim_time:=false

      This launch file includes ``top_localization.launch.py`` and additionally starts the vehicle TF publisher. It also starts the AprilTag overlay image by default.

      Use this launch when the normal robot TF publisher is not already running.

      .. attention::

         Do not start two vehicle TF publishers for the same vehicle unless this is intentional. Duplicate node names or duplicate TF publishers can make debugging difficult.

   .. tab:: Front Camera Ranges Setup (Assignment 2 SEMS/FAV)

      .. code-block:: bash

         ros2 launch visual_localization top_ranges.launch.py \
            vehicle_name:=bluerov01 \
            use_sim_time:=false

      This launch uses ``front_camera`` and ``apriltag_ranges_config.yaml`` by default.

      Check:

      .. code-block:: bash

         ros2 node list | grep front_camera
         ros2 topic list -t | grep front_camera

      Expected topics include:

      .. code-block:: text

         /bluerov01/front_camera/image_raw/compressed
         /bluerov01/front_camera/image_raw
         /bluerov01/front_camera/image_rect
         /bluerov01/front_camera/detections
         /bluerov01/front_camera/tag_transforms
         /bluerov01/front_camera/tag_detections_image
   
      .. attention::

         This Launch setup is meant only for the front camera of the BlueROV. It is used to detect tags at the front wall of the tank.



Check the Image Pipeline
------------------------

After starting localization, check the vertical-camera pipeline:

.. code-block:: bash

   ros2 topic list -t | grep vertical_camera

Expected topics include:

.. code-block:: text

   /bluerov01/vertical_camera/image_raw/compressed
   /bluerov01/vertical_camera/image_raw
   /bluerov01/vertical_camera/image_rect
   /bluerov01/vertical_camera/detections
   /bluerov01/vertical_camera/tag_transforms

Check the node connections:

.. code-block:: bash

   ros2 node info /bluerov01/vertical_camera/rectifier
   ros2 node info /bluerov01/vertical_camera/apriltag_node

Expected:

.. code-block:: text

   rectifier subscribes:
     image_raw
     camera_info

   rectifier publishes:
     image_rect

   apriltag_node subscribes:
     image_rect
     camera_info

   apriltag_node publishes:
     detections
     tag_transforms

The AprilTag detector publishes ``detections`` at camera rate even if no tags are detected. Empty detections do not necessarily mean that the image pipeline is broken.

Display the Camera Image
------------------------

On the offboard PC running the decoder, display the rectified image:

.. code-block:: bash

   ros2 run rqt_image_view rqt_image_view

Select:

.. code-block:: text

   /bluerov01/vertical_camera/image_rect

This is the image used by the AprilTag detector.

If the AprilTag visualization node is running, display:

.. code-block:: text

   /bluerov01/vertical_camera/tag_detections_image

This image overlays detected tags on the rectified image.

.. attention::

   Do not subscribe to raw image topics from another computer unless this is intentional. Raw image topics can create high network load. For remote viewing, prefer compressed image transport.

Check Detections
----------------

Show the detection messages:

.. code-block:: bash

   ros2 topic echo /bluerov01/vertical_camera/detections --once

Show the tag transforms:

.. code-block:: bash

   ros2 topic echo /bluerov01/vertical_camera/tag_transforms --once

Check that the detected tag IDs are present in the configured ``tag_poses_file``.

Also check that there is only one AprilTag publisher:

.. code-block:: bash

   ros2 topic info /bluerov01/vertical_camera/tag_transforms -v

Expected:

.. code-block:: text

   Publisher count: 1
   Node name: apriltag_node
   Node namespace: /bluerov01/vertical_camera

If there is more than one publisher, an old launch process may still be running.

.. Check the Required TF Transform
.. -------------------------------

.. The localization node needs the transform between the vehicle base frame and the camera frame used by the AprilTag measurement.

.. For the real BlueROV setup, check:

.. .. code-block:: bash

..    ros2 run tf2_ros tf2_echo bluerov01/base_link bluerov01/vertical_camera_frame

.. For simulation, the camera frame may be different. Check the frame in the tag transform message:

.. .. code-block:: bash

..    ros2 topic echo /uuv00/vertical_camera/tag_transforms --once

.. The relevant camera frame is the ``header.frame_id`` of the tag transform. In simulation this may be:

.. .. code-block:: text

..    uuv00/vertical_camera

.. This can be different from:

.. .. code-block:: text

..    uuv00/vertical_camera_frame

.. These frames are not necessarily identical.

.. .. note::

..    The localization node should use the frame from the AprilTag transform header and look up the transform from ``base_link`` to that frame.


AprilTag Wrapper Convention
---------------------------

There are two AprilTag ROS setups in use:

.. code-block:: text

   old HippoCampus fork
   released apriltag_ros wrapper

The wrapper that is used depends on the sourced workspace. Check it with:

.. code-block:: bash

   ros2 pkg prefix apriltag_ros

If this points to ``/opt/ros/jazzy``, the released package is used. If it points to a workspace such as ``ros2_underlay``, the local fork is used.

The tag frame convention can differ between wrappers and pose estimation methods. The EKF therefore applies a fixed correction from the detected tag frame convention to the tag frame convention used in ``tag_poses.yaml``.

For the old fork, use:

.. code-block:: yaml

   tag_frame_correction_rpy_deg: [0.0, 0.0, 0.0]

For the released wrapper with ``pose_estimation_method: pnp``, use:

.. code-block:: yaml

   tag_frame_correction_rpy_deg: [180.0, 0.0, 0.0]

This correction is independent of the camera transform. It only converts between tag-frame axis conventions.

.. Simulation
.. ----------

.. The simulation launch can be used to test the AprilTag EKF before testing on the real robot.

.. Start the simulation EKF test:

.. .. code-block:: bash

..    ros2 launch visual_localization top_test_ekf_in_simulation.launch.py \
..      vehicle_name:=uuv00 \
..      vehicle_type:=hippocampus \
..      use_sim_time:=true \
..      start_gui:=true \
..      use_ekf:=true \
..      use_apriltag_viz:=true

.. Start with the path follower:

.. .. code-block:: bash

..    ros2 launch visual_localization top_test_ekf_in_simulation.launch.py \
..      vehicle_name:=uuv00 \
..      vehicle_type:=hippocampus \
..      use_sim_time:=true \
..      start_gui:=true \
..      use_ekf:=true \
..      use_path_follower:=true \
..      use_apriltag_viz:=true

.. To manually send a thrust setpoint in x direction:

.. .. code-block:: bash

..    ros2 topic pub -r 50 /uuv00/thrust_setpoint hippo_control_msgs/msg/ActuatorSetpoint "{x: 0.3}"

.. Stop with ``Ctrl-C``.

.. .. note::

..    In simulation, there may be more than one camera-related TF branch. The AprilTag measurement is expressed in the frame given by the tag transform header. Use this frame when checking the EKF transform chain.

Troubleshooting
---------------

``image_raw`` does not exist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The image decoder is not running or is in the wrong namespace.

Check:

.. code-block:: bash

   ros2 node list | grep image_decoder

Manual decoder test:

.. code-block:: bash

   ros2 run visual_localization image_decoder --ros-args \
     -r __ns:=/bluerov01/vertical_camera

``image_rect`` does not exist
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The rectifier is not running, ``image_raw`` is missing, or ``camera_info`` is missing.

Check:

.. code-block:: bash

   ros2 node info /bluerov01/vertical_camera/rectifier

``detections`` publishes but contains no tags
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Possible reasons:

.. code-block:: text

   no tag visible
   wrong tag family
   wrong tag size
   tag too small in the image
   bad lighting or motion blur
   wrong camera calibration
   wrong tag config

``tag_transforms`` has more than one publisher
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This usually means that an old AprilTag process is still running.

Check:

.. code-block:: bash

   ros2 topic info /bluerov01/vertical_camera/tag_transforms -v
   ps aux | grep apriltag_node | grep -v grep

Clean stale vertical-camera nodes:

.. code-block:: bash

   pkill -f "apriltag_node.*__ns:=/bluerov01/vertical_camera"
   pkill -f "vision_ekf_node.*__ns:=/bluerov01/vertical_camera"
   pkill -f "apriltag_viz.*__ns:=/bluerov01/vertical_camera"
   pkill -f "image_decoder.*__ns:=/bluerov01/vertical_camera"
   pkill -f "topic_tools.*relay.*__ns:=/bluerov01/vertical_camera"

Use ``pkill -f`` carefully. It kills all matching processes.

Duplicate node names
^^^^^^^^^^^^^^^^^^^^

Check exact duplicates:

.. code-block:: bash

   ros2 node list | sort | uniq -d

Check running localization-related processes:

.. code-block:: bash

   ps aux | grep -E "apriltag_node|vision_ekf_node|apriltag_viz|image_decoder|ranges|relay|component_container" | grep -v grep

If no stale processes remain but the ROS graph still looks wrong, restart the ROS daemon:

.. code-block:: bash

   ros2 daemon stop
   ros2 daemon start

``rqt`` shows a compressed topic in red
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not directly select:

.. code-block:: text

   /bluerov01/vertical_camera/image_raw/compressed

as a raw image topic in ``rqt_image_view``. Select the base topic with compressed transport if needed, or view the decoded/rectified image on the offboard computer.

For AprilTag debugging, prefer:

.. code-block:: text

   /bluerov01/vertical_camera/image_rect

or:

.. code-block:: text

   /bluerov01/vertical_camera/tag_detections_image

