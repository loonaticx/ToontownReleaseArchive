# Source Generated with Decompyle++
# File: GraphicsWindow.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsStateGuardian
import GraphicsPipe
import ReferenceCount
import TypeHandle
import Configurable
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_GraphicsWindow():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GraphicsWindow(Configurable.Configurable, ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPO9cYN6ow:
                libpanda._inPO9cYN6ow(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPO9cYcgVA()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getWidth(self):
            returnValue = libpanda._inPO9cYcRGH(self.this)
            return returnValue

        
        def getHeight(self):
            returnValue = libpanda._inPO9cYWET6(self.this)
            return returnValue

        
        def getXorg(self):
            returnValue = libpanda._inPO9cY05eu(self.this)
            return returnValue

        
        def getYorg(self):
            returnValue = libpanda._inPO9cYkXzu(self.this)
            return returnValue

        
        def getGsg(self):
            returnValue = libpanda._inPO9cYVO8F(self.this)
            returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getPipe(self):
            returnValue = libpanda._inPO9cY_Rmk(self.this)
            returnObject = GraphicsPipe.GraphicsPipe(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def closeWindow(self):
            returnValue = libpanda._inPO9cYts8J(self.this)
            return returnValue

        
        def isClosed(self):
            returnValue = libpanda._inPO9cYnXr8(self.this)
            return returnValue

        
        def setFrameNumber(self, parameter1):
            returnValue = libpanda._inPO9cYfYp9(self.this, parameter1)
            return returnValue

        
        def getFrameNumber(self):
            returnValue = libpanda._inPO9cYtsv7(self.this)
            return returnValue

        
        def setSync(self, parameter1):
            returnValue = libpanda._inPO9cYdvSL(self.this, parameter1)
            return returnValue

        
        def getSync(self):
            returnValue = libpanda._inPO9cYv810(self.this)
            return returnValue

        
        def swap(self):
            returnValue = libpanda._inPO9cYuLGg(self.this)
            return returnValue

        
        def getNumInputDevices(self):
            returnValue = libpanda._inPO9cYP2_C(self.this)
            return returnValue

        
        def getInputDeviceName(self, device):
            returnValue = libpanda._inPO9cYj7fW(self.this, device)
            return returnValue

        
        def hasPointer(self, device):
            returnValue = libpanda._inPO9cYRerM(self.this, device)
            return returnValue

        
        def hasKeyboard(self, device):
            returnValue = libpanda._inPO9cYXepH(self.this, device)
            return returnValue

        
        def processEvents(self):
            returnValue = libpanda._inPO9cYdbtc(self.this)
            return returnValue

        
        def flagRedisplay(self):
            returnValue = libpanda._inPO9cYZbbk(self.this)
            return returnValue

        
        def mainLoop(self):
            returnValue = libpanda._inPO9cYt6ty(self.this)
            return returnValue

        
        def supportsUpdate(self):
            returnValue = libpanda._inPO9cYx_CP(self.this)
            return returnValue

        
        def update(self):
            returnValue = libpanda._inPO9cYevsJ(self.this)
            return returnValue

        
        def upcastToReferenceCount(self):
            returnValue = libpanda._inPO9cYP9V6(self.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
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


    globals()['GraphicsWindow'] = GraphicsWindow

