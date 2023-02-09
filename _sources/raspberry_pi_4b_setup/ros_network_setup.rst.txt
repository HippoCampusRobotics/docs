ROS Network Setup
#################

   .. tabs:: 

      .. tab:: hippo-main

         .. tabs::

            .. code-tab:: sh zsh

               echo 'export ROS_MASTER_URI="http://$(hostname --short).local:11311"' >> ~/.zshrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.zshrc

            .. code-tab:: sh bash

               echo 'export ROS_MASTER_URI="http://$(hostname --short).local:11311"' >> ~/.bashrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.bashrc

      .. tab:: hippo-buddy

         .. attention:: Replace the number for hippo-main with the actual one.

         .. tabs::

            .. code-tab:: sh zsh

               HIPPO_MAIN="hippo-main-01"
               echo "export ROS_MASTER_URI=\"http://$HIPPO_MAIN.local:11311\"" >> ~/.zshrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.zshrc

            .. code-tab:: sh bash

               HIPPO_MAIN="hippo-main-01"
               echo "export ROS_MASTER_URI=\"http://$HIPPO_MAIN.local:11311\"" >> ~/.bashrc
               echo 'export ROS_HOSTNAME="$(hostname --short).local"' >> ~/.bashrc
