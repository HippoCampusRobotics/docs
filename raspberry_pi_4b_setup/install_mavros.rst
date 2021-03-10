Install MAVROS
##############

.. code-block:: sh

   cd ~/ros_catkin_ws

.. attention:: Use  :code:`kinetic` in the following command, even if your ROS distro is newer.

.. code-block:: sh

   rosinstall_generator --rosdistro kinetic mavlink | tee /tmp/mavros.rosinstall

.. code-block:: sh

   rosinstall_generator --upstream mavros | tee -a /tmp/mavros.rosinstall

.. attention:: If :code:`rosdep` fails to install dependencies, because they are not available in the repositories, install them via :code:`rosinstall_generator` and :code:`wstool`.

.. code-block:: sh

   wstool merge -t src /tmp/mavros.rosinstall
   wstool update -t src -j4
   sudo apt update
   rosdep install --from-paths src --ignore-src -y

So if your console output of :code:`rosdep install` is

.. code-block:: sh
   :linenos:

   ERROR: the following packages/stacks could not have their rosdep keys resolved
   to system dependencies:
   mavros: No definition of [geographic_msgs] for OS [debian]
   mavros_extras: No definition of [urdf] for OS [debian]
   test_mavros: No definition of [control_toolbox] for OS [debian]
   mavros_msgs: No definition of [geographic_msgs] for OS [debian]
   Continuing to install resolvable dependencies...

Execute

.. code-block:: sh

   rosinstall_generator urdf control_toolbox geographic_msgs | tee /tmp/mavros_deps.rosinstall

and

.. code-block:: sh

   wstool merge -t src /tmp/mavros_deps.rosinstall
   wstool update -t src -j4

rerun :code:`rosdep install` and make sure all dependecies get resolved.

.. note:: It might be necessary to do some iterations of :code:`rosdep install` and the manual installation of dependecies until everything compiles successfully.

Build the code:

.. code-block:: sh

   sudo catkin build --cmake-args -DCMAKE_BUILD_TYPE=Release

After the build process has finished cleanly, you might have to execute the geographiclib install script:

.. code-block:: sh

   sudo ./src/mavros/mavros/scripts/install_geographiclib_datasets.sh