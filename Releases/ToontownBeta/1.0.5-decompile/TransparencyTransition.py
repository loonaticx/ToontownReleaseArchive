# Source Generated with Decompyle++
# File: TransparencyTransition.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
import OnTransition
import TypeHandle
classDefined = 0

def generateClass_TransparencyTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class TransparencyTransition(OnTransition.OnTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor___enum__Mode(self, mode):
            self.this = libpanda._inPuUZ_4kff(mode)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPuUZ_Q8RT()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPuUZ_K5FY:
                libpanda._inPuUZ_K5FY(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPuUZ_U0OI()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setMode(self, mode):
            returnValue = libpanda._inPuUZ_ysp6(self.this, mode)
            return returnValue

        
        def getMode(self):
            returnValue = libpanda._inPuUZ_eJ__(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor___enum__Mode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['TransparencyTransition'] = TransparencyTransition

