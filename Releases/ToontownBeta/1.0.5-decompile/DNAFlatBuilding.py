# Source Generated with Decompyle++
# File: DNAFlatBuilding.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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

def generateClass_DNAFlatBuilding():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNAFlatBuilding(DNANode.DNANode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libtoontown._inPdt4yV_4a(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libtoontown._inPdt4yWuKf()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDNAFlatBuilding(self, building):
            self.this = libtoontown._inPdt4yvfIO(building.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4y2TRK:
                libtoontown._inPdt4y2TRK(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4y4o0g()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setWidth(self, width):
            returnValue = libtoontown._inPdt4ynQs5(self.this, width)
            return returnValue

        
        def getWidth(self):
            returnValue = libtoontown._inPdt4yM1r5(self.this)
            return returnValue

        
        def getCurrentWallHeight(self):
            returnValue = libtoontown._inPdt4yMvhS(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                elif isinstance(_args[0], DNAFlatBuilding):
                    return self.overloaded_constructor_ptrConstDNAFlatBuilding(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <DNAFlatBuilding> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DNAFlatBuilding'] = DNAFlatBuilding

