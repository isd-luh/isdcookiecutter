"""Tests for main module."""

from {{ cookiecutter.project_slug }} import {{ cookiecutter.project_slug }}


class TestMain:
    """Collection of example tests."""

    def test_one(self):
        """Test if letter I is in ISD."""
        x = "ISD"
        assert "I" in x

    def test_main(self):
        """Assure that projects example function returns None."""
        assert {{ cookiecutter.project_slug }}.main() is None
