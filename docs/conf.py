# -*- coding: utf-8 -*-
#
# QuickTile documentation build configuration file, created by
# sphinx-quickstart on Tue Jan 14 02:30:56 2020.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.insert(0, os.path.abspath('..'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.ifconfig',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
    'sphinx_autodoc_typehints',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'QuickTile'
copyright = u'2009-2020, Stephan Sokolow'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#

# The short X.Y version.
from quicktile.version import __version__ as version
# The full version, including alpha/beta/rc tags.
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
today_fmt = '%Y-%m-%d'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = False

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

manpages_url = 'https://manpages.debian.org/{path}'

autodoc_default_options = {

    'private-members':
        '_load_desktop_geometry,_property_prep,_update,_vary_modmask',
    'special-members':
        '__bool__,__call__,__contains__,__repr__,__str__',
    'undoc-members': True,
}

always_document_param_types = True

# Uncomment this to enable display of TODOs in the manual and API docs
#todo_include_todos = True

# No point in confusing people with nonsense filename-line combinations
# calculated against the *output* of automodule directives.
todo_link_only = True

modindex_common_prefix = ['quicktile.']
# Nitpick every broken reference except ones I whitelist because they *have*
# no intersphinx-compatible documentation.
#
# TODO: Investigate how much work it would be to contribute intersphinx
#       generation to python-xlib's documentation pipeline.
nitpicky = True
nitpick_ignore = [
    ('py:class', 'inspect.FrameInfo'),
    ('py:class', 'tokenize.TokenInfo'),
    ('py:class', 'Xlib.display.Display'),
    ('py:meth', 'Xlib.display.Display.create_resource_object'),
    ('py:meth', 'Xlib.display.Display.keycode_to_keysym'),
    ('py:meth', 'Xlib.display.Display.sync'),
    ('py:class', 'Xlib.error.CatchError'),
    ('py:class', 'Xlib.error.XError'),
    ('py:class', 'Xlib.protocol.event.KeyPress'),
    ('py:mod', 'Xlib.Xatom'),
]


# -- Hack to work around sphinx-autodoc-typehints#124 and #38
import inspect, sphinx_autodoc_typehints

qualname_ignored_prefixes = [
    'gi.repository.',
    'gi.overrides.'
]
qualname_overrides = {
    'builtins.frame': ('data', 'types.FrameType'),
    'builtins.traceback': ('class', 'types.TracebackType'),
    'dbus._dbus.SessionBus': ('class', 'dbus.SessionBus'),
    '_io.StringIO': ('class', 'io.StringIO'),
}

fa_orig = sphinx_autodoc_typehints.format_annotation


def format_annotation(annotation, *args, **kwargs):
    if inspect.isclass(annotation):
        full_name = '{}.{}'.format(
            annotation.__module__, annotation.__qualname__)
        for prefix in qualname_ignored_prefixes:
            if full_name.startswith(prefix):
                return ':py:class:`' + full_name[len(prefix):] + '`'
        override = qualname_overrides.get(full_name)
        if override is not None:
            return ':py:{}:`~{}`'.format(*override)
    return fa_orig(annotation, *args, **kwargs)
sphinx_autodoc_typehints.format_annotation = format_annotation

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    'badge_branch': "master",
    'description': 'Keyboard-driven Window Tiling for your existing X11 '
                   'window manager',
    'font_family': 'sans-serif',
    'github_banner': True,
    'github_button': False,
    'github_user': 'ssokolow',
    'github_repo': 'quicktile',
    'head_font_family': 'sans-serif',
    'link': '#004B6B',
    'link_hover': '#004B6B',
    'show_powered_by': False,
    'show_related': True,
    'travis_button': True,
}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
# html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%Y-%m-%d'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
    '**': [
        'about.html',
        'relations.html',
        'searchbox.html',
        'donate.html',
    ]
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'QuickTiledoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # (Uncommented as a MyPy type hint with no import)
    'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'QuickTile.tex', u'QuickTile Documentation',
   u'Stephan Sokolow', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# TODO: Configure this

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'quicktile', u'QuickTile Documentation',
     [u'Stephan Sokolow'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'QuickTile', u'QuickTile Documentation',
   u'Stephan Sokolow', 'QuickTile', 'X11 window-tiling helper',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False


intersphinx_mapping = {
    'cairo': ('https://pycairo.readthedocs.io/en/latest/', None),
    'dbus': ('https://dbus.freedesktop.org/doc/dbus-python/', None),
    'gtk': ('https://lazka.github.io/pgi-docs/Gtk-3.0', None),
    'gdk': ('https://lazka.github.io/pgi-docs/Gdk-3.0', None),
    'gdkx11': ('https://lazka.github.io/pgi-docs/GdkX11-3.0', None),
    'glib': ('https://lazka.github.io/pgi-docs/GLib-2.0', None),
    'python': ('https://docs.python.org/3/', None),
    'wnck': ('https://lazka.github.io/pgi-docs/Wnck-3.0', None),
}
