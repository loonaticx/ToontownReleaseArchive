# Source Generated with Decompyle++
# File: Connection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ConnectionManager
import PRFileDesc
import NetAddress
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_Connection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Connection(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, manager, socket):
            self.this = libpanda._inP9ImMKWjx(manager.this, socket.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMJphL:
                libpanda._inP9ImMJphL(self.this)
            

        
        def getAddress(self):
            returnValue = libpanda._inP9ImM_XAD(self.this)
            returnObject = NetAddress.NetAddress(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getManager(self):
            returnValue = libpanda._inP9ImMvgOO(self.this)
            returnObject = ConnectionManager.ConnectionManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getSocket(self):
            returnValue = libpanda._inP9ImM1HzZ(self.this)
            returnObject = PRFileDesc.PRFileDesc(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setNonblock(self, flag):
            returnValue = libpanda._inP9ImMzoUw(self.this, flag)
            return returnValue

        
        def setLinger(self, flag, time):
            returnValue = libpanda._inP9ImMroTH(self.this, flag, time)
            return returnValue

        
        def setReuseAddr(self, flag):
            returnValue = libpanda._inP9ImM1VaK(self.this, flag)
            return returnValue

        
        def setKeepAlive(self, flag):
            returnValue = libpanda._inP9ImMUAJV(self.this, flag)
            return returnValue

        
        def setRecvBufferSize(self, size):
            returnValue = libpanda._inP9ImM4glj(self.this, size)
            return returnValue

        
        def setSendBufferSize(self, size):
            returnValue = libpanda._inP9ImMMLT1(self.this, size)
            return returnValue

        
        def setIpTimeToLive(self, ttl):
            returnValue = libpanda._inP9ImMJ_WX(self.this, ttl)
            return returnValue

        
        def setIpTypeOfService(self, tos):
            returnValue = libpanda._inP9ImM7CVD(self.this, tos)
            return returnValue

        
        def setNoDelay(self, flag):
            returnValue = libpanda._inP9ImMVTE7(self.this, flag)
            return returnValue

        
        def setMaxSegment(self, size):
            returnValue = libpanda._inP9ImMWsC_(self.this, size)
            return returnValue


    globals()['Connection'] = Connection

