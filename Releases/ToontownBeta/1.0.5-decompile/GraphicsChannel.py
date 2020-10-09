# Source Generated with Decompyle++
# File: GraphicsChannel.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsLayer
import GraphicsWindow
import GraphicsPipe
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_GraphicsChannel():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GraphicsChannel(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inPO9cYdr3A()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_makeLayer_ptrGraphicsChannel_int(self, index):
            returnValue = libpanda._inPO9cYM6eC(self.this, index)
            returnObject = GraphicsLayer.GraphicsLayer(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_makeLayer_ptrGraphicsChannel(self):
            returnValue = libpanda._inPO9cYQeYv(self.this)
            returnObject = GraphicsLayer.GraphicsLayer(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumLayers(self):
            returnValue = libpanda._inPO9cYi9yB(self.this)
            return returnValue

        
        def getLayer(self, index):
            returnValue = libpanda._inPO9cYgHct(self.this, index)
            returnObject = GraphicsLayer.GraphicsLayer(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def moveLayer(self, fromIndex, toIndex):
            returnValue = libpanda._inPO9cY5DCQ(self.this, fromIndex, toIndex)
            return returnValue

        
        def removeLayer(self, index):
            returnValue = libpanda._inPO9cY75TJ(self.this, index)
            return returnValue

        
        def getWindow(self):
            returnValue = libpanda._inPO9cYNCc5(self.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPipe(self):
            returnValue = libpanda._inPO9cYdBxJ(self.this)
            returnObject = GraphicsPipe.GraphicsPipe(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def setActive(self, active):
            returnValue = libpanda._inPO9cYnJOq(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPO9cYmmTC(self.this)
            return returnValue

        
        def makeLayer(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_makeLayer_ptrGraphicsChannel()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_makeLayer_ptrGraphicsChannel_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['GraphicsChannel'] = GraphicsChannel

