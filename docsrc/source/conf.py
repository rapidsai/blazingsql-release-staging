# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx  # isort:skip
from sphinx.util import rpartition  # isort:skip
from sphinx.ext.autodoc import (  # isort:skip
    AttributeDocumenter,
    Documenter,
    MethodDocumenter,
)
from sphinx.ext.autosummary import Autosummary  # isort:skip

sys.path.insert(0, os.path.abspath('../../pyblazing'))
sys.path.insert(0, os.path.abspath('../../pyblazing/blazingsql'))
sys.setrecursionlimit(1500)

# -- Project information -----------------------------------------------------

project = 'BlazingSQL'
copyright = '2020, BlazingDB, Inc'
author = 'BlazingDB, Inc.'

# import blazingsql  # isort:skip

# # version = '%s r%s' % (pandas.__version__, svn_version())
# version = str(blazingsql.__version__)

# # The full version, including alpha/beta/rc tags.
# release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# The full version, including alpha/beta/rc tags
version = '21.08'
release = f'v{version}'

# -- General configuration ---------------------------------------------------

generate_cpp = int(os.environ['SPHINX_NO_CPP'])  ## SPEEDS UP docs generation as we don't read xml each time

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark',
                'sphinx.ext.extlinks',
                'sphinx.ext.todo',
                'sphinx.ext.autodoc',
                "sphinx.ext.autosummary",
                ]

autosummary_generate = True 
autosummary_imported_members = False


if generate_cpp:
    extensions = extensions + ['breathe', 'exhale']
    
    # Setup the exhale extension
    exhale_args = {
        # These arguments are required
        "containmentFolder":     "./xml",
        "rootFileName":          "library_root.rst",
        "rootFileTitle":         "C++ API Reference",
        "doxygenStripFromPath":  "..",
        # Suggested optional arguments
        "createTreeView":        True,
        # TIP: if using the sphinx-bootstrap-theme, you need
        "treeViewIsBootstrap": True
    }

    # Setup the breathe extension
    breathe_projects = {
        "BlazingSQL Engine": "./xml"
    }
    breathe_default_project = "BlazingSQL Engine"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# Tell sphinx what the primary language being documented is.
primary_domain = 'py'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'py'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = [
    "css/getting_started.css",
    "css/blazingsql.css",
    "css/theme.css",
    "css/pandas.css"
]
# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/icons/svg/blazingsql_logo.svg"

html_favicon = "_static/icons/blazingsql-icon.ico"

# If false, no module index is generated.
html_use_modindex = True

html_theme_options = {
    "twitter_url": "https://twitter.com/blazingsql"
    , "github_url": "https://github.com/BlazingDB/blazingsql"
    , "search_bar_position": "sidebar"
    , "search_bar_text": "Search BlazingSQL Docs"
    , "show_prev_next": True
    , 'body_max_width': '1200px'
    , "use_edit_page_button": True
    , "external_links": [
        # {"name": "BlazingSQL", "url": "https://blazingsql.com"}
    ]
    , "show_toc_level": "3"
    , "navigation_with_keys": True
}

# html_theme_options = {
    
# }

extlinks = {'io': (f'https://github.com/rapidsai/cudf/tree/branch-{version}/cpp/src/%s',
                      'cuIO ')}

html_context = {
    "github_user": "blazingdb",
    "github_repo": "blazingsql",
    "github_version": "feedback",
    "doc_path": "docsrc/source",
    "sql": {
        "query": ['SELECT','SELECT_ALL','SELECT_DISTINCT', 'WHERE', 'ORDERBY_']
        , "operators": [
            'OPS_ARITHMETIC','OPS_COMPARISON','OPS_LOGICAL','OPS_IN','OPS_IS'
            , 'OPS_CONCAT'
        ]
        , "math": [
            'MATH_ABS'
            ,'MATH_CEIL','MATH_FLOOR','MATH_ROUND'
            ,'MATH_GREATEST','MATH_LEAST'
            ,'MATH_LN','MATH_LOG10'
            ,'MATH_MOD'
            ,'MATH_POWER','MATH_SQRT'
            ,'MATH_RAND'
            ,'MATH_COS','MATH_ACOS'
            ,'MATH_SIN','MATH_ASIN'
            ,'MATH_TAN','MATH_ATAN'
        ]
        , "strings": [
            'STRING_CHARACTERLENGTH','STRING_CHARLENGTH'
            ,'STRING_CONCAT'
            ,'STRING_INITCAP','STRING_LOWER','STRING_UPPER'
            ,'STRING_LEFT','STRING_RIGHT','STRING_SUBSTRING'
            ,'STRING_LTRIM','STRING_RTRIM','STRING_TRIM'
            ,'STRING_REGEXPREPLACE','STRING_REPLACE'
            ,'STRING_REVERSE'
            
        ]
        , "dates": [
            'DATE_DAYOFMONTH','DATE_DAYOFWEEK','DATE_HOUR','DATE_MINUTE','DATE_MONTH','DATE_SECOND','DATE_YEAR','DATE_EXTRACT'
        ]
        , "conditional": [
            "FUNC_CASE","FUNC_COALESCE","FUNC_NULLIF","FUNC_NVL"
        ]
        , "aggregating": [
            'AGG_AVG','AGG_COUNT','AGG_MAX','AGG_MIN','AGG_STDDEV','AGG_STDDEVPOP','AGG_STDDEVSAMP','AGG_SUM'
            ,'AGG_VARIANCE','AGG_VARPOP','AGG_VARSAMP'            
        ]
        , "windowing": [
            'WINDOW_LEAD','WINDOW_LAG','WINDOW_FIRSTVALUE','WINDOW_LASTVALUE'
            ,'WINDOW_ROWNUMBER','WINDOW_AVG','WINDOW_MAX','WINDOW_MIN','WINDOW_SUM'
        ]
        , "joins": ['JOIN_CROSS','JOIN_INNER','JOIN_FULLOUTER','JOIN_LEFTOUTER']
    }
}

