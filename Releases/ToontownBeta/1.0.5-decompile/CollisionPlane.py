# Source Generated with Decompyle++
# File: CollisionPlane.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Plane
import Vec3
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
classDefined = 0

def generateClass_CollisionPlane():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionPlane(CollisionSolid.CollisionSolid, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConstPlanef(self, planeBase):
            self.this = libpanda._inPHwcae_hc(planeBase.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstCollisionPlane(self, copy):
            self.this = libpanda._inPHwcavPx1(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwcanOTK:
                libpanda._inPHwcanOTK(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwca11yU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getNormal(self):
            returnValue = libpanda._inPHwcafyK9(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def distToPlane(self, point):
            returnValue = libpanda._inPHwcaH18M(self.this, point.this)
            return returnValue

        
        def setPlane(self, planeBase):
            returnValue = libpanda._inPHwca5pAO(self.this, planeBase.this)
            return returnValue

        
        def getPlane(self):
            returnValue = libpanda._inPHwcakWX5(self.this)
            returnObject = Plane.Plane(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Plane.Plane):
                    return self.overloaded_constructor_ptrConstPlanef(_args[0])
                elif isinstance(_args[0], CollisionPlane):
                    return self.overloaded_constructor_ptrConstCollisionPlane(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Plane.Plane> <CollisionPlane> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['CollisionPlane'] = CollisionPlane

