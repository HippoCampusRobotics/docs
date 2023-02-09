AprilTag
========

There is a `PR <https://github.com/AprilRobotics/apriltag_ros/pull/114>`__ for porting the good old :code:`apriltag_ros` package to ROS2. 

.. code-block:: sh

   https://github.com/wep21/apriltag_ros/tree/ros2-port/apriltag_ros

There is an alternative `package <https://github.com/christianrauch/apriltag_ros>`__ by Christian Rauch, that works somewhat different but has a simpler code base. Unfortunately it does not support tag bundles.


Generate Parameter Files
########################

To either select the tags, that should be detected, or create a tag bundle configuration, run

.. code-block:: sh

   ros2 run hippo_sim generate_tag_poses.py --out-dir `pwd`

to create the corresponding files in the current directory.

To show the list of available arguments run

.. code-block:: sh

   ros2 run hippo_sim generate_tag_poses.py -h
