# Source Generated with Decompyle++
# File: libtoontownDowncasts.pyo (Python 2.0)

import types
import libtoontown
import Nametag2d
import MarginPopup
import Nametag3d
import NamedNode
import DNAGroup
import Namable

def downcastToNametag2dFromMarginPopup(this):
    returnValue = libtoontown._inPPj7b6QMF(this.this)
    returnObject = Nametag2d.Nametag2d(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToNametag3dFromNamedNode(this):
    returnValue = libtoontown._inPPj7bA1kd(this.this)
    returnObject = Nametag3d.Nametag3d(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def downcastToDNAGroupFromNamable(this):
    returnValue = libtoontown._inPdt4yCjp5(this.this)
    returnObject = DNAGroup.DNAGroup(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject

