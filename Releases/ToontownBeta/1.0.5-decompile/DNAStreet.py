# Source Generated with Decompyle++
# File: DNAStreet.pyo (Python 2.0)

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

def generateClass_DNAStreet():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAStreet(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4y3fMW(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNAStreet(self, street):
            self.this = libtoontown._inPdt4yHiML(street.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yn8q2:
                libtoontown._inPdt4yn8q2(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yPntw()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCode(self, code):
            returnValue = libtoontown._inPdt4yLAUO(self.this, code)
            return returnValue

        
        def getCode(self):
            returnValue = libtoontown._inPdt4y9pjL(self.this)
            return returnValue

        
        def setStreetTexture(self, streetTexture):
            returnValue = libtoontown._inPdt4y_qeL(self.this, streetTexture)
            return returnValue

        
        def getStreetTexture(self):
            returnValue = libtoontown._inPdt4ysyQY(self.this)
            return returnValue

        
        def setSidewalkTexture(self, sidewalkTexture):
            returnValue = libtoontown._inPdt4yaO_l(self.this, sidewalkTexture)
            return returnValue

        
        def getSidewalkTexture(self):
            returnValue = libtoontown._inPdt4ydrke(self.this)
            return returnValue

        
        def setStreetColor(self, color):
            returnValue = libtoontown._inPdt4ylRwt(self.this, color.this)
            return returnValue

        
        def getStreetColor(self):
            returnValue = libtoontown._inPdt4yqiQg(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setSidewalkColor(self, color):
            returnValue = libtoontown._inPdt4yDFkL(self.this, color.this)
            return returnValue

        
        def getSidewalkColor(self):
            returnValue = libtoontown._inPdt4yfBDn(self.this)
            returnObject = VBase4.VBase4(None)
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
                elif isinstance(_args[0], DNAStreet):
                    return self.overloaded_constructor_ptrConstDNAStreet(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAStreet> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['DNAStreet'] = DNAStreet

