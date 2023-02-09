UART Configuration
##################

.. attention:: By default UART0 is used as a login terminal. Do not change this, unless there is a compelling reason to do so.

We have made the decision to use UART5 for the telemetry communication with the FCU. UART4 is connected to the debug port of the FCU.

UART-KERNELS-Pin Mapping
========================

The UART functions in the following table depend on whether Raspberry Pi is used in a UUV or for the gantry controlling computer.

==== ======================= ===================== =========================
UART KERNELS                 Tx/Rx GPIOs           Function
==== ======================= ===================== =========================
0                            :code:`GPIO14/GPIO15` Access to Login Shell
1                                                  Reserved for Bluetooth
2                            :code:`GPIO0/GPIO1`   -- / --
3    :code:`fe201600.serial` :code:`GPIO4/GPIO5`   -- / x-Axis Motor
4    :code:`fe201800.serial` :code:`GPIO8/GPIO9`   Debug Port / y-Axis Motor
5    :code:`fe201a00.serial` :code:`GPIO12/GPIO13` Telemtry / z-Axis Motor
==== ======================= ===================== =========================

Pinout
======

.. tabs::

   .. tab:: UUV
      
      .. image:: /res/images/pi_pinout_uuv.svg
         :width: 30000
         :align: center
         

   .. tab:: Gantry

      .. image:: /res/images/pi_pinout_gantry.svg
         :width: 30000
         :align: center


UART Rule
=========

Create the file :file:`/etc/udev/rules.d/50-serial.rules` with the following content:

.. tabs::
   
   .. code-tab:: sh UUV

      KERNEL=="ttyAMA[0-9]*", GROUP="dialout", ENV{SERIAL_MARKER}="fcu_serial"

      ENV{SERIAL_MARKER}=="fcu_serial",  SUBSYSTEM=="tty", KERNELS=="fe201800.serial", SYMLINK+="fcu_debug"
      ENV{SERIAL_MARKER}=="fcu_serial",  SUBSYSTEM=="tty", KERNELS=="fe201a00.serial", SYMLINK+="fcu_tele"

   .. code-tab:: sh Gantry

      KERNEL=="ttyAMA[0-9]*", GROUP="dialout", ENV{SERIAL_MARKER}="motor_serial"

      ENV{SERIAL_MARKER}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201600.serial", SYMLINK+="motor_x"
      ENV{SERIAL_MARKER}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201800.serial", SYMLINK+="motor_y"
      ENV{SERIAL_MARKER}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201a00.serial", SYMLINK+="motor_z"

You can apply these changes by

.. code-block:: sh

   sudo udevadm control --reload-rules && sudo udevadm trigger

To check, that the rule is applied correctly, you can execute

.. tabs::

   .. code-tab:: sh UUV

      ls /dev/fcu* -l
   
   .. code-tab:: sh Gantry

      ls /dev/motor* -l

The output should show symbolic links for the serial devices:

.. tabs::

   .. code-tab:: sh UUV

      lrwxrwxrwx 1 root root 7 Dec 11 14:57 /dev/fcu_debug -> ttyAMA1               
      lrwxrwxrwx 1 root root 7 Dec 11 14:57 /dev/fcu_tele -> ttyAMA2 

   .. code-tab:: sh Gantry

      lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_x -> ttyAMA2
      lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_y -> ttyAMA3
      lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_z -> ttyAMA4


.. note:: The :file:`ttyAMA` numbers might differ, depending on the UARTs you have activated.

Identify KERNELS
================

To identify the KERNELS paramter of a certain :file:`ttyAMA` device, execute the following command.

.. code-block:: sh

   udevadm info --name=/dev/ttyAMA1 --attribute-walk


.. code-block:: sh
   :linenos:
   :emphasize-lines: 7

   looking at device '/devices/platform/soc/fe201800.serial/tty/ttyAMA1':
   KERNEL=="ttyAMA1"
   SUBSYSTEM=="tty"
   DRIVER==""

   looking at parent device '/devices/ platform/soc/fe201800.serial':
   KERNELS=="fe201800.serial"
   SUBSYSTEMS=="amba"
   DRIVERS=="uart-pl011"
   ATTRS{driver_override}=="(null)"
   ATTRS{id}=="00241011"
   ATTRS{irq0}=="14"

   looking at parent device '/devices/ platform/soc':
   KERNELS=="soc"
   SUBSYSTEMS=="platform"
   DRIVERS==""
   ATTRS{driver_override}=="(null)"

   looking at parent device '/devices/ platform':
   KERNELS=="platform"
   SUBSYSTEMS==""
   DRIVERS==""

.. attention:: The :file:`ttyAMAx` number is not specific for the UART device and depends on how many UARTs are activated. 