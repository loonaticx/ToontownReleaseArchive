# Source Generated with Decompyle++
# File: PointerToConnection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Connection
import PointerToBaseConnection
classDefined = 0

def generateClass_PointerToConnection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointerToConnection(PointerToBaseConnection.PointerToBaseConnection, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrConnection(self, ptr):
            self.this = libpanda._inP9ImMCls6(ptr.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inP9ImM30bX()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConnection(self, copy):
            self.this = libpanda._inP9ImMSi1Q(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMtufE:
                libpanda._inP9ImMtufE(self.this)
            

        
        def p(self):
            returnValue = libpanda._inP9ImMAH9x(self.this)
            returnObject = Connection.Connection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_assign_ptrPointerToConnection_ptrConnection(self, ptr):
            returnValue = libpanda._inP9ImMDfDQ(self.this, ptr.this)
            returnObject = PointerToConnection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrPointerToConnection_ptrConnection(self, copy):
            returnValue = libpanda._inP9ImMoDZV(self.this, copy.this)
            returnObject = PointerToConnection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isNull(self):
            returnValue = libpanda._inP9ImMbzMY(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inP9ImMRPyp(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], Connection.Connection):
                    return self.overloaded_constructor_ptrConnection(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Connection.Connection> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Connection.Connection):
                    return self.overloaded_assign_ptrPointerToConnection_ptrConnection(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Connection.Connection> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['PointerToConnection'] = PointerToConnection

