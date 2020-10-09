# Source Generated with Decompyle++
# File: PlaneD.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Point3D
import Vec3D
import Mat3D
import Mat4D
import Ostream
classDefined = 0

def generateClass_PlaneD():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PlaneD(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPSkjPgoXP()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPlaned(self, copy):
            self.this = libpanda._inPSkjPO1jn(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3d_ptrConstLPoint3d_ptrConstLPoint3d(self, a, b, c):
            self.this = libpanda._inPSkjPZiG8(a.this, b.this, c.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVector3d_ptrConstLPoint3d(self, normal, point):
            self.this = libpanda._inPSkjP6O1l(normal.this, point.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjPGJrr:
                libpanda._inPSkjPGJrr(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPSkjPpcLO(self.this, copy.this)
            returnObject = PlaneD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___mul___ptrConstPlaned_ptrConstLMatrix3d(self, mat):
            returnValue = libpanda._inPSkjPOtn3(self.this, mat.this)
            returnObject = PlaneD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstPlaned_ptrConstLMatrix4d(self, mat):
            returnValue = libpanda._inPSkjPNdJL(self.this, mat.this)
            returnObject = PlaneD(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getReflectionMat(self):
            returnValue = libpanda._inPSkjPsTh3(self.this)
            returnObject = Mat4D.Mat4D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNormal(self):
            returnValue = libpanda._inPSkjPxoIM(self.this)
            returnObject = Vec3D.Vec3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getPoint(self):
            returnValue = libpanda._inPSkjPGqrN(self.this)
            returnObject = Point3D.Point3D(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def distToPlane(self, point):
            returnValue = libpanda._inPSkjPD6Ci(self.this, point.this)
            return returnValue

        
        def intersectsLine(self, intersectionPoint, p1, p2):
            returnValue = libpanda._inPSkjPs51l(self.this, intersectionPoint.this, p1.this, p2.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPSkjPqMuW(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstPlaned_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPSkjPdl9K(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstPlaned_ptrOstream(self, out):
            returnValue = libpanda._inPSkjP1MYN(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], PlaneD):
                    return self.overloaded_constructor_ptrConstPlaned(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PlaneD> '
            elif numArgs == 2:
                if isinstance(_args[0], Vec3D.Vec3D):
                    if isinstance(_args[1], Point3D.Point3D):
                        return self.overloaded_constructor_ptrConstLVector3d_ptrConstLPoint3d(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3D.Point3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> '
            elif numArgs == 3:
                if isinstance(_args[0], Point3D.Point3D):
                    if isinstance(_args[1], Point3D.Point3D):
                        if isinstance(_args[2], Point3D.Point3D):
                            return self.overloaded_constructor_ptrConstLPoint3d_ptrConstLPoint3d_ptrConstLPoint3d(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3D.Point3D> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3D.Point3D> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3D.Point3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4D.Mat4D):
                    return self.overloaded___mul___ptrConstPlaned_ptrConstLMatrix4d(_args[0])
                elif isinstance(_args[0], Mat3D.Mat3D):
                    return self.overloaded___mul___ptrConstPlaned_ptrConstLMatrix3d(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat3D.Mat3D> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstPlaned_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstPlaned_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['PlaneD'] = PlaneD

