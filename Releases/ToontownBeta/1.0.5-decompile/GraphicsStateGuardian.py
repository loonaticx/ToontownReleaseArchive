# Source Generated with Decompyle++
# File: GraphicsStateGuardian.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import RenderTraverser
import VBase4
import TypeHandle
import NodeTransition
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import GraphicsStateGuardianBase
import TypeHandle
classDefined = 0

def generateClass_GraphicsStateGuardian():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GraphicsStateGuardian(GraphicsStateGuardianBase.GraphicsStateGuardianBase, FFIExternalObject.FFIExternalObject):
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
            

        
        def getClassType():
            returnValue = libpanda._inPO9cYQXKS()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setRenderTraverser(self, rt):
            returnValue = libpanda._inPO9cY9N6_(self.this, rt.this)
            return returnValue

        
        def getRenderTraverser(self):
            returnValue = libpanda._inPO9cYrkTM(self.this)
            returnObject = RenderTraverser.RenderTraverser(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setColorClearValue(self, value):
            returnValue = libpanda._inPO9cY53Yf(self.this, value.this)
            return returnValue

        
        def setDepthClearValue(self, value):
            returnValue = libpanda._inPO9cYqUm5(self.this, value)
            return returnValue

        
        def setStencilClearValue(self, value):
            returnValue = libpanda._inPO9cYY02b(self.this, value)
            return returnValue

        
        def setAccumClearValue(self, value):
            returnValue = libpanda._inPO9cY_oWx(self.this, value.this)
            return returnValue

        
        def getColorClearValue(self):
            returnValue = libpanda._inPO9cYJ4q9(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getDepthClearValue(self):
            returnValue = libpanda._inPO9cYKnPW(self.this)
            return returnValue

        
        def getStencilClearValue(self):
            returnValue = libpanda._inPO9cY9xYX(self.this)
            return returnValue

        
        def getAccumClearValue(self):
            returnValue = libpanda._inPO9cYTZoP(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def enableFrameClear(self, clearColor, clearDepth):
            returnValue = libpanda._inPO9cYmQKD(self.this, clearColor, clearDepth)
            return returnValue

        
        def releaseAllTextures(self):
            returnValue = libpanda._inPO9cYG7tg(self.this)
            return returnValue

        
        def releaseAllGeoms(self):
            returnValue = libpanda._inPO9cYmE3Y(self.this)
            return returnValue

        
        def clearAttribute(self, type):
            returnValue = libpanda._inPO9cYgmdE(self.this, type.this)
            return returnValue

        
        def getAttribute(self, type):
            returnValue = libpanda._inPO9cYffor(self.this, type.this)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['GraphicsStateGuardian'] = GraphicsStateGuardian

