# Source Generated with Decompyle++
# File: PStatClient.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_PStatClient():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PStatClient(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
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
            if libpanda and libpanda._inPhqKx3UEX:
                libpanda._inPhqKx3UEX(self.this)
            

        
        def overloaded_connect_atomicstring_int(parameter0, parameter1):
            returnValue = libpanda._inPhqKxVctG(parameter0, parameter1)
            return returnValue

        overloaded_connect_atomicstring_int = PandaStatic.PandaStatic(overloaded_connect_atomicstring_int)
        
        def overloaded_connect_atomicstring(parameter0):
            returnValue = libpanda._inPhqKxD1_Y(parameter0)
            return returnValue

        overloaded_connect_atomicstring = PandaStatic.PandaStatic(overloaded_connect_atomicstring)
        
        def overloaded_connect():
            returnValue = libpanda._inPhqKxVBxA()
            return returnValue

        overloaded_connect = PandaStatic.PandaStatic(overloaded_connect)
        
        def disconnect():
            returnValue = libpanda._inPhqKx6l4i()
            return returnValue

        disconnect = PandaStatic.PandaStatic(disconnect)
        
        def isConnected():
            returnValue = libpanda._inPhqKxZhkh()
            return returnValue

        isConnected = PandaStatic.PandaStatic(isConnected)
        
        def resumeAfterPause():
            returnValue = libpanda._inPhqKx1mTf()
            return returnValue

        resumeAfterPause = PandaStatic.PandaStatic(resumeAfterPause)
        
        def connect(*_args):
            numArgs = len(_args)
            if numArgs == 0:
                return PStatClient.overloaded_connect()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return PStatClient.overloaded_connect_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return PStatClient.overloaded_connect_atomicstring_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        connect = PandaStatic.PandaStatic(connect)

    globals()['PStatClient'] = PStatClient

