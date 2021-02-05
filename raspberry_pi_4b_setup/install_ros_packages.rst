Install ROS Packages
####################

If you want to install a new package, for example :file:`apriltag_ros` you can generate a new :file:`.rosinstall` file and merge it with your current workspace with :code:`wstool`.

.. todo:: 

   Updating a catkin workspace were packages have been added this way will not work by following :ref:`raspberry_pi_4b_setup/update_catkin_ws:Update Catkin Workspace`. We need to find a good solution of keeping track of packages that have been installed by merging a seperate :file:`.rosinstall` file with :code:`wstool`.


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