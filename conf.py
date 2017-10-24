extensions = ['sphinx.ext.mathjax', 'piximg']
source_suffix = '.rst'
master_doc = 'index'
project = 'tttnns-blog'
copyright = '2017, TitanSnow'
author = 'TitanSnow'
language = 'zh_CN'
exclude_patterns = ['_build']
html_theme = 'diktat'
html_theme_options = {
    'master_color': '#212121',
}
html_short_title = 'tttnns 的博客'
mathjax_path = 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js?config=TeX-AMS_CHTML-full'
html_static_path = ['_static']
