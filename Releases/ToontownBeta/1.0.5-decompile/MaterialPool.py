# Source Generated with Decompyle++
# File: MaterialPool.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Material
import Ostream
classDefined = 0

def generateClass_MaterialPool():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MaterialPool(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPMAKPAQ7j:
                libpanda._inPMAKPAQ7j(self.this)
            

        
        def getMaterial(temp):
            returnValue = libpanda._inPMAKPrJY5(temp.this)
            returnObject = Material.Material(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getMaterial = PandaStatic.PandaStatic(getMaterial)
        
        def garbageCollect():
            returnValue = libpanda._inPMAKPPm0z()
            return returnValue

        garbageCollect = PandaStatic.PandaStatic(garbageCollect)
        
        def listContents(out):
            returnValue = libpanda._inPMAKPzzKx(out.this)
            return returnValue

        listContents = PandaStatic.PandaStatic(listContents)

    globals()['MaterialPool'] = MaterialPool

