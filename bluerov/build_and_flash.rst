Build And Flash
###############

Build The Firmware
==================

We replaced the original FCU with the Pixhawk4, which is a 5th generation board. So the build command is:

.. code-block:: sh

   make px4_fmu-v5_default

If you get an error message that tells you, the :code:`gcc-arm-none-eabi` could not be found, make sure you have installed it (for example via the :file:`Tools/setup/ubuntu.sh` convenience script). In some cases, the path is not correctly extended, so it might be necessary to copy the line similiar to

.. code-block:: sh

   export PATH=/opt/gcc-arm-none-eabi-9-2020-q2-update/bin:$PATH

from :file:`~/.profile` to :file:`~/.bashrc` (or in case you use :code:`zsh` to :file:`~/.zshrc`).

.. attention:: The version of :code:`gcc-arm-none-eabi` might change, so it is necessary that you copy the line from your :file:`~/.profile` and not the one in this docs.

Flash The Firmware
==================

You need to be able to reach the BlueROV's Raspberry Pi via ssh. The most convenient way is to create a :code:`bash` script.

.. note:: Please update the following code block in case the BlueROV's host or username changes.

.. code-block:: sh
   :linenos:

   #!/bin/bash
   scp /PATH/TO/YOUR/PX4/FILE/px4_fmu-v5_default.px4 ubuntu@ubuntu.local:~/px4_fmu-v5_default.px4
   ssh ubuntu@ubuntu.local << EOF
   python3 ~/Firmware/Tools/px_uploader.py --port /dev/ttyACM0 ~/px4_fmu-v5_default.px4
   EOF


For even more convenience, copy your ssh-key to the BlueROV to enable passwordless login and create an entry in your :file:`~/.ssh/config` for the BlueROV similiar to:

.. code-block:: sh
   :linenos:

   Host klopsi
       User ubuntu
       Hostname ubuntu.local
       IdentitiyFile "$HOME/.ssh/id_ed25519"

.. note:: Replace the path for the identity file with the name of your key.

This entry allows you to use :file:`klopsi` instead of :file:`ubuntu@ubuntu.local`.
