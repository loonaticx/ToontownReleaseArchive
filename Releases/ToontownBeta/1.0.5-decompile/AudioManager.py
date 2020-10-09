# Source Generated with Decompyle++
# File: AudioManager.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import AudioSound
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_AudioManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AudioManager(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPMC2_gTId:
                libpanda._inPMC2_gTId(self.this)
            

        
        def createAudioManager():
            returnValue = libpanda._inPMC2_ol8W()
            returnObject = AudioManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        createAudioManager = PandaStatic.PandaStatic(createAudioManager)
        
        def isValid(self):
            returnValue = libpanda._inPMC2_RBmD(self.this)
            return returnValue

        
        def getSound(self, fileName):
            returnValue = libpanda._inPMC2_rcgN(self.this, fileName)
            returnObject = AudioSound.AudioSound(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def dropSound(self, fileName):
            returnValue = libpanda._inPMC2_7p_9(self.this, fileName)
            return returnValue

        
        def setVolume(self, volume):
            returnValue = libpanda._inPMC2_jsxW(self.this, volume)
            return returnValue

        
        def getVolume(self):
            returnValue = libpanda._inPMC2_zv2w(self.this)
            return returnValue

        
        def setActive(self, flag):
            returnValue = libpanda._inPMC2_CYHE(self.this, flag)
            return returnValue

        
        def getActive(self):
            returnValue = libpanda._inPMC2_Uq9m(self.this)
            return returnValue


    globals()['AudioManager'] = AudioManager

