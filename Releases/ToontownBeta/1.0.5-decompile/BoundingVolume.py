# Source Generated with Decompyle++
# File: BoundingVolume.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
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

def generateClass_BoundingVolume():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BoundingVolume(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        IFSome = 2
        IFPossible = 1
        IFDontUnderstand = 8
        IFAll = 4
        IFNoIntersection = 0
        
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
            if libpanda and libpanda._inPSkjPt_oB:
                libpanda._inPSkjPt_oB(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPSkjPk5Vo()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def makeCopy(self):
            returnValue = libpanda._inPSkjPbS0P(self.this)
            returnObject = BoundingVolume(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def isEmpty(self):
            returnValue = libpanda._inPSkjPO5qL(self.this)
            return returnValue

        
        def isInfinite(self):
            returnValue = libpanda._inPSkjP_FGC(self.this)
            return returnValue

        
        def setInfinite(self):
            returnValue = libpanda._inPSkjP8Pim(self.this)
            return returnValue

        
        def extendBy(self, vol):
            returnValue = libpanda._inPSkjP5qix(self.this, vol.this)
            return returnValue

        
        def contains(self, vol):
            returnValue = libpanda._inPSkjPWDQR(self.this, vol.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPSkjPJ1vQ(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstBoundingVolume_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPSkjPCN7_(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstBoundingVolume_ptrOstream(self, out):
            returnValue = libpanda._inPSkjPSQrR(self.this, out.this)
            return returnValue

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstBoundingVolume_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstBoundingVolume_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['BoundingVolume'] = BoundingVolume

