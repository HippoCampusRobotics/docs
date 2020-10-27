Contributing to Documentation
#############################

Forking the Repository
**********************
Go to this documentation's `GitHub repository <https://github.com/HippoCampusRobotics/docs>`_ and fork it (see `GitHub's documentation <https://help.github.com/en/github/getting-started-with-github/fork-a-repo>`_ for details on forking if you do not know how to fork a repository).

Then clone your fork with ``git clone`` so you can work with the repository locally.

Make your Changes
*****************

Modify or complement the existing .rst-files to your liking.

Help with the most common ReStructuredText/Sphinx directives can be found `here <https://documentation-style-guide-sphinx.readthedocs.io/en/latest/style-guide.html>`_. For a more extensive documentation of the capabilities of Sphinx visit the official `website <https://www.sphinx-doc.org/en/master/contents.html>`_.

Build the Docs locally
**********************

Since Sphinx follws the `WYSIWYM paradigm <https://en.wikipedia.org/wiki/WYSIWYM>`_, it is a good idea to build the ``html`` output, to check if your changes work out as expected.

Probably easiest way to do so is to setup a virtual environment for python by executing the following commmand inside your cloned fork of the documentation repository:

.. code-block:: bash

   python3 -m venv venv

Activate the virtual environment with

.. code-block:: bash

   source venv/bin/activate


and install the Sphinx dependencies by executing

.. code-block:: bash

   pip3 install -r requirements.txt

Now you can build the documentation by running

.. code-block:: bash

   make html

.. note:: Always make sure to have the virtual environment activated when executing the ``make html`` command.

View the HTML output
********************

You can view the HTML output by opening :file:`_build/html/index.html` with a webbrowser.