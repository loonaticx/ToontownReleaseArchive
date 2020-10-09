# Source Generated with Decompyle++
# File: MultiTransitionPointerToLightLightNameClass.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Light
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import NodeTransition
import Ostream
import TypeHandle
classDefined = 0

def generateClass_MultiTransitionPointerToLightLightNameClass():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MultiTransitionPointerToLightLightNameClass(NodeTransition.NodeTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
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
            if libpanda and libpanda._inPi0oLOITp:
                libpanda._inPi0oLOITp(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPi0oLCiOX()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def clear(self):
            returnValue = libpanda._inPi0oL4n3C(self.this)
            return returnValue

        
        def overloaded_isIdentity_ptrConstMultiTransitionPointerToLightLightNameClass(self):
            returnValue = libpanda._inPi0oLYW3a(self.this)
            return returnValue

        
        def setDefaultDir(self, dir):
            returnValue = libpanda._inPi0oLk7QH(self.this, dir)
            return returnValue

        
        def getDefaultDir(self):
            returnValue = libpanda._inPi0oL9hPP(self.this)
            return returnValue

        
        def setIdentity(self, prop):
            returnValue = libpanda._inPi0oL_FQn(self.this, prop.this)
            return returnValue

        
        def setOn(self, prop):
            returnValue = libpanda._inPi0oLTxdR(self.this, prop.this)
            return returnValue

        
        def setOff(self, prop):
            returnValue = libpanda._inPi0oLtmYP(self.this, prop.this)
            return returnValue

        
        def overloaded_isIdentity_ptrConstMultiTransitionPointerToLightLightNameClass_ptrLight(self, prop):
            returnValue = libpanda._inPi0oL_z0j(self.this, prop.this)
            return returnValue

        
        def isOn(self, prop):
            returnValue = libpanda._inPi0oLEKBD(self.this, prop.this)
            return returnValue

        
        def isOff(self, prop):
            returnValue = libpanda._inPi0oL7pQh(self.this, prop.this)
            return returnValue

        
        def isIdentity(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_isIdentity_ptrConstMultiTransitionPointerToLightLightNameClass()
            elif numArgs == 1:
                if isinstance(_args[0], Light.Light):
                    return self.overloaded_isIdentity_ptrConstMultiTransitionPointerToLightLightNameClass_ptrLight(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Light.Light> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['MultiTransitionPointerToLightLightNameClass'] = MultiTransitionPointerToLightLightNameClass

