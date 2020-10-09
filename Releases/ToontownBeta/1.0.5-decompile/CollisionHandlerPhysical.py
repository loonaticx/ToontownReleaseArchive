# Source Generated with Decompyle++
# File: CollisionHandlerPhysical.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CollisionHandlerEvent
import CollisionNode
import DriveInterface
import NodeRelation
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import CollisionHandler
import TypeHandle
import CollisionHandlerEvent
import TypeHandle
classDefined = 0

def generateClass_CollisionHandlerPhysical():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionHandlerPhysical(CollisionHandlerEvent.CollisionHandlerEvent, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPHwcaVSmv:
                libpanda._inPHwcaVSmv(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHwcaG_13()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_addCollider_ptrCollisionHandlerPhysical_ptrCollisionNode_ptrDriveInterface(self, node, driveInterface):
            returnValue = libpanda._inPHwcad0qU(self.this, node.this, driveInterface.this)
            return returnValue

        
        def overloaded_addCollider_ptrCollisionHandlerPhysical_ptrCollisionNode_ptrNodeRelation(self, node, arc):
            returnValue = libpanda._inPHwcaQHVM(self.this, node.this, arc.this)
            return returnValue

        
        def removeCollider(self, node):
            returnValue = libpanda._inPHwcazvCL(self.this, node.this)
            return returnValue

        
        def hasCollider(self, node):
            returnValue = libpanda._inPHwcaYZQ4(self.this, node.this)
            return returnValue

        
        def clearColliders(self):
            returnValue = libpanda._inPHwcaNCVz(self.this)
            return returnValue

        
        def addCollider(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], CollisionNode.CollisionNode):
                    if isinstance(_args[1], NodeRelation.NodeRelation):
                        return self.overloaded_addCollider_ptrCollisionHandlerPhysical_ptrCollisionNode_ptrNodeRelation(_args[0], _args[1])
                    elif isinstance(_args[1], DriveInterface.DriveInterface):
                        return self.overloaded_addCollider_ptrCollisionHandlerPhysical_ptrCollisionNode_ptrDriveInterface(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <NodeRelation.NodeRelation> <DriveInterface.DriveInterface> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <CollisionNode.CollisionNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 '


    globals()['CollisionHandlerPhysical'] = CollisionHandlerPhysical

