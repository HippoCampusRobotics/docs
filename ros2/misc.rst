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


Auto-Complete
*************

.. attention:: Check if this `GitHub Isse <https://github.com/ros2/ros2cli/issues/534>`_ is resolved. If so, modify this document. Otherwise add the following to :code:`.zshrc`.

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
