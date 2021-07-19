Installing PX4
##############

We try to stick to the original PX4 software as much as possible.

Feel free to modifiy your fork of the autopilot as much as you want, but if you add functionality, that should be shared with the rest of the world, create a pull request.

.. note:: The following instructions assume, you want to clone the PX4-Autopilot in your home directory. If you don't, you have to modifiy the instructions accordingly.

Get The Code
============

.. code-block:: sh

    git clone --recursive https://github.com/PX4/PX4-Autopilot.git


Export Environment Variables
============================

.. code-block:: sh

    PX4_DIR=$HOME/PX4-Autopilot

Choose the option depending on your shell:

.. tabs::

    .. code-tab:: sh zsh

        echo "source $PX4_DIR/Tools/setup_gazebo.bash $PX4_DIR $PX4_DIR/build/px4_sitl_default > /dev/null" >> ~/.zshrc
        echo "export ROS_PACKAGE_PATH=\$ROS_PACKAGE_PATH:$PX4_DIR" >> ~/.zshrc
        echo "export ROS_PACKAGE_PATH=\$ROS_PACKAGE_PATH:$PX4_DIR/Tools/sitl_gazebo" >> ~/.zshrc

    .. code-tab:: sh bash

        echo "source $PX4_DIR/Tools/setup_gazebo.bash $PX4_DIR $PX4_DIR/build/px4_sitl_default > /dev/null" >> ~/.bashrc
        echo "export ROS_PACKAGE_PATH=\$ROS_PACKAGE_PATH:$PX4_DIR" >> ~/.bashrc
        echo "export ROS_PACKAGE_PATH=\$ROS_PACKAGE_PATH:$PX4_DIR/Tools/sitl_gazebo" >> ~/.bashrc


Build The Code
==============

Set up dependencies:

.. code-block:: sh

    cd ~/PX4-Autopilot && bash ./Tools/setup/ubuntu.sh

Install :code:`xmlstarlet` and :code:`python3-pip`:

.. code-block:: sh

    sudo apt install xmlstarlet python3-pip


Build the firmware:

.. code-block:: sh

    cd ~/PX4-Autopilot && make px4_fmu-v4_default

Build the simulation:

.. code-block:: sh

    DONT_RUN=1 make px4_sitl gazebo_uuv_hippocampus



Sensible Modifications
======================

Battery Invalid
***************

If the battery parameters are set up correctly and your battery values are not shown in QGroundControl, this might be because the firmware detects the battery errenously as invalid. This happens for example on the BlueROV, where the FCU is powered via USB and the power sense module provides only the measurements but not the supply voltage.

In :code:`analog_battery.cpp:l:83` the following expression evaluates as :code:`false`.

.. code-block:: cpp

    bool connected = voltage_v > BOARD_ADC_OPEN_CIRCUIT_V &&
			 (BOARD_ADC_OPEN_CIRCUIT_V <= BOARD_VALID_UV || is_valid());

As a quickfix, replace :code:`is_valid()` with :code:`true`.