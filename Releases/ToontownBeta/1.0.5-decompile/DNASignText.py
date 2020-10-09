# Source Generated with Decompyle++
# File: DNASignText.pyo (Python 2.0)

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

def generateClass_DNASignText():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASignText(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4yNhjl(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4ydrFc()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNASignText(self, signText):
            self.this = libtoontown._inPdt4yF4b4(signText.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4ySKY9:
                libtoontown._inPdt4ySKY9(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4ye9AS()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCode(self, code):
            returnValue = libtoontown._inPdt4yxaw_(self.this, code)
            return returnValue

        
        def getCode(self):
            returnValue = libtoontown._inPdt4y_YSb(self.this)
            return returnValue

        
        def setColor(self, color):
            returnValue = libtoontown._inPdt4ymoiX(self.this, color.this)
            return returnValue

        
        def getColor(self):
            returnValue = libtoontown._inPdt4ycic1(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setLetters(self, letters):
            returnValue = libtoontown._inPdt4y_oYM(self.this, letters)
            return returnValue

        
        def getLetters(self):
            returnValue = libtoontown._inPdt4yhJcX(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNASignText):
                    return self.overloaded_constructor_ptrConstDNASignText(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNASignText> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNASignText'] = DNASignText

