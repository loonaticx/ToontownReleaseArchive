# Source Generated with Decompyle++
# File: PStatCollector.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PStatClient
classDefined = 0

def generateClass_PStatCollector():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PStatCollector(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring_ptrPStatClient(self, name, client):
            self.this = libpanda._inPhqKxww_r(name, client.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPhqKx5ATO(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPStatCollector_atomicstring(self, parent, name):
            self.this = libpanda._inPhqKxsiR6(parent.this, name)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPhqKxW3CV:
                libpanda._inPhqKxW3CV(self.this)
            

        
        def isActive(self):
            returnValue = libpanda._inPhqKxB75b(self.this)
            return returnValue

        
        def start(self):
            returnValue = libpanda._inPhqKxjXQr(self.this)
            return returnValue

        
        def stop(self):
            returnValue = libpanda._inPhqKxze21(self.this)
            return returnValue

        
        def clearLevel(self):
            returnValue = libpanda._inPhqKxkn32(self.this)
            return returnValue

        
        def setLevel(self, parameter1):
            returnValue = libpanda._inPhqKxLiCx(self.this, parameter1)
            return returnValue

        
        def addLevel(self, parameter1):
            returnValue = libpanda._inPhqKxC28M(self.this, parameter1)
            return returnValue

        
        def subLevel(self, parameter1):
            returnValue = libpanda._inPhqKx0ti2(self.this, parameter1)
            return returnValue

        
        def getLevel(self):
            returnValue = libpanda._inPhqKxqML6(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], PStatClient.PStatClient):
                        return self.overloaded_constructor_atomicstring_ptrPStatClient(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <PStatClient.PStatClient> '
                elif isinstance(_args[0], PStatCollector):
                    if isinstance(_args[1], types.StringType):
                        return self.overloaded_constructor_ptrConstPStatCollector_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <PStatCollector> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['PStatCollector'] = PStatCollector

