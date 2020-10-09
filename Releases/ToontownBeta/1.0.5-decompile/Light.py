# Source Generated with Decompyle++
# File: Light.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import Ostream
import ReferenceCount
import TypeHandle
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_Light():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Light(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPi0oL2qsN:
                libpanda._inPi0oL2qsN(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPi0oLi8dT()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getColor(self):
            returnValue = libpanda._inPi0oLef_a(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setColor(self, color):
            returnValue = libpanda._inPi0oL0ZiL(self.this, color.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPi0oLcV0W(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLight_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPi0oLC8aI(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLight_ptrOstream(self, out):
            returnValue = libpanda._inPi0oLMuhe(self.this, out.this)
            return returnValue

        
        def upcastToReferenceCount(self):
            returnValue = libpanda._inPi0oLjiAk(self.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstLight_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstLight_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Light'] = Light

