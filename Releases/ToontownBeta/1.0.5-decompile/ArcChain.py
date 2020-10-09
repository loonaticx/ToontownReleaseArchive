# Source Generated with Decompyle++
# File: ArcChain.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Node
import NodeRelation
import TypeHandle
classDefined = 0

def generateClass_ArcChain():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ArcChain(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
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
            if libpanda and libpanda._inPs9JIe0EH:
                libpanda._inPs9JIe0EH(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPs9JIGpAP()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isEmpty(self):
            returnValue = libpanda._inPs9JI1dl7(self.this)
            return returnValue

        
        def isSingleton(self):
            returnValue = libpanda._inPs9JIJkdk(self.this)
            return returnValue

        
        def hasArcs(self):
            returnValue = libpanda._inPs9JIYQrY(self.this)
            return returnValue

        
        def getNumNodes(self):
            returnValue = libpanda._inPs9JIl12h(self.this)
            return returnValue

        
        def getNode(self, index):
            returnValue = libpanda._inPs9JIa0Cr(self.this, index)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumArcs(self):
            returnValue = libpanda._inPs9JIiNIV(self.this)
            return returnValue

        
        def getArc(self, index):
            returnValue = libpanda._inPs9JIg48Z(self.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getTopNode(self):
            returnValue = libpanda._inPs9JINac1(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def node(self):
            returnValue = libpanda._inPs9JIuQGC(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def arc(self):
            returnValue = libpanda._inPs9JI0z4Z(self.this)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['ArcChain'] = ArcChain

