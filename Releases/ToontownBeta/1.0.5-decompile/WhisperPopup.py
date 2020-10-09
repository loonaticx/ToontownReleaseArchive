# Source Generated with Decompyle++
# File: WhisperPopup.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TextFont
import MarginManager
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
import MarginPopup
import TypeHandle
classDefined = 0

def generateClass_WhisperPopup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class WhisperPopup(MarginPopup.MarginPopup, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, text, font):
            self.this = libtoontown._inPPj7bI3cm(text, font.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libtoontown._inPPj7bHcpI()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def manage(self, manager):
            returnValue = libtoontown._inPPj7bRNAf(self.this, manager.this)
            return returnValue

        
        def unmanage(self, manager):
            returnValue = libtoontown._inPPj7b36LP(self.this, manager.this)
            return returnValue

        
        def isManaged(self):
            returnValue = libtoontown._inPPj7bHCTT(self.this)
            return returnValue


    globals()['WhisperPopup'] = WhisperPopup

