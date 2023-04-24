Misc
####

x2go
====

Fix GLX Issues
**************

#. Install dependencies

   .. code-block:: sh
      
      sudo apt install libxcb-randr0-dev

#. Enable source code in **Additional Drivers** and download with
   
   .. code-block:: sh
      
      apt-get source mesa

#. Inside the mesa directory execute

   .. code-block:: sh
   
      mkdir build && cd build
      meson -D glx=gallium-xlib -D gallium-drivers=swrast -D platforms=x11 -D dri3=false -D dri-drivers="" -D vulkan-drivers="" -D buildtype=release -D optimization=3

   and run

   .. code-block:: sh

      ninja

#. Copy :file:`libgl-xlib` somewhere, e.g. the home directory

   .. code-block:: sh

      cp src/gallium/targets/libgl-xlib ~/

To run :code:`gazebo` or :code:`rviz`, we need a wrapper. The `x2go Wiki <https://wiki.x2go.org/doku.php/wiki:development:glx-xlib-workaround>`__ proposes two different solutions, where only the latter works for :code:`gazebo` and :code:`rviz`.

.. tabs::

   .. code-tab:: sh x2goglx

      #!/bin/sh
      LD_LIBRARY_PATH="$HOME/libgl-xlib:${LD_LIBRARY_PATH}" exec "$@"

   .. code-tab:: sh x2goglx2

      #!/bin/sh
      LD_PRELOAD="$HOME/libgl-xlib/libGL.so.1" exec "$@"

.. todo:: Check if also the second solution can be added as :code:`export` in :file:`.zshrc`.
