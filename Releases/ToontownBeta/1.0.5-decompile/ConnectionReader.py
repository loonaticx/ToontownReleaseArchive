# Source Generated with Decompyle++
# File: ConnectionReader.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Connection
import ConnectionManager
classDefined = 0

def generateClass_ConnectionReader():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ConnectionReader(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inP9ImMAuzi:
                libpanda._inP9ImMAuzi(self.this)
            

        
        def addConnection(self, connection):
            returnValue = libpanda._inP9ImMklA4(self.this, connection.this)
            return returnValue

        
        def removeConnection(self, connection):
            returnValue = libpanda._inP9ImMXuJ8(self.this, connection.this)
            return returnValue

        
        def isConnectionOk(self, connection):
            returnValue = libpanda._inP9ImMGkeX(self.this, connection.this)
            return returnValue

        
        def poll(self):
            returnValue = libpanda._inP9ImMPLGz(self.this)
            return returnValue

        
        def getManager(self):
            returnValue = libpanda._inP9ImMbJdH(self.this)
            returnObject = ConnectionManager.ConnectionManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isPolling(self):
            returnValue = libpanda._inP9ImMEeEA(self.this)
            return returnValue

        
        def getNumThreads(self):
            returnValue = libpanda._inP9ImMv9eO(self.this)
            return returnValue

        
        def setRawMode(self, mode):
            returnValue = libpanda._inP9ImM03uY(self.this, mode)
            return returnValue

        
        def getRawMode(self):
            returnValue = libpanda._inP9ImM7vld(self.this)
            return returnValue


    globals()['ConnectionReader'] = ConnectionReader

