# Source Generated with Decompyle++
# File: NurbsCurve.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import ParametricCurve
import NurbsCurveInterface
import TypeHandle
import VBase3
import VBase4
import Ostream
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
import ParametricCurve
import VBase3
import Filename
import Ostream
import TypeHandle
import PiecewiseCurve
import TypeHandle
import NurbsCurveInterface
import VBase3
import VBase4
import Ostream
import TypeHandle
classDefined = 0

def generateClass_NurbsCurve():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NurbsCurve(PiecewiseCurve.PiecewiseCurve, NurbsCurveInterface.NurbsCurveInterface, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPHc9W8ax5()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstParametricCurve(self, pc):
            self.this = libpanda._inPHc9W_ZYT(pc.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHc9WdFtC:
                libpanda._inPHc9WdFtC(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHc9WAWVd()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def upcastToNurbsCurveInterface(self):
            returnValue = libpanda._inPHc9Wex1R(self.this)
            returnObject = NurbsCurveInterface.NurbsCurveInterface(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isValid(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9WZdM7(upcastSelf.this)
            return returnValue

        
        def getMaxT(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9WTB4O(upcastSelf.this)
            return returnValue

        
        def setCurveType(self, type):
            upcastSelf = self
            returnValue = libpanda._inPHc9WnAfd(upcastSelf.this, type)
            return returnValue

        
        def getCurveType(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9WnpVX(upcastSelf.this)
            return returnValue

        
        def setNumDimensions(self, num):
            upcastSelf = self
            returnValue = libpanda._inPHc9WDI0T(upcastSelf.this, num)
            return returnValue

        
        def getNumDimensions(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9Wed71(upcastSelf.this)
            return returnValue

        
        def overloaded_calcLength_ptrConstParametricCurve(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9WUqeF(upcastSelf.this)
            return returnValue

        
        def overloaded_calcLength_ptrConstParametricCurve_float_float(self, _from, to):
            upcastSelf = self
            returnValue = libpanda._inPHc9W6hNZ(upcastSelf.this, _from, to)
            return returnValue

        
        def findLength(self, startT, lengthOffset):
            upcastSelf = self
            returnValue = libpanda._inPHc9W_LMm(upcastSelf.this, startT, lengthOffset)
            return returnValue

        
        def getPoint(self, t, point):
            upcastSelf = self
            returnValue = libpanda._inPHc9WhTPE(upcastSelf.this, t, point.this)
            return returnValue

        
        def getTangent(self, t, tangent):
            upcastSelf = self
            returnValue = libpanda._inPHc9W_cs0(upcastSelf.this, t, tangent.this)
            return returnValue

        
        def getPt(self, t, point, tangent):
            upcastSelf = self
            returnValue = libpanda._inPHc9WIoPy(upcastSelf.this, t, point.this, tangent.this)
            return returnValue

        
        def get2ndtangent(self, t, tangent2):
            upcastSelf = self
            returnValue = libpanda._inPHc9WIPja(upcastSelf.this, t, tangent2.this)
            return returnValue

        
        def adjustPoint(self, t, px, py, pz):
            upcastSelf = self
            returnValue = libpanda._inPHc9WzJWs(upcastSelf.this, t, px, py, pz)
            return returnValue

        
        def adjustTangent(self, t, tx, ty, tz):
            upcastSelf = self
            returnValue = libpanda._inPHc9WclxE(upcastSelf.this, t, tx, ty, tz)
            return returnValue

        
        def adjustPt(self, t, px, py, pz, tx, ty, tz):
            upcastSelf = self
            returnValue = libpanda._inPHc9Wq0cM(upcastSelf.this, t, px, py, pz, tx, ty, tz)
            return returnValue

        
        def recompute(self):
            upcastSelf = self
            returnValue = libpanda._inPHc9Wgg_o(upcastSelf.this)
            return returnValue

        
        def stitch(self, a, b):
            upcastSelf = self
            returnValue = libpanda._inPHc9WDE8P(upcastSelf.this, a.this, b.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(self, filename, cs):
            upcastSelf = self
            returnValue = libpanda._inPHc9W4EHa(upcastSelf.this, filename.this, cs)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrFilename(self, filename):
            upcastSelf = self
            returnValue = libpanda._inPHc9WqZwA(upcastSelf.this, filename.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
            upcastSelf = self
            returnValue = libpanda._inPHc9Wohju(upcastSelf.this, out.this, filename.this, cs)
            return returnValue

        
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

        
        def setOrder(self, order):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WE7K6(upcastSelf.this, order)
            return returnValue

        
        def getOrder(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WbpY_(upcastSelf.this)
            return returnValue

        
        def getNumCvs(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WP0qD(upcastSelf.this)
            return returnValue

        
        def getNumKnots(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WFq5_(upcastSelf.this)
            return returnValue

        
        def insertCv(self, t):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9W1scU(upcastSelf.this, t)
            return returnValue

        
        def overloaded_appendCv_ptrNurbsCurveInterface_float_float_float(self, x, y, z):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9W6QaR(upcastSelf.this, x, y, z)
            return returnValue

        
        def overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase3f(self, v):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wh5Ti(upcastSelf.this, v.this)
            return returnValue

        
        def overloaded_appendCv_ptrNurbsCurveInterface_ptrConstLVecBase4f(self, v):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WZmdi(upcastSelf.this, v.this)
            return returnValue

        
        def removeCv(self, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wna5o(upcastSelf.this, n)
            return returnValue

        
        def removeAllCvs(self):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wunej(upcastSelf.this)
            return returnValue

        
        def overloaded_setCvPoint_ptrNurbsCurveInterface_int_float_float_float(self, n, x, y, z):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wo1Uc(upcastSelf.this, n, x, y, z)
            return returnValue

        
        def overloaded_setCvPoint_ptrNurbsCurveInterface_int_ptrConstLVecBase3f(self, n, v):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WtRa_(upcastSelf.this, n, v.this)
            return returnValue

        
        def getCvPoint(self, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WDfJB(upcastSelf.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setCvWeight(self, n, w):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wd6Wd(upcastSelf.this, n, w)
            return returnValue

        
        def getCvWeight(self, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WJ6DH(upcastSelf.this, n)
            return returnValue

        
        def setCv(self, n, v):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9Wllws(upcastSelf.this, n, v.this)
            return returnValue

        
        def getCv(self, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9W4tRe(upcastSelf.this, n)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setKnot(self, n, t):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9W8AS8(upcastSelf.this, n, t)
            return returnValue

        
        def getKnot(self, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9W3mjW(upcastSelf.this, n)
            return returnValue

        
        def writeCv(self, out, n):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNurbsCurveInterface()
            returnValue = libpanda._inPHc9WzMcU(upcastSelf.this, out.this, n)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], ParametricCurve.ParametricCurve):
                    return self.overloaded_constructor_ptrConstParametricCurve(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <ParametricCurve.ParametricCurve> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['NurbsCurve'] = NurbsCurve

