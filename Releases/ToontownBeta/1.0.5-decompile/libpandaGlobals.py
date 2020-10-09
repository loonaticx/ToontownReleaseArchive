# Source Generated with Decompyle++
# File: libpandaGlobals.pyo (Python 2.0)

import types
import libpanda
import Node
import AnimControlCollection
import VBase3
import Mat3
import Vec2
import Point2
import VBase4
import Mat4
import Vec3
import Point3
import VBase3D
import Mat3D
import Vec2D
import Point2D
import VBase4D
import Mat4D
import Vec3D
import Point3D
import Quat
import QuatD
import DSearchPath

def __mul__(*_args):
    numArgs = len(_args)
    if numArgs == 2:
        if isinstance(_args[0], Vec3D.Vec3D):
            if isinstance(_args[1], Mat4D.Mat4D):
                return overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], Vec2D.Vec2D):
            if isinstance(_args[1], Mat3D.Mat3D):
                return overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], Vec2.Vec2):
            if isinstance(_args[1], Mat3.Mat3):
                return overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], VBase4D.VBase4D):
            if isinstance(_args[1], Mat4D.Mat4D):
                return overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], VBase4.VBase4):
            if isinstance(_args[1], Mat4.Mat4):
                return overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], VBase3D.VBase3D):
            if isinstance(_args[1], Mat3D.Mat3D):
                return overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], VBase3.VBase3):
            if isinstance(_args[1], Mat3.Mat3):
                return overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], Vec3.Vec3):
            if isinstance(_args[1], Mat4.Mat4):
                return overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], Point3D.Point3D):
            if isinstance(_args[1], Mat4D.Mat4D):
                return overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4D.Mat4D> '
        elif isinstance(_args[0], Point3.Point3):
            if isinstance(_args[1], Mat4.Mat4):
                return overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
        elif isinstance(_args[0], Point2D.Point2D):
            if isinstance(_args[1], Mat3D.Mat3D):
                return overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3D.Mat3D> '
        elif isinstance(_args[0], Point2.Point2):
            if isinstance(_args[1], Mat3.Mat3):
                return overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Mat3.Mat3> '
        elif isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], QuatD.QuatD):
                return overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <QuatD.QuatD> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Quat.Quat):
                return overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], QuatD.QuatD):
                return overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <QuatD.QuatD> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Quat.Quat):
                return overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(_args[0], _args[1])
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Quat.Quat> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Vec3D.Vec3D> <Vec2D.Vec2D> <Vec2.Vec2> <VBase4D.VBase4D> <VBase4.VBase4> <VBase3D.VBase3D> <VBase3.VBase3> <Vec3.Vec3> <Point3D.Point3D> <Point3.Point3> <Point2D.Point2D> <Point2.Point2> <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


def decomposeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        if isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 6:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            if isinstance(_args[5], types.IntType):
                                return overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                            else:
                                raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                            if isinstance(_args[5], types.IntType):
                                return overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                            else:
                                raise TypeError, 'Invalid argument 5, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 6 '


def composeMatrix(*_args):
    numArgs = len(_args)
    if numArgs == 4:
        if isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 5:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], VBase3D.VBase3D):
                if isinstance(_args[2], VBase3D.VBase3D):
                    if isinstance(_args[3], VBase3D.VBase3D):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3D.VBase3D> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3D.VBase3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3D.VBase3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], VBase3.VBase3):
                if isinstance(_args[2], VBase3.VBase3):
                    if isinstance(_args[3], VBase3.VBase3):
                        if isinstance(_args[4], types.IntType):
                            return overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3], _args[4])
                        else:
                            raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 4 5 '


def rotateTo(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    return overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    return overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    return overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    return overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 '


def headsUp(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType):
                    return overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType):
                    return overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType):
                    return overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType):
                    return overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '


