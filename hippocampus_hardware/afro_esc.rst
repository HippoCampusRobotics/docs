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

      git clone https://github.com/hippocampusrobotics/tgy.git

#. Build the firmware

   .. tabs::

      .. tab:: PWM

         Modify at least the following lines in :file:`tgy.asm`

         .. code-block:: sh
         
            RC_PULS_REVERSE = 1 ; This enables forward/reverse throttle
            RC_CALIBRATION = 0 ; 
            STOP_RC_PULS = 1000 ; minimum pwm value
            FULL_RC_PULS = 2000 ; maximum pwm value

         **Optionally** fiddle with the deadband

         .. code-block:: sh

            RCP_DEADBAND = 50 ; default value
         
         Build the firmware

         .. code-block:: sh

            make all

      .. tab:: I2C

         Build the firmware in 8 different versions with different :code:`MOTOR_ID` values starting from :code:`0x29` and increasing by 1 per step.

            .. code-block:: sh

               make build_8

#. Connect the Afro Programmer with your computer and connect the data wires with the ESC. Supply the ESC with an appropriate voltage (probably ~10-12V).

#. Install or :download:`download </res/misc/avrdude>` :code:`avrdude`.

   .. attention:: Newer versions of :code:`avrdude` do not seem to work with the AFRO programmer. So you may want to stick with the older version in the download.

#. Flash the :file:`afro_nfet.hex` firmware you have built before. 

   .. code-block:: sh

      avrdude -b 9600 -p m8 -P /dev/ttyUSB0 -c stk500v2 -e -U flash:w:afro_nfet.hex.0:i 

   .. important:: Make sure :code:`avrdude` verifies the flashed data successfully. Otherwise rebuilt the firmware with :code:`make clean && make all` and try again.
   