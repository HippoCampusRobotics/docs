Ethernet Configuration
######################

The Raspberry Pis are connected with each other via Ethernet. To have a flexible solution, we define a fallback profile in :file:`/etc/dhcpcd.conf`. So in case you connect the Raspberry Pi directly to the Router, it uses DHCP. If no DHCP server is available, the Raspberry Pis use the static IP address defined in the fallback profile.

Either uncomment the existing lines or add them, so :file:`dhcpcd.conf` contains the following:

.. tabs:: 

   .. code-tab:: sh hippo-main

      # It is possible to fall back to a static IP if DHCP fails:
      # define static profile
      profile static_eth0
      static ip_address=10.0.0.1/24

      # fallback to static profile on eth0
      interface eth0
      fallback static_eth0


   .. code-tab:: sh hippo-buddy

      # It is possible to fall back to a static IP if DHCP fails:
      # define static profile
      profile static_eth0
      static ip_address=10.0.0.2/24

      # fallback to static profile on eth0
      interface eth0
      fallback static_eth0

You might want to restart the Raspberry Pis.