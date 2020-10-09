# Source Generated with Decompyle++
# File: PTAVertexf.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import Point3
import PointerToBaseRefCountObjpvectorLPoint3f
classDefined = 0

def generateClass_PTAVertexf():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PTAVertexf(PointerToBaseRefCountObjpvectorLPoint3f.PointerToBaseRefCountObjpvectorLPoint3f, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVZN3fBGP()
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint(self, n):
            self.this = libpanda._inPVZN3enJp(n)
            self.userManagesMemory = 1

        
        def overloaded_constructor_unsignedint_ptrConstLPoint3f(self, n, value):
            self.this = libpanda._inPVZN3aZf7(n, value.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstPTAVertexf(self, copy):
            self.this = libpanda._inPVZN3C1XT(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVZN3ssHs:
                libpanda._inPVZN3ssHs(self.this)
            

        
        def size(self):
            returnValue = libpanda._inPVZN3BKAM(self.this)
            return returnValue

        
        def pushBack(self, x):
            returnValue = libpanda._inPVZN3H7iH(self.this, x.this)
            return returnValue

        
        def popBack(self):
            returnValue = libpanda._inPVZN3fq8V(self.this)
            return returnValue

        
        def makeEmpty(self):
            returnValue = libpanda._inPVZN30kuT(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_unsignedint(_args[0])
                elif isinstance(_args[0], PTAVertexf):
                    return self.overloaded_constructor_ptrConstPTAVertexf(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <PTAVertexf> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_constructor_unsignedint_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['PTAVertexf'] = PTAVertexf

