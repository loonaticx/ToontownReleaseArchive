# Source Generated with Decompyle++
# File: PhysicsObject.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import Vec3
import LOrientationf
import Mat4
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

def generateClass_PhysicsObject():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PhysicsObject(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inP9fJJuXEv()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPhysicsObject(self, copy):
            self.this = libpandaphysics._inP9fJJg8DU(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpandaphysics._inP9fJJU5oM()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, other):
            returnValue = libpandaphysics._inP9fJJDZrc(self.this, other.this)
            returnObject = PhysicsObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setMass(self, parameter1):
            returnValue = libpandaphysics._inP9fJJ0zyt(self.this, parameter1)
            return returnValue

        
        def getMass(self):
            returnValue = libpandaphysics._inP9fJJxDtm(self.this)
            return returnValue

        
        def overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(self, pos):
            returnValue = libpandaphysics._inP9fJJq6Ag(self.this, pos.this)
            return returnValue

        
        def overloaded_setPosition_ptrPhysicsObject_float_float_float(self, x, y, z):
            returnValue = libpandaphysics._inP9fJJvvGQ(self.this, x, y, z)
            return returnValue

        
        def getPosition(self):
            returnValue = libpandaphysics._inP9fJJvmf1(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setPositionHandOfGod(self, pos):
            returnValue = libpandaphysics._inP9fJJuB5n(self.this, pos.this)
            return returnValue

        
        def setLastPosition(self, pos):
            returnValue = libpandaphysics._inP9fJJrXQ2(self.this, pos.this)
            return returnValue

        
        def getLastPosition(self):
            returnValue = libpandaphysics._inP9fJJYpBj(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setVelocity_ptrPhysicsObject_ptrConstLVector3f(self, vel):
            returnValue = libpandaphysics._inP9fJJStzH(self.this, vel.this)
            return returnValue

        
        def overloaded_setVelocity_ptrPhysicsObject_float_float_float(self, x, y, z):
            returnValue = libpandaphysics._inP9fJJ5iOH(self.this, x, y, z)
            return returnValue

        
        def getVelocity(self):
            returnValue = libpandaphysics._inP9fJJRdns(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setActive(self, flag):
            returnValue = libpandaphysics._inP9fJJdRL1(self.this, flag)
            return returnValue

        
        def getActive(self):
            returnValue = libpandaphysics._inP9fJJ5Ryf(self.this)
            return returnValue

        
        def setOriented(self, flag):
            returnValue = libpandaphysics._inP9fJJ4nXG(self.this, flag)
            return returnValue

        
        def getOriented(self):
            returnValue = libpandaphysics._inP9fJJX101(self.this)
            return returnValue

        
        def setTerminalVelocity(self, tv):
            returnValue = libpandaphysics._inP9fJJVedt(self.this, tv)
            return returnValue

        
        def getTerminalVelocity(self):
            returnValue = libpandaphysics._inP9fJJOeE2(self.this)
            return returnValue

        
        def setOrientation(self, orientation):
            returnValue = libpandaphysics._inP9fJJJxq_(self.this, orientation.this)
            return returnValue

        
        def getOrientation(self):
            returnValue = libpandaphysics._inP9fJJE0E6(self.this)
            returnObject = LOrientationf.LOrientationf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setRotation(self, rotation):
            returnValue = libpandaphysics._inP9fJJSE9W(self.this, rotation.this)
            return returnValue

        
        def getRotation(self):
            returnValue = libpandaphysics._inP9fJJRnx7(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getInertialTensor(self):
            returnValue = libpandaphysics._inP9fJJvkW7(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getLcs(self):
            returnValue = libpandaphysics._inP9fJJcSLt(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def makeCopy(self):
            returnValue = libpandaphysics._inP9fJJPp2J(self.this)
            returnObject = PhysicsObject(None)
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
                if isinstance(_args[0], PhysicsObject):
                    return self.overloaded_constructor_ptrConstPhysicsObject(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PhysicsObject> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setPosition(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_setPosition_ptrPhysicsObject_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPosition_ptrPhysicsObject_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def setVelocity(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_setVelocity_ptrPhysicsObject_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setVelocity_ptrPhysicsObject_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['PhysicsObject'] = PhysicsObject

