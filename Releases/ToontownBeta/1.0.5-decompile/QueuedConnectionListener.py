# Source Generated with Decompyle++
# File: QueuedConnectionListener.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionManager
import PointerToConnection
import NetAddress
import QueuedReturnConnectionListenerData
import ConnectionReader
import Connection
import ConnectionManager
import ConnectionListener
import QueuedReturnConnectionListenerData
classDefined = 0

def generateClass_QueuedConnectionListener():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QueuedConnectionListener(ConnectionListener.ConnectionListener, QueuedReturnConnectionListenerData.QueuedReturnConnectionListenerData, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, manager, numThreads):
            self.this = libpanda._inP9ImME6Yr(manager.this, numThreads)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMGYOM:
                libpanda._inP9ImMGYOM(self.this)
            

        
        def newConnectionAvailable(self):
            returnValue = libpanda._inP9ImMcf0a(self.this)
            return returnValue

        
        def overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection_ptrNetAddress_ptrPointerToConnection(self, rendezvous, address, newConnection):
            returnValue = libpanda._inP9ImMb4yI(self.this, rendezvous.this, address.this, newConnection.this)
            return returnValue

        
        def overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection(self, newConnection):
            returnValue = libpanda._inP9ImMp1mC(self.this, newConnection.this)
            return returnValue

        
        def upcastToQueuedReturnConnectionListenerData(self):
            returnValue = libpanda._inP9ImM31nE(self.this)
            returnObject = QueuedReturnConnectionListenerData.QueuedReturnConnectionListenerData(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def addConnection(self, connection):
            upcastSelf = self
            returnValue = libpanda._inP9ImMklA4(upcastSelf.this, connection.this)
            return returnValue

        
        def removeConnection(self, connection):
            upcastSelf = self
            returnValue = libpanda._inP9ImMXuJ8(upcastSelf.this, connection.this)
            return returnValue

        
        def isConnectionOk(self, connection):
            upcastSelf = self
            returnValue = libpanda._inP9ImMGkeX(upcastSelf.this, connection.this)
            return returnValue

        
        def poll(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImMPLGz(upcastSelf.this)
            return returnValue

        
        def getManager(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImMbJdH(upcastSelf.this)
            returnObject = ConnectionManager.ConnectionManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isPolling(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImMEeEA(upcastSelf.this)
            return returnValue

        
        def getNumThreads(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImMv9eO(upcastSelf.this)
            return returnValue

        
        def setRawMode(self, mode):
            upcastSelf = self
            returnValue = libpanda._inP9ImM03uY(upcastSelf.this, mode)
            return returnValue

        
        def getRawMode(self):
            upcastSelf = self
            returnValue = libpanda._inP9ImM7vld(upcastSelf.this)
            return returnValue

        
        def setMaxQueueSize(self, maxSize):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
            returnValue = libpanda._inP9ImMKxgW(upcastSelf.this, maxSize)
            return returnValue

        
        def getMaxQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
            returnValue = libpanda._inP9ImM3Eeb(upcastSelf.this)
            return returnValue

        
        def getCurrentQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnConnectionListenerData()
            returnValue = libpanda._inP9ImMsntc(upcastSelf.this)
            return returnValue

        
        def getNewConnection(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], PointerToConnection.PointerToConnection):
                    return self.overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PointerToConnection.PointerToConnection> '
            elif numArgs == 3:
                if isinstance(_args[0], PointerToConnection.PointerToConnection):
                    if isinstance(_args[1], NetAddress.NetAddress):
                        if isinstance(_args[2], PointerToConnection.PointerToConnection):
                            return self.overloaded_getNewConnection_ptrQueuedConnectionListener_ptrPointerToConnection_ptrNetAddress_ptrPointerToConnection(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <PointerToConnection.PointerToConnection> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <NetAddress.NetAddress> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PointerToConnection.PointerToConnection> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['QueuedConnectionListener'] = QueuedConnectionListener

