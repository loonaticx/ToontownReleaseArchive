# Source Generated with Decompyle++
# File: BoundingLine.pyo (Python 2.0)

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
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import BoundingVolume
import Ostream
import TypeHandle
import GeometricBoundingVolume
import Point3
import Mat4
import TypeHandle
classDefined = 0

def generateClass_BoundingLine():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BoundingLine(GeometricBoundingVolume.GeometricBoundingVolume, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPSkjPAGM1()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLPoint3f_ptrConstLPoint3f(self, a, b):
            self.this = libpanda._inPSkjP5q_R(a.this, b.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjPgaIV:
                libpanda._inPSkjPgaIV(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjPf2Uv()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getPointA(self):
            returnValue = libpanda._inPSkjPKiF_(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getPointB(self):
            returnValue = libpanda._inPSkjPBQH_(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
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
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


    globals()['BoundingLine'] = BoundingLine

