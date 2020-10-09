# Source Generated with Decompyle++
# File: AnimControl.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Event
import PartBundle
import AnimBundle
import TypeHandle
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_AnimControl():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AnimControl(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPn9gMotrw:
                libpanda._inPn9gMotrw(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPn9gMlCdh()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_play_ptrAnimControl_ptrConstEvent(self, stopEvent):
            returnValue = libpanda._inPn9gMOpKG(self.this, stopEvent.this)
            return returnValue

        
        def overloaded_play_ptrAnimControl(self):
            returnValue = libpanda._inPn9gMnVss(self.this)
            return returnValue

        
        def overloaded_play_ptrAnimControl_int_int_ptrConstEvent(self, _from, to, stopEvent):
            returnValue = libpanda._inPn9gMI3_s(self.this, _from, to, stopEvent.this)
            return returnValue

        
        def overloaded_play_ptrAnimControl_int_int(self, _from, to):
            returnValue = libpanda._inPn9gMXbT0(self.this, _from, to)
            return returnValue

        
        def overloaded_loop_ptrAnimControl_bool(self, restart):
            returnValue = libpanda._inPn9gMExO_(self.this, restart)
            return returnValue

        
        def overloaded_loop_ptrAnimControl_bool_int_int(self, restart, _from, to):
            returnValue = libpanda._inPn9gMnhvR(self.this, restart, _from, to)
            return returnValue

        
        def pingpong(self, restart, _from, to):
            returnValue = libpanda._inPn9gMzPSK(self.this, restart, _from, to)
            return returnValue

        
        def stop(self):
            returnValue = libpanda._inPn9gM86aN(self.this)
            return returnValue

        
        def pose(self, frame):
            returnValue = libpanda._inPn9gMLfkS(self.this, frame)
            return returnValue

        
        def addEvent(self, frame, event):
            returnValue = libpanda._inPn9gMT43u(self.this, frame, event.this)
            return returnValue

        
        def removeEvent(self, eventName):
            returnValue = libpanda._inPn9gM1Ikl(self.this, eventName)
            return returnValue

        
        def removeAllEvents(self):
            returnValue = libpanda._inPn9gMGTC1(self.this)
            return returnValue

        
        def setPlayRate(self, playRate):
            returnValue = libpanda._inPn9gMA9lM(self.this, playRate)
            return returnValue

        
        def getPlayRate(self):
            returnValue = libpanda._inPn9gM341Y(self.this)
            return returnValue

        
        def getFrameRate(self):
            returnValue = libpanda._inPn9gMijSW(self.this)
            return returnValue

        
        def getFrame(self):
            returnValue = libpanda._inPn9gMRC6O(self.this)
            return returnValue

        
        def getNumFrames(self):
            returnValue = libpanda._inPn9gMKzad(self.this)
            return returnValue

        
        def isPlaying(self):
            returnValue = libpanda._inPn9gMw80D(self.this)
            return returnValue

        
        def getPart(self):
            returnValue = libpanda._inPn9gMbBS8(self.this)
            returnObject = PartBundle.PartBundle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getAnim(self):
            returnValue = libpanda._inPn9gMYbvN(self.this)
            returnObject = AnimBundle.AnimBundle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def loop(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_loop_ptrAnimControl_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_loop_ptrAnimControl_bool_int_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def play(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_play_ptrAnimControl()
            elif numArgs == 1:
                if isinstance(_args[0], Event.Event):
                    return self.overloaded_play_ptrAnimControl_ptrConstEvent(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Event.Event> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_play_ptrAnimControl_int_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], Event.Event):
                            return self.overloaded_play_ptrAnimControl_int_int_ptrConstEvent(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Event.Event> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 3 '


    globals()['AnimControl'] = AnimControl

