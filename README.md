# isdcookiecutter 

A cookiecutter template for a well structured python project. It depends on [uv](https://docs.astral.sh/uv/) and [nox](https://nox.thea.codes/en/stable/) for management of tools and virtual enviroments.

To use this template for a new project run

```bash
cookiecutter https://github.com/isd-luh/isdcookiecutter
```

## How to answer the questions / configuration decisions?

1. project_name: A short but meaningful name for the project
2. project_slug: a lowercase version of project_name for use in urls and in pip. Rules are:
   - only lowercase letters
   - has to start with a letter
   - must not contain special signs (umlauts...)
   - only (english) letters numbers and underscores. No hyphens!
3. project_short_description: Short description of the project. Will be used in `LICENSE`, `pyproject.toml` and documentation.
4. institute: e.g. "Institut für Statik und Dynamik". Will be used for copyright. E.g. "(C) 2024 Leibniz Universität Hannover, Institut für Statik und Dynamik"
5. author: Used in `pyproject.toml`. Later on we will use it for AUTHOR- or credits-files. Could be used for GitHub or ReadTheDocs.
6. email: email of author
7. version: defaults to 0.1. Will be used for git tags. And can be used for releases on github / gitlab.
8. open_source_license: is used to autogenerate `LICENSE` and header for example source code file.

## Start coding...

We decided to exlusivly use the **src layout scheme** for our Python projects. This offers many advantages in terms of reproducibility and the program is easier to install on other computers and operating systems. 
Nowadays the overhead of using src-layout over flat layout is very small - thanks to [uv](https://docs.astral.sh/uv/) and others. 
Main takeaway: The package must first be installed before it can be used. 


```bash
# in this example we used "my_new_project" as project_slug.
cd my_new_project # freshly created new project dir named after project_slug.
git init . # create a git repo
git add . # add everything to git repo
git commit -m "Initial commit."
uv run my_new_project # run example script of your project.
# or lint, format, run tests, build documentation:
uvx nox 
# Strongly recommended: install all dependencies in virtual environment:
uv sync --all-groups
```

## uv run magic

`uv run` enables a *virtual environmet* located in `.venv` and installs your package in this environment in editable mode (same as `pip install --editable .` (the dot at the end is important)). If the *virtual enviroment* does not exist it is created on the fly. 

If you make changes to the source code you dont't have to reinstall the package because of editable mode. 


## Preconfigured things in this cookiecutter-template

The configuration for all tools (except nox) is located in `pyproject.toml`

+ [Ruff](https://docs.astral.sh/ruff/) is used for formatting and static checks. A rather large set of checks is enabled. Disable them, if errors get to much. E.g. doctrings in numpy-style are enforced by default.

+ [pytest](https://docs.pytest.org/en/stable/) and [Coverage.py](https://coverage.readthedocs.io/en/7.9.1/)  are configured to run all tests in `tests` dir and check the code coverage of your tests. 

+ [mkdocs](https://www.mkdocs.org/) is used to build the documentation from your docstrings. Run `uvx nox` and have a look at your documentation in folder `public` afterwards.



## Coding with Spyder

To use the virtual environment with your global Spyder installation you have to add `spyder-kernels` as developement dependency to your project:

```bash
uv add --dev spyder-kernels
```

After this you may switch your Spyder Python-Interpreter (menu `Tools` / `prefenrences` / `Python Interpreter` ) to the Python executable in your projects virtual environment.
