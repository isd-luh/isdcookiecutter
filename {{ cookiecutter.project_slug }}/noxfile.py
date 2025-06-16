"""Configuration for nox."""

import nox

# Use uv to manage the virtual environment for all sessions
nox.options.default_venv_backend = "uv"


@nox.session
def lint(session: nox.Session) -> None:
    """Lint and format all python files with ruff.

    See pyproject.toml for configuration.
    """
    session.run(
        "uv",
        "sync",
        "--group",
        "lint",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True,
    )

    session.run("ruff", "format")
    session.run("ruff", "check", "--fix")


@nox.session
def test(session: nox.Session) -> None:
    """Run tests and check code coverage.

    See pyproject.toml for configuration.
    """
    session.run(
        "uv",
        "sync",
        "--group",
        "test",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True,
    )

    session.run("pytest")


@nox.session
def docs(session: nox.Session) -> None:
    """Create documentation with mkdocs and mkdocstrings.

    See mkdocs.yml and docs/index.md.
    """
    session.run(
        "uv",
        "sync",
        "--group",
        "doc",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
        external=True,
    )
    session.run("mkdocs", "build", "-d", "public")
