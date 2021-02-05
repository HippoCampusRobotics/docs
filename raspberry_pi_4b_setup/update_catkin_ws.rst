Update Catkin Workspace
#######################

If you want to update already existing packages in the :file:`/ros_catkin_ws`, you have to update the :file:`.rosinstall` file and merge it with your current workspace with :code:`wstool`.

.. attention:: 
   
   We assume here that you haven't added any new ROS packages by following the :ref:`raspberry_pi_4b_setup/install_ros_packages:Install ROS packages` guide. If you have, these won't be updated by following these steps.

#. Change directory

   .. code-block:: sh

      cd ~/ros_catkin_ws

#. Update your :file:`.rosinstall` file

   - First, move your existing rosinstall file (assuming :code:`melodic-ros_comm-perception-wet.rosinstall`) so that it doesn't get overwritten:

      .. code-block:: sh

         mv -i melodic-ros_comm-perception-wet.rosinstall melodic-ros_comm-perception-wet.rosinstall.old

   - Generate new rosinstall file with same, but updated packages: 

      .. code-block:: sh

         rosinstall_generator ros_comm perception --rosdistro melodic --deps --wet-only --tar > melodic-ros_comm-perception-wet.rosinstall

   - You can compare the new rosinstall file to the old version to see which packages will be updated: 

      .. code-block:: sh 

         diff -u melodic-ros_comm-perception-wet.rosinstall melodic-ros_comm-perception-wet.rosinstall.old

#. Merge

   .. code-block:: sh

      wstool merge -t src melodic-ros_comm-perception-wet.rosinstall

#. Update

   .. code-block:: sh

      wstool update -t src


#. Build

   .. code-block:: sh

      sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release





