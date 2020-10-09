# Source Generated with Decompyle++
# File: Physical.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PhysicsManager
import PhysicalNode
import PhysicsObject
import LinearForce
import AngularForce
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_Physical():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Physical(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_int_bool(self, ttlObjects, preAlloc):
            self.this = libpandaphysics._inP9fJJorxK(ttlObjects, preAlloc)
            self.userManagesMemory = 1

        
        def overloaded_constructor_int(self, ttlObjects):
            self.this = libpandaphysics._inP9fJJwUyJ(ttlObjects)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJLzEx()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPhysical(self, copy):
            self.this = libpandaphysics._inP9fJJkw30(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJxk_k()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getPhysicsManager(self):
            returnValue = libpandaphysics._inP9fJJ_AIU(self.this)
            returnObject = PhysicsManager.PhysicsManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPhysicalNode(self):
            returnValue = libpandaphysics._inP9fJJ4J5Q(self.this)
            returnObject = PhysicalNode.PhysicalNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getPhysBody(self):
            returnValue = libpandaphysics._inP9fJJJD8H(self.this)
            returnObject = PhysicsObject.PhysicsObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearLinearForces(self):
            returnValue = libpandaphysics._inP9fJJdjZ_(self.this)
            return returnValue

        
        def clearAngularForces(self):
            returnValue = libpandaphysics._inP9fJJRVpN(self.this)
            return returnValue

        
        def clearPhysicsObjects(self):
            returnValue = libpandaphysics._inP9fJJCIoY(self.this)
            return returnValue

        
        def addLinearForce(self, f):
            returnValue = libpandaphysics._inP9fJJRM1c(self.this, f.this)
            return returnValue

        
        def addAngularForce(self, f):
            returnValue = libpandaphysics._inP9fJJhnNk(self.this, f.this)
            return returnValue

        
        def addPhysicsObject(self, po):
            returnValue = libpandaphysics._inP9fJJ_Eir(self.this, po.this)
            return returnValue

        
        def removeLinearForce(self, f):
            returnValue = libpandaphysics._inP9fJJe_U3(self.this, f.this)
            return returnValue

        
        def removeAngularForce(self, f):
            returnValue = libpandaphysics._inP9fJJwl9H(self.this, f.this)
            return returnValue

        
        def getNumLinearForces(self):
            returnValue = libpandaphysics._inP9fJJyMhv(self.this)
            return returnValue

        
        def getLinearForce(self, index):
            returnValue = libpandaphysics._inP9fJJIuJj(self.this, index)
            returnObject = LinearForce.LinearForce(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumAngularForces(self):
            returnValue = libpandaphysics._inP9fJJCHVr(self.this)
            return returnValue

        
        def getAngularForce(self, index):
            returnValue = libpandaphysics._inP9fJJ6uLw(self.this, index)
            returnObject = AngularForce.AngularForce(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_int(_args[0])
                elif isinstance(_args[0], Physical):
                    return self.overloaded_constructor_ptrConstPhysical(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <Physical> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_int_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['Physical'] = Physical

