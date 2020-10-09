# Source Generated with Decompyle++
# File: QueuedReturnNetDatagram.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_QueuedReturnNetDatagram():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class QueuedReturnNetDatagram(FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inP9ImMMcal(self.this, maxSize)
            return returnValue

        
        def getMaxQueueSize(self):
            returnValue = libpanda._inP9ImMvd9N(self.this)
            return returnValue

        
        def getCurrentQueueSize(self):
            returnValue = libpanda._inP9ImMAde3(self.this)
            return returnValue


    globals()['QueuedReturnNetDatagram'] = QueuedReturnNetDatagram

