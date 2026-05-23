# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'sphinx_test'
copyright = '2026, Amanda'
author = 'Amanda'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# -- Sphinx autodoc configuration -------------------------------------------------
# Añadimos el path de nuestra app 
import os 
import sys 
sys.path.insert(0, os.path.abspath("../../app")) 
# Activamos que incluya los TODO (veremos ejemplo) 
todo_include_todos = True 
# Podemos cambiar el tema para la generación html
#html_theme = "sphinx_rtd_theme"
# Añadimos extensiones 
extensions = [ 
 "sphinx.ext.autodoc", 
 "sphinx.ext.todo", 
 "sphinx.ext.viewcode", 
]