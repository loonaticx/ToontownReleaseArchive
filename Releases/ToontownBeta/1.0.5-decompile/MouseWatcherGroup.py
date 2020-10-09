# Source Generated with Decompyle++
# File: MouseWatcherGroup.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import MouseWatcherRegion
import ReferenceCount
import TypeHandle
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_MouseWatcherGroup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class MouseWatcherGroup(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
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
            if libpanda and libpanda._inPyiw5LHuB:
                libpanda._inPyiw5LHuB(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPyiw5wYko()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def addRegion(self, region):
            returnValue = libpanda._inPyiw5quMA(self.this, region.this)
            return returnValue

        
        def hasRegion(self, region):
            returnValue = libpanda._inPyiw50TuC(self.this, region.this)
            return returnValue

        
        def removeRegion(self, region):
            returnValue = libpanda._inPyiw5gy6C(self.this, region.this)
            return returnValue

        
        def findRegion(self, name):
            returnValue = libpanda._inPyiw5vszS(self.this, name)
            returnObject = MouseWatcherRegion.MouseWatcherRegion(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearRegions(self):
            returnValue = libpanda._inPyiw52d_y(self.this)
            return returnValue

        
        def upcastToReferenceCount(self):
            returnValue = libpanda._inPyiw5QwnS(self.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['MouseWatcherGroup'] = MouseWatcherGroup

