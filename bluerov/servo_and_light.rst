Servo And Light
###############

The LED headlights and the camera servo are controlled via PWM signals. To get a jitter-free PWM signal, a library, supporting hardware PWM, is required. For example :code:`pigpio`.

Install PIGPIO
==============

Raspbian
********

.. code-block:: sh

   sudo apt-get update
   sudo apt-get install pigpio python-pigpio python3-pigpio

Ubuntu
******

.. code-block:: sh

   wget https://github.com/joan2937/pigpio/archive/master.zip
   unzip master.zip
   cd pigpio-master
   make
   sudo make install
