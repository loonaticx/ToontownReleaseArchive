# Source Generated with Decompyle++
# File: ParametricCurveDrawer.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ParametricCurve
import ParametricCurveCollection
import GeomNode
import Node
import TypeHandle
import TypedObject
import TypeHandle
classDefined = 0

def generateClass_ParametricCurveDrawer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ParametricCurveDrawer(TypedObject.TypedObject, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHc9W7o8Y()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPHc9W3N_E()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCurve(self, curve):
            returnValue = libpanda._inPHc9W1AwO(self.this, curve.this)
            return returnValue

        
        def setCurves(self, curves):
            returnValue = libpanda._inPHc9WqBxy(self.this, curves.this)
            return returnValue

        
        def clearCurves(self):
            returnValue = libpanda._inPHc9WMR28(self.this)
            return returnValue

        
        def getCurves(self):
            returnValue = libpanda._inPHc9Wp0oA(self.this)
            returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getGeomNode(self):
            returnValue = libpanda._inPHc9WGgBt(self.this)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def detachGeomNode(self):
            returnValue = libpanda._inPHc9WqUTb(self.this)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setNumSegs(self, numSegs):
            returnValue = libpanda._inPHc9WBWbT(self.this, numSegs)
            return returnValue

        
        def getNumSegs(self):
            returnValue = libpanda._inPHc9Wv9u9(self.this)
            return returnValue

        
        def setNumTicks(self, numTicks):
            returnValue = libpanda._inPHc9WD96Q(self.this, numTicks)
            return returnValue

        
        def getNumTicks(self):
            returnValue = libpanda._inPHc9WZgZz(self.this)
            return returnValue

        
        def setColor(self, r, g, b):
            returnValue = libpanda._inPHc9WvqPs(self.this, r, g, b)
            return returnValue

        
        def setTickColor(self, r, g, b):
            returnValue = libpanda._inPHc9W1lPy(self.this, r, g, b)
            return returnValue

        
        def setTickGeometry(self, geom):
            returnValue = libpanda._inPHc9WEhsJ(self.this, geom.this)
            return returnValue

        
        def clearTickGeometry(self):
            returnValue = libpanda._inPHc9WuhbM(self.this)
            return returnValue

        
        def setFrameAccurate(self, frameAccurate):
            returnValue = libpanda._inPHc9Wqp9Z(self.this, frameAccurate)
            return returnValue

        
        def getFrameAccurate(self):
            returnValue = libpanda._inPHc9WdPSe(self.this)
            return returnValue

        
        def draw(self):
            returnValue = libpanda._inPHc9W8L4i(self.this)
            return returnValue

        
        def hide(self):
            returnValue = libpanda._inPHc9WwrC9(self.this)
            return returnValue

        
        def setTickScale(self, scale):
            returnValue = libpanda._inPHc9Wm2t8(self.this, scale)
            return returnValue

        
        def getTickScale(self):
            returnValue = libpanda._inPHc9W9gZj(self.this)
            return returnValue


    globals()['ParametricCurveDrawer'] = ParametricCurveDrawer

