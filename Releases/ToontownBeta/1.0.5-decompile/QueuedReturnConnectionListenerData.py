# Source Generated with Decompyle++
# File: QueuedReturnConnectionListenerData.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_QueuedReturnConnectionListenerData():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QueuedReturnConnectionListenerData(FFIExternalObject.FFIExternalObject):
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
            

        
        def setMaxQueueSize(self, maxSize):
            returnValue = libpanda._inP9ImMKxgW(self.this, maxSize)
            return returnValue

        
        def getMaxQueueSize(self):
            returnValue = libpanda._inP9ImM3Eeb(self.this)
            return returnValue

        
        def getCurrentQueueSize(self):
            returnValue = libpanda._inP9ImMsntc(self.this)
            return returnValue


    globals()['QueuedReturnConnectionListenerData'] = QueuedReturnConnectionListenerData

