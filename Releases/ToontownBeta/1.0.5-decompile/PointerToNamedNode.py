# Source Generated with Decompyle++
# File: PointerToNamedNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import NamedNode
import PointerToBaseNamedNode
classDefined = 0

def generateClass_PointerToNamedNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointerToNamedNode(PointerToBaseNamedNode.PointerToBaseNamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrNamedNode(self, ptr):
            self.this = libpanda._inPs9JIXH7Z(ptr.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPs9JIlqlZ()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNamedNode(self, copy):
            self.this = libpanda._inPs9JId40E(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPs9JIhEAh:
                libpanda._inPs9JIhEAh(self.this)
            

        
        def p(self):
            returnValue = libpanda._inPs9JI_maI(self.this)
            returnObject = NamedNode.NamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_assign_ptrPointerToNamedNode_ptrNamedNode(self, ptr):
            returnValue = libpanda._inPs9JIxCGQ(self.this, ptr.this)
            returnObject = PointerToNamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrPointerToNamedNode_ptrNamedNode(self, copy):
            returnValue = libpanda._inPs9JIfuau(self.this, copy.this)
            returnObject = PointerToNamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isNull(self):
            returnValue = libpanda._inPs9JIqglb(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPs9JIlvLM(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], NamedNode.NamedNode):
                    return self.overloaded_constructor_ptrNamedNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NamedNode.NamedNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NamedNode.NamedNode):
                    return self.overloaded_assign_ptrPointerToNamedNode_ptrNamedNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NamedNode.NamedNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['PointerToNamedNode'] = PointerToNamedNode

