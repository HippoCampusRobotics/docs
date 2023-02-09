System Configuration
====================

Insert SD card into Raspberry Pi. If your network is configured appropriately you can SSH into the Raspberry Pi. Otherwise connect your computer with the TX/RX pins of the Raspberry Pi via an USB-serial-converter.

Login with default credentials, i.e. :code:`pi:raspberry`. Change the password by typing :code:`passwd`.

Perform a system update:

.. code-block:: bash

   sudo apt update && sudo apt upgrade -y

Reboot the Pi.

.. code-block:: bash

   sudo reboot