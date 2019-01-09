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
    progId = RequiredAttribute('ProgId', ST_String)
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
    # TODO: not support ``wp:anchor`` currently
    inline = OneAndOnlyOne('wp:inline')
