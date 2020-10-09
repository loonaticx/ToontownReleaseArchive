# Source Generated with Decompyle++
# File: PandaLoader.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Filename
import Node
import AsyncUtility
classDefined = 0

def generateClass_PandaLoader():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PandaLoader(AsyncUtility.AsyncUtility, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inP6KMsjWgi()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def resolveFilename(self, filename):
            returnValue = libpanda._inP6KMsvroc(self.this, filename.this)
            return returnValue

        
        def loadSync(self, filename):
            returnValue = libpanda._inP6KMssVzV(self.this, filename.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def requestLoad(self, filename, eventName):
            returnValue = libpanda._inP6KMsDSs2(self.this, filename.this, eventName)
            return returnValue

        
        def checkLoad(self, id):
            returnValue = libpanda._inP6KMs9RRu(self.this, id)
            return returnValue

        
        def fetchLoad(self, id):
            returnValue = libpanda._inP6KMst_TC(self.this, id)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()


    globals()['PandaLoader'] = PandaLoader

