"""
Custom element class for embedded object elements like ``<w:object>``
"""
from .simpletypes import (
    ST_TwipsMeasure, ST_RelationshipId, ST_String, ST_OLEType
)

from .xmlchemy import (
    BaseOxmlElement, OptionalAttribute, RequiredAttribute,
    ZeroOrOne, OneAndOnlyOne
)


class CT_EmbeddedObject(BaseOxmlElement):
    # specified the original (natural) size of the image
    # representation of the current control within the document
    dxaOrig = RequiredAttribute('w:dxaOrig', ST_TwipsMeasure)
    dyaOrig = RequiredAttribute('w:dyaOrig', ST_TwipsMeasure)

    oleObject = ZeroOrOne('o:OLEObject')


class CT_OLEObject(BaseOxmlElement):
    rId = RequiredAttribute('r:id', ST_RelationshipId)
    progId = RequiredAttribute('ProgID', ST_String)
    shapeID = RequiredAttribute('ShapeID', ST_String)
    type_ = RequiredAttribute('Type', ST_OLEType)
    objectID = RequiredAttribute('ObjectID', ST_String)


class CT_VML_Shape(BaseOxmlElement):
    _imageData = ZeroOrOne('v:imagedata')
    style = RequiredAttribute('style', ST_String)


class CT_VML_ImageData(BaseOxmlElement):
    rId = RequiredAttribute('r:id', ST_RelationshipId)
    title = OptionalAttribute('o:title', ST_String)


class CT_Drawing(BaseOxmlElement):
    """
    This element specifies that a DrawingML object is located at this position
    in the run’s contents. The layout properties of this DrawingML object
    are specified using the WordprocessingML Drawing syntax (§20.4).
    """
    # TODO: not support ``wp:anchor`` currently
    inline = OneAndOnlyOne('wp:inline')


    @property
    def cx(self):
        try:
            return self.inline.extent.cx
        except KeyError:
            return 0

    @property
    def cy(self):
        try:
            return self.inline.extent.cy
        except KeyError:
            return 0

    @property
    def embed(self):
        try:
            return self.inline.graphic.graphicData.pic.blipFill.blip.embed
        except KeyError:
            return ''
