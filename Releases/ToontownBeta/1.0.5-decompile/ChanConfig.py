# Source Generated with Decompyle++
# File: ChanConfig.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import GraphicsPipe
import Node
import ChanCfgOverrides
import NamedNode
import DisplayRegion
import GraphicsWindow
classDefined = 0

def generateClass_ChanConfig():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ChanConfig(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrGraphicsPipe_atomicstring_ptrNode_ptrChanCfgOverrides(self, parameter0, parameter1, render, parameter3):
            self.this = libpanda._inPeYohDAGc(parameter0.this, parameter1, render.this, parameter3.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrGraphicsPipe_atomicstring_ptrNode(self, parameter0, parameter1, render):
            self.this = libpanda._inPeYohJVrY(parameter0.this, parameter1, render.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPeYohOMv_:
                libpanda._inPeYohOMv_(self.this)
            

        
        def getGroupNode(self, nodeIndex):
            returnValue = libpanda._inPeYoh3O3t(self.this, nodeIndex)
            returnObject = NamedNode.NamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getGroupMembership(self, drIndex):
            returnValue = libpanda._inPeYohoUQs(self.this, drIndex)
            return returnValue

        
        def getNumGroups(self):
            returnValue = libpanda._inPeYohh6yc(self.this)
            return returnValue

        
        def getNumDrs(self):
            returnValue = libpanda._inPeYohxUNu(self.this)
            return returnValue

        
        def getDr(self, drIndex):
            returnValue = libpanda._inPeYohvvik(self.this, drIndex)
            returnObject = DisplayRegion.DisplayRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getWin(self):
            returnValue = libpanda._inPeYohKWKL(self.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                    if isinstance(_args[1], types.StringType):
                        if isinstance(_args[2], Node.Node):
                            return self.overloaded_constructor_ptrGraphicsPipe_atomicstring_ptrNode(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Node.Node> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
            elif numArgs == 4:
                if isinstance(_args[0], GraphicsPipe.GraphicsPipe):
                    if isinstance(_args[1], types.StringType):
                        if isinstance(_args[2], Node.Node):
                            if isinstance(_args[3], ChanCfgOverrides.ChanCfgOverrides):
                                return self.overloaded_constructor_ptrGraphicsPipe_atomicstring_ptrNode_ptrChanCfgOverrides(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <ChanCfgOverrides.ChanCfgOverrides> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Node.Node> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsPipe.GraphicsPipe> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '


    globals()['ChanConfig'] = ChanConfig

