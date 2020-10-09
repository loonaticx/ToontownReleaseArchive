# Source Generated with Decompyle++
# File: PGMouseWatcherParameter.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
import MouseWatcherParameter
import TypeHandle
import ReferenceCount
import TypedReferenceCount
import ButtonHandle
import ModifierButtons
import Point2
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import MouseWatcherParameter
import ButtonHandle
import ModifierButtons
import Point2
import Ostream
classDefined = 0

def generateClass_PGMouseWatcherParameter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGMouseWatcherParameter(TypedReferenceCount.TypedReferenceCount, MouseWatcherParameter.MouseWatcherParameter, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
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
            if libpanda and libpanda._inPVvimfZ6X:
                libpanda._inPVvimfZ6X(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPVvimzRhq()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def output(self, out):
            returnValue = libpanda._inPVvimRTj_(self.this, out.this)
            return returnValue

        
        def upcastToMouseWatcherParameter(self):
            returnValue = libpanda._inPVvimcJKV(self.this)
            returnObject = MouseWatcherParameter.MouseWatcherParameter(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtDe8f(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getType(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtuIyI(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getTypeIndex(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtfVBU(upcastSelf.this)
            return returnValue

        
        def isOfType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtgfKt(upcastSelf.this, handle.this)
            return returnValue

        
        def isExactType(self, handle):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxt0xzz(upcastSelf.this, handle.this)
            return returnValue

        
        def getRefCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtIP2_(upcastSelf.this)
            return returnValue

        
        def ref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtTs5_(upcastSelf.this)
            return returnValue

        
        def unref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtpMWy(upcastSelf.this)
            return returnValue

        
        def testRefCountIntegrity(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtoDk2(upcastSelf.this)
            return returnValue

        
        def hasButton(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw5A3BJ(upcastSelf.this)
            return returnValue

        
        def getButton(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw5P1t7(upcastSelf.this)
            returnObject = ButtonHandle.ButtonHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getModifierButtons(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw58Pbu(upcastSelf.this)
            returnObject = ModifierButtons.ModifierButtons(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def hasMouse(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw5wy9y(upcastSelf.this)
            return returnValue

        
        def getMouse(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw5gfpl(upcastSelf.this)
            returnObject = Point2.Point2(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isOutside(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToMouseWatcherParameter()
            returnValue = libpanda._inPyiw57Had(upcastSelf.this)
            return returnValue


    globals()['PGMouseWatcherParameter'] = PGMouseWatcherParameter

