# Source Generated with Decompyle++
# File: MovingPartACMatrixSwitchType.pyo (Python 2.0)

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
import Namable
import Ostream
import TypeHandle
import PartGroup
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedWritableReferenceCount
import MovingPartBase
import TypeHandle
classDefined = 0

def generateClass_MovingPartACMatrixSwitchType():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MovingPartACMatrixSwitchType(MovingPartBase.MovingPartBase, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPn9gMZ1KX:
                libpanda._inPn9gMZ1KX(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPn9gM4xwN()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['MovingPartACMatrixSwitchType'] = MovingPartACMatrixSwitchType

