# Source Generated with Decompyle++
# File: DNANode.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase3
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
import DNAGroup
import NodePath
import DNAStorage
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_DNANode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNANode(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4ykvoe(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNANode(self, node):
            self.this = libtoontown._inPdt4yf558(node.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yu026:
                libtoontown._inPdt4yu026(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4y1VuV()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setPos(self, pos):
            returnValue = libtoontown._inPdt4yEFjI(self.this, pos.this)
            return returnValue

        
        def getPos(self):
            returnValue = libtoontown._inPdt4y9EQN(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setHpr(self, hpr):
            returnValue = libtoontown._inPdt4yMgac(self.this, hpr.this)
            return returnValue

        
        def getHpr(self):
            returnValue = libtoontown._inPdt4yj2Gh(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setScale(self, scale):
            returnValue = libtoontown._inPdt4ybi61(self.this, scale.this)
            return returnValue

        
        def getScale(self):
            returnValue = libtoontown._inPdt4y4MNF(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNANode):
                    return self.overloaded_constructor_ptrConstDNANode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNANode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['DNANode'] = DNANode

