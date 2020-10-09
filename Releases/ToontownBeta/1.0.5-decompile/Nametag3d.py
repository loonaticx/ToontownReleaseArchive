# Source Generated with Decompyle++
# File: Nametag3d.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import libpanda
import libpandaDowncasts
import FFIExternalObject
import NamedNode
import TypeHandle
import Nametag
import NametagGroup
import Node
import ReferenceCount
import Namable
import ReferenceCount
import TypeHandle
import Nametag
import NametagGroup
import Node
import TypeHandle
import ReferenceCount
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
classDefined = 0

def generateClass_Nametag3d():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Nametag3d(Nametag.Nametag, NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts,
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
            if libtoontown and libtoontown._inPPj7bx77N:
                libtoontown._inPPj7bx77N(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPPj7bgugM()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setBillboardOffset(self, billboardOffset):
            returnValue = libtoontown._inPPj7bBRIg(self.this, billboardOffset)
            return returnValue

        
        def getBillboardOffset(self):
            returnValue = libtoontown._inPPj7bNVEo(self.this)
            return returnValue

        
        def upcastToNamedNode(self):
            returnValue = libtoontown._inPPj7bVuLN(self.this)
            returnObject = NamedNode.NamedNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setContents(self, flags):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bEeaT(upcastSelf.this, flags)
            return returnValue

        
        def getContents(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bCegG(upcastSelf.this)
            return returnValue

        
        def setActive(self, active):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bLFzD(upcastSelf.this, active)
            return returnValue

        
        def isActive(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bhm1i(upcastSelf.this)
            return returnValue

        
        def hasGroup(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bMiee(upcastSelf.this)
            return returnValue

        
        def getGroup(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bU9Np(upcastSelf.this)
            returnObject = NametagGroup.NametagGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setDrawOrder(self, drawOrder):
            upcastSelf = self
            returnValue = libtoontown._inPPj7batHf(upcastSelf.this, drawOrder)
            return returnValue

        
        def clearDrawOrder(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7b_Mq7(upcastSelf.this)
            return returnValue

        
        def setChatWordwrap(self, wordwrap):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bfcNR(upcastSelf.this, wordwrap)
            return returnValue

        
        def getChatWordwrap(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bb3ZX(upcastSelf.this)
            return returnValue

        
        def setAvatarNode(self, node):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bnq5m(upcastSelf.this, node.this)
            return returnValue

        
        def clearAvatarNode(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bBm0m(upcastSelf.this)
            return returnValue

        
        def getAvatarNode(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bTt6d(upcastSelf.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getType(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bK3Xg(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libtoontown._inPPj7bd6q5(upcastSelf.this)
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

        
        def upcastToNamable(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIno_M(upcastSelf.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumParents(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIYyPA(upcastSelf.this, type.this)
            return returnValue

        
        def getParent(self, type, index):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIUDMq(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumChildren(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JI4P8C(upcastSelf.this, type.this)
            return returnValue

        
        def getChild(self, type, index):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JI7VEc(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIk2tf(upcastSelf.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream_int(self, out, indentLevel):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JI8GS7(upcastSelf.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIMU__(upcastSelf.this, out.this)
            return returnValue

        
        def upcastToBoundedObject(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JITXbS(upcastSelf.this)
            returnObject = BoundedObject.BoundedObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPs9JIJBIE(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToWritable(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpanda._inPflbo_8Kt(upcastSelf.this)
            returnObject = Writable.Writable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getType(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpandaexpress._inPKoxtuIyI(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getTypeIndex(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpandaexpress._inPKoxtfVBU(upcastSelf.this)
            return returnValue

        
        def isOfType(self, handle):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpandaexpress._inPKoxtgfKt(upcastSelf.this, handle.this)
            return returnValue

        
        def isExactType(self, handle):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            returnValue = libpandaexpress._inPKoxt0xzz(upcastSelf.this, handle.this)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI7U7J(upcastSelf.this, type)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JINvRr(upcastSelf.this, volume.this)
            return returnValue

        
        def getBound(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
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
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI_RvI(upcastSelf.this)
            return returnValue

        
        def forceBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIcPQw(upcastSelf.this)
            return returnValue

        
        def isBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JId0c5(upcastSelf.this)
            return returnValue

        
        def setFinal(self, flag):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIrXwH(upcastSelf.this, flag)
            return returnValue

        
        def isFinal(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIUIM4(upcastSelf.this)
            return returnValue

        
        def getRefCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtIP2_(upcastSelf.this)
            return returnValue

        
        def ref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtTs5_(upcastSelf.this)
            return returnValue

        
        def unref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtpMWy(upcastSelf.this)
            return returnValue

        
        def testRefCountIntegrity(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtoDk2(upcastSelf.this)
            return returnValue

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setName(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtEnBW(upcastSelf.this, name)
            return returnValue

        
        def clearName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtSJVl(upcastSelf.this)
            return returnValue

        
        def hasName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtR9hC(upcastSelf.this)
            return returnValue

        
        def getName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtYaRN(upcastSelf.this)
            return returnValue

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamedNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxthN8q(upcastSelf.this, out.this)
            return returnValue


    globals()['Nametag3d'] = Nametag3d

