# Source Generated with Decompyle++
# File: ButtonThrower.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ModifierButtons
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

def generateClass_ButtonThrower():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ButtonThrower(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPyiw5dSyy(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPyiw5HbP2()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPyiw53Ag1:
                libpanda._inPyiw53Ag1(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPyiw5fohU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setPrefix(self, prefix):
            returnValue = libpanda._inPyiw51Hc8(self.this, prefix)
            return returnValue

        
        def hasPrefix(self):
            returnValue = libpanda._inPyiw5rBZr(self.this)
            return returnValue

        
        def getPrefix(self):
            returnValue = libpanda._inPyiw5wA_a(self.this)
            return returnValue

        
        def getModifierButtons(self):
            returnValue = libpanda._inPyiw5__sX(self.this)
            returnObject = ModifierButtons.ModifierButtons(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setModifierButtons(self, mods):
            returnValue = libpanda._inPyiw50__D(self.this, mods.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['ButtonThrower'] = ButtonThrower