def lookAt(*_args):
    numArgs = len(_args)
    if numArgs == 3:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType):
                    return overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType):
                    return overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], types.IntType):
                    return overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], types.IntType):
                    return overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    elif numArgs == 4:
        if isinstance(_args[0], Mat4D.Mat4D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat4.Mat4):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        elif isinstance(_args[0], Mat3D.Mat3D):
            if isinstance(_args[1], Vec3D.Vec3D):
                if isinstance(_args[2], Vec3D.Vec3D):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3D.Vec3D> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3D.Vec3D> '
        elif isinstance(_args[0], Mat3.Mat3):
            if isinstance(_args[1], Vec3.Vec3):
                if isinstance(_args[2], Vec3.Vec3):
                    if isinstance(_args[3], types.IntType):
                        return overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(_args[0], _args[1], _args[2], _args[3])
                    else:
                        raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
            else:
                raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <Mat4D.Mat4D> <Mat4.Mat4> <Mat3D.Mat3D> <Mat3.Mat3> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 '


def deg2Rad(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return overloaded_deg2Rad_float(_args[0])
        elif isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return overloaded_deg2Rad_double(_args[0])
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def rad2Deg(*_args):
    numArgs = len(_args)
    if numArgs == 1:
        if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return overloaded_rad2Deg_float(_args[0])
        elif isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
            return overloaded_rad2Deg_double(_args[0])
        else:
            raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.FloatType> '
    else:
        raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


def autoBind(rootNode, controls, hierarchyMatchFlags):
    returnValue = libpanda._inPn9gM_2uP(rootNode.this, controls.this, hierarchyMatchFlags)
    return returnValue


def traverseDataGraph(root):
    returnValue = libpanda._inPSLSelzN1(root.this)
    return returnValue


def overloaded_deg2Rad_double(f):
    returnValue = libpanda._inPVZN3Tto4(f)
    return returnValue


def overloaded_rad2Deg_double(f):
    returnValue = libpanda._inPVZN3ZDSs(f)
    return returnValue


def overloaded_deg2Rad_float(f):
    returnValue = libpanda._inPVZN3KkCI(f)
    return returnValue


def overloaded_rad2Deg_float(f):
    returnValue = libpanda._inPVZN3B1q7(f)
    return returnValue


def overloaded___mul___ptrConstLVecBase3f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3Ssml(v.this, m.this)
    returnObject = VBase3.VBase3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVector2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3Yz0h(v.this, m.this)
    returnObject = Vec2.Vec2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLPoint2f_ptrConstLMatrix3f(v, m):
    returnValue = libpanda._inPVZN3LcRW(v.this, m.this)
    returnObject = Point2.Point2(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVecBase4f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN3eH2G(v.this, m.this)
    returnObject = VBase4.VBase4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVector3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN30Z3o(v.this, m.this)
    returnObject = Vec3.Vec3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLPoint3f_ptrConstLMatrix4f(v, m):
    returnValue = libpanda._inPVZN3XneO(v.this, m.this)
    returnObject = Point3.Point3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVecBase3d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN3z54W(v.this, m.this)
    returnObject = VBase3D.VBase3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVector2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN3J_Wf(v.this, m.this)
    returnObject = Vec2D.Vec2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLPoint2d_ptrConstLMatrix3d(v, m):
    returnValue = libpanda._inPVZN3r5KI(v.this, m.this)
    returnObject = Point2D.Point2D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVecBase4d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3ADI4(v.this, m.this)
    returnObject = VBase4D.VBase4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLVector3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3p1Zm(v.this, m.this)
    returnObject = Vec3D.Vec3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLPoint3d_ptrConstLMatrix4d(v, m):
    returnValue = libpanda._inPVZN3fwZA(v.this, m.this)
    returnObject = Point3D.Point3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLMatrix3f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPVZN3dCmH(m.this, q.this)
    returnObject = Mat3.Mat3(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLMatrix4f_ptrConstLQuaternionf(m, q):
    returnValue = libpanda._inPVZN3jDmO(m.this, q.this)
    returnObject = Mat4.Mat4(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLMatrix3d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPVZN38MkX(m.this, q.this)
    returnObject = Mat3D.Mat3D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded___mul___ptrConstLMatrix4d_ptrConstLQuaterniond(m, q):
    returnValue = libpanda._inPVZN3KGke(m.this, q.this)
    returnObject = Mat4D.Mat4D(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    returnObject.userManagesMemory = 1
    return returnObject


def overloaded_composeMatrix_ptrLMatrix3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3x0Bn(mat.this, scale.this, hpr.this, cs)
    return returnValue


def overloaded_composeMatrix_ptrLMatrix4f_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN3JYz_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3Di_s(mat.this, scale.this, hpr.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(mat, scale, hpr, roll, cs):
    returnValue = libpanda._inPVZN3mOw6(mat.this, scale.this, hpr.this, roll, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN3JlRi(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix4f_ptrLVecBase3f_ptrLVecBase3f_ptrLVecBase3f_float___enum__CoordinateSystem(mat, scale, hpr, translate, roll, cs):
    returnValue = libpanda._inPVZN3rRsF(mat.this, scale.this, hpr.this, translate.this, roll, cs)
    return returnValue


def overloaded_composeMatrix_ptrLMatrix3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3rvzC(mat.this, scale.this, hpr.this, cs)
    return returnValue


def overloaded_composeMatrix_ptrLMatrix4d_ptrConstLVecBase3d_ptrConstLVecBase3d_ptrConstLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN31kjT(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, cs):
    returnValue = libpanda._inPVZN3kgAD(mat.this, scale.this, hpr.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(mat, scale, hpr, roll, cs):
    returnValue = libpanda._inPVZN3Mw8r(mat.this, scale.this, hpr.this, roll, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d___enum__CoordinateSystem(mat, scale, hpr, translate, cs):
    returnValue = libpanda._inPVZN30M1_(mat.this, scale.this, hpr.this, translate.this, cs)
    return returnValue


def overloaded_decomposeMatrix_ptrConstLMatrix4d_ptrLVecBase3d_ptrLVecBase3d_ptrLVecBase3d_double___enum__CoordinateSystem(mat, scale, hpr, translate, roll, cs):
    returnValue = libpanda._inPVZN3siDK(mat.this, scale.this, hpr.this, translate.this, roll, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPlHnb(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPsGPP(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPyEWz(mat.this, fwd.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPMr_D(mat.this, fwd.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPljfg(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPE2XP(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPygM4(mat.this, fwd.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix4f_ptrConstLVector3f___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPUaJE(mat.this, fwd.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPf9So(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPXRo7(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPryd4(mat.this, fwd.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPv8J6(mat.this, fwd.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPfZLt(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, up, cs):
    returnValue = libpanda._inPSkjPP_x7(mat.this, fwd.this, up.this, cs)
    return returnValue


def overloaded_headsUp_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjPrOW9(mat.this, fwd.this, cs)
    return returnValue


def overloaded_lookAt_ptrLMatrix4d_ptrConstLVector3d___enum__CoordinateSystem(mat, fwd, cs):
    returnValue = libpanda._inPSkjP3rT6(mat.this, fwd.this, cs)
    return returnValue


def overloaded_rotateTo_ptrLMatrix3f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjPzINk(mat.this, a.this, b.this)
    return returnValue


def overloaded_rotateTo_ptrLMatrix3d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjP1NG6(mat.this, a.this, b.this)
    return returnValue


def overloaded_rotateTo_ptrLMatrix4f_ptrConstLVector3f_ptrConstLVector3f(mat, a, b):
    returnValue = libpanda._inPSkjP4IbA(mat.this, a.this, b.this)
    return returnValue


def overloaded_rotateTo_ptrLMatrix4d_ptrConstLVector3d_ptrConstLVector3d(mat, a, b):
    returnValue = libpanda._inPSkjPqNUW(mat.this, a.this, b.this)
    return returnValue


def getModelPath():
    returnValue = libpanda._inPflbovUeg()
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getTexturePath():
    returnValue = libpanda._inPflboQ6tZ()
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject


def getSoundPath():
    returnValue = libpanda._inPflbouWvu()
    returnObject = DSearchPath.DSearchPath(None)
    returnObject.this = returnValue
    if returnObject.this == 0:
        return None
    
    return returnObject

HCCUT = 1
HCFREE = 2
HCG1 = 3
HCSMOOTH = 4
PCTHPR = 2
PCTNONE = 0
PCTT = 3
PCTXYZ = 1
TMALIGNCENTER = 3
TMALIGNLEFT = 1
TMALIGNRIGHT = 2
