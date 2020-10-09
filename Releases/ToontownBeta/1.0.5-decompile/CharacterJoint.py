# Source Generated with Decompyle++
# File: CharacterJoint.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import NodeRelation
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
import MovingPartACMatrixSwitchType
import TypeHandle
import MovingPartMatrix
import TypeHandle
classDefined = 0

def generateClass_CharacterJoint():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CharacterJoint(MovingPartMatrix.MovingPartMatrix, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPnRYRcZnB:
                libpanda._inPnRYRcZnB(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPnRYRiZgE()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addNetTransform(self, arc):
            returnValue = libpanda._inPnRYRPMDD(self.this, arc.this)
            return returnValue

        
        def removeNetTransform(self, arc):
            returnValue = libpanda._inPnRYRWP42(self.this, arc.this)
            return returnValue

        
        def hasNetTransform(self, arc):
            returnValue = libpanda._inPnRYRrhel(self.this, arc.this)
            return returnValue

        
        def clearNetTransforms(self):
            returnValue = libpanda._inPnRYREdWU(self.this)
            return returnValue

        
        def addLocalTransform(self, arc):
            returnValue = libpanda._inPnRYRNJng(self.this, arc.this)
            return returnValue

        
        def removeLocalTransform(self, arc):
            returnValue = libpanda._inPnRYRI1Cm(self.this, arc.this)
            return returnValue

        
        def hasLocalTransform(self, arc):
            returnValue = libpanda._inPnRYRSUBo(self.this, arc.this)
            return returnValue

        
        def clearLocalTransforms(self):
            returnValue = libpanda._inPnRYR_J2l(self.this)
            return returnValue


    globals()['CharacterJoint'] = CharacterJoint

