# Source Generated with Decompyle++
# File: GraphicsLayer.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DisplayRegion
import GraphicsChannel
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

def generateClass_GraphicsLayer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GraphicsLayer(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inPO9cY62nF()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_makeDisplayRegion_ptrGraphicsLayer(self):
            returnValue = libpanda._inPO9cYbc1O(self.this)
            returnObject = DisplayRegion.DisplayRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_makeDisplayRegion_ptrGraphicsLayer_float_float_float_float(self, l, r, b, t):
            returnValue = libpanda._inPO9cY3E33(self.this, l, r, b, t)
            returnObject = DisplayRegion.DisplayRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumDrs(self):
            returnValue = libpanda._inPO9cYbV_D(self.this)
            return returnValue

        
        def getDr(self, index):
            returnValue = libpanda._inPO9cYhrO1(self.this, index)
            returnObject = DisplayRegion.DisplayRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_removeDr_ptrGraphicsLayer_int(self, index):
            returnValue = libpanda._inPO9cYHwCB(self.this, index)
            return returnValue

        
        def overloaded_removeDr_ptrGraphicsLayer_ptrDisplayRegion(self, displayRegion):
            returnValue = libpanda._inPO9cYxI6p(self.this, displayRegion.this)
            return returnValue

        
        def getChannel(self):
            returnValue = libpanda._inPO9cYUkvA(self.this)
            returnObject = GraphicsChannel.GraphicsChannel(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getWindow(self):
            returnValue = libpanda._inPO9cYpYYk(self.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPipe(self):
            returnValue = libpanda._inPO9cY9WxO(self.this)
            returnObject = GraphicsPipe.GraphicsPipe(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def setActive(self, active):
            returnValue = libpanda._inPO9cY37Ju(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPO9cYNcvw(self.this)
            return returnValue

        
        def removeDr(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_removeDr_ptrGraphicsLayer_int(_args[0])
                elif isinstance(_args[0], DisplayRegion.DisplayRegion):
                    return self.overloaded_removeDr_ptrGraphicsLayer_ptrDisplayRegion(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <DisplayRegion.DisplayRegion> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def makeDisplayRegion(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_makeDisplayRegion_ptrGraphicsLayer()
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_makeDisplayRegion_ptrGraphicsLayer_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '


    globals()['GraphicsLayer'] = GraphicsLayer

