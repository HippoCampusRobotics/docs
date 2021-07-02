Afro ESC
########

#. Download :code:`AVRA`.

   .. code-block:: sh

      git clone https://github.com/Ro5bert/avra.git

#. Build and install :code:`AVRA`

   .. code-block:: sh

      cd avra && sudo make install

#. Download the firmware

   .. code-block:: sh

      git clone https://github.com/sim-/tgy.git

#. Modify at least the following lines in :file:`tgy.asm`

   .. code-block:: sh
   
      RC_PULS_REVERSE = 1 ; This enables forward/reverse throttle
      RC_CALIBRATION = 0 ; 
      STOP_RC_PULS = 1000 ; minimum pwm value
      FULL_RC_PULS = 2000 ; maximum pwm value

#. **Optionally** fiddle with the deadband

   .. code-block:: sh

      RCP_DEADBAND = 50 ; default value

#. Build the firmware

   .. code-block:: sh

      make all

#. Connect the Afro Programmer with your computer and connect the data wires with the ESC. Supply the ESC with an appropriate voltage (probably ~10-12V).

#. Download :download:`KKmulticopter Flash Tool <https://lazyzero.de/_media/modellbau/kkmulticopterflashtool/kkmulticopterflashtool_0.90beta1.zip>`.

#. Flash the :file:`afro_nfet.hex` firmware you have built before. Select :code:`afrousb` as programmer and leave the checkbox for default settings selected.

   .. important:: Make sure :code:`avrdude` verifies the flashed data successfully. Otherwise rebuilt the firmware with :code:`make clean && make all` and try again.
   