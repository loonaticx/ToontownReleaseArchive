# Source Generated with Decompyle++
# File: CollisionTraverser.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import TypeHandle
import CollisionNode
import CollisionHandler
import Node
import NodePath
import Ostream
import TraverserVisitorNullTransitionWrapperCollisionLevelState
classDefined = 0

def generateClass_CollisionTraverser():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CollisionTraverser(TraverserVisitorNullTransitionWrapperCollisionLevelState.TraverserVisitorNullTransitionWrapperCollisionLevelState, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrTypeHandle(self, graphType):
            self.this = libpanda._inPHwcaH6xz(graphType.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHwcaEy8j()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHwca88LK:
                libpanda._inPHwca88LK(self.this)
            

        
        def addCollider(self, node, handler):
            returnValue = libpanda._inPHwcaBxgA(self.this, node.this, handler.this)
            return returnValue

        
        def removeCollider(self, node):
            returnValue = libpanda._inPHwcaU82L(self.this, node.this)
            return returnValue

        
        def hasCollider(self, node):
            returnValue = libpanda._inPHwcaKNjx(self.this, node.this)
            return returnValue

        
        def getNumColliders(self):
            returnValue = libpanda._inPHwcaHRl0(self.this)
            return returnValue

        
        def getCollider(self, n):
            returnValue = libpanda._inPHwca18E2(self.this, n)
            returnObject = CollisionNode.CollisionNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getHandler(self, node):
            returnValue = libpanda._inPHwcaWagr(self.this, node.this)
            returnObject = CollisionHandler.CollisionHandler(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearColliders(self):
            returnValue = libpanda._inPHwcasWkc(self.this)
            return returnValue

        
        def overloaded_traverse_ptrCollisionTraverser_ptrNode(self, root):
            returnValue = libpanda._inPHwcaT84b(self.this, root.this)
            return returnValue

        
        def overloaded_traverse_ptrCollisionTraverser_ptrConstNodePath(self, root):
            returnValue = libpanda._inPHwcaB6Ji(self.this, root.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPHwcaDFI1(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstCollisionTraverser_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPHwca_h_7(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstCollisionTraverser_ptrOstream(self, out):
            returnValue = libpanda._inPHwcaO2LN(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], TypeHandle.TypeHandle):
                    return self.overloaded_constructor_ptrTypeHandle(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle.TypeHandle> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def traverse(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodePath.NodePath):
                    return self.overloaded_traverse_ptrCollisionTraverser_ptrConstNodePath(_args[0])
                elif isinstance(_args[0], Node.Node):
                    return self.overloaded_traverse_ptrCollisionTraverser_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath.NodePath> <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstCollisionTraverser_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstCollisionTraverser_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['CollisionTraverser'] = CollisionTraverser

