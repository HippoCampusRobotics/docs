ROS2 Workspace
##############

.. attention:: The following workspace structure is recommended in general, but is mandatory for shared devices (i.e. every device that is ot your own computer, like Raspberry Pis or lab computers) to avoid confusion.

We use :file:`ros2` as depicted in :numref:`ros2-dev-workspace-structure` as development workspace and :file:`ros2_underlay` shown in :numref:`ros2-underlay-workspace-structure` for larger manually compiled non-development packages that take a lot of time to compile/recompile.

.. code-block:: bash
   :caption: Development Workspace
   :name: ros2-dev-workspace-structure

   ~/ros2
   ├── build
   │   └── ...
   ├── install
   │   └── ...
   ├── log
   │   └── ...
   └── src
      ├── hippo_core                   # required for every ros2 workspace
      ├── hippo_simulation             # not needed for Raspberry Pi setups
      ├── qualisys_bridge              # only needed for the computer running the qualisys bridge
      ├── rapid_trajectories           # example for your custom development ros packages
      ├── rapid_trajectories_msgs      # exampale for your corresponding custom msg package
      └── ...
   
.. code-block:: bash
   :caption: Underlay Workspace
   :name: ros2-underlay-workspace-structure

   ~/ros2_underlay
   ├── build
   │   └── ...
   ├── install
   │   └── ...
   ├── log
   │   └── ...
   └── src
      ├── apriltag_ros
      ├── PlotJuggler
      └── px4_msgs                     # Takes very long to build! Even if built already.



Having them in a separate workspace reduces compilation time for the development workspace.
Typical packages for :file:`ros2_underlay` are :code:`plot_juggler`, :code:`px4_msgs`, :code:`apriltag_ros` and everything that is not going to be modified regularily. 
