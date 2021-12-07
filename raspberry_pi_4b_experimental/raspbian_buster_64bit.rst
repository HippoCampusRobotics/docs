Raspbian Buster 64bit
=====================

An experimental 64bit image of Raspbian can be downloaded from `here <https://downloads.raspberrypi.org/raspios_arm64/images/>`__. The advantage of the 64bit version are the prebuilt packages for ROS. But at the same time problems regarding the camera can occure. The Arducam library depends on MMAL. This is not prebuilt for 64bit systems. It would be rather nice to not rely on Arducam's OV9281 camera board but to use an USB camera. But for now this is how it is.

Preparation
###########

Append the following to :file:`/boot/config.txt`:

.. code-block:: sh

   # enable additional uarts if you need them
   dtoverlay=uart4
   dtoverlay=uart5
   # enable login via serial console
   enable_uart=1
   # enable camera
   start_x=1
   # increase GPU memory if camera is used.
   gpu_mem=256
   # Needed for OV9281 camera. Feel free to remove this line if not needed.
   dtparam=i2c_vc=on

Also create an empty :file:`ssh` file on :file:`/boot` and change the hostname according to our general naming convention in :ref:`raspberry_pi_4b_setup/pre_boot_configuration:Pre-Boot Configuration`.

Install ROS
###########

You can in general follow the official installation guidelines at the `ROS wiki <http://wiki.ros.org/noetic/Installation/Ubuntu>`__ (even if it is the Ubuntu guide). 

Compile Userland Libraries
##########################

.. code-block:: sh

   git clone https://github.com/raspberrypi/userland && cd userland
.. code-block:: sh

   git revert f97b1af1b3e653f9da2c1a3643479bfd469e3b74

.. code-block:: sh

   git revert e31da99739927e87707b2e1bc978e75653706b9c

.. code-block:: sh

   export LDFLAGS="-Wl,--no-as-needed"
   ./buildme --aarch64

.. code-block:: sh

   sudo cp build/lib/*.so /usr/lib/aarch64-linux-gnu/

Install Arducam Library
#######################

.. code-block:: sh

   cd && git clone https://github.com/ArduCAM/MIPI_Camera.git

.. code-block:: sh

   sudo cp MIPI_Camera/RPI/lib/aarch64/libarducam_mipicamera /usr/lib/

Create Symbolic Links
#####################

In our `camera package <https://github.com/hippoCampusRobotics/camera>`__ is a script to create necessary symlinks for the libraries. Otherwise the linker will complain because of undefined references when executing :code:`catkin build`.