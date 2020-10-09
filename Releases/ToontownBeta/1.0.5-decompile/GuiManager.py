# Source Generated with Decompyle++
# File: GuiManager.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import MouseWatcherRegion
import GuiLabel
import Node
import EventHandler
import GraphicsWindow
import MouseAndKeyboard
classDefined = 0

def generateClass_GuiManager():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiManager(FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPlRE2rL_h:
                libpanda._inPlRE2rL_h(self.this)
            

        
        def getPtr(parameter0, parameter1, root2d):
            returnValue = libpanda._inPlRE2vLal(parameter0.this, parameter1.this, root2d.this)
            returnObject = GuiManager(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        getPtr = PandaStatic.PandaStatic(getPtr)
        
        def addRegion(self, parameter1):
            returnValue = libpanda._inPlRE2rAOI(self.this, parameter1.this)
            return returnValue

        
        def overloaded_addLabel_ptrGuiManager_ptrGuiLabel(self, parameter1):
            returnValue = libpanda._inPlRE2cyF8(self.this, parameter1.this)
            return returnValue

        
        def overloaded_addLabel_ptrGuiManager_ptrGuiLabel_ptrNode(self, parameter1, parameter2):
            returnValue = libpanda._inPlRE2zpcp(self.this, parameter1.this, parameter2.this)
            return returnValue

        
        def removeRegion(self, parameter1):
            returnValue = libpanda._inPlRE2gzqI(self.this, parameter1.this)
            return returnValue

        
        def removeLabel(self, parameter1):
            returnValue = libpanda._inPlRE2s8DK(self.this, parameter1.this)
            return returnValue

        
        def hasRegion(self, parameter1):
            returnValue = libpanda._inPlRE22vjw(self.this, parameter1.this)
            return returnValue

        
        def hasLabel(self, parameter1):
            returnValue = libpanda._inPlRE26UZk(self.this, parameter1.this)
            return returnValue

        
        def recomputePriorities(self):
            returnValue = libpanda._inPlRE28q4y(self.this)
            return returnValue

        
        def getNextDrawOrder(self):
            returnValue = libpanda._inPlRE2MGYQ(self.this)
            return returnValue

        
        def setNextDrawOrder(self, parameter1):
            returnValue = libpanda._inPlRE2ZBOt(self.this, parameter1)
            return returnValue

        
        def getStartDrawOrder(self):
            returnValue = libpanda._inPlRE2y3_z(self.this)
            return returnValue

        
        def setStartDrawOrder(self, parameter1):
            returnValue = libpanda._inPlRE2xdAO(self.this, parameter1)
            return returnValue

        
        def isSane(self):
            returnValue = libpanda._inPlRE2l6kl(self.this)
            return returnValue

        
        def sanityCheck(self):
            returnValue = libpanda._inPlRE2Ter_(self.this)
            return returnValue

        
        def getPrivateHandler(self):
            returnValue = libpanda._inPlRE2EsRk(self.this)
            returnObject = EventHandler.EventHandler(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def addLabel(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], GuiLabel.GuiLabel):
                    return self.overloaded_addLabel_ptrGuiManager_ptrGuiLabel(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiLabel.GuiLabel> '
            elif numArgs == 2:
                if isinstance(_args[0], GuiLabel.GuiLabel):
                    if isinstance(_args[1], Node.Node):
                        return self.overloaded_addLabel_ptrGuiManager_ptrGuiLabel_ptrNode(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Node.Node> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GuiLabel.GuiLabel> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['GuiManager'] = GuiManager

