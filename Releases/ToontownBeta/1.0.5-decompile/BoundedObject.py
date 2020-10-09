# Source Generated with Decompyle++
# File: BoundedObject.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import BoundingVolume
import TypeHandle
classDefined = 0

def generateClass_BoundedObject():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class BoundedObject(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        BVTStatic = 0
        BVTDynamicSphere = 1
        
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
            if libpanda and libpanda._inPs9JIVjrv:
                libpanda._inPs9JIVjrv(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPs9JI_u7v()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
            returnValue = libpanda._inPs9JI7U7J(self.this, type)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
            returnValue = libpanda._inPs9JINvRr(self.this, volume.this)
            return returnValue

        
        def getBound(self):
            returnValue = libpanda._inPs9JImoIb(self.this)
            returnObject = BoundingVolume.BoundingVolume(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def markBoundStale(self):
            returnValue = libpanda._inPs9JI_RvI(self.this)
            return returnValue

        
        def forceBoundStale(self):
            returnValue = libpanda._inPs9JIcPQw(self.this)
            return returnValue

        
        def isBoundStale(self):
            returnValue = libpanda._inPs9JId0c5(self.this)
            return returnValue

        
        def setFinal(self, flag):
            returnValue = libpanda._inPs9JIrXwH(self.this, flag)
            return returnValue

        
        def isFinal(self):
            returnValue = libpanda._inPs9JIUIM4(self.this)
            return returnValue

        
        def setBound(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(_args[0])
                elif isinstance(_args[0], BoundingVolume.BoundingVolume):
                    return self.overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <BoundingVolume.BoundingVolume> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['BoundedObject'] = BoundedObject

