# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys
sys.path.insert(0, os.path.abspath('..')) # Esto es para que sphinx busque los modulos en el directorio actual (source)

project = 'Documentacion 2 Sphinx para DI'
copyright = '2024, Angi'
author = 'Angi'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', # Esto es para que se genere la documentacion de los modulos de python
              'sphinx.ext.intersphinx', # Esto es para que se puedan hacer referencias a otros modulos y/o proyectos
              'sphinx.ext.viewcode' # Esto es para que se pueda ver el codigo fuente de los modulos
              ]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
