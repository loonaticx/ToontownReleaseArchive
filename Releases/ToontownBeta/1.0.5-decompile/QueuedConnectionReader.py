# Source Generated with Decompyle++
# File: QueuedConnectionReader.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionManager
import NetDatagram
import Datagram
import QueuedReturnNetDatagram
import ConnectionReader
import Connection
import ConnectionReader
import Connection
import ConnectionManager
import QueuedReturnNetDatagram
classDefined = 0

def generateClass_QueuedConnectionReader():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QueuedConnectionReader(ConnectionReader.ConnectionReader, QueuedReturnNetDatagram.QueuedReturnNetDatagram, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, manager, numThreads):
            self.this = libpanda._inP9ImMZUxa(manager.this, numThreads)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMr1Dn:
                libpanda._inP9ImMr1Dn(self.this)
            

        
        def dataAvailable(self):
            returnValue = libpanda._inP9ImMwUOV(self.this)
            return returnValue

        
        def overloaded_getData_ptrQueuedConnectionReader_ptrNetDatagram(self, result):
            returnValue = libpanda._inP9ImMQPBn(self.this, result.this)
            return returnValue

        
        def overloaded_getData_ptrQueuedConnectionReader_ptrDatagram(self, result):
            returnValue = libpanda._inP9ImMxM0z(self.this, result.this)
            return returnValue

        
        def upcastToQueuedReturnNetDatagram(self):
            returnValue = libpanda._inP9ImMiJ3h(self.this)
            returnObject = QueuedReturnNetDatagram.QueuedReturnNetDatagram(None)
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
            upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
            returnValue = libpanda._inP9ImMMcal(upcastSelf.this, maxSize)
            return returnValue

        
        def getMaxQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
            returnValue = libpanda._inP9ImMvd9N(upcastSelf.this)
            return returnValue

        
        def getCurrentQueueSize(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToQueuedReturnNetDatagram()
            returnValue = libpanda._inP9ImMAde3(upcastSelf.this)
            return returnValue

        
        def getData(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Datagram.Datagram):
                    return self.overloaded_getData_ptrQueuedConnectionReader_ptrDatagram(_args[0])
                elif isinstance(_args[0], NetDatagram.NetDatagram):
                    return self.overloaded_getData_ptrQueuedConnectionReader_ptrNetDatagram(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram.NetDatagram> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['QueuedConnectionReader'] = QueuedConnectionReader

