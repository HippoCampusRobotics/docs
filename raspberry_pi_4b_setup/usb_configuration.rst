USB Configuration
#################

Similar to the UART configuration we can add a UDEV rule to identify the Pixracer if connected via USB and create a symlink with meaningful name.

Create the file :file:`/etc/udev/rules.d/50-fcu.rules` and add the following lines:

.. tabs::

   .. code-tab:: sh PixRacer

      KERNEL=="ttyACM[0-9]*", GROUP="dialout", ENV{FCU_USB}="fcu_usb"

      ENV{FCU_USB}=="fcu_usb", SUBSYSTEM=="tty", ATTRS{idVendor}=="26ac", ATTRS{idProduct}=="0012", SYMLINK+="fcu_usb"
   
   .. code-tab:: sh PixHawk 4

      KERNEL=="ttyACM[0-9]*", GROUP="dialout", ENV{FCU_USB}="fcu_usb"

      ENV{FCU_USB}=="fcu_usb", SUBSYSTEM=="tty", ATTRS{idVendor}=="26ac", ATTRS{idProduct}=="0032", SYMLINK+="fcu_usb"

   .. code-tab:: sh PixHawk 6C

      SUBSYSTEM=="tty", ATTRS{idVendor}=="1d6b", ATTRS{idProduct}=="0002", SYMLINK+="fcu_usb", MODE="0666"

Retrigger the rules:

.. code-block:: console

   $ sudo udevadm control --reload-rules && sudo udevadm trigger

To check, that the rule is applied correctly, you can execute

.. code-block:: console

   $ ls /dev/fcu* -l

And the result should show at least the marked line:

.. code-block:: console
   :emphasize-lines: 3

   lrwxrwxrwx 1 root root 7 Jun 16 08:13 /dev/fcu_debug -> ttyAMA1
   lrwxrwxrwx 1 root root 7 Jun 16 08:13 /dev/fcu_tele -> ttyAMA2
   lrwxrwxrwx 1 root root 7 Jun 16 08:13 /dev/fcu_usb -> ttyACM0
