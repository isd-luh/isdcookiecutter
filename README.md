# cookie-python

A cookiecutter template for a well structured python project. It depends on [uv](https://docs.astral.sh/uv/) for management of tools and virtual enviroments.

To use this template for a new project run

```bash
cookiecutter https://gitlab.projekt.uni-hannover.de/fbg-admin/cookie-python
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

## How to use src-layout scheme?

We decided to exlusivly use the src layout scheme for our Python projects. This offers many advantages in terms of reproducibility. 
The program is easier to install on other computers and operating systems. 
Nowadays the overhead of using src-layout over flat layout is very small - thanks to [uv](https://docs.astral.sh/uv/) and others. 
Main takeaway: The package must first be installed before it can be used. 


```bash
cd PROJECTDIR # freshly created new project dir named after project_slug.
git init . # create a git repo
git add . # add everything to git repo
git commit -m "Initial commit."
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
