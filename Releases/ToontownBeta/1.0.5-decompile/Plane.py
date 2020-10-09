# Source Generated with Decompyle++
# File: Plane.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Point3
import Vec3
import Mat3
import Mat4
import Ostream
classDefined = 0

def generateClass_Plane():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Plane(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPSkjPGRcW()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPlanef(self, copy):
            self.this = libpanda._inPSkjPYuPv(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c):
            self.this = libpanda._inPSkjPZfjF(a.this, b.this, c.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLVector3f_ptrConstLPoint3f(self, normal, point):
            self.this = libpanda._inPSkjP9b54(normal.this, point.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjPdYxL:
                libpanda._inPSkjPdYxL(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPSkjPfDUO(self.this, copy.this)
            returnObject = Plane(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded___mul___ptrConstPlanef_ptrConstLMatrix3f(self, mat):
            returnValue = libpanda._inPSkjPO3cZ(self.this, mat.this)
            returnObject = Plane(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded___mul___ptrConstPlanef_ptrConstLMatrix4f(self, mat):
            returnValue = libpanda._inPSkjPOn_s(self.this, mat.this)
            returnObject = Plane(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getReflectionMat(self):
            returnValue = libpanda._inPSkjPQYm3(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNormal(self):
            returnValue = libpanda._inPSkjPNhNM(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getPoint(self):
            returnValue = libpanda._inPSkjPiiwN(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def distToPlane(self, point):
            returnValue = libpanda._inPSkjPrrLi(self.this, point.this)
            return returnValue

        
        def intersectsLine(self, intersectionPoint, p1, p2):
            returnValue = libpanda._inPSkjP04H0(self.this, intersectionPoint.this, p1.this, p2.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPSkjPmUzW(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstPlanef_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPSkjPxdCL(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstPlanef_ptrOstream(self, out):
            returnValue = libpanda._inPSkjPRlcN(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Plane):
                    return self.overloaded_constructor_ptrConstPlanef(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Plane> '
            elif numArgs == 2:
                if isinstance(_args[0], Vec3.Vec3):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_constructor_ptrConstLVector3f_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Vec3.Vec3> '
            elif numArgs == 3:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Point3.Point3):
                            return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '

        
        def __mul__(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4.Mat4):
                    return self.overloaded___mul___ptrConstPlanef_ptrConstLMatrix4f(_args[0])
                elif isinstance(_args[0], Mat3.Mat3):
                    return self.overloaded___mul___ptrConstPlanef_ptrConstLMatrix3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> <Mat3.Mat3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstPlanef_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstPlanef_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Plane'] = Plane

