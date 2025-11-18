# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

project = "The Zen of Reffing"
copyright = "2018-2025, Axis of Stevil, Luna, Blocktopus, Trampling Bias"
author = "Axis of Stevil, Luna, Blocktopus, Trampling Bias"
release = "1.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_last_updated_by_git"]

templates_path = ["_templates"]
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
html_theme_options = {
    "repository_url": "https://github.com/mrogaski/zenref",
    "use_repository_button": True,
}
html_title = "The Zen of Reffing Roller Derby"

# Options for timestamps
git_last_updated_timezone = "UTC"
