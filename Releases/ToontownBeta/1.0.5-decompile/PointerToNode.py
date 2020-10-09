# Source Generated with Decompyle++
# File: PointerToNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Node
import PointerToBaseNode
classDefined = 0

def generateClass_PointerToNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointerToNode(PointerToBaseNode.PointerToBaseNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrNode(self, ptr):
            self.this = libpanda._inPs9JIN70d(ptr.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPs9JI4HcA()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNode(self, copy):
            self.this = libpanda._inPs9JIu6Y9(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPs9JIvwHE:
                libpanda._inPs9JIvwHE(self.this)
            

        
        def p(self):
            returnValue = libpanda._inPs9JIvt03(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_assign_ptrPointerToNode_ptrNode(self, ptr):
            returnValue = libpanda._inPs9JIwbfD(self.this, ptr.this)
            returnObject = PointerToNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrPointerToNode_ptrNode(self, copy):
            returnValue = libpanda._inPs9JIo1k2(self.this, copy.this)
            returnObject = PointerToNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isNull(self):
            returnValue = libpanda._inPs9JI0OZB(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPs9JIUgtZ(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Node.Node):
                    return self.overloaded_constructor_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Node.Node):
                    return self.overloaded_assign_ptrPointerToNode_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['PointerToNode'] = PointerToNode

