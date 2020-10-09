# Source Generated with Decompyle++
# File: ConnectionManager.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Connection
import NetAddress
classDefined = 0

def generateClass_ConnectionManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ConnectionManager(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inP9ImM8imi:
                libpanda._inP9ImM8imi(self.this)
            

        
        def getHostName():
            returnValue = libpanda._inP9ImM78Tl()
            return returnValue

        getHostName = PandaStatic.PandaStatic(getHostName)
        
        def overloaded_openUDPConnection_ptrConnectionManager_int(self, port):
            returnValue = libpanda._inP9ImMn8qs(self.this, port)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openUDPConnection_ptrConnectionManager(self):
            returnValue = libpanda._inP9ImMGlgh(self.this)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def openTCPServerRendezvous(self, port, backlog):
            returnValue = libpanda._inP9ImMZdIi(self.this, port, backlog)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(self, address, timeoutMs):
            returnValue = libpanda._inP9ImM8jvU(self.this, address.this, timeoutMs)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(self, hostname, port, timeoutMs):
            returnValue = libpanda._inP9ImMgGQM(self.this, hostname, port, timeoutMs)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def closeConnection(self, connection):
            returnValue = libpanda._inP9ImMb6qc(self.this, connection.this)
            return returnValue

        
        def openTCPClientConnection(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], NetAddress.NetAddress):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NetAddress.NetAddress> '
            elif numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def openUDPConnection(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_openUDPConnection_ptrConnectionManager()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_openUDPConnection_ptrConnectionManager_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['ConnectionManager'] = ConnectionManager

