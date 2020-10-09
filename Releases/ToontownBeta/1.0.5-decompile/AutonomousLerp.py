# Source Generated with Decompyle++
# File: AutonomousLerp.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import LerpFunctor
import LerpBlendType
import EventHandler
import TypeHandle
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_AutonomousLerp():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class AutonomousLerp(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType_ptrEventHandler(self, func, endt, blend, handler):
            self.this = libpanda._inPjRdzrgSy(func.this, endt, blend.this, handler.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType_ptrEventHandler(self, func, startt, endt, blend, handler):
            self.this = libpanda._inPjRdzBEOi(func.this, startt, endt, blend.this, handler.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstAutonomousLerp(self, parameter0):
            self.this = libpanda._inPjRdzgPni(parameter0.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPjRdzgslS()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, parameter1):
            returnValue = libpanda._inPjRdzdRM_(self.this, parameter1.this)
            returnObject = AutonomousLerp(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def start(self):
            returnValue = libpanda._inPjRdzn1E1(self.this)
            return returnValue

        
        def stop(self):
            returnValue = libpanda._inPjRdz4Yt_(self.this)
            return returnValue

        
        def resume(self):
            returnValue = libpanda._inPjRdzYX_9(self.this)
            return returnValue

        
        def isDone(self):
            returnValue = libpanda._inPjRdzV70a(self.this)
            return returnValue

        
        def getFunctor(self):
            returnValue = libpanda._inPjRdzdEp1(self.this)
            returnObject = LerpFunctor.LerpFunctor(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setT(self, parameter1):
            returnValue = libpanda._inPjRdzNkt3(self.this, parameter1)
            return returnValue

        
        def getT(self):
            returnValue = libpanda._inPjRdzMGcG(self.this)
            return returnValue

        
        def setEndEvent(self, parameter1):
            returnValue = libpanda._inPjRdzdAeC(self.this, parameter1)
            return returnValue

        
        def getEndEvent(self):
            returnValue = libpanda._inPjRdzBf7x(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], AutonomousLerp):
                    return self.overloaded_constructor_ptrConstAutonomousLerp(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AutonomousLerp> '
            elif numArgs == 4:
                if isinstance(_args[0], LerpFunctor.LerpFunctor):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], LerpBlendType.LerpBlendType):
                            if isinstance(_args[3], EventHandler.EventHandler):
                                return self.overloaded_constructor_ptrLerpFunctor_float_ptrLerpBlendType_ptrEventHandler(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <EventHandler.EventHandler> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <LerpBlendType.LerpBlendType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LerpFunctor.LerpFunctor> '
            elif numArgs == 5:
                if isinstance(_args[0], LerpFunctor.LerpFunctor):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], LerpBlendType.LerpBlendType):
                                if isinstance(_args[4], EventHandler.EventHandler):
                                    return self.overloaded_constructor_ptrLerpFunctor_float_float_ptrLerpBlendType_ptrEventHandler(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <EventHandler.EventHandler> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <LerpBlendType.LerpBlendType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <LerpFunctor.LerpFunctor> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 5 '


    globals()['AutonomousLerp'] = AutonomousLerp

