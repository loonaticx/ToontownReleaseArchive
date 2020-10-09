# Source Generated with Decompyle++
# File: SequenceNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TimedCycle
import TypeHandle
import SwitchNodeOne
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
import SwitchNode
import TypeHandle
import SwitchNodeOne
import TypeHandle
import TimedCycle
classDefined = 0

def generateClass_SequenceNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class SequenceNode(SwitchNodeOne.SwitchNodeOne, TimedCycle.TimedCycle, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, initialName):
            self.this = libpanda._inPVub0EFFS(initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVub0grOA()
            self.userManagesMemory = 1

        
        def overloaded_constructor_float_atomicstring(self, switchTime, initialName):
            self.this = libpanda._inPVub0q6As(switchTime, initialName)
            self.userManagesMemory = 1

        
        def overloaded_constructor_float(self, switchTime):
            self.this = libpanda._inPVub05GbK(switchTime)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPVub04V8X:
                libpanda._inPVub04V8X(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPVub0Gj9E()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setSwitchTime(self, switchTime):
            returnValue = libpanda._inPVub0OuB9(self.this, switchTime)
            return returnValue

        
        def upcastToTimedCycle(self):
            returnValue = libpanda._inPVub0PJOa(self.this)
            returnObject = TimedCycle.TimedCycle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def assign(self, copy):
            upcastSelf = self
            returnValue = libpanda._inPVub0ZqFj(upcastSelf.this, copy.this)
            returnObject = SwitchNodeOne.SwitchNodeOne(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def assign(self, copy):
            upcastSelf = self
            returnValue = libpanda._inPAJa76Xl2(upcastSelf.this, copy.this)
            returnObject = SwitchNode.SwitchNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def upcastToNamable(self):
            upcastSelf = self
            returnValue = libpanda._inPs9JIno_M(upcastSelf.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumParents(self, type):
            upcastSelf = self
            returnValue = libpanda._inPs9JIYyPA(upcastSelf.this, type.this)
            return returnValue

        
        def getParent(self, type, index):
            upcastSelf = self
            returnValue = libpanda._inPs9JIUDMq(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumChildren(self, type):
            upcastSelf = self
            returnValue = libpanda._inPs9JI4P8C(upcastSelf.this, type.this)
            return returnValue

        
        def getChild(self, type, index):
            upcastSelf = self
            returnValue = libpanda._inPs9JI7VEc(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def output(self, out):
            upcastSelf = self
            returnValue = libpanda._inPs9JIk2tf(upcastSelf.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream_int(self, out, indentLevel):
            upcastSelf = self
            returnValue = libpanda._inPs9JI8GS7(upcastSelf.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream(self, out):
            upcastSelf = self
            returnValue = libpanda._inPs9JIMU__(upcastSelf.this, out.this)
            return returnValue

        
        def upcastToBoundedObject(self):
            upcastSelf = self
            returnValue = libpanda._inPs9JITXbS(upcastSelf.this)
            returnObject = BoundedObject.BoundedObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpanda._inPs9JIJBIE(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToWritable(self):
            upcastSelf = self
            returnValue = libpanda._inPflbo_8Kt(upcastSelf.this)
            returnObject = Writable.Writable(None)
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

        
        def overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI7U7J(upcastSelf.this, type)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JINvRr(upcastSelf.this, volume.this)
            return returnValue

        
        def getBound(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JImoIb(upcastSelf.this)
            returnObject = BoundingVolume.BoundingVolume(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def markBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI_RvI(upcastSelf.this)
            return returnValue

        
        def forceBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIcPQw(upcastSelf.this)
            return returnValue

        
        def isBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JId0c5(upcastSelf.this)
            return returnValue

        
        def setFinal(self, flag):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIrXwH(upcastSelf.this, flag)
            return returnValue

        
        def isFinal(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIUIM4(upcastSelf.this)
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

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor_float(_args[0])
                elif isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.StringType):
                        return self.overloaded_constructor_float_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['SequenceNode'] = SequenceNode

