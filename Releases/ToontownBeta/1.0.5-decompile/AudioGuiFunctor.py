# Source Generated with Decompyle++
# File: AudioGuiFunctor.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import AudioSound
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import GuiBehavior
import TypeHandle
classDefined = 0

def generateClass_AudioGuiFunctor():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AudioGuiFunctor(GuiBehavior.GuiBehavior.BehaviorFunctor, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrAudioSound_ptrBehaviorFunctor(self, parameter0, parameter1):
            self.this = libpanda._inPMC2_c36A(parameter0.this, parameter1.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrAudioSound(self, parameter0):
            self.this = libpanda._inPMC2_6TUu(parameter0.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPMC2_JYRN()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPMC2_GrQ0()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getSound(self):
            returnValue = libpanda._inPMC2_0GHk(self.this)
            returnObject = AudioSound.AudioSound(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getPrev(self):
            returnValue = libpanda._inPMC2_DQaf(self.this)
            returnObject = GuiBehavior.GuiBehavior.BehaviorFunctor(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], AudioSound.AudioSound):
                    return self.overloaded_constructor_ptrAudioSound(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AudioSound.AudioSound> '
            elif numArgs == 2:
                if isinstance(_args[0], AudioSound.AudioSound):
                    if isinstance(_args[1], GuiBehavior.GuiBehavior.BehaviorFunctor):
                        return self.overloaded_constructor_ptrAudioSound_ptrBehaviorFunctor(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <GuiBehavior.GuiBehavior.BehaviorFunctor> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AudioSound.AudioSound> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['AudioGuiFunctor'] = AudioGuiFunctor

