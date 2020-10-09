# Source Generated with Decompyle++
# File: DNALoader.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
import Node
import DNAStorage
import DNAData
classDefined = 0

def generateClass_DNALoader():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DNALoader(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libtoontown._inPdt4yg0cW()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPdt4ySrXO:
                libtoontown._inPdt4ySrXO(self.this)
            

        
        def overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(self, dnaStore, editing):
            returnValue = libtoontown._inPdt4yP6dC(self.this, dnaStore.this, editing)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(self, dnaStore):
            returnValue = libtoontown._inPdt4yL9xN(self.this, dnaStore.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getData(self):
            returnValue = libtoontown._inPdt4ymWGI(self.this)
            returnObject = DNAData.DNAData(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def buildGraph(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], DNAStorage.DNAStorage):
                    return self.overloaded_buildGraph_ptrDNALoader_ptrDNAStorage(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
            elif numArgs == 2:
                if isinstance(_args[0], DNAStorage.DNAStorage):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_buildGraph_ptrDNALoader_ptrDNAStorage_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <DNAStorage.DNAStorage> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['DNALoader'] = DNALoader

