# Source Generated with Decompyle++
# File: AnimControlCollection.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import AnimControl
import Event
classDefined = 0

def generateClass_AnimControlCollection():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AnimControlCollection(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPn9gM9uyR()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPn9gMdADm:
                libpanda._inPn9gMdADm(self.this)
            

        
        def storeAnim(self, control, name):
            returnValue = libpanda._inPn9gMCAu2(self.this, control.this, name)
            return returnValue

        
        def findAnim(self, name):
            returnValue = libpanda._inPn9gM87vI(self.this, name)
            returnObject = AnimControl.AnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def unbindAnim(self, name):
            returnValue = libpanda._inPn9gMXXcu(self.this, name)
            return returnValue

        
        def getNumAnims(self):
            returnValue = libpanda._inPn9gMhoNk(self.this)
            return returnValue

        
        def clearAnims(self):
            returnValue = libpanda._inPn9gMG8LN(self.this)
            return returnValue

        
        def setStopEvent(self, stopEvent):
            returnValue = libpanda._inPn9gMqSwI(self.this, stopEvent.this)
            return returnValue

        
        def clearStopEvent(self):
            returnValue = libpanda._inPn9gMfsKm(self.this)
            return returnValue

        
        def hasStopEvent(self):
            returnValue = libpanda._inPn9gMvUuA(self.this)
            return returnValue

        
        def getStopEvent(self):
            returnValue = libpanda._inPn9gMKCaz(self.this)
            returnObject = Event.Event(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_play_ptrAnimControlCollection_atomicstring(self, animName):
            returnValue = libpanda._inPn9gMNnjN(self.this, animName)
            return returnValue

        
        def overloaded_play_ptrAnimControlCollection_atomicstring_int_int(self, animName, _from, to):
            returnValue = libpanda._inPn9gM3gRl(self.this, animName, _from, to)
            return returnValue

        
        def overloaded_loop_ptrAnimControlCollection_atomicstring_bool(self, animName, restart):
            returnValue = libpanda._inPn9gM6iEH(self.this, animName, restart)
            return returnValue

        
        def overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(self, animName, restart, _from, to):
            returnValue = libpanda._inPn9gMMoG2(self.this, animName, restart, _from, to)
            return returnValue

        
        def stop(self, animName):
            returnValue = libpanda._inPn9gMnBiQ(self.this, animName)
            return returnValue

        
        def pose(self, animName, frame):
            returnValue = libpanda._inPn9gMfa9Z(self.this, animName, frame)
            return returnValue

        
        def overloaded_playAll_ptrAnimControlCollection(self):
            returnValue = libpanda._inPn9gMm8z5(self.this)
            return returnValue

        
        def overloaded_playAll_ptrAnimControlCollection_int_int(self, _from, to):
            returnValue = libpanda._inPn9gMVTrb(self.this, _from, to)
            return returnValue

        
        def overloaded_loopAll_ptrAnimControlCollection_bool(self, restart):
            returnValue = libpanda._inPn9gMF4O5(self.this, restart)
            return returnValue

        
        def overloaded_loopAll_ptrAnimControlCollection_bool_int_int(self, restart, _from, to):
            returnValue = libpanda._inPn9gMK_09(self.this, restart, _from, to)
            return returnValue

        
        def stopAll(self):
            returnValue = libpanda._inPn9gMQux8(self.this)
            return returnValue

        
        def poseAll(self, frame):
            returnValue = libpanda._inPn9gMCHfr(self.this, frame)
            return returnValue

        
        def overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(self, animName):
            returnValue = libpanda._inPn9gMzcy2(self.this, animName)
            return returnValue

        
        def overloaded_getFrame_ptrConstAnimControlCollection(self):
            returnValue = libpanda._inPn9gMaxpY(self.this)
            return returnValue

        
        def getNumFrames(self, animName):
            returnValue = libpanda._inPn9gMo_KP(self.this, animName)
            return returnValue

        
        def overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(self, animName):
            returnValue = libpanda._inPn9gMf45y(self.this, animName)
            return returnValue

        
        def overloaded_isPlaying_ptrConstAnimControlCollection(self):
            returnValue = libpanda._inPn9gMzfhs(self.this)
            return returnValue

        
        def whichAnimPlaying(self):
            returnValue = libpanda._inPn9gM6hcV(self.this)
            return returnValue

        
        def loop(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_loop_ptrAnimControlCollection_atomicstring_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.IntType):
                                return self.overloaded_loop_ptrAnimControlCollection_atomicstring_bool_int_int(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.IntType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def getFrame(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getFrame_ptrConstAnimControlCollection()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_getFrame_ptrConstAnimControlCollection_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def playAll(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_playAll_ptrAnimControlCollection()
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_playAll_ptrAnimControlCollection_int_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '

        
        def isPlaying(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_isPlaying_ptrConstAnimControlCollection()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_isPlaying_ptrConstAnimControlCollection_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def play(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_play_ptrAnimControlCollection_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_play_ptrAnimControlCollection_atomicstring_int_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def loopAll(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_loopAll_ptrAnimControlCollection_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_loopAll_ptrAnimControlCollection_bool_int_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['AnimControlCollection'] = AnimControlCollection

