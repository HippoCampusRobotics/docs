Structuring Catkin Packages
###########################

Python Packages
***************

.. note:: In the following the place holder :file:`your_package` is used. For your own package replace it with the name of your Catkin package.

Most packages will be written in Python. The structure should follow the conventions proposed in `REP 8 <https://www.ros.org/reps/rep-0008.html>`_. So the package structure will look like::

   your_package
   ├── CMakeLists.txt
   ├── README.md
   ├── package.xml
   ├── setup.py
   ├── config
   │   └── a_config_file.yaml
   ├── launch
   │   ├── start_a.launch
   │   └── start_b.launch
   ├── msg
   │   └── message_file.msg
   ├── nodes
   │   ├── cool_node
   │   └── also_quite_okay_node
   ├── scripts
   │       └── script_that_is_not_a_node.py
   ├── src
   │   └── your_package
   │       ├── __init__.py
   │       ├── module_a.py
   │       └── module_b.py
   └── srv
       └── servie_file.srv

config
   Contains configuration parameters stored in :file:`.yaml` files.

launch
   Contains your launch files.

msg
   Contains the definitions of your package's custom messages.

nodes
   Contains executable Python scripts. To be consistent with :code:`C++` executables omit the :file:`.py`.

src
   Contains a Python package. This has to have the same name as your Catkin package.

srv
   Contains definitions of your package's custom services.

There is no need to have the full directory structure if directories would be empty. So for example if your package does not have any services or messages, just omit the :file:`srv` or :file:`msg` directory respectively.

The Python modules inside :file:`src/your_package` can be reused by other Python scripts via :code:`import your_package.module_a` and are available for all your other Catkin packages aswell.

If your package has the :file:`src/your_package` directory make sure, your :file:`CMakeLists.txt` contains the line

.. code-block::

   catkin_python_setup()

and your package has a :file:`setup.py` that looks like

.. code-block:: python

   from distutils.core import setup
   from catkin_pkg.python_setup import generate_distutils_setup
   
   setup_args = generate_distutils_setup(
       packages=["your_package"],
       package_dir={"": "src"},
   )
   
   setup(**setup_args)

.. note::
   Replace :code:`your_package` in :code:`packages=["your_package"]` with your actual package name.

Also keep the hint in `REP 8 <https://www.ros.org/reps/rep-0008.html>`_ in mind:
   NOTE: we strive to keep ROS-specific code separate from reusable, generic code. The separation of 'node files' and files you place in src/packagename helps encourage this.