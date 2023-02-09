Installing QGroundControl
#########################

QGroundControl (QCG) is the Ground Control Station we use for deploying HippoCampus.
More info about QGC can be found in the `docs <https://docs.qgroundcontrol.com/master/en/>`_.

The Daily Build AppImage 
========================

... can be downloaded `here <https://docs.qgroundcontrol.com/master/en/releases/daily_builds.html>`__.

It is a good idea to keep this up-to-date. 
Alternatively, stable releases can be found `here <https://docs.qgroundcontrol.com/master/en/getting_started/download_and_install.html>`__.

Adding a desktop entry
======================

For convenience, we will add a desktop entry for QGC. This makes it possible to search for the application on your system, and add the application's icon to your dock.

For this, move the downloaded AppImage :file:`QGroundControl.AppImage` to a folder :file:`~/bin` (you may have to create this directory first).
Don't forget to make the AppImage file executable.

You will also need an app icon, an image with transparent background will look best.
Let's name it :file:`qgc_icon.png`, and put it here: :file:`~/.local/share/icons/qgc_icon.png`.

Now, we can create a desktop entry. We will call this file :file:`qgroundcontrol.desktop`, however, the name doesn't really matter.

.. code-block:: sh

   cd ~/.local/share/applications && touch qgroundcontrol.desktop

Open this file in your favourite text editor and paste the following lines:

.. code-block:: text

   [Desktop Entry]
   Type=Application
   Name=QGroundControl
   GenericName=Ground Control Station
   Comment=UAS ground control station
   Icon=/home/[YOUR_USERNAME]/.local/share/icons/qgc_icon.png
   Exec=/home/[YOUR_USERNAME]/bin/QGroundControl.AppImage
   Terminal=false
   Categories=Utility;

Make sure to adjust the paths to icon and AppImage to the correct ones.

You can check everything works by typing QGroundControl into the search, the application should come up with the icon you selected.

.. note:: 

   Every time you download the newest version of QGC, all you have to do is to replace the AppImage file in :file:`~/bin`.
