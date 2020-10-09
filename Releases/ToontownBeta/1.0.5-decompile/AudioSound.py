# Source Generated with Decompyle++
# File: AudioSound.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_AudioSound():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AudioSound(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        BAD = 0
        PLAYING = 2
        READY = 1
        
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
            if libpanda and libpanda._inPMC2_3ha6:
                libpanda._inPMC2_3ha6(self.this)
            

        
        def play(self):
            returnValue = libpanda._inPMC2_3Jih(self.this)
            return returnValue

        
        def stop(self):
            returnValue = libpanda._inPMC2_WoiG(self.this)
            return returnValue

        
        def overloaded_setLoop_ptrAudioSound_bool(self, loop):
            returnValue = libpanda._inPMC2_lqm7(self.this, loop)
            return returnValue

        
        def overloaded_setLoop_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_XDYp(self.this)
            return returnValue

        
        def getLoop(self):
            returnValue = libpanda._inPMC2_dXgo(self.this)
            return returnValue

        
        def overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(self, loopCount):
            returnValue = libpanda._inPMC2_S0hU(self.this, loopCount)
            return returnValue

        
        def overloaded_setLoopCount_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_Ol64(self.this)
            return returnValue

        
        def getLoopCount(self):
            returnValue = libpanda._inPMC2_Ntas(self.this)
            return returnValue

        
        def overloaded_setTime_ptrAudioSound_float(self, startTime):
            returnValue = libpanda._inPMC2_lLKX(self.this, startTime)
            return returnValue

        
        def overloaded_setTime_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_vBA5(self.this)
            return returnValue

        
        def getTime(self):
            returnValue = libpanda._inPMC2_aGJ4(self.this)
            return returnValue

        
        def overloaded_setVolume_ptrAudioSound_float(self, volume):
            returnValue = libpanda._inPMC2_XPJ3(self.this, volume)
            return returnValue

        
        def overloaded_setVolume_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_0ZoT(self.this)
            return returnValue

        
        def getVolume(self):
            returnValue = libpanda._inPMC2_sLs3(self.this)
            return returnValue

        
        def overloaded_setBalance_ptrAudioSound_float(self, balanceRight):
            returnValue = libpanda._inPMC2_gDJq(self.this, balanceRight)
            return returnValue

        
        def overloaded_setBalance_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_CR_4(self.this)
            return returnValue

        
        def getBalance(self):
            returnValue = libpanda._inPMC2_prl7(self.this)
            return returnValue

        
        def overloaded_setActive_ptrAudioSound_bool(self, flag):
            returnValue = libpanda._inPMC2_4m0J(self.this, flag)
            return returnValue

        
        def overloaded_setActive_ptrAudioSound(self):
            returnValue = libpanda._inPMC2_MhGV(self.this)
            return returnValue

        
        def getActive(self):
            returnValue = libpanda._inPMC2_rdK5(self.this)
            return returnValue

        
        def getName(self):
            returnValue = libpanda._inPMC2_uOG5(self.this)
            return returnValue

        
        def length(self):
            returnValue = libpanda._inPMC2_utDx(self.this)
            return returnValue

        
        def status(self):
            returnValue = libpanda._inPMC2_fgiV(self.this)
            return returnValue

        
        def setVolume(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setVolume_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setVolume_ptrAudioSound_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setActive(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setActive_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setActive_ptrAudioSound_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setLoop(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setLoop_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setLoop_ptrAudioSound_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setTime(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setTime_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setTime_ptrAudioSound_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setLoopCount(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setLoopCount_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setLoopCount_ptrAudioSound_longUnsignedlongint(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setBalance(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setBalance_ptrAudioSound()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setBalance_ptrAudioSound_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['AudioSound'] = AudioSound

