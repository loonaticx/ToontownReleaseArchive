# Source Generated with Decompyle++
# File: ModifierButtons.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ButtonHandle
import ButtonEvent
import Ostream
classDefined = 0

def generateClass_ModifierButtons():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ModifierButtons(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPflboNvR4()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstModifierButtons(self, copy):
            self.this = libpanda._inPflboILgU(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPflboEqES:
                libpanda._inPflboEqES(self.this)
            

        
        def assign(self, copy):
            returnValue = libpanda._inPflboYKzS(self.this, copy.this)
            returnObject = ModifierButtons(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def eq(self, other):
            returnValue = libpanda._inPflboT7ow(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPflbob63N(self.this, other.this)
            return returnValue

        
        def lessThan(self, other):
            returnValue = libpanda._inPflbos0OV(self.this, other.this)
            return returnValue

        
        def addButton(self, button):
            returnValue = libpanda._inPflboMlZg(self.this, button.this)
            return returnValue

        
        def hasButton(self, button):
            returnValue = libpanda._inPflboFhRl(self.this, button.this)
            return returnValue

        
        def removeButton(self, button):
            returnValue = libpanda._inPflbobICm(self.this, button.this)
            return returnValue

        
        def getNumButtons(self):
            returnValue = libpanda._inPflbopXD5(self.this)
            return returnValue

        
        def getButton(self, index):
            returnValue = libpanda._inPflboDjca(self.this, index)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def buttonDown(self, button):
            returnValue = libpanda._inPflbob6E5(self.this, button.this)
            return returnValue

        
        def buttonUp(self, button):
            returnValue = libpanda._inPflbowwnW(self.this, button.this)
            return returnValue

        
        def addEvent(self, event):
            returnValue = libpanda._inPflboXBNb(self.this, event.this)
            return returnValue

        
        def allButtonsUp(self):
            returnValue = libpanda._inPflboXj_1(self.this)
            return returnValue

        
        def overloaded_isDown_ptrConstModifierButtons_ptrButtonHandle(self, button):
            returnValue = libpanda._inPflbozJDj(self.this, button.this)
            return returnValue

        
        def overloaded_isDown_ptrConstModifierButtons_int(self, index):
            returnValue = libpanda._inPflbon2QV(self.this, index)
            return returnValue

        
        def isAnyDown(self):
            returnValue = libpanda._inPflboLOeb(self.this)
            return returnValue

        
        def getPrefix(self):
            returnValue = libpanda._inPflbo2fCN(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPflboU4aY(self.this, out.this)
            return returnValue

        
        def write(self, out):
            returnValue = libpanda._inPflbo8qR3(self.this, out.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], ModifierButtons):
                    return self.overloaded_constructor_ptrConstModifierButtons(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ModifierButtons> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def isDown(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_isDown_ptrConstModifierButtons_int(_args[0])
                elif isinstance(_args[0], ButtonHandle.ButtonHandle):
                    return self.overloaded_isDown_ptrConstModifierButtons_ptrButtonHandle(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <ButtonHandle.ButtonHandle> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['ModifierButtons'] = ModifierButtons

