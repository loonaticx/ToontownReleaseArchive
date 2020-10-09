# Source Generated with Decompyle++
# File: DNASuitEdge.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DNASuitPoint
import Ostream
import DNAStorage
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_DNASuitEdge():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNASuitEdge(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, startPoint, endPoint, zoneId):
            self.this = libtoontown._inPdt4yEPYC(startPoint.this, endPoint.this, zoneId)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4yTNtM:
                libtoontown._inPdt4yTNtM(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPdt4yHvpE()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getStartPoint(self):
            returnValue = libtoontown._inPdt4yaV38(self.this)
            returnObject = DNASuitPoint.DNASuitPoint(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getEndPoint(self):
            returnValue = libtoontown._inPdt4y0cdh(self.this)
            returnObject = DNASuitPoint.DNASuitPoint(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getZoneId(self):
            returnValue = libtoontown._inPdt4yXLAO(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libtoontown._inPdt4ylqOc(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage_int(self, out, store, indentLevel):
            returnValue = libtoontown._inPdt4ydmts(self.this, out.this, store.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage(self, out, store):
            returnValue = libtoontown._inPdt4yZv5N(self.this, out.this, store.this)
            return returnValue

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        return self.overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], DNAStorage.DNAStorage):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_write_ptrConstDNASuitEdge_ptrOstream_ptrDNAStorage_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <DNAStorage.DNAStorage> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '


    globals()['DNASuitEdge'] = DNASuitEdge

