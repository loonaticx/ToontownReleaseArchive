# Source Generated with Decompyle++
# File: SimpleLerpFunctorLVector4f.pyo (Python 2.0)

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
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import LerpFunctor
import TypeHandle
classDefined = 0

def generateClass_SimpleLerpFunctorLVector4f():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class SimpleLerpFunctorLVector4f(LerpFunctor.LerpFunctor, FFIExternalObject.FFIExternalObject):
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
            

        
        def getClassType():
            returnValue = libpanda._inPjRdz0eVT()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)

    globals()['SimpleLerpFunctorLVector4f'] = SimpleLerpFunctorLVector4f

