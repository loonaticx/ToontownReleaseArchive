# Source Generated with Decompyle++
# File: PTANormalf.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Vec3
import PointerToBaseRefCountObjpvectorLVector3f
classDefined = 0

def generateClass_PTANormalf():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PTANormalf(PointerToBaseRefCountObjpvectorLVector3f.PointerToBaseRefCountObjpvectorLVector3f, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3eH8W()
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint(self, n):
            self.this = libpanda._inPVZN3PsrZ(n)
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint_ptrConstLVector3f(self, n, value):
            self.this = libpanda._inPVZN36ral(n, value.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPTANormalf(self, copy):
            self.this = libpanda._inPVZN3myAY(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN31Hd3:
                libpanda._inPVZN31Hd3(self.this)
            

        
        def size(self):
            returnValue = libpanda._inPVZN3QqQz(self.this)
            return returnValue

        
        def pushBack(self, x):
            returnValue = libpanda._inPVZN3Vcnk(self.this, x.this)
            return returnValue

        
        def popBack(self):
            returnValue = libpanda._inPVZN38mfx(self.this)
            return returnValue

        
        def makeEmpty(self):
            returnValue = libpanda._inPVZN35rVq(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_unsignedint(_args[0])
                elif isinstance(_args[0], PTANormalf):
                    return self.overloaded_constructor_ptrConstPTANormalf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PTANormalf> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_constructor_unsignedint_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['PTANormalf'] = PTANormalf

