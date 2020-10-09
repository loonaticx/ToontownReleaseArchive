# Source Generated with Decompyle++
# File: DNASign.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
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
import DNANode
import VBase3
import TypeHandle
classDefined = 0

def generateClass_DNASign():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASign(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4ylVC5(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yMAn0()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNASign(self, sign):
            self.this = libtoontown._inPdt4ySqjF(sign.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yRLNw:
                libtoontown._inPdt4yRLNw(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yhSMt()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCode(self, code):
            returnValue = libtoontown._inPdt4ydQxJ(self.this, code)
            return returnValue

        
        def getCode(self):
            returnValue = libtoontown._inPdt4yBBAB(self.this)
            return returnValue

        
        def setColor(self, color):
            returnValue = libtoontown._inPdt4ysUgF(self.this, color.this)
            return returnValue

        
        def getColor(self):
            returnValue = libtoontown._inPdt4yco5j(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNASign):
                    return self.overloaded_constructor_ptrConstDNASign(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASign> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNASign'] = DNASign

