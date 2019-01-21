# encoding: utf-8

from __future__ import absolute_import, division, print_function

from .constants import MIME_TYPE
from .helpers import LITTLE_ENDIAN, StreamReader
from .image import BaseImageHeader


class Wmf(BaseImageHeader):
    @classmethod
    def from_stream(cls, stream):
        # TODO: BoundingBox offset=6, size=8
        reader = StreamReader(stream, byte_order=LITTLE_ENDIAN, base_offset=6)
        x = reader.read_short(0, 0)
        y = reader.read_short(0, 2)
        w = reader.read_short(0, 4)
        h = reader.read_short(0, 6)
        inch = reader.read_short(0, 8)
        # print('x={x}, y={y}, w={w}, h={h}, inch={inch}'.format(x=x, y=y, w=w, h=h, inch=inch))
        return cls(x, y, 100, 100)

    @property
    def default_ext(self):
        return '.wmf'

    @property
    def content_type(self):
        return MIME_TYPE.WMF
