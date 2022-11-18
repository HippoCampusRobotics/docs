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
