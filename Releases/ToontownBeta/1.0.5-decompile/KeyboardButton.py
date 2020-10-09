# Source Generated with Decompyle++
# File: KeyboardButton.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import ButtonHandle
classDefined = 0

def generateClass_KeyboardButton():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class KeyboardButton(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
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
            if libpanda and libpanda._inPflbom50c:
                libpanda._inPflbom50c(self.this)
            

        
        def asciiKey(asciiEquivalent):
            returnValue = libpanda._inPflboYTpq(asciiEquivalent)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        asciiKey = PandaStatic.PandaStatic(asciiKey)
        
        def space():
            returnValue = libpanda._inPflbopJPd()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        space = PandaStatic.PandaStatic(space)
        
        def backspace():
            returnValue = libpanda._inPflbopfyx()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        backspace = PandaStatic.PandaStatic(backspace)
        
        def tab():
            returnValue = libpanda._inPflboCIg_()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        tab = PandaStatic.PandaStatic(tab)
        
        def enter():
            returnValue = libpanda._inPflbocdap()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        enter = PandaStatic.PandaStatic(enter)
        
        def escape():
            returnValue = libpanda._inPflboklDY()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        escape = PandaStatic.PandaStatic(escape)
        
        def f1():
            returnValue = libpanda._inPflbouoGt()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f1 = PandaStatic.PandaStatic(f1)
        
        def f2():
            returnValue = libpanda._inPflbovoUJ()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f2 = PandaStatic.PandaStatic(f2)
        
        def f3():
            returnValue = libpanda._inPflbopoil()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f3 = PandaStatic.PandaStatic(f3)
        
        def f4():
            returnValue = libpanda._inPflbo2owB()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f4 = PandaStatic.PandaStatic(f4)
        
        def f5():
            returnValue = libpanda._inPflbo4o_d()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f5 = PandaStatic.PandaStatic(f5)
        
        def f6():
            returnValue = libpanda._inPflboyoM6()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f6 = PandaStatic.PandaStatic(f6)
        
        def f7():
            returnValue = libpanda._inPflbozoaW()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f7 = PandaStatic.PandaStatic(f7)
        
        def f8():
            returnValue = libpanda._inPflbodooy()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f8 = PandaStatic.PandaStatic(f8)
        
        def f9():
            returnValue = libpanda._inPflboao2O()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f9 = PandaStatic.PandaStatic(f9)
        
        def f10():
            returnValue = libpanda._inPflboEfnR()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f10 = PandaStatic.PandaStatic(f10)
        
        def f11():
            returnValue = libpanda._inPflboS0nY()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f11 = PandaStatic.PandaStatic(f11)
        
        def f12():
            returnValue = libpanda._inPflboo1nf()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        f12 = PandaStatic.PandaStatic(f12)
        
        def left():
            returnValue = libpanda._inPflboZFC1()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        left = PandaStatic.PandaStatic(left)
        
        def right():
            returnValue = libpanda._inPflboUhch()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        right = PandaStatic.PandaStatic(right)
        
        def up():
            returnValue = libpanda._inPflbonCIo()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        up = PandaStatic.PandaStatic(up)
        
        def down():
            returnValue = libpanda._inPflboYYHf()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        down = PandaStatic.PandaStatic(down)
        
        def pageUp():
            returnValue = libpanda._inPflbo0xIX()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        pageUp = PandaStatic.PandaStatic(pageUp)
        
        def pageDown():
            returnValue = libpanda._inPflboJGIF()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        pageDown = PandaStatic.PandaStatic(pageDown)
        
        def home():
            returnValue = libpanda._inPflbokSjM()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        home = PandaStatic.PandaStatic(home)
        
        def end():
            returnValue = libpanda._inPflbouYGy()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        end = PandaStatic.PandaStatic(end)
        
        def insert():
            returnValue = libpanda._inPflboBAlh()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        insert = PandaStatic.PandaStatic(insert)
        
        def _del():
            returnValue = libpanda._inPflboRGQn()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        _del = PandaStatic.PandaStatic(_del)
        
        def shift():
            returnValue = libpanda._inPflbotqFY()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        shift = PandaStatic.PandaStatic(shift)
        
        def control():
            returnValue = libpanda._inPflbogZYd()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        control = PandaStatic.PandaStatic(control)
        
        def alt():
            returnValue = libpanda._inPflboT0IW()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        alt = PandaStatic.PandaStatic(alt)
        
        def meta():
            returnValue = libpanda._inPflbooat7()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        meta = PandaStatic.PandaStatic(meta)
        
        def capsLock():
            returnValue = libpanda._inPflbogq06()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        capsLock = PandaStatic.PandaStatic(capsLock)
        
        def shiftLock():
            returnValue = libpanda._inPflboDgms()
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        shiftLock = PandaStatic.PandaStatic(shiftLock)

    globals()['KeyboardButton'] = KeyboardButton

