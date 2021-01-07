"""Provide pyproject.toml contents as python file.

Based on Poetry mechanism to split authors name and email from pyproject.toml:
    https://github.com/python-poetry/poetry/blob/35058edf97e24ef1ac2b77563c84eed66d46939e/poetry/packages/package.py

"""
import toml
import re
from typing import Tuple

AUTHOR_REGEX = re.compile(r"(?u)^(?P<name>[- .,\w\d'’\"()]+)(?: <(?P<email>.+?)>)?$")


def get_author(s: str) -> Tuple[str, str]:
    m = AUTHOR_REGEX.match(s)
    name = m.group("name")
    email = m.group("email")
    return name, email


d = toml.load("pyproject.toml")["tool"]["poetry"]
project = d["name"]
author_name, author_email = get_author(d["authors"][0])
