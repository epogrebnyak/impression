"""Sphinx configuration."""
from datetime import datetime

project = "ssg"
author = "Evgeniy Pogrebnyak"
year = datetime.now().year
copyright = f"{year}, {author}"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "sphinx_rtd_theme",
]
autodoc_typehints = "description"
html_theme = "sphinx_rtd_theme"
