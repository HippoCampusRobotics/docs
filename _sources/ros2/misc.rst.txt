Misc
####

Build Command
*************

Symlink builds are recommended, so symbolic links to :file:`src` are used where possible. 


.. code-block:: sh
   
   colcon build --symlink-install

In case :file:`compile_commands.json` is needed for parsing/autocompletion

.. code-block:: sh

   colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON

.. attention:: 
   If one likes to source the custom workspace in :file:`.zshrc`, make sure you do **not** use this environment to build the workspace. Instead run the build command in — for example — :code:`bash`, where you only source workspaces outside the workspace you want to build! To avoid inheriting environment variables you can run :code:`env -i bash` or for a docker setup run

   .. code-block:: sh

      docker exec -it ros2 bash

.. hint:: 
   On a native Ubuntu installation, aliases for building the ROS workspaces are quite handy.

   .. code:: sh

      alias build_ros="env -i HOME=$HOME USER=$USER TERM=xterm-256color bash -l -c 'source $HOME/ros2_underlay/install/setup.bash && cd $HOME/ros2 && colcon build --symlink-install --cmake-args -DCMAKE_EXPORT_COMPILE_COMMANDS=ON'"
      alias build_underlay="env -i HOME=$HOME USER=$USER TERM=xterm-256color bash -l -c 'source /opt/ros/humble/setup.bash && cd $HOME/ros2_underlay && colcon build'"

   The development workspace and the underlay can be built from any directory with the commands :code:`build_ros` and :code:`build_underlay`, respectively.


Installing Dependencies
***********************

.. code-block:: sh

   rosdep install --from-paths src -y --ignore-src


Auto-Complete
*************

.. attention:: ROS2 command line tools do not autocomplete as of this `GitHub Issue <https://github.com/ros2/ros2cli/issues/534>`_. While this issue has since been closed, the problem still occurs. To fix it, add the following to :code:`.zshrc`.

.. code-block::
   :name: test
   
   eval "$(register-python-argcomplete3 ros2)"
   eval "$(register-python-argcomplete3 colcon)"

.. attention:: Auto-completing topic names seems to work only after an execution of `ros2 topic list`. Before the auto-complete gets stuck and has to be canceled by :kbd:`Ctrl` + :kbd:`C`.

.. note:: Sourcing :file:`install/setup.zsh` might reset this. Better source :file:`install/local_setup.zsh`.

Verifying XACRO
***************

.. code-block:: sh

   check_urdf <(xacro path/to/your/file.xacro)
