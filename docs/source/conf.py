
import sys, os
html_theme = 'shibuya'
# html_theme_path = [sphinx_readable_theme.get_html_theme_path()]
html_theme_options = {
    "color_mode": "light",   # force light mode
}




# Include source folders.
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(0, os.path.abspath('../../services/bot/src/'))
sys.path.insert(0, os.path.abspath('../../services/bot/src/pbot/'))
sys.path.insert(0, os.path.abspath('../../services/bot/src/pbot/middleware'))
sys.path.insert(0, os.path.abspath('../../services/transceiver/src/'))
sys.path.insert(0, os.path.abspath('../../services/transceiver/src/transceiver/'))


project = 'PBot'
copyright = '2025, Chris Cummings'
author = 'Chris Cummings'
release = '0.1'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

# Add Assets
html_css_files = [
    'css/prism.css',
    'css/custom.css'
]
html_js_files = [
    'js/prism.js',
]

html_static_path = ['_static']

html_sidebars = {
    "**": ["globaltoc.html", "sourcelink.html", "searchbox.html"],
}



# html_theme_options = {
#     "palette": [
#         {
#             "media": "(prefers-color-scheme: light)",
#             "scheme": "default",
#             "primary": "blue",
#             "accent": "deep-purple",
#             "toggle": {
#                 "icon": "material/weather-night",
#                 "name": "Switch to dark mode",
#             },
#         },
#         {
#             "media": "(prefers-color-scheme: dark)",
#             "scheme": "slate",
#             "primary": "blue",
#             "accent": "deep-purple",
#             "toggle": {
#                 "icon": "material/weather-sunny",
#                 "name": "Switch to light mode",
#             },
#         },
#     ],
#     "font": {
#         "text": "Roboto",  # used for all the pages' text
#         "code": "Roboto Mono"  # used for literal code blocks
#     },
# }


extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.autosummary"
]


autodoc_mock_imports = [
	'tiktoken',
	'openai',
	'pytest',
    'redis',
    'discord',
    'urllib',
    'dotenv'
]

autodoc_default_options = {
    'members':         True,
    'member-order':    'bysource',
    'special-members': '__init__',
}
