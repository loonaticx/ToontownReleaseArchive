# Source Generated with Decompyle++
# File: PGWaitBar.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PGFrameStyle
import TypeHandle
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
import PGItem
import VBase4
import Node
import ArcChain
import PGFrameStyle
import ButtonHandle
import AudioSound
import TextNode
import TypeHandle
classDefined = 0

def generateClass_PGWaitBar():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGWaitBar(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPVvimw6ol(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVvim6caN()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPVvimj5JI()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setup(self, width, height, range):
            returnValue = libpanda._inPVvimX_iW(self.this, width, height, range)
            return returnValue

        
        def setRange(self, range):
            returnValue = libpanda._inPVvimjd51(self.this, range)
            return returnValue

        
        def getRange(self):
            returnValue = libpanda._inPVvimt84i(self.this)
            return returnValue

        
        def setValue(self, value):
            returnValue = libpanda._inPVvimFbDg(self.this, value)
            return returnValue

        
        def getValue(self):
            returnValue = libpanda._inPVvimM5CN(self.this)
            return returnValue

        
        def getPercent(self):
            returnValue = libpanda._inPVvimg0Cx(self.this)
            return returnValue

        
        def setBarStyle(self, style):
            returnValue = libpanda._inPVvimljct(self.this, style.this)
            return returnValue

        
        def getBarStyle(self):
            returnValue = libpanda._inPVvim5J5C(self.this)
            returnObject = PGFrameStyle.PGFrameStyle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
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


    globals()['PGWaitBar'] = PGWaitBar

