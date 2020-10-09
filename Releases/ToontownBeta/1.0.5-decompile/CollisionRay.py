# Source Generated with Decompyle++
# File: CollisionRay.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import Vec3
import ProjectionNode
import Point2
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
import BoundedObject
import BoundingVolume
import TypeHandle
import CollisionSolid
import Ostream
import BoundedObject
import TypeHandle
import ReferenceCount
import TypedWritableReferenceCount
import BoundingVolume
classDefined = 0

def generateClass_CollisionRay():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionRay(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHwcaHB0J()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(self, origin, direction):
            self.this = libpanda._inPHwcanwsc(origin.this, direction.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float_float_float(self, ox, oy, oz, dx, dy, dz):
            self.this = libpanda._inPHwcaljco(ox, oy, oz, dx, dy, dz)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcafayp:
                libpanda._inPHwcafayp(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaO_1_()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(self, origin):
            returnValue = libpanda._inPHwcaPqg4(self.this, origin.this)
            return returnValue

        
        def overloaded_setOrigin_ptrCollisionRay_float_float_float(self, x, y, z):
            returnValue = libpanda._inPHwca7dZ5(self.this, x, y, z)
            return returnValue

        
        def getOrigin(self):
            returnValue = libpanda._inPHwcahVBW(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(self, direction):
            returnValue = libpanda._inPHwca_AK_(self.this, direction.this)
            return returnValue

        
        def overloaded_setDirection_ptrCollisionRay_float_float_float(self, x, y, z):
            returnValue = libpanda._inPHwcanTl9(self.this, x, y, z)
            return returnValue

        
        def getDirection(self):
            returnValue = libpanda._inPHwcaq2uk(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_setProjection_ptrCollisionRay_ptrProjectionNode_ptrConstLPoint2f(self, camera, point):
            returnValue = libpanda._inPHwcaW4i9(self.this, camera.this, point.this)
            return returnValue

        
        def overloaded_setProjection_ptrCollisionRay_ptrProjectionNode_float_float(self, camera, px, py):
            returnValue = libpanda._inPHwcanBaS(self.this, camera.this, px, py)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 6:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        return self.overloaded_constructor_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 6 '

        
        def setOrigin(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_setOrigin_ptrCollisionRay_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setOrigin_ptrCollisionRay_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def setProjection(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], ProjectionNode.ProjectionNode):
                    if isinstance(_args[1], Point2.Point2):
                        return self.overloaded_setProjection_ptrCollisionRay_ptrProjectionNode_ptrConstLPoint2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ProjectionNode.ProjectionNode> '
            elif numArgs == 3:
                if isinstance(_args[0], ProjectionNode.ProjectionNode):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setProjection_ptrCollisionRay_ptrProjectionNode_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ProjectionNode.ProjectionNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def setDirection(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Vec3.Vec3):
                    return self.overloaded_setDirection_ptrCollisionRay_ptrConstLVector3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setDirection_ptrCollisionRay_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['CollisionRay'] = CollisionRay

