# pylint: disable=invalid-name,too-few-public-methods
"""This file is for `sphinx-build` configuration"""
import os
import sys
import pygments.styles
from pygments.style import Style
from pygments.token import (
    Text,
    Other,
    Comment,
    Keyword,
    Name,
    Literal,
    String,
    Number,
    Operator,
    Generic,
    Punctuation,
)


sys.path.insert(0, os.path.abspath(".."))

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "sphinx_copybutton",
    # "rst2pdf.pdfbuilder",  # for local pdf builder support
]

# Uncomment the below if you use native CircuitPython modules such as
# digitalio, micropython and busio. List the modules you use. Without it, the
# autodoc module docs will fail to generate with a warning.
autodoc_mock_imports = ["digitalio", "busio", "usb_hid", "microcontroller"]
autodoc_member_order = "bysource"

intersphinx_mapping = {
    "python": ("https://docs.python.org/3.7", None),
    "BusDevice": (
        "https://circuitpython.readthedocs.io/projects/busdevice/en/latest/",
        None,
    ),
    "CircuitPython": ("https://circuitpython.readthedocs.io/en/latest/", None),
}

html_baseurl = "https://circuitpython-nrf24l01.readthedocs.io/"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# General information about the project.
# pylint: disable=redefined-builtin
copyright = u"2019 Brendan Doherty"
# pylint: enable=redefined-builtin
project = u"nRF24L01 Library"
author = u"Brendan Doherty"

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = u"2.0.0"
# The full version, including alpha/beta/rc tags.
release = u"2.0.0"

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = [
    "_build",
    "Thumbs.db",
    ".DS_Store",
    ".env",
    "CODE_OF_CONDUCT.md",
    "requirements.txt",
]

# The reST default role (used for this markup: `text`) to use for all
# documents.
default_role = "any"

# If true, '()' will be appended to :func: etc. cross-reference text.
add_function_parentheses = True

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# If this is True, todo emits a warning for each TODO entries. The default is False.
todo_emit_warnings = False

napoleon_numpy_docstring = False

# pygment custom style
# --------------------------------------------------

class DarkPlus(Style):
    """A custom pygment highlighting scheme based on
    VSCode's builtin `Dark Plus` theme"""

    background_color = "#1E1E1E"
    highlight_color = "#ff0000"
    line_number_color = "#FCFCFC"
    line_number_background_color = "#282828"

    default_style = ""
    styles = {
        Text: "#FEFEFE",
        Comment.Single: "#5E9955",
        Comment.Multiline: "#5E9955",
        Comment.Preproc: "#B369BF",
        Other: "#FEFEFE",
        Keyword: "#499CD6",
        Keyword.Declaration: "#C586C0",
        Keyword.Namespace: "#B369BF",
        # Keyword.Pseudo: "#499CD6",
        # Keyword.Reserved: "#499CD6",
        Keyword.Type: "#48C999",
        Name: "#FEFEFE",
        Name.Builtin: "#EAEB82",
        Name.Builtin.Pseudo: "#499DC7",
        Name.Class: "#48C999",
        Name.Decorator: "#EAEB82",
        Name.Exception: "#48C999",
        Name.Attribute: "#569CD6",
        Name.Variable:" #9CDCFE",
        Name.Variable.Magic: "#EAEB82",
        Name.Function: "#EAEB82",
        Name.Function.Magic: "#EAEB82",
        Literal: "#AC4C1E",
        String: "#B88451",
        String.Escape: "#DEA868",
        String.Affix: "#499DC7",
        Number: "#B3D495",
        Operator: "#FEFEFE",
        Operator.Word: "#499DC7",
        Generic.Output: "#F4DA8B",
        Generic.Prompt: "#99FFA2",
        Generic.Traceback: "#FF0909",
        Generic.Error: "#FF0909",
        Punctuation: "#FEFEFE",
    }


def pygments_monkeypatch_style(mod_name, cls):
    """ function to inject a custom pygment style """
    cls_name = cls.__name__
    mod = type(__import__("os"))(mod_name)
    setattr(mod, cls_name, cls)
    setattr(pygments.styles, mod_name, mod)
    sys.modules["pygments.styles." + mod_name] = mod
    pygments.styles.STYLE_MAP[mod_name] = mod_name + "::" + cls_name


pygments_monkeypatch_style("dark_plus", DarkPlus)
# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "dark_plus"

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "sphinx_material"
# Material theme options
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

html_theme_options = {
    # Set the name of the project to appear in the navigation.
    "nav_title": "CircuitPython-nRF24L01",
    # A list of dictionaries where each has three keys:
    #   href: The URL or pagename (str)
    #   title: The title to appear (str)
    #   internal: Flag indicating to use pathto (bool)
    "nav_links": [
        {
            "href": "examples",
            "title": "Examples",
            "internal": True
        },
        {
            "href": "basic_api",
            "title": "Basic RF24 API",
            "internal": True
        },
        {
            "href": "advanced_api",
            "title": "Advanced RF24 API",
            "internal": True
        },
        {
            "href": "configure_api",
            "title": "Configurable RF24 API",
            "internal": True
        },
        {
            "href": "ble_api",
            "title": "BLE API Reference",
            "internal": True
        },
        {
            "href": "troubleshooting",
            "title": "Troubleshooting",
            "internal": True
        },
    ],
    # Set the color and the accent color
    "color_primary": "blue",
    "color_accent": "light-blue",
    # Set the repo location to get a badge with stats
    "repo_url": "https://github.com/2bndy5/CircuitPython_nRF24L01/",
    "repo_name": "CircuitPython_nRF24L01",
    # Visible levels of the global TOC; -1 means unlimited
    "globaltoc_depth": 1,
    # If False, expand all TOC entries
    "globaltoc_collapse": False,
    # If True, show hidden TOC entries
    "globaltoc_includehidden": True,
}


# Set link name generated in the top bar.
html_title = "Introduction"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    "dark_material.css",
]

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "_static/new_favicon.ico"

# project logo
html_logo = "_static/Logo large.png"

# project logo
html_logo = "_static/Logo.png"

# Output file base name for HTML help builder.
htmlhelp_basename = "nRF24L01_Library_doc"
# html_copy_source = True
# html_show_sourcelink = True

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    #
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    #
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    #
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
    #
    # Latex figure (float) alignment
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc,
        "nRF24L01Library.tex",
        u"nRF24L01 Library Documentation",
        author,
        "manual",
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, "nRF24L01library", u"nRF24L01 Library Documentation", [author], 1)
]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "nRF24L01Library",
        u" nRF24L01 Library Documentation",
        author,
        "nRF24L01Library",
        "nRF24L01 on CircuitPython devices.",
        "Wireless",
    ),
]

# ---Options for PDF output-----------------------------------------
# requires `rst2pdf` module which is not builtin to Python 3.4 nor
# readthedocs.org's docker)

# pdf_documents = [
#     (
#         "index",
#         u"CircuitPython-nRF24L01",
#         u"CircuitPython-nRF24L01 library documentation",
#         u"Brendan Doherty",
#     ),
# ]
