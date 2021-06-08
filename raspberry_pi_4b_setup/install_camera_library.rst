Install MIPI Camera Library
###########################

If the Raspberry Pi uses an OV9281 camera, you will have to install the MIPI camera library by Arducam.


32-bit Library
==============

.. code-block:: sh

   cd && git clone https://github.com/ArduCAM/MIPI_Camera.git

.. code-block:: sh

   cd ~/MIPI_Camera/RPI && make install

64-bit Library
==============

.. code-block:: sh

   git clone https://github.com/raspberrypi/userland
   cd userland
   git revert f97b1af1b3e653f9da2c1a3643479bfd469e3b74
   git revert e31da99739927e87707b2e1bc978e75653706b9c

.. code-block:: sh

   export LDFLAGS="-Wl,--no-as-needed"
   ./buildme --aarch64
   sudo cp build/lib/*.so /usr/lib/aarch64-linux-gnu/

.. code-block:: sh

   cd && git clone https://github.com/ArduCAM/MIPI_Camera.git 
   sudo cp MIPI_Camera/RPI/lib/aarch64/libarducam_mipicamera.so /usr/lib

