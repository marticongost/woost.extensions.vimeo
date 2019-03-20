#-*- coding: utf-8 -*-
"""

.. moduleauthor:: Jordi Fernández <jordi.fernandez@whads.com>
"""
import json
from urllib.request import urlopen
from woost.models.rendering import ImageURIRenderer
from .vimeovideo import VimeoVideo

METADATA_URL_PATTERN = "http://vimeo.com/api/v2/video/%s.json"

def get_video_metadata(video_id, timeout = 15):
    url = METADATA_URL_PATTERN % video_id
    json = urlopen(url, timeout = timeout).read()
    return json.loads(json)[0]


class VimeoVideoRenderer(ImageURIRenderer):

    def can_render(self, item, **parameters):
        return isinstance(item, VimeoVideo) and item.video_id

    def get_item_uri(self, item):
        return get_video_metadata(item.video_id)["thumbnail_large"]

