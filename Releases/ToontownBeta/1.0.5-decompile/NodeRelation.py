# Source Generated with Decompyle++
# File: NodeRelation.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
import Node
import TypeHandle
import NodeTransition
import NodeTransitions
import UpdateSeq
import BoundedObject
import ReferenceCount
import TypedWritableReferenceCount
import BoundingVolume
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import ReferenceCount
import TypeHandle
import TypedWritableReferenceCount
import ReferenceCount
import TypeHandle
import Writable
import TypedWritable
import BoundedObject
import BoundingVolume
import TypeHandle
classDefined = 0

def generateClass_NodeRelation():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NodeRelation(TypedWritableReferenceCount.TypedWritableReferenceCount, BoundedObject.BoundedObject, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPs9JI9Jmk:
                libpanda._inPs9JI9Jmk(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPs9JIeQ1i()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getStashedType():
            returnValue = libpanda._inPs9JI0__d()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getStashedType = PandaStatic.PandaStatic(getStashedType)
        
        def output(self, out):
            returnValue = libpanda._inPs9JILreV(self.this, out.this)
            return returnValue

        
        def outputTransitions(self, out):
            returnValue = libpanda._inPs9JIJpMg(self.this, out.this)
            return returnValue

        
        def overloaded_writeTransitions_ptrConstNodeRelation_ptrOstream_int(self, out, indent):
            returnValue = libpanda._inPs9JIGTG3(self.this, out.this, indent)
            return returnValue

        
        def overloaded_writeTransitions_ptrConstNodeRelation_ptrOstream(self, out):
            returnValue = libpanda._inPs9JIYgHC(self.this, out.this)
            return returnValue

        
        def getParent(self):
            returnValue = libpanda._inPs9JINHP9(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getChild(self):
            returnValue = libpanda._inPs9JIeM77(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getSort(self):
            returnValue = libpanda._inPs9JIVqPR(self.this)
            return returnValue

        
        def getGraphType(self):
            returnValue = libpanda._inPs9JIEQrM(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def isAttached(self):
            returnValue = libpanda._inPs9JI4Mtj(self.this)
            return returnValue

        
        def refParent(self):
            returnValue = libpanda._inPs9JIqTbK(self.this)
            return returnValue

        
        def unrefParent(self):
            returnValue = libpanda._inPs9JIBo3x(self.this)
            return returnValue

        
        def overloaded_changeParent_ptrNodeRelation_ptrNode(self, parent):
            returnValue = libpanda._inPs9JI1AM4(self.this, parent.this)
            return returnValue

        
        def overloaded_changeParent_ptrNodeRelation_ptrNode_int(self, parent, sort):
            returnValue = libpanda._inPs9JIJ00X(self.this, parent.this, sort)
            return returnValue

        
        def changeChild(self, child):
            returnValue = libpanda._inPs9JIzG_h(self.this, child.this)
            return returnValue

        
        def changeParentAndChild(self, parent, child):
            returnValue = libpanda._inPs9JIYoD6(self.this, parent.this, child.this)
            return returnValue

        
        def setSort(self, sort):
            returnValue = libpanda._inPs9JIHWft(self.this, sort)
            return returnValue

        
        def setGraphType(self, graphType):
            returnValue = libpanda._inPs9JIxQx4(self.this, graphType.this)
            return returnValue

        
        def overloaded_setTransition_ptrNodeRelation_ptrTypeHandle_ptrNodeTransition(self, handle, trans):
            returnValue = libpanda._inPs9JIK8Ww(self.this, handle.this, trans.this)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setTransition_ptrNodeRelation_ptrNodeTransition(self, trans):
            returnValue = libpanda._inPs9JIdqgB(self.this, trans.this)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setTransition_ptrNodeRelation_ptrNodeTransition_int(self, trans, priority):
            returnValue = libpanda._inPs9JIntYU(self.this, trans.this, priority)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearTransition(self, handle):
            returnValue = libpanda._inPs9JIOlIK(self.this, handle.this)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def hasTransition(self, handle):
            returnValue = libpanda._inPs9JIrZwd(self.this, handle.this)
            return returnValue

        
        def hasAnyTransition(self):
            returnValue = libpanda._inPs9JIx2dS(self.this)
            return returnValue

        
        def getTransition(self, handle):
            returnValue = libpanda._inPs9JIsXOz(self.this, handle.this)
            returnObject = NodeTransition.NodeTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_copyTransitionsFrom_ptrNodeRelation_ptrConstNodeRelation(self, arc):
            returnValue = libpanda._inPs9JIIar4(self.this, arc.this)
            return returnValue

        
        def overloaded_composeTransitionsFrom_ptrNodeRelation_ptrConstNodeRelation(self, arc):
            returnValue = libpanda._inPs9JIkY7n(self.this, arc.this)
            return returnValue

        
        def overloaded_copyTransitionsFrom_ptrNodeRelation_ptrConstNodeTransitions(self, trans):
            returnValue = libpanda._inPs9JIZily(self.this, trans.this)
            return returnValue

        
        def overloaded_composeTransitionsFrom_ptrNodeRelation_ptrConstNodeTransitions(self, trans):
            returnValue = libpanda._inPs9JIC6Cp(self.this, trans.this)
            return returnValue

        
        def adjustAllPriorities(self, adjustment):
            returnValue = libpanda._inPs9JIoMBz(self.this, adjustment)
            return returnValue

        
        def compareTransitionsTo(self, arc):
            returnValue = libpanda._inPs9JIkf0f(self.this, arc.this)
            return returnValue

        
        def getLastUpdate(self):
            returnValue = libpanda._inPs9JIasri(self.this)
            returnObject = UpdateSeq.UpdateSeq(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def clearWrtCache(self):
            returnValue = libpanda._inPs9JIyqN1(self.this)
            return returnValue

        
        def upcastToBoundedObject(self):
            returnValue = libpanda._inPs9JI1_qj(self.this)
            returnObject = BoundedObject.BoundedObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpanda._inPflbod2f_(upcastSelf.this)
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

        
        def setTransition(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodeTransition.NodeTransition):
                    return self.overloaded_setTransition_ptrNodeRelation_ptrNodeTransition(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodeTransition.NodeTransition> '
            elif numArgs == 2:
                if isinstance(_args[0], TypeHandle.TypeHandle):
                    if isinstance(_args[1], NodeTransition.NodeTransition):
                        return self.overloaded_setTransition_ptrNodeRelation_ptrTypeHandle_ptrNodeTransition(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <NodeTransition.NodeTransition> '
                elif isinstance(_args[0], NodeTransition.NodeTransition):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setTransition_ptrNodeRelation_ptrNodeTransition_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle.TypeHandle> <NodeTransition.NodeTransition> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def copyTransitionsFrom(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodeTransitions.NodeTransitions):
                    return self.overloaded_copyTransitionsFrom_ptrNodeRelation_ptrConstNodeTransitions(_args[0])
                elif isinstance(_args[0], NodeRelation):
                    return self.overloaded_copyTransitionsFrom_ptrNodeRelation_ptrConstNodeRelation(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodeTransitions.NodeTransitions> <NodeRelation> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def changeParent(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Node.Node):
                    return self.overloaded_changeParent_ptrNodeRelation_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            elif numArgs == 2:
                if isinstance(_args[0], Node.Node):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_changeParent_ptrNodeRelation_ptrNode_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def writeTransitions(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_writeTransitions_ptrConstNodeRelation_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_writeTransitions_ptrConstNodeRelation_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def composeTransitionsFrom(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodeTransitions.NodeTransitions):
                    return self.overloaded_composeTransitionsFrom_ptrNodeRelation_ptrConstNodeTransitions(_args[0])
                elif isinstance(_args[0], NodeRelation):
                    return self.overloaded_composeTransitionsFrom_ptrNodeRelation_ptrConstNodeRelation(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodeTransitions.NodeTransitions> <NodeRelation> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '


    globals()['NodeRelation'] = NodeRelation

