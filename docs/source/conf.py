# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'JAX AI Stacks'
copyright = '2024, The JAX Authors. NumPy and SciPy documentation are copyright the respective authors.'
author = 'The JAX authors'

# The short X.Y version
version = ''
# The full version, including alpha/beta/rc tags
release = ''

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_book_theme'
html_static_path = ["_static"]
html_css_files = ["css/custom.css"]


html_theme_options = {
    'show_toc_level': 2,
    'repository_url': 'https://github.com/google/jax',
    'use_repository_button': True,     # add a "link to repository" button
    'navigation_with_keys': False,
}


# -- Options for EPUB output
epub_show_urls = 'footnote'
