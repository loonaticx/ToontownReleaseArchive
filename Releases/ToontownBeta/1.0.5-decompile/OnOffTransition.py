# Source Generated with Decompyle++
# File: OnOffTransition.pyo (Python 2.0)

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
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import NodeTransition
import Ostream
import TypeHandle
classDefined = 0

def generateClass_OnOffTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class OnOffTransition(NodeTransition.NodeTransition, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPs9JI3ffN:
                libpanda._inPs9JI3ffN(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPs9JIku1v()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setIdentity(self):
            returnValue = libpanda._inPs9JIGKcn(self.this)
            return returnValue

        
        def setOn(self):
            returnValue = libpanda._inPs9JIJQsg(self.this)
            return returnValue

        
        def setOff(self):
            returnValue = libpanda._inPs9JID5Na(self.this)
            return returnValue

        
        def isIdentity(self):
            returnValue = libpanda._inPs9JI_7Em(self.this)
            return returnValue

        
        def isOn(self):
            returnValue = libpanda._inPs9JIaJYv(self.this)
            return returnValue

        
        def isOff(self):
            returnValue = libpanda._inPs9JIvJvd(self.this)
            return returnValue


    globals()['OnOffTransition'] = OnOffTransition

