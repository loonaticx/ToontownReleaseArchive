# Source Generated with Decompyle++
# File: PTATexCoordf.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Point2
import PointerToBaseRefCountObjpvectorLPoint2f
classDefined = 0

def generateClass_PTATexCoordf():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PTATexCoordf(PointerToBaseRefCountObjpvectorLPoint2f.PointerToBaseRefCountObjpvectorLPoint2f, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3SPFP()
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint(self, n):
            self.this = libpanda._inPVZN3VcIp(n)
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint_ptrConstLPoint2f(self, n, value):
            self.this = libpanda._inPVZN3lnOf(n, value.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPTATexCoordf(self, copy):
            self.this = libpanda._inPVZN3O6Wz(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3xmGs:
                libpanda._inPVZN3xmGs(self.this)
            

        
        def size(self):
            returnValue = libpanda._inPVZN38n_L(self.this)
            return returnValue

        
        def pushBack(self, x):
            returnValue = libpanda._inPVZN3RtFP(self.this, x.this)
            return returnValue

        
        def popBack(self):
            returnValue = libpanda._inPVZN3i87V(self.this)
            return returnValue

        
        def makeEmpty(self):
            returnValue = libpanda._inPVZN3dOuT(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_unsignedint(_args[0])
                elif isinstance(_args[0], PTATexCoordf):
                    return self.overloaded_constructor_ptrConstPTATexCoordf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PTATexCoordf> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Point2.Point2):
                        return self.overloaded_constructor_unsignedint_ptrConstLPoint2f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point2.Point2> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['PTATexCoordf'] = PTATexCoordf

