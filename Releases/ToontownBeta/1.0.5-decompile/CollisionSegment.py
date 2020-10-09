# Source Generated with Decompyle++
# File: CollisionSegment.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
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

def generateClass_CollisionSegment():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionSegment(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHwca_Y1_()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, a, db):
            self.this = libpanda._inPHwcaa2IM(a.this, db.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_float_float_float_float_float(self, ax, ay, az, bx, by, bz):
            self.this = libpanda._inPHwca_rlK(ax, ay, az, bx, by, bz)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcaPhZw:
                libpanda._inPHwcaPhZw(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcadimW()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setPointA_ptrCollisionSegment_ptrConstLPoint3f(self, a):
            returnValue = libpanda._inPHwcay4bw(self.this, a.this)
            return returnValue

        
        def overloaded_setPointA_ptrCollisionSegment_float_float_float(self, x, y, z):
            returnValue = libpanda._inPHwcar4Py(self.this, x, y, z)
            return returnValue

        
        def getPointA(self):
            returnValue = libpanda._inPHwcaqxkX(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_setPointB_ptrCollisionSegment_ptrConstLPoint3f(self, b):
            returnValue = libpanda._inPHwcarvbM(self.this, b.this)
            return returnValue

        
        def overloaded_setPointB_ptrCollisionSegment_float_float_float(self, x, y, z):
            returnValue = libpanda._inPHwcau1PO(self.this, x, y, z)
            return returnValue

        
        def getPointB(self):
            returnValue = libpanda._inPHwcaykkz(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_setProjection_ptrCollisionSegment_ptrProjectionNode_ptrConstLPoint2f(self, camera, point):
            returnValue = libpanda._inPHwcajeYa(self.this, camera.this, point.this)
            return returnValue

        
        def overloaded_setProjection_ptrCollisionSegment_ptrProjectionNode_float_float(self, camera, px, py):
            returnValue = libpanda._inPHwcatrqv(self.this, camera.this, px, py)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
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

        
        def setPointA(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_setPointA_ptrCollisionSegment_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPointA_ptrCollisionSegment_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def setPointB(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_setPointB_ptrCollisionSegment_ptrConstLPoint3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPointB_ptrCollisionSegment_float_float_float(_args[0], _args[1], _args[2])
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
                        return self.overloaded_setProjection_ptrCollisionSegment_ptrProjectionNode_ptrConstLPoint2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ProjectionNode.ProjectionNode> '
            elif numArgs == 3:
                if isinstance(_args[0], ProjectionNode.ProjectionNode):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setProjection_ptrCollisionSegment_ptrProjectionNode_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ProjectionNode.ProjectionNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['CollisionSegment'] = CollisionSegment

