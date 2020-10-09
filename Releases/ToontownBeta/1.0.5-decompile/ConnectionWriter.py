# Source Generated with Decompyle++
# File: ConnectionWriter.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionManager
import Datagram
import Connection
import NetAddress
classDefined = 0

def generateClass_ConnectionWriter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ConnectionWriter(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, manager, numThreads):
            self.this = libpanda._inP9ImMpJ_q(manager.this, numThreads)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMl4TQ:
                libpanda._inP9ImMl4TQ(self.this)
            

        
        def overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection(self, datagram, connection):
            returnValue = libpanda._inP9ImMyYgV(self.this, datagram.this, connection.this)
            return returnValue

        
        def overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection_ptrConstNetAddress(self, datagram, connection, address):
            returnValue = libpanda._inP9ImMylcw(self.this, datagram.this, connection.this, address.this)
            return returnValue

        
        def isValidForUdp(self, datagram):
            returnValue = libpanda._inP9ImMuGJn(self.this, datagram.this)
            return returnValue

        
        def getManager(self):
            returnValue = libpanda._inP9ImMMvbQ(self.this)
            returnObject = ConnectionManager.ConnectionManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isImmediate(self):
            returnValue = libpanda._inP9ImMDZHm(self.this)
            return returnValue

        
        def getNumThreads(self):
            returnValue = libpanda._inP9ImMfRfX(self.this)
            return returnValue

        
        def setRawMode(self, mode):
            returnValue = libpanda._inP9ImMxBuh(self.this, mode)
            return returnValue

        
        def getRawMode(self):
            returnValue = libpanda._inP9ImMz9jm(self.this)
            return returnValue

        
        def send(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Datagram.Datagram):
                    if isinstance(_args[1], Connection.Connection):
                        return self.overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Connection.Connection> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> '
            elif numArgs == 3:
                if isinstance(_args[0], Datagram.Datagram):
                    if isinstance(_args[1], Connection.Connection):
                        if isinstance(_args[2], NetAddress.NetAddress):
                            return self.overloaded_send_ptrConnectionWriter_ptrConstDatagram_ptrConnection_ptrConstNetAddress(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <NetAddress.NetAddress> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Connection.Connection> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['ConnectionWriter'] = ConnectionWriter

