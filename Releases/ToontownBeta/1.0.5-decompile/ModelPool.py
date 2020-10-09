# Source Generated with Decompyle++
# File: ModelPool.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Node
import Ostream
classDefined = 0

def generateClass_ModelPool():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ModelPool(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inP6KMshJLs:
                libpanda._inP6KMshJLs(self.this)
            

        
        def hasModel(filename):
            returnValue = libpanda._inP6KMsyeJQ(filename)
            return returnValue

        hasModel = PandaStatic.PandaStatic(hasModel)
        
        def verifyModel(filename):
            returnValue = libpanda._inP6KMsaMOk(filename)
            return returnValue

        verifyModel = PandaStatic.PandaStatic(verifyModel)
        
        def loadModel(filename):
            returnValue = libpanda._inP6KMstohZ(filename)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        loadModel = PandaStatic.PandaStatic(loadModel)
        
        def addModel(filename, model):
            returnValue = libpanda._inP6KMsdti6(filename, model.this)
            return returnValue

        addModel = PandaStatic.PandaStatic(addModel)
        
        def releaseModel(filename):
            returnValue = libpanda._inP6KMs53cZ(filename)
            return returnValue

        releaseModel = PandaStatic.PandaStatic(releaseModel)
        
        def releaseAllModels():
            returnValue = libpanda._inP6KMsxNRY()
            return returnValue

        releaseAllModels = PandaStatic.PandaStatic(releaseAllModels)
        
        def garbageCollect():
            returnValue = libpanda._inP6KMsjwBO()
            return returnValue

        garbageCollect = PandaStatic.PandaStatic(garbageCollect)
        
        def listContents(out):
            returnValue = libpanda._inP6KMs6nv6(out.this)
            return returnValue

        listContents = PandaStatic.PandaStatic(listContents)

    globals()['ModelPool'] = ModelPool

