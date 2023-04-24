Underwater Camera
#################

.. note:: At the time of writing the IP addresses of the cameras are :code:`192.168.0.116` and :code:`192.168.0.148`. This might change in the future.

.. tabs::
   .. code-tab:: sh Camera 1

      IP_CAMERA_ADDRESS="192.168.0.116"

   .. code-tab:: sh Camera 2

      IP_CAMERA_ADDRESS="192.168.0.148"

Streaming
=========

.. tabs::

   .. code-tab:: sh No Latency

      gst-launch-1.0 rtspsrc location=rtsp://${IP_CAMERA_ADDRESS}:554/11 latency=0 buffer-mode=auto ! queue ! rtph265depay ! h265parse ! decodebin ! videoconvert ! autovideosink

   .. code-tab:: sh Stable

      gst-launch-1.0 rtspsrc location=rtsp://${IP_CAMERA_ADDRESS}:554/11 buffer-mode=auto ! queue ! rtph265depay ! h265parse ! decodebin ! videoconvert ! autovideosink

Save to File
============

.. code-block:: sh

   gst-launch-1.0 rtspsrc location=rtsp://${IP_CAMERA_ADDRESS}:554/11 buffer-mode=auto ! queue ! rtph265depay ! h265parse ! mp4mux ! filesink location=test.mp4 -e

