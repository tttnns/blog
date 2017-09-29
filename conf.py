extensions = ['sphinx.ext.mathjax']
source_suffix = '.rst'
master_doc = 'index'
project = 'tttnns-blog'
copyright = '2017, TitanSnow'
author = 'TitanSnow'
language = 'zh_CN'
exclude_patterns = ['_build']
html_theme_path = ['.']
html_theme = 'alab'
html_static_path = ['_static']
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'searchbox.html',
    ]
}
html_theme_options = {
    'font_family': 'serif',
    'code_font_family': '"Fira Mono", monospace',
    'head_font_family': 'sans-serif',
    'body_text_align': 'justify',
}
