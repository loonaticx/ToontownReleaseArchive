# Source Generated with Decompyle++
# File: CharacterJointBundle.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Character
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import Namable
import Ostream
import TypeHandle
import PartGroup
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedWritableReferenceCount
import AnimControlCollection
import AnimControl
import Event
import PartBundle
import PartBundleNode
import AnimControl
import Ostream
import AnimBundle
import AnimControlCollection
import TypeHandle
import PartGroup
import Namable
import Event
classDefined = 0

def generateClass_CharacterJointBundle():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CharacterJointBundle(PartBundle.PartBundle, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPnRYR03c9:
                libpanda._inPnRYR03c9(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPnRYRT_Yp()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getNode(self):
            returnValue = libpanda._inPnRYRSdUp(self.this)
            returnObject = Character.Character(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['CharacterJointBundle'] = CharacterJointBundle

