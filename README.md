# cookie-python

A cookiecutter template for a well structured python project.

To use this template for a new project run
```bash
cookiecutter https://gitlab.projekt.uni-hannover.de/isd-it/cookie-python
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
5. author: not used at all for now. Later on we will use it for AUTHOR- or credits-files. Could be used for GitHub or ReadTheDocs.
6. email: email of author
7. version: defaults to 0.1. Will be used for git tags. And can be used for releases on github / gitlab.
8. use_pre_commit: enable default set of pre-commit hooks for git. This enforces the use of clean code: checks for encoding, credentials, docstring format.
9. open_source_license: is used to autogenerate `LICENSE`

## How to use src-layout scheme?

The src layout offers many advantages in terms of reproducibility. 
The program is easier to install on other computers and operating systems. 
It is only minimally more complicated to use. 
The package must first be installed before it can be used. 
We strongly recommend to use `virtualenv` virtual environments.

```bash
pip install -e .[dev]
```

is everything you have to do. For this you have to be in the same directory as the `pyproject.toml`-file. 
(The dot ist important). `-e` (same as `--editable`) creates links to your working copy of the software. 
If you make changes to the sourcecode you dont't have to reinstall the package because of this. 
The `[dev]`-part is for installing all developement dependencies. At the moment these are
- nox
- ruff
- bump-my-version
- Spyder
