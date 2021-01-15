> Note: this is an early version of the template, structure and workflow are to be improved.

# Minimal cookiecutter for Poetry, Sphinx and Streamlit 

This is a minimal setup to work with Poetry, Sphinx and Streamlit out of the box.

## How to run

Install cookiecutter if you do not have it yet:

```
pip install cookiecutter
```

Run at prompt and answer several questions about your new package:

```
cookiecutter https://github.com/epogrebnyak/impression
```

The way you may anwser questions is similar to this:

```console
λ cookiecutter https://github.com/epogrebnyak/impression
package_name [pkg]: foo
author_name [Evgeniy Pogrebnyak]: Gino Forchione
author_email [e.pogrebnyak@gmail.com]: keep.it.a@secret.com
```

The project from example above will be created at `foo` folder. 

## Customisation

Please refer to [Cookiecutter documentation](https://cookiecutter.readthedocs.io)
for customisation.

## Features

 - [Poetry](https://python-poetry.org/) package and environment manager
 - [pytest](https://docs.pytest.org/en/stable/) and [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) testing pipeline
 - [Sphinx](https://www.sphinx-doc.org/en/master/) documentation with:
   - markdown support via powerful [myst-parser](https://myst-parser.readthedocs.io/en/latest/)
   - beautiful [PyData theme](https://pydata-sphinx-theme.readthedocs.io/en/latest/)
   - publishing to Github Pages
- justfile for [just](https://github.com/casey/just) command runner
- [streamlit](https://docs.streamlit.io/en/stable/) for quick dashboards
- [MIT license](LISENCE)


## How I test the package

I do it manually:

- `poetry run pytest`: ok
- `just docs`: fails
- `just show`: ok
- `just app`: ok

## Ideas

- badges (streamlit, test results)
- Read the docs compatibility 
- git init
- command line wrapper

<!--
## Not yet

 - precommit hooks
 - nox
 - coverage
!--> 
 
## Alternatives and inspiration

- https://github.com/cjolowicz/cookiecutter-hypermodern-python

