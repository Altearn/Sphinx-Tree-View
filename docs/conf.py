"""Configuration file for the Sphinx documentation builder."""

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "Sphinx Tree View"
copyright = "2025, Altearn"
author = "Aksiome & theogiraudet"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
extensions = [
    "sphinx.ext.extlinks",
    "sphinx.ext.viewcode",
    "sphinx_inline_tabs",
    "sphinx_treeview",
    "myst_parser",
]
templates_path = ["_templates"]

# -- Options for extlinks ----------------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/sphinx/reference.html

extlinks = {
    "pypi": ("https://pypi.org/project/%s/", ""),
}

# -- Options for Markdown files ----------------------------------------------
# https://myst-parser.readthedocs.io/en/latest/sphinx/reference.html

myst_admonition_enable = True
myst_deflist_enable = True
myst_heading_anchors = 3
myst_enable_extensions = [
    "colon_fence",
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "furo"
html_title = project
