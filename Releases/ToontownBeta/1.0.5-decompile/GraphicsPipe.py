# Source Generated with Decompyle++
# File: GraphicsPipe.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsWindow
import TypeHandle
import Namable
import ReferenceCount
import TypedReferenceCount
import Ostream
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
classDefined = 0

def generateClass_GraphicsPipe():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GraphicsPipe(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPO9cY0_yM:
                libpanda._inPO9cY0_yM(self.this)
            

        
        def getNumPipes():
            returnValue = libpanda._inPO9cYZoX_()
            return returnValue

        getNumPipes = PandaStatic.PandaStatic(getNumPipes)
        
        def getPipe(n):
            returnValue = libpanda._inPO9cYeOUt(n)
            returnObject = GraphicsPipe(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getPipe = PandaStatic.PandaStatic(getPipe)
        
        def getClassType():
            returnValue = libpanda._inPO9cYdm1K()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_makeWindow_ptrGraphicsPipe(self):
            returnValue = libpanda._inPO9cY7rBJ(self.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_makeWindow_ptrGraphicsPipe_ptrConstProperties(self, parameter1):
            returnValue = libpanda._inPO9cYG1nH(self.this, parameter1.this)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def removeWindow(self, window):
            returnValue = libpanda._inPO9cYzemX(self.this, window.this)
            return returnValue

        
        def getWindowType(self):
            returnValue = libpanda._inPO9cYeBo3(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumWindows(self):
            returnValue = libpanda._inPO9cYsvfY(self.this)
            return returnValue

        
        def getWindow(self, n):
            returnValue = libpanda._inPO9cYo_m2(self.this, n)
            returnObject = GraphicsWindow.GraphicsWindow(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def upcastToNamable(self):
            returnValue = libpanda._inPO9cYDH6z(self.this)
            returnObject = Namable.Namable(None)
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

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setName(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtEnBW(upcastSelf.this, name)
            return returnValue

        
        def clearName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtSJVl(upcastSelf.this)
            return returnValue

        
        def hasName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtR9hC(upcastSelf.this)
            return returnValue

        
        def getName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtYaRN(upcastSelf.this)
            return returnValue

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxthN8q(upcastSelf.this, out.this)
            return returnValue

        
        def makeWindow(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_makeWindow_ptrGraphicsPipe()
            elif numArgs == 1:
                if isinstance(_args[0], GraphicsWindow.GraphicsWindow.Properties):
                    return self.overloaded_makeWindow_ptrGraphicsPipe_ptrConstProperties(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsWindow.GraphicsWindow.Properties> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['GraphicsPipe'] = GraphicsPipe
