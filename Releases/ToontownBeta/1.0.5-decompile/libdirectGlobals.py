# Source Generated with Decompyle++
# File: libdirectGlobals.pyo (Python 2.0)

import types
import libdirect
import DSearchPath
import GraphicsPipe
import ChanConfig
import NodeRelation
import NodePath
import GraphicsWindow
import Node
import Camera
import ConfigConfigureGetConfigConfigShowbase

def getParticlePath():
    returnValue = libdirect._inPL4GTlD_F()
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def makeGraphicsPipe():
    returnValue = libdirect._inPL4GT1wTd()
    returnObject = GraphicsPipe.GraphicsPipe(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject.setPointer()


def makeGraphicsWindow(pipe, renderArc):
    returnValue = libdirect._inPL4GTYwHR(pipe.this, renderArc.this)
    returnObject = ChanConfig.ChanConfig(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def setupPanda2d(win, name):
    returnValue = libdirect._inPL4GT_cMm(win.this, name)
    returnObject = NodePath.NodePath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def addRenderLayer(win, renderTop, camera):
    returnValue = libdirect._inPL4GTkljf(win.this, renderTop.this, camera.this)
    return returnValue


def toggleWireframe(renderArc):
    returnValue = libdirect._inPL4GTNBXr(renderArc.this)
    return returnValue


def toggleTexture(renderArc):
    returnValue = libdirect._inPL4GTZR4x(renderArc.this)
    return returnValue


def toggleBackface(renderArc):
    returnValue = libdirect._inPL4GTTzt3(renderArc.this)
    return returnValue


def takeSnapshot(win, name):
    returnValue = libdirect._inPL4GTCcZr(win.this, name)
    return returnValue


def getConfigShowbase():
    returnValue = libdirect._inPL4GTJl_f()
    returnObject = ConfigConfigureGetConfigConfigShowbase.ConfigConfigureGetConfigConfigShowbase(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
TMALIGNCENTER = 3
TMALIGNLEFT = 1
TMALIGNRIGHT = 2
