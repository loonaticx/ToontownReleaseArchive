# Source Generated with Decompyle++
# File: LightTransition.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import MultiTransitionPointerToLightLightNameClass
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
import MultiTransitionPointerToLightLightNameClass
import Light
import TypeHandle
classDefined = 0

def generateClass_LightTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LightTransition(MultiTransitionPointerToLightLightNameClass.MultiTransitionPointerToLightLightNameClass, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPi0oLzy_m()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstLightTransition(self, copy):
            self.this = libpanda._inPi0oLBlPX(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPi0oLOITp:
                libpanda._inPi0oLOITp(self.this)
            

        
        def allOff():
            returnValue = libpanda._inPi0oL2OiK()
            returnObject = LightTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        allOff = PandaStatic.PandaStatic(allOff)
        
        def getClassType():
            returnValue = libpanda._inPi0oLorKr()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], LightTransition):
                    return self.overloaded_constructor_ptrConstLightTransition(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LightTransition> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['LightTransition'] = LightTransition

