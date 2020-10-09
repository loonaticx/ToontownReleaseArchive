# Source Generated with Decompyle++
# File: GuiBehavior.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GuiItem
import TypeHandle
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
import GuiItem
import GuiManager
import EventHandler
import Node
import Vec3
import GuiLabel
import Vec4
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
classDefined = 0

def generateClass_GuiBehavior():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GuiBehavior(GuiItem.GuiItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        import TypeHandle
        import TypedObject
        import TypeHandle
        import ReferenceCount
        import TypeHandle
        import TypedReferenceCount
        import ReferenceCount
        import TypeHandle
        import TypedObject
        
        class BehaviorFunctor(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
                

            
            def getClassType():
                returnValue = libpanda._inPlRE2zt3_()
                returnObject = TypeHandle.TypeHandle(None)
                returnObject.this = returnValue
                if returnObject.this == 0:
                    return None
                
                returnObject.userManagesMemory = 1
                return returnObject

            getClassType = PandaStatic.PandaStatic(getClassType)

        
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
            if libpanda and libpanda._inPlRE2Ktya:
                libpanda._inPlRE2Ktya(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPlRE2d872()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def startBehavior(self):
            returnValue = libpanda._inPlRE25PwJ(self.this)
            return returnValue

        
        def stopBehavior(self):
            returnValue = libpanda._inPlRE2G1Dg(self.this)
            return returnValue

        
        def resetBehavior(self):
            returnValue = libpanda._inPlRE2oxd5(self.this)
            return returnValue


    globals()['GuiBehavior'] = GuiBehavior

