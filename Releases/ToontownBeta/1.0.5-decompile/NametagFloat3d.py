# Source Generated with Decompyle++
# File: NametagFloat3d.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Nametag3d
import TypeHandle
import ReferenceCount
import TypeHandle
import Nametag
import NametagGroup
import Node
import TypeHandle
import ReferenceCount
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
import Nametag3d
import NamedNode
import TypeHandle
import Nametag
import NametagGroup
import Node
import ReferenceCount
import Namable
classDefined = 0

def generateClass_NametagFloat3d():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NametagFloat3d(Nametag3d.Nametag3d, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts,
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libtoontown._inPPj7bohU4()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPPj7bx77N:
                libtoontown._inPPj7bx77N(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPPj7b0dqn()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['NametagFloat3d'] = NametagFloat3d

