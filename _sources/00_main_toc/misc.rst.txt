Misc
####

x2go
====

Fix GLX Issues with rviz2
*************************

#. Install dependencies

   .. code-block:: sh
      
      sudo apt install libxcb-randr0-dev meson ninja-build byacc flex

#. Enable source code in **Additional Drivers** and download with
   
   .. code-block:: sh
      
      apt-get source mesa

#. Inside the mesa directory execute

   .. code-block:: sh
   
      mkdir build && cd build
      meson -D glx=xlib -D gallium-drivers=swrast -D platforms=x11 -D dri3=false -D dri-drivers="" -D vulkan-drivers="" -D buildtype=release -D optimization=3

   and run

   .. code-block:: sh

      ninja

#. Copy :file:`libgl-xlib` somewhere, e.g. the home directory

   .. code-block:: sh

      sudo cp -r src/gallium/targets/libgl-xlib /

To run :code:`gazebo` or :code:`rviz`, we need a wrapper. The `x2go Wiki <https://wiki.x2go.org/doku.php/wiki:development:glx-xlib-workaround>`__ proposes two different solutions, where only the latter works for :code:`gazebo` and :code:`rviz`.

.. tabs::

   .. code-tab:: sh x2goglx

      #!/bin/sh
      LD_LIBRARY_PATH="$HOME/libgl-xlib:${LD_LIBRARY_PATH}" exec "$@"

   .. code-tab:: sh x2goglx2

      #!/bin/sh
      LD_PRELOAD="$HOME/libgl-xlib/libGL.so.1" exec "$@"

.. todo:: Check if also the second solution can be added as :code:`export` in :file:`.zshrc`.

Forward Gamepad
===============

.. tabs::

   .. tab:: F710

      .. code-block:: sh
      
         cat /proc/bus/input/devices | awk '/F710/' RS= | grep -E 'Name=|event[0-9]+'

      .. code-block:: sh

         EVENT_DEVICE='dev/input/event2'

      .. asciinema:: /res/asciinema/get_f710_event.cast
         :speed: 1
         :start-at: 0
         :idle-time-limit: 0.1
         :poster: npt:1:01
         :cols: 120
         :rows: 25
         :preload: 1

   .. tab:: Everything

      .. code-block:: sh

         cat /proc/bus/input/devices | grep -E 'Name=|event[0-9]+' 

      .. code-block:: sh

         EVENT_DEVICE='dev/input/event2'
      
      .. asciinema:: /res/asciinema/get_all_event_devices.cast
         :speed: 1
         :start-at: 0
         :idle-time-limit: 0.1
         :poster: npt:1:01
         :cols: 120
         :rows: 25
         :preload: 1


.. note:: Replace the hostname/IP address of the remote target.

.. code-block:: sh

   REMOTE_ADDRESS='XXX.XXX.XXX.XXX'

.. code-block:: sh

   REMOTE_USER='remote_user_name'

.. code-block:: sh

   python -u ~/input-over-ssh/input_over_ssh/client.py -p ${EVENT_DEVICE} | ssh ${REMOTE_USER}@${REMOTE_ADDRESS} -t 'bash -c "python3 -u ~/input-over-ssh/input_over_ssh/server.py"'

On the remote target you can start the joy node.

 .. code-block:: sh

   ros2 run joy joy_node --ros-args -p device_name:='Logitech Gamepad F710 (via input-over-ssh)'

.. note:: For some reason it takes very long (up to a minute) for the joy node to detect the joystick device.

We can expect the node to publish messages as soon as it ouputs the following line:

.. code-block:: sh

   [INFO] [...] [joy_node]: Opened joystick: Logitech Gamepad F710 (via input-over-ssh).  deadzone: 0.050000

