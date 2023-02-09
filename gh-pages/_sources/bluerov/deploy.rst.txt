Deploy Klopsi
=============

SSH Access
**********

For convenience, copy your ssh-key to the BlueROV to enable passwordless login and create an entry in your :file:`~/.ssh/config` for the BlueROV similiar to:

.. tabs::
   .. code-tab:: sh Pi in upper tube

      Host klopsi-main
          User pi
          Hostname klopsi-main.local
          IdentitiyFile "~/.ssh/id_ed25519"
   
   .. code-tab:: sh Pi in lower tube

      Host klopsi-buddy
          User pi
          Hostname klopsi-buddy.local
          IdentitiyFile "~/.ssh/id_ed25519"

.. note:: Replace the path for the identity file with the name of your key.

This entry allows you to use :code:`ssh klopsi-main` instead of :code:`ssh pi@klopsi-main.local`.

Environment Variables Checklist
*******************************

#. Change :code:`ROS_MASTER_URI` in :file:`~/.zshrc` to your desired value for both Raspberry Pis. For example
   .. code-block::

      ROS_MASTER_URI="http://hippo-celsius.local:11311"
   
   .. attention:: Do not forget to resource :file:`~/.zshrc`!

#. Change :code:`QGC_HOST` in :file:`~/bin/mavros` on :file:`klopsi-main` to the hostname of the computer you want to have QGroundControl running on.

   .. code-block::

      QGC_HOST="hippo-celsius.local"

Start the usual Setup
*********************

.. tabs::
   .. tab:: klopsi-main
      
      #. Start MAVROS
         .. code-block::
            
            mavros bluerov

      #. Start
      
         * Front Camera
         * Lights
         * Camera Servo
         * Barometer

         .. code-block::

            roslaunch hardware_interfaces top_hardware_bluerov.launch vehicle_name:=bluerov

         All these nodes can be reconfigured via :code:`dynamic_reconfigure`.

   .. tab:: klopsi-buddy

      Start the vertical camera
         .. code-block::

            roslaunch camera camera_node.launch vehicle_name:=bluerov

         This camera can be configured via :code:`dynamic_reconfigure`.
