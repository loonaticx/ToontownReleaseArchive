# Source Generated with Decompyle++
# File: LODNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
import SwitchNode
import TypeHandle
import SwitchNodeOne
import TypeHandle
classDefined = 0

def generateClass_LODNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LODNode(SwitchNodeOne.SwitchNodeOne, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPVub0gkZh(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVub0WO_c()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVub0j6kj:
                libpanda._inPVub0j6kj(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPVub0ehCR()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addSwitch(self, _in, out):
            returnValue = libpanda._inPVub0Kfoz(self.this, _in, out)
            return returnValue

        
        def setSwitch(self, index, _in, out):
            returnValue = libpanda._inPVub0aDeI(self.this, index, _in, out)
            return returnValue

        
        def clearSwitches(self):
            returnValue = libpanda._inPVub0vTEC(self.this)
            return returnValue

        
        def getNumSwitches(self):
            returnValue = libpanda._inPVub0UU6Z(self.this)
            return returnValue

        
        def getIn(self, index):
            returnValue = libpanda._inPVub0LhPo(self.this, index)
            return returnValue

        
        def getOut(self, index):
            returnValue = libpanda._inPVub0Po_6(self.this, index)
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


    globals()['LODNode'] = LODNode

