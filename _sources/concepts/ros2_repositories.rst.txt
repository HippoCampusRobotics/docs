ROS2 Repositories
#################

`hippo_core <https://github.com/hippoCampusRobotics/hippo_core>`__ 
==================================================================

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
==============================================================================

These packages contain code required for the gazebo simulation, i.e. models. ,plugins, etc. Since they have many dependencies and are not required for devices inside the real robots, the simulation related code has its own repository.

.. code-block:: bash

   hippo_simulation
   ├── hippo_gz_plugins    # contains gazebo plugins required for the simulation.
   ├── hippo_sim           # contains models and launch files for the gazebo sim.
   └── README.md

