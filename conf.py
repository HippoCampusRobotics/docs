# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import o
# import sys
# sys.path.insert(0, os.path.abspath('_ext'))

import sphinx_rtd_theme
import os
import sys

packages = ["hippocampus_common", "control",
"mu_auv_localization", "path_planning"]
for pkg in packages:
        sys.path.insert(0, os.path.abspath("./src/{}/src".format(pkg)))

autodoc_mock_imports = [
        "geometry_msgs",
        "std_msgs",
        "geometry_msgs",
        "nav_msgs",
        "numpy",
        "rospy",
        "smbus",
        "smbus2",
        "tf",
        "tf2_ros",
        "dynamic_reconfigure",
        "control.cfg",
        "matplotlib",
]

# -- Project information -----------------------------------------------------

project = 'HippoCampusDocs'
copyright = '2020, Thies Lennart Alff'
author = 'Thies Lennart Alff'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "sphinx.ext.githubpages",
        "sphinx.ext.todo",
        "sphinx.ext.autosectionlabel",
        "sphinx_tabs.tabs",
        "sphinx.ext.autodoc",
        "sphinx.ext.autosummary",
        "sphinx.ext.napoleon"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'venv']


# -- Options for HTML output -------------------------------------------------
# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []
html_context = {
        "display_github": True,
        "github_user": "HippoCampusRobotics",
        "github_repo": "docs",
        "github_version": "master/"
}


[extensions]
show_authors = True
todo_include_todos = True
autosectionlabel_prefix_document = True
autosummary_generate = True

