Install ROS Packages
####################

If you want to install a new package, for example :file:`apriltag_ros` you can generate a new :file:`.rosinstall` file and merge it with your current workspace with :code:`wstool`.

#. Change directory

   .. code-block:: sh

      cd ~/ros_catkin_ws

#. New :file:`.rosinstall` file

   .. code-block:: sh

      rosinstall_generator apriltag apriltag_ros > apriltag_ros.rosinstall

#. Merge

   .. code-block:: sh

      wstool merge -t src apriltag_ros.rosinstall

#. Update

   .. code-block:: sh

      wstool update -t src

#. Install dependencies

   .. code-block:: sh

      rosdep install -y --from-paths src --ignore-src -r

#. Build

   .. code-block:: sh

      sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release