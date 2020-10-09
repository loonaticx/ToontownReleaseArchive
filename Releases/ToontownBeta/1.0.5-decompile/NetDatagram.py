# Source Generated with Decompyle++
# File: NetDatagram.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Datagram
import Connection
import NetAddress
import TypeHandle
import TypedObject
import TypeHandle
import Datagram
import TypedObject
import Ostream
import TypeHandle
classDefined = 0

def generateClass_NetDatagram():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NetDatagram(Datagram.Datagram, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inP9ImM__Xx()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstDatagram(self, copy):
            self.this = libpanda._inP9ImMkt0b(copy.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstNetDatagram(self, copy):
            self.this = libpanda._inP9ImMO_0H(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMB8rl:
                libpanda._inP9ImMB8rl(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inP9ImMlG2L()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_assign_ptrNetDatagram_ptrConstDatagram(self, copy):
            returnValue = libpanda._inP9ImMOHmI(self.this, copy.this)
            returnObject = NetDatagram(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def overloaded_assign_ptrNetDatagram_ptrConstNetDatagram(self, copy):
            returnValue = libpanda._inP9ImMe69z(self.this, copy.this)
            returnObject = NetDatagram(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def setConnection(self, connection):
            returnValue = libpanda._inP9ImM3jK9(self.this, connection.this)
            return returnValue

        
        def getConnection(self):
            returnValue = libpanda._inP9ImMRLDi(self.this)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setAddress(self, address):
            returnValue = libpanda._inP9ImMX0ZL(self.this, address.this)
            return returnValue

        
        def getAddress(self):
            returnValue = libpanda._inP9ImM8hhL(self.this)
            returnObject = NetAddress.NetAddress(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Datagram.Datagram):
                    return self.overloaded_constructor_ptrConstDatagram(_args[0])
                elif isinstance(_args[0], NetDatagram):
                    return self.overloaded_constructor_ptrConstNetDatagram(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Datagram.Datagram):
                    return self.overloaded_assign_ptrNetDatagram_ptrConstDatagram(_args[0])
                elif isinstance(_args[0], NetDatagram):
                    return self.overloaded_assign_ptrNetDatagram_ptrConstNetDatagram(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['NetDatagram'] = NetDatagram

