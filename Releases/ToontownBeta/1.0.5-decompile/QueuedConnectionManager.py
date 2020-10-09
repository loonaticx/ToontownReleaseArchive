# Source Generated with Decompyle++
# File: QueuedConnectionManager.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PointerToConnection
import QueuedReturnPointerToConnection
import Connection
import ConnectionManager
import NetAddress
import ConnectionManager
import Connection
import NetAddress
import QueuedReturnPointerToConnection
classDefined = 0

def generateClass_QueuedConnectionManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QueuedConnectionManager(ConnectionManager.ConnectionManager, QueuedReturnPointerToConnection.QueuedReturnPointerToConnection, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inP9ImMxunC()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMjhMK:
                libpanda._inP9ImMjhMK(self.this)
            

        
        def resetConnectionAvailable(self):
            returnValue = libpanda._inP9ImMxAar(self.this)
            return returnValue

        
        def getResetConnection(self, connection):
            returnValue = libpanda._inP9ImMbc0F(self.this, connection.this)
            return returnValue

        
        def upcastToQueuedReturnPointerToConnection(self):
            returnValue = libpanda._inP9ImMoQHO(self.this)
            returnObject = QueuedReturnPointerToConnection.QueuedReturnPointerToConnection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_openUDPConnection_ptrConnectionManager_int(self, port):
            upcastSelf = self
            returnValue = libpanda._inP9ImMn8qs(upcastSelf.this, port)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openUDPConnection_ptrConnectionManager(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImMGlgh(upcastSelf.this)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def openTCPServerRendezvous(self, port, backlog):
            upcastSelf = self
            returnValue = libpanda._inP9ImMZdIi(upcastSelf.this, port, backlog)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openTCPClientConnection_ptrConnectionManager_ptrConstNetAddress_int(self, address, timeoutMs):
            upcastSelf = self
            returnValue = libpanda._inP9ImM8jvU(upcastSelf.this, address.this, timeoutMs)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_openTCPClientConnection_ptrConnectionManager_atomicstring_int_int(self, hostname, port, timeoutMs):
            upcastSelf = self
            returnValue = libpanda._inP9ImMgGQM(upcastSelf.this, hostname, port, timeoutMs)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def closeConnection(self, connection):
            upcastSelf = self
            returnValue = libpanda._inP9ImMb6qc(upcastSelf.this, connection.this)
            return returnValue

        
        def setMaxQueueSize(self, maxSize):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
            returnValue = libpanda._inP9ImM_gvr(upcastSelf.this, maxSize)
            return returnValue

        
        def getMaxQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
            returnValue = libpanda._inP9ImM7zPK(upcastSelf.this)
            return returnValue

        
        def getCurrentQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnPointerToConnection()
            returnValue = libpanda._inP9ImMmKPz(upcastSelf.this)
            return returnValue


    globals()['QueuedConnectionManager'] = QueuedConnectionManager

