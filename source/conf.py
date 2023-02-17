# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Constitution Senna'
copyright = '2022, Pierre Pavia'
author = 'Pierre Pavia'

import sys, os
sys.path.append(os.path.abspath('.'))

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sennadoc']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_static_path = ['_static']

html_permalinks = True

html_title = project

html_theme_options = dict(
    repository_url='https://github.com/Gouvernathor/senna',
    repository_branch='main',
    use_repository_button=True,
    use_issues_button=True,
    use_edit_page_button=True,

    use_download_button=True,

    extra_navbar='',

    use_sidenotes=True,
)
