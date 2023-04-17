Concepts
########

ROS2 Workspace
==============

.. attention:: The following workspace structure is recommended in general, but is mandatory for shared devices (i.e. every device that is ot your own computer, like Raspberry Pis or lab computers) to avoid confusion.

We use :file:`ros2` as depicted in :numref:`ros2-dev-workspace-structure` as development workspace and :file:`ros2_underlay` shown in :numref:`ros2-underlay-workspace-structure` for larger manually compiled non-development packages that take a lot of time to compile/recompile.

.. code-block:: bash
   :caption: Development Workspace
   :name: ros2-dev-workspace-structure

   ~/ros2
   ├── build
   │   └── ...
   ├── install
   │   └── ...
   ├── log
   │   └── ...
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
   │   └── ...
   ├── install
   │   └── ...
   ├── log
   │   └── ...
   └── src
      ├── apriltag_ros
      ├── PlotJuggler
      └── px4_msgs                     # Takes very long to build! Even if built already.



Having them in a separate workspace reduces compilation time for the development workspace.
Typical packages for :file:`ros2_underlay` are :code:`plot_juggler`, :code:`px4_msgs`, :code:`apriltag_ros` and everything that is not going to be modified regularily. 

`hippo_core <https://github.com/hippoCampusRobotics/hippo_core>`__ 
------------------------------------------------------------------

Contains required ROS packages used in every ROS setup.

.. code-block:: bash

   hippo_core
   ├── esc
   ├── hippo_common        # contains utility and convenience functions
   ├── hippo_control       # basic control and actuator mixer code
   ├── hippo_gz_msgs       # custom gazebo protobuf message definitions
   ├── hippo_msgs          # general hippo_msgs that are not in a separate msg package.
   └── README.md


`hippo_simulation <https://github.com/HippoCampusRobotics/hippo_simulation>`__
------------------------------------------------------------------------------

These packages contain code required for the gazebo simulation, i.e. models. ,plugins, etc. Since they have many dependencies and are not required for devices inside the real robots, the simulation related code has its own repository.

.. code-block:: bash

   hippo_simulation
   ├── hippo_gz_plugins    # contains gazebo plugins required for the simulation.
   ├── hippo_sim           # contains models and launch files for the gazebo sim.
   └── README.md

