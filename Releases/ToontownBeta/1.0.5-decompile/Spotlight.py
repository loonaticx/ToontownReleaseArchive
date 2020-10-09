# Source Generated with Decompyle++
# File: Spotlight.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase4
import ProjectionNode
import TypeHandle
import Light
import Ostream
import ReferenceCount
import Projection
import Point3
import ReferenceCount
import TypeHandle
import Light
import VBase4
import Ostream
import ReferenceCount
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
import ProjectionNode
import Projection
import Point3
import TypeHandle
classDefined = 0

def generateClass_Spotlight():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Spotlight(Light.Light, ProjectionNode.ProjectionNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPi0oLCnYH(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPi0oLk4Lv()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPi0oL34_q:
                libpanda._inPi0oL34_q(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPi0oLcBIs()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getExponent(self):
            returnValue = libpanda._inPi0oLr_CB(self.this)
            return returnValue

        
        def setExponent(self, exponent):
            returnValue = libpanda._inPi0oLRqlj(self.this, exponent)
            return returnValue

        
        def getCutoffAngle(self):
            returnValue = libpanda._inPi0oLz4p5(self.this)
            return returnValue

        
        def getSpecular(self):
            returnValue = libpanda._inPi0oLJxHE(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setSpecular(self, color):
            returnValue = libpanda._inPi0oLKpgk(self.this, color.this)
            return returnValue

        
        def getConstantAttenuation(self):
            returnValue = libpanda._inPi0oLd_E8(self.this)
            return returnValue

        
        def setConstantAttenuation(self, att):
            returnValue = libpanda._inPi0oLBsCH(self.this, att)
            return returnValue

        
        def getLinearAttenuation(self):
            returnValue = libpanda._inPi0oLLIVU(self.this)
            return returnValue

        
        def setLinearAttenuation(self, att):
            returnValue = libpanda._inPi0oLnUkG(self.this, att)
            return returnValue

        
        def getQuadraticAttenuation(self):
            returnValue = libpanda._inPi0oLBlWQ(self.this)
            return returnValue

        
        def setQuadraticAttenuation(self, att):
            returnValue = libpanda._inPi0oL6xKj(self.this, att)
            return returnValue

        
        def upcastToProjectionNode(self):
            returnValue = libpanda._inPi0oL3pDg(self.this)
            returnObject = ProjectionNode.ProjectionNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getColor(self):
            upcastSelf = self
            returnValue = libpanda._inPi0oLef_a(upcastSelf.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setColor(self, color):
            upcastSelf = self
            returnValue = libpanda._inPi0oL0ZiL(upcastSelf.this, color.this)
            return returnValue

        
        def output(self, out):
            upcastSelf = self
            returnValue = libpanda._inPi0oLcV0W(upcastSelf.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstLight_ptrOstream_int(self, out, indentLevel):
            upcastSelf = self
            returnValue = libpanda._inPi0oLC8aI(upcastSelf.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstLight_ptrOstream(self, out):
            upcastSelf = self
            returnValue = libpanda._inPi0oLMuhe(upcastSelf.this, out.this)
            return returnValue

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpanda._inPi0oLjiAk(upcastSelf.this)
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

        
        def setProjection(self, projection):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7I4R8(upcastSelf.this, projection.this)
            return returnValue

        
        def shareProjection(self, projection):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7Lh7k(upcastSelf.this, projection.this)
            return returnValue

        
        def getProjection(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7Cj_V(upcastSelf.this)
            returnObject = Projection.Projection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def isInView(self, pos):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7phri(upcastSelf.this, pos.this)
            return returnValue

        
        def getHfov(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7Hg5g(upcastSelf.this)
            return returnValue

        
        def getVfov(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7nILl(upcastSelf.this)
            return returnValue

        
        def overloaded_setFov_ptrProjectionNode_float(self, hfov):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7MCcT(upcastSelf.this, hfov)
            return returnValue

        
        def overloaded_setFov_ptrProjectionNode_float_float(self, hfov, vfov):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7qQe0(upcastSelf.this, hfov, vfov)
            return returnValue

        
        def setHfov(self, hfov):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7yd2C(upcastSelf.this, hfov)
            return returnValue

        
        def setVfov(self, vfov):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7SyHH(upcastSelf.this, vfov)
            return returnValue

        
        def getAspect(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7aXUW(upcastSelf.this)
            return returnValue

        
        def setAspect(self, aspect):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7odQ_(upcastSelf.this, aspect)
            return returnValue

        
        def setNearFar(self, cnear, cfar):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7tvHd(upcastSelf.this, cnear, cfar)
            return returnValue

        
        def getNear(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7qZ2K(upcastSelf.this)
            return returnValue

        
        def setNear(self, cnear):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7M9ys(upcastSelf.this, cnear)
            return returnValue

        
        def getFar(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7WVMp(upcastSelf.this)
            return returnValue

        
        def setFar(self, cfar):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPAJa7GSAp(upcastSelf.this, cfar)
            return returnValue

        
        def upcastToNamable(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIno_M(upcastSelf.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNumParents(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIYyPA(upcastSelf.this, type.this)
            return returnValue

        
        def getParent(self, type, index):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIUDMq(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumChildren(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JI4P8C(upcastSelf.this, type.this)
            return returnValue

        
        def getChild(self, type, index):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JI7VEc(upcastSelf.this, type.this, index)
            returnObject = NodeRelation.NodeRelation(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIk2tf(upcastSelf.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream_int(self, out, indentLevel):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JI8GS7(upcastSelf.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstNode_ptrOstream(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIMU__(upcastSelf.this, out.this)
            return returnValue

        
        def upcastToBoundedObject(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JITXbS(upcastSelf.this)
            returnObject = BoundedObject.BoundedObject(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPs9JIJBIE(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToWritable(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpanda._inPflbo_8Kt(upcastSelf.this)
            returnObject = Writable.Writable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getType(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpandaexpress._inPKoxtuIyI(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getTypeIndex(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpandaexpress._inPKoxtfVBU(upcastSelf.this)
            return returnValue

        
        def isOfType(self, handle):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpandaexpress._inPKoxtgfKt(upcastSelf.this, handle.this)
            return returnValue

        
        def isExactType(self, handle):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            returnValue = libpandaexpress._inPKoxt0xzz(upcastSelf.this, handle.this)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject___enum__BoundingVolumeType(self, type):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI7U7J(upcastSelf.this, type)
            return returnValue

        
        def overloaded_setBound_ptrBoundedObject_ptrConstBoundingVolume(self, volume):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JINvRr(upcastSelf.this, volume.this)
            return returnValue

        
        def getBound(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
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
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JI_RvI(upcastSelf.this)
            return returnValue

        
        def forceBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIcPQw(upcastSelf.this)
            return returnValue

        
        def isBoundStale(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JId0c5(upcastSelf.this)
            return returnValue

        
        def setFinal(self, flag):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIrXwH(upcastSelf.this, flag)
            return returnValue

        
        def isFinal(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToBoundedObject()
            returnValue = libpanda._inPs9JIUIM4(upcastSelf.this)
            return returnValue

        
        def getRefCount(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtIP2_(upcastSelf.this)
            return returnValue

        
        def ref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtTs5_(upcastSelf.this)
            return returnValue

        
        def unref(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtpMWy(upcastSelf.this)
            return returnValue

        
        def testRefCountIntegrity(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToReferenceCount()
            returnValue = libpandaexpress._inPKoxtoDk2(upcastSelf.this)
            return returnValue

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setName(self, name):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtEnBW(upcastSelf.this, name)
            return returnValue

        
        def clearName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtSJVl(upcastSelf.this)
            return returnValue

        
        def hasName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtR9hC(upcastSelf.this)
            return returnValue

        
        def getName(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtYaRN(upcastSelf.this)
            return returnValue

        
        def output(self, out):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToProjectionNode()
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxthN8q(upcastSelf.this, out.this)
            return returnValue

        
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


    globals()['Spotlight'] = Spotlight

