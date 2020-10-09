# Source Generated with Decompyle++
# File: Fog.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import Ostream
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_Fog():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Fog(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        MExponential = 1
        MLinear = 0
        MExponentialSquared = 2
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor___enum__Mode_int(self, mode, bitsPerColorChannel):
            self.this = libpanda._inPMAKPc9CG(mode, bitsPerColorChannel)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__Mode(self, mode):
            self.this = libpanda._inPMAKPlQ7N(mode)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPMAKPOcEK()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPYlii()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getMode(self):
            returnValue = libpanda._inPMAKPGEAQ(self.this)
            return returnValue

        
        def setMode(self, mode):
            returnValue = libpanda._inPMAKP_5Pt(self.this, mode)
            return returnValue

        
        def getColor(self):
            returnValue = libpanda._inPMAKPKsgO(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setColor(self, color):
            returnValue = libpanda._inPMAKPC62n(self.this, color.this)
            return returnValue

        
        def setRange(self, onset, opaque):
            returnValue = libpanda._inPMAKPiJru(self.this, onset, opaque)
            return returnValue

        
        def getDensity(self):
            returnValue = libpanda._inPMAKPO47f(self.this)
            return returnValue

        
        def setDensity(self, fDensity):
            returnValue = libpanda._inPMAKPSOw7(self.this, fDensity)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPMAKPyX43(self.this, out.this)
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
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor___enum__Mode_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['Fog'] = Fog

