# Source Generated with Decompyle++
# File: Projection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point2
import Point3
import Vec3
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

def generateClass_Projection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Projection(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPMAKPicxH:
                libpanda._inPMAKPicxH(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPChGn()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def makeCopy(self):
            returnValue = libpanda._inPMAKPUque(self.this)
            returnObject = Projection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_extrude_ptrConstProjection_ptrConstLPoint2f_ptrLPoint3f_ptrLVector3f___enum__CoordinateSystem(self, point2d, origin, direction, cs):
            returnValue = libpanda._inPMAKPliGJ(self.this, point2d.this, origin.this, direction.this, cs)
            return returnValue

        
        def overloaded_extrude_ptrConstProjection_ptrConstLPoint2f_ptrLPoint3f_ptrLVector3f(self, point2d, origin, direction):
            returnValue = libpanda._inPMAKPe6U5(self.this, point2d.this, origin.this, direction.this)
            return returnValue

        
        def overloaded_project_ptrConstProjection_ptrConstLPoint3f_ptrLPoint2f___enum__CoordinateSystem(self, point3d, point2d, cs):
            returnValue = libpanda._inPMAKPLmq5(self.this, point3d.this, point2d.this, cs)
            return returnValue

        
        def overloaded_project_ptrConstProjection_ptrConstLPoint3f_ptrLPoint2f(self, point3d, point2d):
            returnValue = libpanda._inPMAKP0jRL(self.this, point3d.this, point2d.this)
            return returnValue

        
        def project(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point2.Point2):
                        return self.overloaded_project_ptrConstProjection_ptrConstLPoint3f_ptrLPoint2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            elif numArgs == 3:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point2.Point2):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_project_ptrConstProjection_ptrConstLPoint3f_ptrLPoint2f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def extrude(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], Point2.Point2):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            return self.overloaded_extrude_ptrConstProjection_ptrConstLPoint2f_ptrLPoint3f_ptrLVector3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point2.Point2> '
            elif numArgs == 4:
                if isinstance(_args[0], Point2.Point2):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            if isinstance(_args[3], types.IntType):
                                return self.overloaded_extrude_ptrConstProjection_ptrConstLPoint2f_ptrLPoint3f_ptrLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point2.Point2> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '


    globals()['Projection'] = Projection

