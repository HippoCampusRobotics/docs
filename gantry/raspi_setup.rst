Raspberry Pi Setup
##################

Requirements
============

* Raspberry Pi 4 (previous versions do not have enough UART devices!)

* Ubuntu 18.04 Server image installed on Raspberry

Enable UART
===========

Either pre-boot directly on the :file:`/boot` partition or from the running Raspberry Pi in the :file:`/boot/firmware` directory, modify the :file:`usercfg.txt` and add the following lines:

.. code-block:: sh

   dtoverlay=uart3
   dtoverlay=uart4
   dtoverlay=uart5


UDEV Rules
==========

The Raspberry Pi uses it's UARTs to communicate with the Faulhaber motors. The name of the UART ports depends on the number of activated UART devices on the dtoverlay. So it is hard to identify which of the :file:`/dev/ttyAMAn` devices corresponds to which physical UART device.

To simplify things you can add UDEV rules.

Executing 

.. code-block:: sh

   udevadm info --name=/dev/ttyAMA2 --attribute-walk

produces the following output:

.. code-block:: sh
   :linenos:

   looking at device '/devices/platform/soc/fe201800.serial/tty/ttyAMA2':
     KERNEL=="ttyAMA2"
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

The identifier of the physical interface is defined by line 7 :code:`KERNELS=="fe201800.serial"`

Since the value is defined in the parent device, you can not apply the UDEV rule to the :code:`/dev/ttyAMAn` device, but you have to use an environment variable.

* Motor X-Axis
   UART3

   .. code-block:: sh

      Tx/Rx <-> GPIO4/GPIO5 (KERNELS=="fe201600.serial")



* Motor Y-Axis
   UART4

   .. code-block:: sh

      Tx/Rx <-> GPIO8/GPIO9 (KERNELS=="fe201800.serial")

* Motor Z-Axis
   UART5

   .. code-block:: sh

      Tx/Rx <-> GPIO12/GPIO13 (KERNELS=="fe201a00.serial")

The resulting UDEV rule in :file:`/etc/udev/rules.d/50-serial.rules` is:

.. code-block:: sh
   :linenos:

   KERNEL=="ttyAMA[0-9]*", GROUP="dialout", ENV{MOTOR_SERIAL}="motor_serial"

   ENV{MOTOR_SERIAL}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201600.serial", SYMLINK+="motor_x"
   ENV{MOTOR_SERIAL}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201800.serial", SYMLINK+="motor_y"
   ENV{MOTOR_SERIAL}=="motor_serial",  SUBSYSTEM=="tty", KERNELS=="fe201a00.serial", SYMLINK+="motor_z"

You can apply these changes by

.. code-block:: sh

   sudo udevadm control --reload-rules && sudo udevadm trigger

To check, that the rule is applied correctly, you can execute

.. code-block:: sh

   ls /dev/motor* -l 

The output should show symbolic links for the three motor axes.

.. code-block:: sh

   lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_x -> ttyAMA2
   lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_y -> ttyAMA3
   lrwxrwxrwx 1 root root 7 Aug  7 01:00 /dev/motor_z -> ttyAMA4


