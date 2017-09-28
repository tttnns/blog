使用 sphinx_ 和 readthedocs.io_ 搭建博客
========================================

.. _sphinx: http://www.sphinx-doc.org
.. _readthedocs.io: https://readthedocs.io
.. _jekyll: https://jekyllrb.com
.. _github-pages: https://pages.github.com

我曾经用 jekyll_ 和 github-pages_ 搭建博客，
但我很快发现了两个大问题：

* 我不会 markdown
* 我不会 ruby

于是很快就放弃了。

至于 cnblogs 之流。。。没用过不评价。

我唯一会一点的标记语言只有 ReStructuredText --
就是那种只要会一点 python 就会的标记语言。

于是乎对我而言，搭建博客的方式就是用
sphinx_ 和 readthedocs.io_ 了。

我发现用这种方式搭博客还是比较少见的，故记之。

sphinx_ (rst) 优点
------------------

* 用的人少，逼格高。

* 适合不会 markdown 的菜鸡。

* sphinx 文档是文本文件，方便用 git 进行版本控制；与所见即所得相反， sphinx 文档是要编译的 -- 类似 latex 的优点(?)。

* 编译目标多种多样，可以编译到 html ，可以编译到 latex （没错，编译到 latex ）， etc 。 markdown 试试？

* 内容与样式分离。 sphinx 文档只有结构标记，没有样式标记 -- 暴艹 markdown 和 latex

  sphinx 中样式是由 sphinx 主题控制的；因此你不用一个一个地去改文档，直接换一个主题所有页面观感就天翻地覆。 比如我的博客的 sphinx 主题是被我细微魔改的 Alabaster_ 。

* 不像 markdown 到处是方言，每个地方都不一样。

* toctree 真是好用。

.. _Alabaster: https://github.com/bitprophet/alabaster

sphinx_ (rst) 缺点
------------------

* 用的人少。

* 不及 markdown 易学。

* 编译和 latex 一样快（man)。

* （编译目标多这个应该无人能敌。）

* 我至今没有找到一个符合我审美的 sphinx 主题。

* （markdown 鏼鏼发抖。）

* 这个应该不止 sphinx 里有。

rst 入门
--------

这个。。。会 python 的应该都会 rst 吧。。。不讲了。

搭建步骤
--------

1. 开一个 github repo ，把 sphinx project 推上去。

2. 在 readthedocs.io_ 上 import 。

3. 然后你每次 push ，博客就相应更新啦！

微小的工作
----------

Alabaster_ 根本没有考虑中文字体。。。
它的正文字体设为衬线字体。在万恶的 Windows 下，就是辣眼睛的 **中易宋体** 。
（点阵版的哦）

而能和 MathJax 字体配合的 free 中文字体 -- 没得选了，只有思源宋体了。

于是乎本博客字体搭配：

* 正文：思源宋体
* 标题：思源黑体
* 代码：Fira Mono

Fira Mono 用的是 `mozilla 的 cdn`_ （嘿嘿）。
中文字体就比较难办了，因为涉及到 Dynamic Subsetting 。
最后我用的是 `Adobe Typekit`_ 。
当我发现它有 free plan 时还以为 Adobe 终于良心发现了，
结果 -- 1 kit with 2 fonts
（不过够用了；如果再多一个字体，我就可以把 Fira Mono 换成 Source Code Pro 了， Ain't it a party of Source font family? ）

.. _`mozilla 的 cdn`: https://code.cdn.mozilla.net
.. _`Adobe Typekit`: https://typekit.com

结果上线以后发现 -- woc ， `Adobe Typekit`_ 在墙外，这就尴尬了。
你看到本博客，如果被中易宋体辣到了眼睛，
这不是我的错。怎么会变成这个样子。。。
