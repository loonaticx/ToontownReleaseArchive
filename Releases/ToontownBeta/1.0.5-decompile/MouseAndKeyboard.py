# Source Generated with Decompyle++
# File: MouseAndKeyboard.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsWindow
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import DataNode
import TypeHandle
classDefined = 0

def generateClass_MouseAndKeyboard():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseAndKeyboard(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrGraphicsWindow_int_atomicstring(self, window, device, name):
            self.this = libpanda._inPOfOPbKWV(window.this, device, name)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrGraphicsWindow_int(self, window, device):
            self.this = libpanda._inPOfOPVuwz(window.this, device)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPOfOPJjPx:
                libpanda._inPOfOPJjPx(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPOfOPpqKX()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], GraphicsWindow.GraphicsWindow):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_ptrGraphicsWindow_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsWindow.GraphicsWindow> '
            elif numArgs == 3:
                if isinstance(_args[0], GraphicsWindow.GraphicsWindow):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.StringType):
                            return self.overloaded_constructor_ptrGraphicsWindow_int_atomicstring(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.StringType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsWindow.GraphicsWindow> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['MouseAndKeyboard'] = MouseAndKeyboard

