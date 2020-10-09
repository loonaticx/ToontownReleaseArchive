# Source Generated with Decompyle++
# File: DriveInterface.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import VBase3
import Mat4
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import DataNode
import TypeHandle
classDefined = 0

def generateClass_DriveInterface():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DriveInterface(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPyiw5jxDJ(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPyiw5BN_n()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPyiw5tESB()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setForwardSpeed(self, speed):
            returnValue = libpanda._inPyiw5Dtpq(self.this, speed)
            return returnValue

        
        def getForwardSpeed(self):
            returnValue = libpanda._inPyiw5YkJb(self.this)
            return returnValue

        
        def setReverseSpeed(self, speed):
            returnValue = libpanda._inPyiw52Q5G(self.this, speed)
            return returnValue

        
        def getReverseSpeed(self):
            returnValue = libpanda._inPyiw5lnX3(self.this)
            return returnValue

        
        def setRotateSpeed(self, speed):
            returnValue = libpanda._inPyiw5FIRt(self.this, speed)
            return returnValue

        
        def getRotateSpeed(self):
            returnValue = libpanda._inPyiw51QCa(self.this)
            return returnValue

        
        def setVerticalDeadZone(self, zone):
            returnValue = libpanda._inPyiw54k6o(self.this, zone)
            return returnValue

        
        def getVerticalDeadZone(self):
            returnValue = libpanda._inPyiw5PEgE(self.this)
            return returnValue

        
        def setHorizontalDeadZone(self, zone):
            returnValue = libpanda._inPyiw5rxFf(self.this, zone)
            return returnValue

        
        def getHorizontalDeadZone(self):
            returnValue = libpanda._inPyiw5aZKJ(self.this)
            return returnValue

        
        def setVerticalRampUpTime(self, rampUpTime):
            returnValue = libpanda._inPyiw5Tq8o(self.this, rampUpTime)
            return returnValue

        
        def getVerticalRampUpTime(self):
            returnValue = libpanda._inPyiw5jZSD(self.this)
            return returnValue

        
        def setVerticalRampDownTime(self, rampDownTime):
            returnValue = libpanda._inPyiw5dwik(self.this, rampDownTime)
            return returnValue

        
        def getVerticalRampDownTime(self):
            returnValue = libpanda._inPyiw5bVRW(self.this)
            return returnValue

        
        def setHorizontalRampUpTime(self, rampUpTime):
            returnValue = libpanda._inPyiw5zPeH(self.this, rampUpTime)
            return returnValue

        
        def getHorizontalRampUpTime(self):
            returnValue = libpanda._inPyiw5GiM5(self.this)
            return returnValue

        
        def setHorizontalRampDownTime(self, rampDownTime):
            returnValue = libpanda._inPyiw5vEo5(self.this, rampDownTime)
            return returnValue

        
        def getHorizontalRampDownTime(self):
            returnValue = libpanda._inPyiw55bXI(self.this)
            return returnValue

        
        def getSpeed(self):
            returnValue = libpanda._inPyiw5oVix(self.this)
            return returnValue

        
        def getRotSpeed(self):
            returnValue = libpanda._inPyiw5JNE6(self.this)
            return returnValue

        
        def reset(self):
            returnValue = libpanda._inPyiw5D1cV(self.this)
            return returnValue

        
        def getPos(self):
            returnValue = libpanda._inPyiw5WA0H(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getX(self):
            returnValue = libpanda._inPyiw56qV2(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPyiw5KJp2(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPyiw5an82(self.this)
            return returnValue

        
        def overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(self, vec):
            returnValue = libpanda._inPyiw55_wj(self.this, vec.this)
            return returnValue

        
        def overloaded_setPos_ptrDriveInterface_float_float_float(self, x, y, z):
            returnValue = libpanda._inPyiw5cvcP(self.this, x, y, z)
            return returnValue

        
        def setX(self, x):
            returnValue = libpanda._inPyiw5itmn(self.this, x)
            return returnValue

        
        def setY(self, y):
            returnValue = libpanda._inPyiw5SL7n(self.this, y)
            return returnValue

        
        def setZ(self, z):
            returnValue = libpanda._inPyiw5CxNo(self.this, z)
            return returnValue

        
        def getHpr(self):
            returnValue = libpanda._inPyiw5RWtW(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getH(self):
            returnValue = libpanda._inPyiw56Gdx(self.this)
            return returnValue

        
        def getP(self):
            returnValue = libpanda._inPyiw5645z(self.this)
            return returnValue

        
        def getR(self):
            returnValue = libpanda._inPyiw5a1g0(self.this)
            return returnValue

        
        def overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(self, hpr):
            returnValue = libpanda._inPyiw5_1oy(self.this, hpr.this)
            return returnValue

        
        def overloaded_setHpr_ptrDriveInterface_float_float_float(self, h, p, r):
            returnValue = libpanda._inPyiw5xdVe(self.this, h, p, r)
            return returnValue

        
        def setH(self, h):
            returnValue = libpanda._inPyiw5iRvi(self.this, h)
            return returnValue

        
        def setP(self, p):
            returnValue = libpanda._inPyiw5ibKl(self.this, p)
            return returnValue

        
        def setR(self, r):
            returnValue = libpanda._inPyiw5Cfxl(self.this, r)
            return returnValue

        
        def setForceRoll(self, forceRoll):
            returnValue = libpanda._inPyiw5BPSy(self.this, forceRoll)
            return returnValue

        
        def isForceRoll(self):
            returnValue = libpanda._inPyiw5nOKH(self.this)
            return returnValue

        
        def clearForceRoll(self):
            returnValue = libpanda._inPyiw5HQCb(self.this)
            return returnValue

        
        def setCoordinateSystem(self, cs):
            returnValue = libpanda._inPyiw5PY0W(self.this, cs)
            return returnValue

        
        def getCoordinateSystem(self):
            returnValue = libpanda._inPyiw597_j(self.this)
            return returnValue

        
        def setIgnoreMouse(self, ignoreMouse):
            returnValue = libpanda._inPyiw5lB_J(self.this, ignoreMouse)
            return returnValue

        
        def getIgnoreMouse(self):
            returnValue = libpanda._inPyiw5Ao_x(self.this)
            return returnValue

        
        def setMat(self, mat):
            returnValue = libpanda._inPyiw5Mtoo(self.this, mat.this)
            return returnValue

        
        def getMat(self):
            returnValue = libpanda._inPyiw5c2p2(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def forceDgraph(self):
            returnValue = libpanda._inPyiw5JQXr(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_setHpr_ptrDriveInterface_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setHpr_ptrDriveInterface_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def setPos(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_setPos_ptrDriveInterface_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPos_ptrDriveInterface_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['DriveInterface'] = DriveInterface

