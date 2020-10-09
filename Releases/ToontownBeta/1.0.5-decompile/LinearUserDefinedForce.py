# Source Generated with Decompyle++
# File: LinearUserDefinedForce.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
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
import BaseForce
import ForceNode
import Vec3
import PhysicsObject
import TypeHandle
import LinearForce
import TypeHandle
classDefined = 0

def generateClass_LinearUserDefinedForce():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LinearUserDefinedForce(LinearForce.LinearForce, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJhGOC()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLinearUserDefinedForce(self, copy):
            self.this = libpandaphysics._inP9fJJHMZN(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJgysf()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], LinearUserDefinedForce):
                    return self.overloaded_constructor_ptrConstLinearUserDefinedForce(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LinearUserDefinedForce> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['LinearUserDefinedForce'] = LinearUserDefinedForce

