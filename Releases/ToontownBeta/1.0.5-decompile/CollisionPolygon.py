# Source Generated with Decompyle++
# File: CollisionPolygon.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Point3
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
import CollisionPlane
import Plane
import Vec3
import Point3
import TypeHandle
classDefined = 0

def generateClass_CollisionPolygon():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionPolygon(CollisionPlane.CollisionPlane, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c):
            self.this = libpanda._inPHwcaq8iq(a.this, b.this, c.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b, c, d):
            self.this = libpanda._inPHwca_WtC(a.this, b.this, c.this, d.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, begin, end):
            self.this = libpanda._inPHwcaEcpw(begin.this, end.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwca9k82:
                libpanda._inPHwca9k82(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaBX_a()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
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
            elif numArgs == 4:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Point3.Point3):
                            if isinstance(_args[3], Point3.Point3):
                                return self.overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f_ptrConstLPoint3f(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <Point3.Point3> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Point3.Point3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 4 '


    globals()['CollisionPolygon'] = CollisionPolygon

