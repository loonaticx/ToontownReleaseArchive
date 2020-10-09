# Source Generated with Decompyle++
# File: Trackball.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
import VBase3
import Node
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

def generateClass_Trackball():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Trackball(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPyiw5_l2w(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPyiw5kDqY()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPyiw55svH()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def reset(self):
            returnValue = libpanda._inPyiw5Jm3x(self.this)
            return returnValue

        
        def getPos(self):
            returnValue = libpanda._inPyiw553AL(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getX(self):
            returnValue = libpanda._inPyiw5vvRC(self.this)
            return returnValue

        
        def getY(self):
            returnValue = libpanda._inPyiw53ebC(self.this)
            return returnValue

        
        def getZ(self):
            returnValue = libpanda._inPyiw5fRlC(self.this)
            return returnValue

        
        def overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(self, vec):
            returnValue = libpanda._inPyiw5vGB5(self.this, vec.this)
            return returnValue

        
        def overloaded_setPos_ptrTrackball_float_float_float(self, x, y, z):
            returnValue = libpanda._inPyiw5LFzu(self.this, x, y, z)
            return returnValue

        
        def setX(self, x):
            returnValue = libpanda._inPyiw57e66(self.this, x)
            return returnValue

        
        def setY(self, y):
            returnValue = libpanda._inPyiw5TOF7(self.this, y)
            return returnValue

        
        def setZ(self, z):
            returnValue = libpanda._inPyiw5LBP7(self.this, z)
            return returnValue

        
        def getHpr(self):
            returnValue = libpanda._inPyiw52_cy(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getH(self):
            returnValue = libpanda._inPyiw5uh1_(self.this)
            return returnValue

        
        def getP(self):
            returnValue = libpanda._inPyiw5vmDB(self.this)
            return returnValue

        
        def getR(self):
            returnValue = libpanda._inPyiw5fIXB(self.this)
            return returnValue

        
        def overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(self, hpr):
            returnValue = libpanda._inPyiw5pVdg(self.this, hpr.this)
            return returnValue

        
        def overloaded_setHpr_ptrTrackball_float_float_float(self, h, p, r):
            returnValue = libpanda._inPyiw5JaRW(self.this, h, p, r)
            return returnValue

        
        def setH(self, h):
            returnValue = libpanda._inPyiw57Qf4(self.this, h)
            return returnValue

        
        def setP(self, p):
            returnValue = libpanda._inPyiw57ls5(self.this, p)
            return returnValue

        
        def setR(self, r):
            returnValue = libpanda._inPyiw5LIB6(self.this, r)
            return returnValue

        
        def resetOriginHere(self):
            returnValue = libpanda._inPyiw5JILj(self.this)
            return returnValue

        
        def moveOrigin(self, x, y, z):
            returnValue = libpanda._inPyiw5ZM77(self.this, x, y, z)
            return returnValue

        
        def setInvert(self, flag):
            returnValue = libpanda._inPyiw5NeSo(self.this, flag)
            return returnValue

        
        def getInvert(self):
            returnValue = libpanda._inPyiw5IRyR(self.this)
            return returnValue

        
        def setRelTo(self, relTo):
            returnValue = libpanda._inPyiw58l7T(self.this, relTo.this)
            return returnValue

        
        def getRelTo(self):
            returnValue = libpanda._inPyiw5F6gh(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setCoordinateSystem(self, cs):
            returnValue = libpanda._inPyiw5vJfS(self.this, cs)
            return returnValue

        
        def getCoordinateSystem(self):
            returnValue = libpanda._inPyiw5yzF5(self.this)
            return returnValue

        
        def setMat(self, mat):
            returnValue = libpanda._inPyiw5bBbb(self.this, mat.this)
            return returnValue

        
        def getMat(self):
            returnValue = libpanda._inPyiw5SPbi(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getTransMat(self):
            returnValue = libpanda._inPyiw5PJHL(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
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
                    return self.overloaded_setHpr_ptrTrackball_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setHpr_ptrTrackball_float_float_float(_args[0], _args[1], _args[2])
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
                    return self.overloaded_setPos_ptrTrackball_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPos_ptrTrackball_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['Trackball'] = Trackball