skip_methods = ['add_remove_table', 'partition', 'do_progress_bar', 'localfs']

def skip(app, what, name, obj, would_skip, options):
    if name == "__init__":
        return True
    elif name[0] == '_':
        return True
    elif name in skip_methods:
        return True
    return would_skip

class AccessorDocumenter(MethodDocumenter):
    """
    Specialized Documenter subclass for accessors.
    """

    objtype = "accessor"
    directivetype = "method"

    # lower than MethodDocumenter so this is not chosen for normal methods
    priority = 0.6

    def format_signature(self):
        # this method gives an error/warning for the accessors, therefore
        # overriding it (accessor has no arguments)
        return ""


class AccessorLevelDocumenter(Documenter):
    """
    Specialized Documenter subclass for objects on accessor level (methods,
    attributes).
    """

    # This is the simple straightforward version
    # modname is None, base the last elements (eg 'hour')
    # and path the part before (eg 'Series.dt')
    # def resolve_name(self, modname, parents, path, base):
    #     modname = 'pandas'
    #     mod_cls = path.rstrip('.')
    #     mod_cls = mod_cls.split('.')
    #
    #     return modname, mod_cls + [base]
    def resolve_name(self, modname, parents, path, base):
        if modname is None:
            if path:
                mod_cls = path.rstrip(".")
            else:
                mod_cls = None
                # if documenting a class-level object without path,
                # there must be a current class, either from a parent
                # auto directive ...
                mod_cls = self.env.temp_data.get("autodoc:class")
                # ... or from a class directive
                if mod_cls is None:
                    mod_cls = self.env.temp_data.get("py:class")
                # ... if still None, there's no way to know
                if mod_cls is None:
                    return None, []
            # HACK: this is added in comparison to ClassLevelDocumenter
            # mod_cls still exists of class.accessor, so an extra
            # rpartition is needed
            modname, accessor = rpartition(mod_cls, ".")
            modname, cls = rpartition(modname, ".")
            parents = [cls, accessor]
            # if the module name is still missing, get it like above
            if not modname:
                modname = self.env.temp_data.get("autodoc:module")
            if not modname:
                if sphinx.__version__ > "1.3":
                    modname = self.env.ref_context.get("py:module")
                else:
                    modname = self.env.temp_data.get("py:module")
            # ... else, it stays None, which means invalid
        return modname, parents + [base]


class AccessorAttributeDocumenter(AccessorLevelDocumenter, AttributeDocumenter):
    objtype = "accessorattribute"
    directivetype = "attribute"

    # lower than AttributeDocumenter so this is not chosen for normal
    # attributes
    priority = 0.6


class AccessorMethodDocumenter(AccessorLevelDocumenter, MethodDocumenter):
    objtype = "accessormethod"
    directivetype = "method"

    # lower than MethodDocumenter so this is not chosen for normal methods
    priority = 0.6


class AccessorCallableDocumenter(AccessorLevelDocumenter, MethodDocumenter):
    """
    This documenter lets us removes .__call__ from the method signature for
    callable accessors like Series.plot
    """

    objtype = "accessorcallable"
    directivetype = "method"

    # lower than MethodDocumenter; otherwise the doc build prints warnings
    priority = 0.5

    def format_name(self):
        return MethodDocumenter.format_name(self).rstrip(".__call__")

def rstjinja(app, docname, source):
    """
    Render our pages as a jinja template for fancy templating goodness.
    """
    # https://www.ericholscher.com/blog/2016/jul/25/integrating-jinja-rst-sphinx/
    # Make sure we're outputting HTML
    if app.builder.format != "html":
        return
    src = source[0]
    # print(docname, source)
    rendered = app.builder.templates.render_string(src, app.config.html_context)
    # print(rendered)
    source[0] = rendered

def setup(app):
    app.add_js_file("js/d3.v3.min.js")
    app.connect("autodoc-skip-member", skip)
    app.connect("source-read", rstjinja)
    # app.connect("env-get-outdated", test2)
    # app.connect("autodoc-process-docstring", remove_flags_docstring)
    # app.connect("autodoc-process-docstring", process_class_docstrings)
    # app.connect("autodoc-process-docstring", process_business_alias_docstrings)
    app.add_autodocumenter(AccessorDocumenter)
    app.add_autodocumenter(AccessorAttributeDocumenter)
    app.add_autodocumenter(AccessorMethodDocumenter)
    app.add_autodocumenter(AccessorCallableDocumenter)
