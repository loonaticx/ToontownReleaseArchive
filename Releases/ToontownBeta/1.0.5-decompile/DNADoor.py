# Source Generated with Decompyle++
# File: DNADoor.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import NodePath
import DNAStorage
import Vec4
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

def generateClass_DNADoor():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNADoor(DNAGroup.DNAGroup, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4yMhFL(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yB_rG()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNADoor(self, door):
            self.this = libtoontown._inPdt4yVXHJ(door.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4ymFiA:
                libtoontown._inPdt4ymFiA(self.this)
            

        
        def setupDoor(doorNodePath, parent, doorOrigin, store, block, color):
            returnValue = libtoontown._inPdt4ydsvf(doorNodePath.this, parent.this, doorOrigin.this, store.this, block, color.this)
            return returnValue

        setupDoor = PandaStatic.PandaStatic(setupDoor)
        
        def getClassType():
            returnValue = libtoontown._inPdt4yxlO9()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setCode(self, code):
            returnValue = libtoontown._inPdt4ytj0Z(self.this, code)
            return returnValue

        
        def getCode(self):
            returnValue = libtoontown._inPdt4yq2DR(self.this)
            return returnValue

        
        def setColor(self, color):
            returnValue = libtoontown._inPdt4ycdjV(self.this, color.this)
            return returnValue

        
        def getColor(self):
            returnValue = libtoontown._inPdt4yM79z(self.this)
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
                elif isinstance(_args[0], DNADoor):
                    return self.overloaded_constructor_ptrConstDNADoor(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNADoor> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNADoor'] = DNADoor

