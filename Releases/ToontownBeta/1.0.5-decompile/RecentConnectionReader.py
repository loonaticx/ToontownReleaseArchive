# Source Generated with Decompyle++
# File: RecentConnectionReader.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ConnectionManager
import ConnectionReader
import NetDatagram
import Datagram
import ConnectionReader
import Connection
import ConnectionManager
classDefined = 0

def generateClass_RecentConnectionReader():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class RecentConnectionReader(ConnectionReader.ConnectionReader, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, manager):
            self.this = libpanda._inP9ImM5YRe(manager.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP9ImMAuzi:
                libpanda._inP9ImMAuzi(self.this)
            

        
        def dataAvailable(self):
            returnValue = libpanda._inP9ImMfpBT(self.this)
            return returnValue

        
        def overloaded_getData_ptrRecentConnectionReader_ptrNetDatagram(self, result):
            returnValue = libpanda._inP9ImMW10k(self.this, result.this)
            return returnValue

        
        def overloaded_getData_ptrRecentConnectionReader_ptrDatagram(self, result):
            returnValue = libpanda._inP9ImMZBnx(self.this, result.this)
            return returnValue

        
        def getData(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Datagram.Datagram):
                    return self.overloaded_getData_ptrRecentConnectionReader_ptrDatagram(_args[0])
                elif isinstance(_args[0], NetDatagram.NetDatagram):
                    return self.overloaded_getData_ptrRecentConnectionReader_ptrNetDatagram(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Datagram.Datagram> <NetDatagram.NetDatagram> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['RecentConnectionReader'] = RecentConnectionReader

