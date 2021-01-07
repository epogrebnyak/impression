"""Sphinx configuration."""
from datetime import datetime

year = datetime.now().year

project = "{{cookiecutter.package_name}}"
author = "{{cookiecutter.author_name}}"
copyright = f"{year}, {author}"
extensions = ["sphinx.ext.autodoc", "sphinx.ext.autosummary", "myst_parser"]
autodoc_typehints = "description"
html_theme = "pydata_sphinx_theme"
