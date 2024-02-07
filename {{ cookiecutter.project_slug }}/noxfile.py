import nox

@nox.session
def lint(session):
    """Lint all python files with ruff.
    see pyproject.toml for configuration
    fix unsorted imports
    """
    session.install("ruff")
    session.run("ruff", "format", ".")
    session.run("ruff", ".", "--fix")

@nox.session
def docs(session):
    """Create documentation with mkdocs and mkdocstrings.
    see mkdocs.yml and docs/index.md
    """
    session.install("-r", "docs/requirements.txt")
    session.install("./")
    session.run("mkdocs", "build", "-d", "public")
