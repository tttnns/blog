piximg_ ：在 sphinx doc 中插入P站图片
=====================================

.. _piximg: https://github.com/TitanSnow/piximg

为了在博客里 **愉快地** 插入P站图片，
我略微花了两小时，搞了个 sphinx extension --
piximg_ ，用P站的 embed API 插入图片。
这样一来我就可以在 source file 里一句话插入一张图片，
而且还不用自己托管图片文件。
从今以后我的博客就可以大肆插图了 QwQ

Example
-------

*
    .. code-block:: rst

        .. piximg:: 62034471

    .. piximg:: 62034471

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: small

    .. piximg:: 62034471
       :size: small

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: medium

    .. piximg:: 62034471
       :size: medium

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: large

    .. piximg:: 62034471
       :size: large

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: small
           :border: on

    .. piximg:: 62034471
       :size: small
       :border: on

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: medium
           :border: on

    .. piximg:: 62034471
       :size: medium
       :border: on

*
    .. code-block:: rst

        .. piximg:: 62034471
           :size: large
           :border: on

    .. piximg:: 62034471
       :size: large
       :border: on
