# Source Generated with Decompyle++
# File: NetAddress.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import PRNetAddr
import Ostream
classDefined = 0

def generateClass_NetAddress():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NetAddress(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inP9ImM4xOH()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPRNetAddr(self, addr):
            self.this = libpanda._inP9ImM0HGa(addr.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMUyRe:
                libpanda._inP9ImMUyRe(self.this)
            

        
        def setAny(self, port):
            returnValue = libpanda._inP9ImM8DN_(self.this, port)
            return returnValue

        
        def setLocalhost(self, port):
            returnValue = libpanda._inP9ImMICye(self.this, port)
            return returnValue

        
        def setHost(self, hostname, port):
            returnValue = libpanda._inP9ImMau_T(self.this, hostname, port)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inP9ImM74pu(self.this)
            return returnValue

        
        def getPort(self):
            returnValue = libpanda._inP9ImMahNt(self.this)
            return returnValue

        
        def setPort(self, port):
            returnValue = libpanda._inP9ImMsg63(self.this, port)
            return returnValue

        
        def getIpString(self):
            returnValue = libpanda._inP9ImMFRnv(self.this)
            return returnValue

        
        def getIp(self):
            returnValue = libpanda._inP9ImM5KiR(self.this)
            return returnValue

        
        def getIpComponent(self, n):
            returnValue = libpanda._inP9ImM8YlR(self.this, n)
            return returnValue

        
        def getAddr(self):
            returnValue = libpanda._inP9ImMC9jL(self.this)
            returnObject = PRNetAddr.PRNetAddr(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def output(self, out):
            returnValue = libpanda._inP9ImM6IBY(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], PRNetAddr.PRNetAddr):
                    return self.overloaded_constructor_ptrConstPRNetAddr(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <PRNetAddr.PRNetAddr> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['NetAddress'] = NetAddress

