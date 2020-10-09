# Source Generated with Decompyle++
# File: PointerToAnimControl.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import AnimControl
import PointerToBaseAnimControl
classDefined = 0

def generateClass_PointerToAnimControl():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PointerToAnimControl(PointerToBaseAnimControl.PointerToBaseAnimControl, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrAnimControl(self, ptr):
            self.this = libpanda._inPn9gMDg8O(ptr.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPn9gM_O3j()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrAnimControl(self, copy):
            self.this = libpanda._inPn9gMy1e4(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPn9gM6WWG:
                libpanda._inPn9gM6WWG(self.this)
            

        
        def p(self):
            returnValue = libpanda._inPn9gMvfy0(self.this)
            returnObject = AnimControl.AnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_assign_ptrPointerToAnimControl_ptrAnimControl(self, ptr):
            returnValue = libpanda._inPn9gMDtyX(self.this, ptr.this)
            returnObject = PointerToAnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def overloaded_assign_ptrPointerToAnimControl_ptrAnimControl(self, copy):
            returnValue = libpanda._inPn9gMvR1K(self.this, copy.this)
            returnObject = PointerToAnimControl(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isNull(self):
            returnValue = libpanda._inPn9gMMjc9(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPn9gMyulu(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], AnimControl.AnimControl):
                    return self.overloaded_constructor_ptrAnimControl(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimControl.AnimControl> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def assign(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], AnimControl.AnimControl):
                    return self.overloaded_assign_ptrPointerToAnimControl_ptrAnimControl(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <AnimControl.AnimControl> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['PointerToAnimControl'] = PointerToAnimControl

