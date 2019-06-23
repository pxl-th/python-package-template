from os.path import (
    abspath,
    join,
)
import sys

sys.path.insert(0, abspath(join("..", "template")))

project = "Python Package Template"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.doctest",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.ifconfig",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
]

napoleon_google_docstring = True
napoleon_use_param = False
napoleon_use_ivar = True

mathjax_path = (
    "https://cdn.mathjax.org/mathjax/latest/MathJax.js"
    "?config=TeX-AMS-MML_HTMLorMML"
)

source_suffix = ".rst"
master_doc = "index"

todo_include_todos = True
language = None

pygments_style = "sphinx"
exclude_patterns = []

htmlhelp_basename = "templatedoc"
html_theme = "haiku"

latex_elements = {}

latex_documents = [(
    master_doc,
    "template.tex",
    "Template Documentation",
)]
man_pages = [(
    master_doc,
    "template",
    "Template Documentation",
)]
texinfo_documents = [(
    master_doc,
    "template",
    "Template Documentation",
)]

epub_title = project
epub_copyright = copyright
epub_exclude_files = ["search.html"]
