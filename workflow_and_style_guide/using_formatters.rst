Using Formatters
################

Python
******

For Python code we use :code:`yapf` as formatter with these settings:

.. code-block::

   [style]
   based_on_style = pep8
   column_limit = 80

The default :file:`.style.yapf` :code:`yapf` style file can be found on `GitHub Gist <https://gist.github.com/lennartalff/42dc02ee01ced47bfb0f75d715e5dcf9>`_ or directly downloaded in your current directory by executing: 

.. code-block:: bash

   wget https://gist.githubusercontent.com/lennartalff/42dc02ee01ced47bfb0f75d715e5dcf9/raw/da9d31abbf27d1d71b24a25dbe1c840506a17bfb/.style.yapf

.. note:: The downloaded file is named :code:`.style.yapf` and is therefore hidden. To show up in command line use :code:`ls -a` or hit :kbd:`Ctrl` + :kbd:`H` in your GUI filebrowser.

To run :code:`yapf` via the commandline and show the differences on formatting it suggests enter your project's directory and enter:

.. code-block:: bash
   
   yapf --diff --recursive .

If no output shows up this means all the Python files are already formatted according to the style settings in :file:`.style.yapf`.

To apply changes on all files run:

.. code-block:: bash
   
   yapf -i --recursive .


.. hint:: A more detailed description on how to use :code:`yapf` can be found in it's `README <https://github.com/google/yapf>`_.


