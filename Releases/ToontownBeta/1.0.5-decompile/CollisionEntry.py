# Source Generated with Decompyle++
# File: CollisionEntry.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionSolid
import CollisionNode
import NamedNode
import NodePath
import Mat4
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

def generateClass_CollisionEntry():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionEntry(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPHwcamqwG:
                libpanda._inPHwcamqwG(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaLiuZ()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getFrom(self):
            returnValue = libpanda._inPHwca_JZK(self.this)
            returnObject = CollisionSolid.CollisionSolid(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def hasInto(self):
            returnValue = libpanda._inPHwcantcn(self.this)
            return returnValue

        
        def getInto(self):
            returnValue = libpanda._inPHwca_pba(self.this)
            returnObject = CollisionSolid.CollisionSolid(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getFromNode(self):
            returnValue = libpanda._inPHwcaXSyC(self.this)
            returnObject = CollisionNode.CollisionNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getIntoNode(self):
            returnValue = libpanda._inPHwca3S1S(self.this)
            returnObject = NamedNode.NamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getIntoNodePath(self):
            returnValue = libpanda._inPHwca1RTn(self.this)
            returnObject = NodePath.NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getFromSpace(self):
            returnValue = libpanda._inPHwcaqN11(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getIntoSpace(self):
            returnValue = libpanda._inPHwcaJL4F(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getWrtSpace(self):
            returnValue = libpanda._inPHwca_ged(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getInvWrtSpace(self):
            returnValue = libpanda._inPHwca03HE(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setIntoIntersectionPoint(self, point):
            returnValue = libpanda._inPHwcaMr8J(self.this, point.this)
            return returnValue

        
        def hasIntoIntersectionPoint(self):
            returnValue = libpanda._inPHwcaRZMr(self.this)
            return returnValue

        
        def getIntoIntersectionPoint(self):
            returnValue = libpanda._inPHwcapuLe(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def hasFromIntersectionPoint(self):
            returnValue = libpanda._inPHwcaxMHb(self.this)
            return returnValue

        
        def getFromIntersectionPoint(self):
            returnValue = libpanda._inPHwcaJuGO(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setIntoSurfaceNormal(self, normal):
            returnValue = libpanda._inPHwcav0ZL(self.this, normal.this)
            return returnValue

        
        def hasIntoSurfaceNormal(self):
            returnValue = libpanda._inPHwcaLfZi(self.this)
            return returnValue

        
        def getIntoSurfaceNormal(self):
            returnValue = libpanda._inPHwcajZXV(self.this)
            returnObject = Vec3.Vec3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setIntoDepth(self, depth):
            returnValue = libpanda._inPHwcaJumw(self.this, depth)
            return returnValue

        
        def hasIntoDepth(self):
            returnValue = libpanda._inPHwcaLWMs(self.this)
            return returnValue

        
        def getIntoDepth(self):
            returnValue = libpanda._inPHwcaj1Lf(self.this)
            return returnValue


    globals()['CollisionEntry'] = CollisionEntry

