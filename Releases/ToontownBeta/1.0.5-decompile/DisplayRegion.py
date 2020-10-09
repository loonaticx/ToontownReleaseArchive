# Source Generated with Decompyle++
# File: DisplayRegion.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsLayer
import GraphicsChannel
import GraphicsWindow
import GraphicsPipe
import Camera
import ProjectionNode
import Ostream
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_DisplayRegion():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DisplayRegion(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPO9cYeRcD:
                libpanda._inPO9cYeRcD(self.this)
            

        
        def getLeft(self):
            returnValue = libpanda._inPO9cY1enQ(self.this)
            return returnValue

        
        def getRight(self):
            returnValue = libpanda._inPO9cY1TCK(self.this)
            return returnValue

        
        def getBottom(self):
            returnValue = libpanda._inPO9cY7ild(self.this)
            return returnValue

        
        def getTop(self):
            returnValue = libpanda._inPO9cYitxi(self.this)
            return returnValue

        
        def setDimensions(self, l, r, b, t):
            returnValue = libpanda._inPO9cYm07G(self.this, l, r, b, t)
            return returnValue

        
        def getLayer(self):
            returnValue = libpanda._inPO9cYNG_x(self.this)
            returnObject = GraphicsLayer.GraphicsLayer(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getChannel(self):
            returnValue = libpanda._inPO9cYsH7W(self.this)
            returnObject = GraphicsChannel.GraphicsChannel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getWindow(self):
            returnValue = libpanda._inPO9cYD9j6(self.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPipe(self):
            returnValue = libpanda._inPO9cYzU9k(self.this)
            returnObject = GraphicsPipe.GraphicsPipe(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def setCamera(self, camera):
            returnValue = libpanda._inPO9cYqyV0(self.this, camera.this)
            return returnValue

        
        def getCamera(self):
            returnValue = libpanda._inPO9cYFQMQ(self.this)
            returnObject = Camera.Camera(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setCullFrustum(self, cullFrustum):
            returnValue = libpanda._inPO9cYZrUY(self.this, cullFrustum.this)
            return returnValue

        
        def getCullFrustum(self):
            returnValue = libpanda._inPO9cYDV1f(self.this)
            returnObject = ProjectionNode.ProjectionNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setActive(self, active):
            returnValue = libpanda._inPO9cYImVE(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPO9cYi47G(self.this)
            return returnValue

        
        def computePixels(self, x, y):
            returnValue = libpanda._inPO9cY0lZf(self.this, x, y)
            return returnValue

        
        def getPixelWidth(self):
            returnValue = libpanda._inPO9cY2qnq(self.this)
            return returnValue

        
        def getPixelHeight(self):
            returnValue = libpanda._inPO9cYDqDR(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPO9cYpkBx(self.this, out.this)
            return returnValue


    globals()['DisplayRegion'] = DisplayRegion

