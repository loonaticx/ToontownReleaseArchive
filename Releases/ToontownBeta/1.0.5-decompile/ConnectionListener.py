# Source Generated with Decompyle++
# File: ConnectionListener.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionReader
import Connection
import ConnectionManager
classDefined = 0

def generateClass_ConnectionListener():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ConnectionListener(ConnectionReader.ConnectionReader, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inP9ImMkMno:
                libpanda._inP9ImMkMno(self.this)
            


    globals()['ConnectionListener'] = ConnectionListener

