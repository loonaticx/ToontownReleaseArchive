# Source Generated with Decompyle++
# File: PTAColorf.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4
import PointerToBaseRefCountObjpvectorLVecBase4f
classDefined = 0

def generateClass_PTAColorf():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PTAColorf(PointerToBaseRefCountObjpvectorLVecBase4f.PointerToBaseRefCountObjpvectorLVecBase4f, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3KZax()
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint(self, n):
            self.this = libpanda._inPVZN3qv5K(n)
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint_ptrConstLVecBase4f(self, n, value):
            self.this = libpanda._inPVZN3GsjW(n, value.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPTAColorf(self, copy):
            self.this = libpanda._inPVZN3rM5B(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3zsyC:
                libpanda._inPVZN3zsyC(self.this)
            

        
        def size(self):
            returnValue = libpanda._inPVZN3eM77(self.this)
            return returnValue

        
        def pushBack(self, x):
            returnValue = libpanda._inPVZN3brDO(self.this, x.this)
            return returnValue

        
        def popBack(self):
            returnValue = libpanda._inPVZN35nTD(self.this)
            return returnValue

        
        def makeEmpty(self):
            returnValue = libpanda._inPVZN3J2sd(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_unsignedint(_args[0])
                elif isinstance(_args[0], PTAColorf):
                    return self.overloaded_constructor_ptrConstPTAColorf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PTAColorf> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4.VBase4):
                        return self.overloaded_constructor_unsignedint_ptrConstLVecBase4f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['PTAColorf'] = PTAColorf

