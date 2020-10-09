# Source Generated with Decompyle++
# File: DataValve.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TypeHandle
import ModifierButtons
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import BoundedObject
import BoundingVolume
import TypeHandle
import ReferenceCount
import TypeHandle
import Node
import TypeHandle
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import Writable
import TypedWritable
import BoundingVolume
import Namable
import Ostream
import TypeHandle
import NamedNode
import Namable
import TypeHandle
import Node
import NodeRelation
import Ostream
import BoundedObject
import ReferenceCount
import DataNode
import TypeHandle
classDefined = 0

def generateClass_DataValve():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class DataValve(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        import ModifierButtons
        import DataValve
        import Ostream
        import ReferenceCount
        import TypeHandle
        
        class Control(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
            __CModuleDowncasts__ = [
                libpandaDowncasts,
                libpandaexpressDowncasts]
            
            def __init__(self, *_args):
                FFIExternalObject.FFIExternalObject.__init__(self)
                if len(_args) == 1 and _args[0] == None:
                    return None
                
                apply(self.constructor, _args)

            
            def constructor(self):
                self.this = libpanda._inPyiw5kV5K()
                self.userManagesMemory = 1

            
            def __del__(self):
                if self.userManagesMemory and self.this != 0:
                    self.destructor()
                

            
            def destructor(self):
                if libpanda and libpanda._inPyiw5LyPx:
                    libpanda._inPyiw5LyPx(self.this)
                

            
            def setOn(self):
                returnValue = libpanda._inPyiw5rS0o(self.this)
                return returnValue

            
            def setOff(self):
                returnValue = libpanda._inPyiw5gOzp(self.this)
                return returnValue

            
            def setButtons(self, mods):
                returnValue = libpanda._inPyiw59Z8h(self.this, mods.this)
                return returnValue

            
            def isOn(self, valve):
                returnValue = libpanda._inPyiw5nyjy(self.this, valve.this)
                return returnValue

            
            def output(self, out):
                returnValue = libpanda._inPyiw5oTUm(self.this, out.this)
                return returnValue


        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPyiw51M8y(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPyiw5_Ova()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPyiw58s_p()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setDefaultControl(self, control):
            returnValue = libpanda._inPyiw5AtdC(self.this, control.this)
            return returnValue

        
        def getDefaultControl(self):
            returnValue = libpanda._inPyiw5Fj8M(self.this)
            returnObject = DataValve.Control(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setControl(self, childIndex, control):
            returnValue = libpanda._inPyiw5L8n7(self.this, childIndex, control.this)
            return returnValue

        
        def clearControl(self, childIndex):
            returnValue = libpanda._inPyiw5lQr_(self.this, childIndex)
            return returnValue

        
        def hasControl(self, childIndex):
            returnValue = libpanda._inPyiw5QIxN(self.this, childIndex)
            return returnValue

        
        def getControl(self, childIndex):
            returnValue = libpanda._inPyiw5cdRH(self.this, childIndex)
            returnObject = DataValve.Control(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFineControl(self, childIndex, dataType, control):
            returnValue = libpanda._inPyiw5RNat(self.this, childIndex, dataType.this, control.this)
            return returnValue

        
        def clearFineControl(self, childIndex, dataType):
            returnValue = libpanda._inPyiw5iwl_(self.this, childIndex, dataType.this)
            return returnValue

        
        def hasFineControl(self, childIndex, dataType):
            returnValue = libpanda._inPyiw5gpAE(self.this, childIndex, dataType.this)
            return returnValue

        
        def getFineControl(self, childIndex, dataType):
            returnValue = libpanda._inPyiw5VSh9(self.this, childIndex, dataType.this)
            returnObject = DataValve.Control(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setModifierButtons(self, mods):
            returnValue = libpanda._inPyiw5Lr6h(self.this, mods.this)
            return returnValue

        
        def getModifierButtons(self):
            returnValue = libpanda._inPyiw5XPed(self.this)
            returnObject = ModifierButtons.ModifierButtons(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['DataValve'] = DataValve

