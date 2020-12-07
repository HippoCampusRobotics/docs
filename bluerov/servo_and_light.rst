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

Enable The Daemon
=================

Ubuntu only
***********

You need to create the :file:`pigpiod.service` file at :file:`/etc/systemd/system`.

.. code-block:: sh

   [Unit]
   Description=Pigpio daemon

   [Service]
   Type=forking
   PIDFile=pigpio.pid
   ExecStart=/usr/bin/pigpiod

   [Install]
   WantedBy=multi-user.target



Raspbian and Ubuntu
*******************

Enable the service

.. code-block:: sh

   sudo systemctl enable pigpiod.service

and run the service

.. code-block:: sh

   sudo systemctl start pigpiod.service
