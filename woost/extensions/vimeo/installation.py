#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Martí Congost <marti.congost@whads.com>
"""
from woost.models import ExtensionAssets
from woost.models.rendering import ChainRenderer
from .vimeovideorenderer import VimeoVideoRenderer

def install():
    """Creates the assets required by the vimeo extension."""

    assets = ExtensionAssets("vimeo")
    content_renderer = ChainRenderer.require_instance(
        qname = "woost.content_renderer"
    )
    vimeo_renderer = assets.require(VimeoVideoRenderer, "renderer")
    content_renderer.renderers.append(vimeo_renderer)

