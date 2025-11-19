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

html_theme = "furo"
html_static_path = ["_static"]
html_title = "The Zen of Reffing Roller Derby"
html_last_updated_fmt = "%Y-%m-%d"
html_last_updated_use_utc = True
html_permalinks = True
html_theme_options = {
    "source_repository": "https://github.com/mrogaski/zenref",
    "source_branch": "main",
    "source_directory": "source",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/mrogaski/zenref",
            "html": "",
            "class": "fa-brands fa-solid fa-github fa-2x",
        },
    ],
}
html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/fontawesome.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/solid.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.7.2/css/brands.min.css",
]

# Options for timestamps
git_last_updated_timezone = "UTC"
