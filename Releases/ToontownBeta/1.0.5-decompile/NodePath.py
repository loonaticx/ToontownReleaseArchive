# Source Generated with Decompyle++
# File: NodePath.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import TypeHandle
import Node
import NodeRelation
import ArcChain
import NodePathCollection
import Ostream
import AllTransitionsWrapper
import VBase3
import Point3
import Mat4
import VBase4
import Vec3
import Texture
import Material
import Fog
import GraphicsStateGuardianBase
import BoundingVolume
import ArcChain
import Node
import NodeRelation
import TypeHandle
classDefined = 0

def generateClass_NodePath():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NodePath(ArcChain.ArcChain, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        ETNotFound = 1
        ETOk = 0
        ETRemoved = 2
        ETFail = 3
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrTypeHandle(self, graphType):
            self.this = libpanda._inPbPIPlV8x(graphType.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPbPIPWL_g()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNode_ptrTypeHandle(self, topNode, graphType):
            self.this = libpanda._inPbPIPUsLP(topNode.this, graphType.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNode(self, topNode):
            self.this = libpanda._inPbPIP_wlR(topNode.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrNodeRelation(self, arc):
            self.this = libpanda._inPbPIPJnMt(arc.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstArcChain_ptrTypeHandle(self, chain, graphType):
            self.this = libpanda._inPbPIP_g5R(chain.this, graphType.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstNodePath(self, copy):
            self.this = libpanda._inPbPIPC0Jj(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPbPIPXxq7:
                libpanda._inPbPIPXxq7(self.this)
            

        
        def notFound():
            returnValue = libpanda._inPbPIPAUHR()
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        notFound = PandaStatic.PandaStatic(notFound)
        
        def removed():
            returnValue = libpanda._inPbPIPVElY()
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        removed = PandaStatic.PandaStatic(removed)
        
        def fail():
            returnValue = libpanda._inPbPIPDJhx()
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        fail = PandaStatic.PandaStatic(fail)
        
        def setMaxSearchDepth(maxSearchDepth):
            returnValue = libpanda._inPbPIP_RGI(maxSearchDepth)
            return returnValue

        setMaxSearchDepth = PandaStatic.PandaStatic(setMaxSearchDepth)
        
        def getMaxSearchDepth():
            returnValue = libpanda._inPbPIPcbwf()
            return returnValue

        getMaxSearchDepth = PandaStatic.PandaStatic(getMaxSearchDepth)
        
        def getClassType():
            returnValue = libpanda._inPbPIPmRxh()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def assign(self, copy):
            returnValue = libpanda._inPbPIPk960(self.this, copy.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def eq(self, other):
            returnValue = libpanda._inPbPIPsil9(self.this, other.this)
            return returnValue

        
        def ne(self, other):
            returnValue = libpanda._inPbPIPKoU9(self.this, other.this)
            return returnValue

        
        def compareTo(self, other):
            returnValue = libpanda._inPbPIPApj2(self.this, other.this)
            return returnValue

        
        def setGraphType(self, graphType):
            returnValue = libpanda._inPbPIPuMUB(self.this, graphType.this)
            return returnValue

        
        def getGraphType(self):
            returnValue = libpanda._inPbPIPFWl_(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_extendBy_ptrNodePath_ptrNode(self, dnode):
            returnValue = libpanda._inPbPIPN3ci(self.this, dnode.this)
            return returnValue

        
        def overloaded_extendBy_ptrNodePath_ptrNodeRelation(self, darc):
            returnValue = libpanda._inPbPIPWYdX(self.this, darc.this)
            return returnValue

        
        def overloaded_extendBy_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPYthU(self.this, other.this)
            return returnValue

        
        def overloaded_extendBy_ptrNodePath_atomicstring(self, path):
            returnValue = libpanda._inPbPIPlbdz(self.this, path)
            return returnValue

        
        def extendDownTo(self, dnode):
            returnValue = libpanda._inPbPIP2di8(self.this, dnode.this)
            return returnValue

        
        def overloaded_shorten_ptrNodePath_int(self, numNodes):
            returnValue = libpanda._inPbPIP1LSM(self.this, numNodes)
            return returnValue

        
        def overloaded_shorten_ptrNodePath(self):
            returnValue = libpanda._inPbPIP83gX(self.this)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPbPIPiKhV(self.this)
            return returnValue

        
        def getErrorType(self):
            returnValue = libpanda._inPbPIPuVWc(self.this)
            return returnValue

        
        def shareWith(self, other):
            returnValue = libpanda._inPbPIPgYo7(self.this, other.this)
            return returnValue

        
        def verifyConnectivity(self):
            returnValue = libpanda._inPbPIPTDpm(self.this)
            return returnValue

        
        def amputateBadness(self):
            returnValue = libpanda._inPbPIP6tZp(self.this)
            return returnValue

        
        def repairConnectivity(self, top):
            returnValue = libpanda._inPbPIPXQPX(self.this, top.this)
            return returnValue

        
        def getSiblings(self):
            returnValue = libpanda._inPbPIP6HaI(self.this)
            returnObject = NodePathCollection.NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getChildren(self):
            returnValue = libpanda._inPbPIPZ18V(self.this)
            returnObject = NodePathCollection.NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getNumChildren(self):
            returnValue = libpanda._inPbPIPLtCh(self.this)
            return returnValue

        
        def getChild(self, n):
            returnValue = libpanda._inPbPIPTftX(self.this, n)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def hasParent(self):
            returnValue = libpanda._inPbPIPa21w(self.this)
            return returnValue

        
        def getParent(self):
            returnValue = libpanda._inPbPIP81oI(self.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def findPathDownTo(self, dnode):
            returnValue = libpanda._inPbPIPCT7t(self.this, dnode.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def find(self, path):
            returnValue = libpanda._inPbPIPHXAc(self.this, path)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def findAllPathsDownTo(self, dnode):
            returnValue = libpanda._inPbPIPOrxr(self.this, dnode.this)
            returnObject = NodePathCollection.NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def findAllMatches(self, path):
            returnValue = libpanda._inPbPIPnDIP(self.this, path)
            returnObject = NodePathCollection.NodePathCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def findSingularTransform(self):
            returnValue = libpanda._inPbPIPE7gJ(self.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
            returnValue = libpanda._inPbPIPxwHK(self.this, other.this, sort)
            return returnValue

        
        def overloaded_reparentTo_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPsGzP(self.this, other.this)
            return returnValue

        
        def overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(self, other, sort):
            returnValue = libpanda._inPbPIPeB8s(self.this, other.this, sort)
            return returnValue

        
        def overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPpfTN(self.this, other.this)
            return returnValue

        
        def overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
            returnValue = libpanda._inPbPIPvmo6(self.this, other.this, sort)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPM_PD(self.this, other.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(self, other, sort):
            returnValue = libpanda._inPbPIPqtlc(self.this, other.this, sort)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPmi_l(self.this, other.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_attachNewNode_ptrConstNodePath_ptrNode_int(self, dnode, sort):
            returnValue = libpanda._inPbPIPvhrM(self.this, dnode.this, sort)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_attachNewNode_ptrConstNodePath_ptrNode(self, dnode):
            returnValue = libpanda._inPbPIPmL_k(self.this, dnode.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(self, name, sort):
            returnValue = libpanda._inPbPIPeCel(self.this, name, sort)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_attachNewNode_ptrConstNodePath_atomicstring(self, name):
            returnValue = libpanda._inPbPIP1Fk7(self.this, name)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def removeNode(self):
            returnValue = libpanda._inPbPIPe8uR(self.this)
            return returnValue

        
        def overloaded_asString_ptrConstNodePath_int(self, startAtNode):
            returnValue = libpanda._inPbPIPytMW(self.this, startAtNode)
            return returnValue

        
        def overloaded_asString_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPUVxx(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPbPIPhcbM(self.this, out.this)
            return returnValue

        
        def overloaded_writeTransitions_ptrConstNodePath_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPbPIPSLLn(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_writeTransitions_ptrConstNodePath_ptrOstream(self, out):
            returnValue = libpanda._inPbPIPwcxX(self.this, out.this)
            return returnValue

        
        def getNetTransitions(self):
            returnValue = libpanda._inPbPIPpgfV(self.this)
            returnObject = AllTransitionsWrapper.AllTransitionsWrapper(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_ls_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPoCML(self.this)
            return returnValue

        
        def overloaded_ls_ptrConstNodePath_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPbPIPuNzE(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_ls_ptrConstNodePath_ptrOstream(self, out):
            returnValue = libpanda._inPbPIPnO3a(self.this, out.this)
            return returnValue

        
        def lsTransitions(self):
            returnValue = libpanda._inPbPIPLeP6(self.this)
            return returnValue

        
        def lsTransforms(self):
            returnValue = libpanda._inPbPIP7e_I(self.this)
            return returnValue

        
        def analyze(self):
            returnValue = libpanda._inPbPIPzpN4(self.this)
            return returnValue

        
        def flattenLight(self):
            returnValue = libpanda._inPbPIPsBMC(self.this)
            return returnValue

        
        def overloaded_flattenMedium_ptrNodePath_int(self, maxChildren):
            returnValue = libpanda._inPbPIPZDFW(self.this, maxChildren)
            return returnValue

        
        def overloaded_flattenMedium_ptrNodePath(self):
            returnValue = libpanda._inPbPIPjvep(self.this)
            return returnValue

        
        def overloaded_flattenStrong_ptrNodePath_int(self, maxChildren):
            returnValue = libpanda._inPbPIPTICA(self.this, maxChildren)
            return returnValue

        
        def overloaded_flattenStrong_ptrNodePath(self):
            returnValue = libpanda._inPbPIPZ3aT(self.this)
            return returnValue

        
        def writeBamFile(self, filename):
            returnValue = libpanda._inPbPIP88rd(self.this, filename)
            return returnValue

        
        def overloaded_setPos_ptrNodePath_float_float_float(self, x, y, z):
            returnValue = libpanda._inPbPIPVSAL(self.this, x, y, z)
            return returnValue

        
        def overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(self, pos):
            returnValue = libpanda._inPbPIPmvV9(self.this, pos.this)
            return returnValue

        
        def overloaded_setX_ptrNodePath_float(self, x):
            returnValue = libpanda._inPbPIPW0Zh(self.this, x)
            return returnValue

        
        def overloaded_setY_ptrNodePath_float(self, y):
            returnValue = libpanda._inPbPIPv6ZR(self.this, y)
            return returnValue

        
        def overloaded_setZ_ptrNodePath_float(self, z):
            returnValue = libpanda._inPbPIPRNaB(self.this, z)
            return returnValue

        
        def overloaded_getPos_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPHC5T(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getX_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPt_ol(self.this)
            return returnValue

        
        def overloaded_getY_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPTspV(self.this)
            return returnValue

        
        def overloaded_getZ_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPq2oF(self.this)
            return returnValue

        
        def overloaded_setHpr_ptrNodePath_float_float_float(self, h, p, r):
            returnValue = libpanda._inPbPIP_6OG(self.this, h, p, r)
            return returnValue

        
        def overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(self, hpr):
            returnValue = libpanda._inPbPIPA3k4(self.this, hpr.this)
            return returnValue

        
        def overloaded_setH_ptrNodePath_float(self, h):
            returnValue = libpanda._inPbPIPysUh(self.this, h)
            return returnValue

        
        def overloaded_setP_ptrNodePath_float(self, p):
            returnValue = libpanda._inPbPIPoYYh(self.this, p)
            return returnValue

        
        def overloaded_setR_ptrNodePath_float(self, r):
            returnValue = libpanda._inPbPIPjxXB(self.this, r)
            return returnValue

        
        def overloaded_getHpr_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPd7JP(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getHpr_ptrConstNodePath_float(self, roll):
            returnValue = libpanda._inPbPIPo6kH(self.this, roll)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getH_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPJHkl(self.this)
            return returnValue

        
        def overloaded_getP_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIP7ill(self.this)
            return returnValue

        
        def overloaded_getR_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPAKmF(self.this)
            return returnValue

        
        def overloaded_setScale_ptrNodePath_float(self, scale):
            returnValue = libpanda._inPbPIPmtLn(self.this, scale)
            return returnValue

        
        def overloaded_setScale_ptrNodePath_float_float_float(self, sx, sy, sz):
            returnValue = libpanda._inPbPIPGGHl(self.this, sx, sy, sz)
            return returnValue

        
        def overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(self, sv3):
            returnValue = libpanda._inPbPIPS0Rp(self.this, sv3.this)
            return returnValue

        
        def overloaded_setSx_ptrNodePath_float(self, sx):
            returnValue = libpanda._inPbPIP9GJx(self.this, sx)
            return returnValue

        
        def overloaded_setSy_ptrNodePath_float(self, sy):
            returnValue = libpanda._inPbPIPV0Rx(self.this, sy)
            return returnValue

        
        def overloaded_setSz_ptrNodePath_float(self, sz):
            returnValue = libpanda._inPbPIPNlbx(self.this, sz)
            return returnValue

        
        def overloaded_getScale_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPy3jS(self.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getSx_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPgU4U(self.this)
            return returnValue

        
        def overloaded_getSy_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPoFCV(self.this)
            return returnValue

        
        def overloaded_getSz_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPQuLV(self.this)
            return returnValue

        
        def overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(self, x, y, z, h, p, r):
            returnValue = libpanda._inPbPIP_0xa(self.this, x, y, z, h, p, r)
            return returnValue

        
        def overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr):
            returnValue = libpanda._inPbPIP3kIO(self.this, pos.this, hpr.this)
            return returnValue

        
        def overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(self, x, y, z, h, p, r, sx, sy, sz):
            returnValue = libpanda._inPbPIPaRCw(self.this, x, y, z, h, p, r, sx, sy, sz)
            return returnValue

        
        def overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, pos, hpr, scale):
            returnValue = libpanda._inPbPIPPlWQ(self.this, pos.this, hpr.this, scale.this)
            return returnValue

        
        def overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(self, mat):
            returnValue = libpanda._inPbPIPzrbe(self.this, mat.this)
            return returnValue

        
        def clearMat(self):
            returnValue = libpanda._inPbPIPSWCU(self.this)
            return returnValue

        
        def hasMat(self):
            returnValue = libpanda._inPbPIPnm1u(self.this)
            return returnValue

        
        def overloaded_getMat_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPBmoG(self.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def hasColorScale(self):
            returnValue = libpanda._inPbPIPaXr2(self.this)
            return returnValue

        
        def clearColorScale(self):
            returnValue = libpanda._inPbPIPGgLo(self.this)
            return returnValue

        
        def overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(self, sv4):
            returnValue = libpanda._inPbPIPbg1C(self.this, sv4.this)
            return returnValue

        
        def overloaded_setColorScale_ptrNodePath_float_float_float_float(self, sx, sy, sz, sa):
            returnValue = libpanda._inPbPIPNfGH(self.this, sx, sy, sz, sa)
            return returnValue

        
        def setSr(self, sr):
            returnValue = libpanda._inPbPIPNaNw(self.this, sr)
            return returnValue

        
        def setSg(self, sg):
            returnValue = libpanda._inPbPIPFEju(self.this, sg)
            return returnValue

        
        def setSb(self, sb):
            returnValue = libpanda._inPbPIPNYyt(self.this, sb)
            return returnValue

        
        def setSa(self, sa):
            returnValue = libpanda._inPbPIPVbnt(self.this, sa)
            return returnValue

        
        def getColorScale(self):
            returnValue = libpanda._inPbPIPAXeO(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getSr(self):
            returnValue = libpanda._inPbPIPQ39T(self.this)
            return returnValue

        
        def getSg(self):
            returnValue = libpanda._inPbPIP4VSS(self.this)
            return returnValue

        
        def getSb(self):
            returnValue = libpanda._inPbPIPQphR(self.this)
            return returnValue

        
        def getSa(self):
            returnValue = libpanda._inPbPIPo4XR(self.this)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_float_float_float(self, x, y, z):
            returnValue = libpanda._inPbPIPMr_Y(self.this, x, y, z)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
            returnValue = libpanda._inPbPIPo3rT(self.this, point.this, up.this)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPbPIPHo_M(self.this, point.this)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_float_float_float(self, x, y, z):
            returnValue = libpanda._inPbPIPWjov(self.this, x, y, z)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
            returnValue = libpanda._inPbPIPxTxG(self.this, point.this, up.this)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPbPIPDTtu(self.this, point.this)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_float_float_float(self, x, y, z):
            returnValue = libpanda._inPbPIPQqDd(self.this, x, y, z)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
            returnValue = libpanda._inPbPIP6E2y(self.this, point.this, up.this)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPbPIP7X38(self.this, point.this)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_float_float_float(self, x, y, z):
            returnValue = libpanda._inPbPIPYzG0(self.this, x, y, z)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, point, up):
            returnValue = libpanda._inPbPIPbLys(self.this, point.this, up.this)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstLPoint3f(self, point):
            returnValue = libpanda._inPbPIP94_r(self.this, point.this)
            return returnValue

        
        def overloaded_printPos_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPm3k7(self.this)
            return returnValue

        
        def overloaded_printHpr_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPfKwp(self.this)
            return returnValue

        
        def overloaded_printScale_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIP4dLs(self.this)
            return returnValue

        
        def overloaded_printPosHpr_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPPeM0(self.this)
            return returnValue

        
        def overloaded_printPosHprScale_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIP4QdJ(self.this)
            return returnValue

        
        def overloaded_printMat_ptrConstNodePath(self):
            returnValue = libpanda._inPbPIPyi3o(self.this)
            return returnValue

        
        def printColorScale(self):
            returnValue = libpanda._inPbPIPHrfY(self.this)
            return returnValue

        
        def overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
            returnValue = libpanda._inPbPIPt8Uk(self.this, other.this, x, y, z)
            return returnValue

        
        def overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, pos):
            returnValue = libpanda._inPbPIPp6ot(self.this, other.this, pos.this)
            return returnValue

        
        def overloaded_setX_ptrNodePath_ptrConstNodePath_float(self, other, x):
            returnValue = libpanda._inPbPIPJ4z_(self.this, other.this, x)
            return returnValue

        
        def overloaded_setY_ptrNodePath_ptrConstNodePath_float(self, other, y):
            returnValue = libpanda._inPbPIPrkzv(self.this, other.this, y)
            return returnValue

        
        def overloaded_setZ_ptrNodePath_ptrConstNodePath_float(self, other, z):
            returnValue = libpanda._inPbPIPNT0f(self.this, other.this, z)
            return returnValue

        
        def overloaded_getPos_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIP74Lu(self.this, other.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getX_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPlqU6(self.this, other.this)
            return returnValue

        
        def overloaded_getY_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPDeUq(self.this, other.this)
            return returnValue

        
        def overloaded_getZ_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPhTVa(self.this, other.this)
            return returnValue

        
        def overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(self, other, h, p, r):
            returnValue = libpanda._inPbPIPT1lf(self.this, other.this, h, p, r)
            return returnValue

        
        def overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, hpr):
            returnValue = libpanda._inPbPIPHC4o(self.this, other.this, hpr.this)
            return returnValue

        
        def overloaded_setH_ptrNodePath_ptrConstNodePath_float(self, other, h):
            returnValue = libpanda._inPbPIPtwu_(self.this, other.this, h)
            return returnValue

        
        def overloaded_setP_ptrNodePath_ptrConstNodePath_float(self, other, p):
            returnValue = libpanda._inPbPIP7Lx_(self.this, other.this, p)
            return returnValue

        
        def overloaded_setR_ptrNodePath_ptrConstNodePath_float(self, other, r):
            returnValue = libpanda._inPbPIP_uwf(self.this, other.this, r)
            return returnValue

        
        def overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPRuap(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getHpr_ptrConstNodePath_ptrConstNodePath_float(self, other, roll):
            returnValue = libpanda._inPbPIP2eqn(self.this, other.this, roll)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getH_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIP5yP6(self.this, other.this)
            return returnValue

        
        def overloaded_getP_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPLPS6(self.this, other.this)
            return returnValue

        
        def overloaded_getR_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPP2Ra(self.this, other.this)
            return returnValue

        
        def overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(self, other, sx, sy, sz):
            returnValue = libpanda._inPbPIPqk_k(self.this, other.this, sx, sy, sz)
            return returnValue

        
        def overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(self, other, scale):
            returnValue = libpanda._inPbPIPi4f1(self.this, other.this, scale.this)
            return returnValue

        
        def overloaded_setSx_ptrNodePath_ptrConstNodePath_float(self, other, sx):
            returnValue = libpanda._inPbPIPh83_(self.this, other.this, sx)
            return returnValue

        
        def overloaded_setSy_ptrNodePath_ptrConstNodePath_float(self, other, sy):
            returnValue = libpanda._inPbPIPZvB_(self.this, other.this, sy)
            return returnValue

        
        def overloaded_setSz_ptrNodePath_ptrConstNodePath_float(self, other, sz):
            returnValue = libpanda._inPbPIPxeL_(self.this, other.this, sz)
            return returnValue

        
        def overloaded_getScale_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPTA2z(self.this, other.this)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_getSx_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIP7wrr(self.this, other.this)
            return returnValue

        
        def overloaded_getSy_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPDe1r(self.this, other.this)
            return returnValue

        
        def overloaded_getSz_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPLP9r(self.this, other.this)
            return returnValue

        
        def overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(self, other, x, y, z, h, p, r):
            returnValue = libpanda._inPbPIPa1I1(self.this, other.this, x, y, z, h, p, r)
            return returnValue

        
        def overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr):
            returnValue = libpanda._inPbPIPU6SC(self.this, other.this, pos.this, hpr.this)
            return returnValue

        
        def overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(self, other, x, y, z, h, p, r, sx, sy, sz):
            returnValue = libpanda._inPbPIPOhTJ(self.this, other.this, x, y, z, h, p, r, sx, sy, sz)
            return returnValue

        
        def overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(self, other, pos, hpr, scale):
            returnValue = libpanda._inPbPIPzxbK(self.this, other.this, pos.this, hpr.this, scale.this)
            return returnValue

        
        def overloaded_getMat_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIP4D6g(self.this, other.this)
            returnObject = Mat4.Mat4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(self, other, mat):
            returnValue = libpanda._inPbPIPXUwZ(self.this, other.this, mat.this)
            return returnValue

        
        def getRelativePoint(self, other, point):
            returnValue = libpanda._inPbPIPYRNh(self.this, other.this, point.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
            returnValue = libpanda._inPbPIPhCVy(self.this, other.this, x, y, z)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
            returnValue = libpanda._inPbPIP79Nd(self.this, other.this, point.this, up.this)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
            returnValue = libpanda._inPbPIPl3PC(self.this, other.this, point.this)
            return returnValue

        
        def overloaded_lookAt_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPzQMs(self.this, other.this)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
            returnValue = libpanda._inPbPIPsoob(self.this, other.this, x, y, z)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
            returnValue = libpanda._inPbPIP4OA4(self.this, other.this, point.this, up.this)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
            returnValue = libpanda._inPbPIPusnX(self.this, other.this, point.this)
            return returnValue

        
        def overloaded_headsUp_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPpiWV(self.this, other.this)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
            returnValue = libpanda._inPbPIPTeAo(self.this, other.this, x, y, z)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
            returnValue = libpanda._inPbPIPdII_(self.this, other.this, point.this, up.this)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
            returnValue = libpanda._inPbPIPs_Dn(self.this, other.this, point.this)
            return returnValue

        
        def overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPwzg2(self.this, other.this)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_float_float_float(self, other, x, y, z):
            returnValue = libpanda._inPbPIP3rCU(self.this, other.this, x, y, z)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(self, other, point, up):
            returnValue = libpanda._inPbPIPTPx2(self.this, other.this, point.this, up.this)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(self, other, point):
            returnValue = libpanda._inPbPIPbsmz(self.this, other.this, point.this)
            return returnValue

        
        def overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPEoVh(self.this, other.this)
            return returnValue

        
        def overloaded_printPos_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPM_1c(self.this, other.this)
            return returnValue

        
        def overloaded_printHpr_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPYeAL(self.this, other.this)
            return returnValue

        
        def overloaded_printScale_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPtxyZ(self.this, other.this)
            return returnValue

        
        def overloaded_printPosHpr_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPEVSG(self.this, other.this)
            return returnValue

        
        def overloaded_printPosHprScale_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIP0_nO(self.this, other.this)
            return returnValue

        
        def overloaded_printMat_ptrConstNodePath_ptrConstNodePath(self, other):
            returnValue = libpanda._inPbPIPAkIK(self.this, other.this)
            return returnValue

        
        def getDistance(self, other):
            returnValue = libpanda._inPbPIPZ2tf(self.this, other.this)
            return returnValue

        
        def overloaded_setColor_ptrNodePath_float_float_float_float_int(self, r, g, b, a, priority):
            returnValue = libpanda._inPbPIPtU7r(self.this, r, g, b, a, priority)
            return returnValue

        
        def overloaded_setColor_ptrNodePath_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPbPIPq2aQ(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setColor_ptrNodePath_float_float_float(self, r, g, b):
            returnValue = libpanda._inPbPIPJSPM(self.this, r, g, b)
            return returnValue

        
        def overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(self, color, priority):
            returnValue = libpanda._inPbPIPT3vm(self.this, color.this, priority)
            return returnValue

        
        def overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(self, color):
            returnValue = libpanda._inPbPIPORas(self.this, color.this)
            return returnValue

        
        def overloaded_setColorOff_ptrNodePath_int(self, priority):
            returnValue = libpanda._inPbPIPpQ8z(self.this, priority)
            return returnValue

        
        def overloaded_setColorOff_ptrNodePath(self):
            returnValue = libpanda._inPbPIP9OhC(self.this)
            return returnValue

        
        def clearColor(self):
            returnValue = libpanda._inPbPIPuAs9(self.this)
            return returnValue

        
        def hasColor(self):
            returnValue = libpanda._inPbPIPUN5h(self.this)
            return returnValue

        
        def getColor(self):
            returnValue = libpanda._inPbPIPdNs5(self.this)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setBin_ptrNodePath_atomicstring_int_int(self, binName, drawOrder, priority):
            returnValue = libpanda._inPbPIPqEEK(self.this, binName, drawOrder, priority)
            return returnValue

        
        def overloaded_setBin_ptrNodePath_atomicstring_int(self, binName, drawOrder):
            returnValue = libpanda._inPbPIPSbGG(self.this, binName, drawOrder)
            return returnValue

        
        def clearBin(self):
            returnValue = libpanda._inPbPIPUNFW(self.this)
            return returnValue

        
        def hasBin(self):
            returnValue = libpanda._inPbPIPMAtC(self.this)
            return returnValue

        
        def getBinName(self):
            returnValue = libpanda._inPbPIPEaFg(self.this)
            return returnValue

        
        def getBinDrawOrder(self):
            returnValue = libpanda._inPbPIPvnw9(self.this)
            return returnValue

        
        def overloaded_setTexture_ptrNodePath_ptrTexture_int(self, tex, priority):
            returnValue = libpanda._inPbPIP_dvx(self.this, tex.this, priority)
            return returnValue

        
        def overloaded_setTexture_ptrNodePath_ptrTexture(self, tex):
            returnValue = libpanda._inPbPIPV7Tm(self.this, tex.this)
            return returnValue

        
        def overloaded_setTextureOff_ptrNodePath_int(self, priority):
            returnValue = libpanda._inPbPIPpScU(self.this, priority)
            return returnValue

        
        def overloaded_setTextureOff_ptrNodePath(self):
            returnValue = libpanda._inPbPIP4SwA(self.this)
            return returnValue

        
        def clearTexture(self):
            returnValue = libpanda._inPbPIPGnBp(self.this)
            return returnValue

        
        def hasTexture(self):
            returnValue = libpanda._inPbPIPj_wf(self.this)
            return returnValue

        
        def hasTextureOff(self):
            returnValue = libpanda._inPbPIPqe64(self.this)
            return returnValue

        
        def getTexture(self):
            returnValue = libpanda._inPbPIPI_l3(self.this)
            returnObject = Texture.Texture(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setMaterial_ptrNodePath_ptrMaterial_int(self, tex, priority):
            returnValue = libpanda._inPbPIPYzam(self.this, tex.this, priority)
            return returnValue

        
        def overloaded_setMaterial_ptrNodePath_ptrMaterial(self, tex):
            returnValue = libpanda._inPbPIPvxcl(self.this, tex.this)
            return returnValue

        
        def clearMaterial(self):
            returnValue = libpanda._inPbPIP6uUw(self.this)
            return returnValue

        
        def hasMaterial(self):
            returnValue = libpanda._inPbPIPOYf6(self.this)
            return returnValue

        
        def getMaterial(self):
            returnValue = libpanda._inPbPIPkYSS(self.this)
            returnObject = Material.Material(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setFog_ptrNodePath_ptrFog_int(self, fog, priority):
            returnValue = libpanda._inPbPIPfiDI(self.this, fog.this, priority)
            return returnValue

        
        def overloaded_setFog_ptrNodePath_ptrFog(self, fog):
            returnValue = libpanda._inPbPIPoa0X(self.this, fog.this)
            return returnValue

        
        def overloaded_setFogOff_ptrNodePath_int(self, priority):
            returnValue = libpanda._inPbPIP2Eb5(self.this, priority)
            return returnValue

        
        def overloaded_setFogOff_ptrNodePath(self):
            returnValue = libpanda._inPbPIPY6I_(self.this)
            return returnValue

        
        def clearFog(self):
            returnValue = libpanda._inPbPIPIl5h(self.this)
            return returnValue

        
        def hasFog(self):
            returnValue = libpanda._inPbPIPCReh(self.this)
            return returnValue

        
        def hasFogOff(self):
            returnValue = libpanda._inPbPIPQw1z(self.this)
            return returnValue

        
        def getFog(self):
            returnValue = libpanda._inPbPIPPRR5(self.this)
            returnObject = Fog.Fog(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_setRenderModeWireframe_ptrNodePath_int(self, priority):
            returnValue = libpanda._inPbPIPwAKB(self.this, priority)
            return returnValue

        
        def overloaded_setRenderModeWireframe_ptrNodePath(self):
            returnValue = libpanda._inPbPIP9SWy(self.this)
            return returnValue

        
        def overloaded_setRenderModeFilled_ptrNodePath_int(self, priority):
            returnValue = libpanda._inPbPIP_2Fx(self.this, priority)
            return returnValue

        
        def overloaded_setRenderModeFilled_ptrNodePath(self):
            returnValue = libpanda._inPbPIPFx6K(self.this)
            return returnValue

        
        def clearRenderMode(self):
            returnValue = libpanda._inPbPIPzTUZ(self.this)
            return returnValue

        
        def hasRenderMode(self):
            returnValue = libpanda._inPbPIPgdaf(self.this)
            return returnValue

        
        def overloaded_setTwoSided_ptrNodePath_bool_int(self, twoSided, priority):
            returnValue = libpanda._inPbPIPNkd_(self.this, twoSided, priority)
            return returnValue

        
        def overloaded_setTwoSided_ptrNodePath_bool(self, twoSided):
            returnValue = libpanda._inPbPIP3m_e(self.this, twoSided)
            return returnValue

        
        def clearTwoSided(self):
            returnValue = libpanda._inPbPIPhjBF(self.this)
            return returnValue

        
        def hasTwoSided(self):
            returnValue = libpanda._inPbPIPhHUb(self.this)
            return returnValue

        
        def getTwoSided(self):
            returnValue = libpanda._inPbPIP_GHz(self.this)
            return returnValue

        
        def doBillboardAxis(self, camera, offset):
            returnValue = libpanda._inPbPIPHial(self.this, camera.this, offset)
            return returnValue

        
        def doBillboardPointEye(self, camera, offset):
            returnValue = libpanda._inPbPIPU_bl(self.this, camera.this, offset)
            return returnValue

        
        def doBillboardPointWorld(self, camera, offset):
            returnValue = libpanda._inPbPIPQjcU(self.this, camera.this, offset)
            return returnValue

        
        def overloaded_setBillboardAxis_ptrNodePath_float(self, offset):
            returnValue = libpanda._inPbPIPFhYU(self.this, offset)
            return returnValue

        
        def overloaded_setBillboardAxis_ptrNodePath(self):
            returnValue = libpanda._inPbPIPq8Dy(self.this)
            return returnValue

        
        def overloaded_setBillboardPointEye_ptrNodePath_float(self, offset):
            returnValue = libpanda._inPbPIPZONU(self.this, offset)
            return returnValue

        
        def overloaded_setBillboardPointEye_ptrNodePath(self):
            returnValue = libpanda._inPbPIPQceP(self.this)
            return returnValue

        
        def overloaded_setBillboardPointWorld_ptrNodePath_float(self, offset):
            returnValue = libpanda._inPbPIPH0qP(self.this, offset)
            return returnValue

        
        def overloaded_setBillboardPointWorld_ptrNodePath(self):
            returnValue = libpanda._inPbPIPDjae(self.this)
            return returnValue

        
        def clearBillboard(self):
            returnValue = libpanda._inPbPIPTaTv(self.this)
            return returnValue

        
        def hasBillboard(self):
            returnValue = libpanda._inPbPIPwCXg(self.this)
            return returnValue

        
        def overloaded_setTransparency_ptrNodePath_bool_int(self, transparency, priority):
            returnValue = libpanda._inPbPIP7Tdb(self.this, transparency, priority)
            return returnValue

        
        def overloaded_setTransparency_ptrNodePath_bool(self, transparency):
            returnValue = libpanda._inPbPIP3RCQ(self.this, transparency)
            return returnValue

        
        def clearTransparency(self):
            returnValue = libpanda._inPbPIPVu7Z(self.this)
            return returnValue

        
        def hasTransparency(self):
            returnValue = libpanda._inPbPIPYd3E(self.this)
            return returnValue

        
        def getTransparency(self):
            returnValue = libpanda._inPbPIPxcoc(self.this)
            return returnValue

        
        def adjustAllPriorities(self, adjustment):
            returnValue = libpanda._inPbPIPU_Ul(self.this, adjustment)
            return returnValue

        
        def show(self):
            returnValue = libpanda._inPbPIP8Jw_(self.this)
            return returnValue

        
        def hide(self):
            returnValue = libpanda._inPbPIPkdIm(self.this)
            return returnValue

        
        def showCollisionSolids(self):
            returnValue = libpanda._inPbPIP_lf_(self.this)
            return returnValue

        
        def hideCollisionSolids(self):
            returnValue = libpanda._inPbPIPl_5m(self.this)
            return returnValue

        
        def isHidden(self):
            returnValue = libpanda._inPbPIPRtUU(self.this)
            return returnValue

        
        def getHiddenAncestor(self):
            returnValue = libpanda._inPbPIPBcma(self.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def stash(self):
            returnValue = libpanda._inPbPIPbB0Q(self.this)
            return returnValue

        
        def unstash(self):
            returnValue = libpanda._inPbPIPF_f6(self.this)
            return returnValue

        
        def isStashed(self):
            returnValue = libpanda._inPbPIP3pEj(self.this)
            return returnValue

        
        def getStashedAncestor(self):
            returnValue = libpanda._inPbPIPStAQ(self.this)
            returnObject = NodePath(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase_bool(self, gsg, forceRetainedMode):
            returnValue = libpanda._inPbPIPYZJ2(self.this, gsg.this, forceRetainedMode)
            return returnValue

        
        def overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase(self, gsg):
            returnValue = libpanda._inPbPIPthH0(self.this, gsg.this)
            return returnValue

        
        def clearWrtCache(self):
            returnValue = libpanda._inPbPIPTqKI(self.this)
            return returnValue

        
        def showBounds(self):
            returnValue = libpanda._inPbPIPuDtR(self.this)
            return returnValue

        
        def hideBounds(self):
            returnValue = libpanda._inPbPIPt5G5(self.this)
            return returnValue

        
        def getBounds(self):
            returnValue = libpanda._inPbPIPioSR(self.this)
            returnObject = BoundingVolume.BoundingVolume(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def writeBounds(self, out):
            returnValue = libpanda._inPbPIPvJxc(self.this, out.this)
            return returnValue

        
        def calcTightBounds(self, minPoint, maxPoint):
            returnValue = libpanda._inPbPIPoDS_(self.this, minPoint.this, maxPoint.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], TypeHandle.TypeHandle):
                    return self.overloaded_constructor_ptrTypeHandle(_args[0])
                elif isinstance(_args[0], NodeRelation.NodeRelation):
                    return self.overloaded_constructor_ptrNodeRelation(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_constructor_ptrConstNodePath(_args[0])
                elif isinstance(_args[0], Node.Node):
                    return self.overloaded_constructor_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <TypeHandle.TypeHandle> <NodeRelation.NodeRelation> <NodePath> <Node.Node> '
            elif numArgs == 2:
                if isinstance(_args[0], Node.Node):
                    if isinstance(_args[1], TypeHandle.TypeHandle):
                        return self.overloaded_constructor_ptrNode_ptrTypeHandle(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <TypeHandle.TypeHandle> '
                elif isinstance(_args[0], ArcChain.ArcChain):
                    if isinstance(_args[1], TypeHandle.TypeHandle):
                        return self.overloaded_constructor_ptrConstArcChain_ptrTypeHandle(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <TypeHandle.TypeHandle> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Node.Node> <ArcChain.ArcChain> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def getMat(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getMat_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getMat_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setSy(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setSy_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setSy_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def extendBy(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_extendBy_ptrNodePath_atomicstring(_args[0])
                elif isinstance(_args[0], NodeRelation.NodeRelation):
                    return self.overloaded_extendBy_ptrNodePath_ptrNodeRelation(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_extendBy_ptrNodePath_ptrConstNodePath(_args[0])
                elif isinstance(_args[0], Node.Node):
                    return self.overloaded_extendBy_ptrNodePath_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <NodeRelation.NodeRelation> <NodePath> <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 '

        
        def printPos(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printPos_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printPos_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def writeTransitions(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_writeTransitions_ptrConstNodePath_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_writeTransitions_ptrConstNodePath_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setRenderModeFilled(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setRenderModeFilled_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setRenderModeFilled_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setColorScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColorScale_ptrNodePath_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColorScale_ptrNodePath_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 4 '

        
        def setBillboardAxis(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setBillboardAxis_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setBillboardAxis_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setPos(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_setPos_ptrNodePath_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setPos_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setPos_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setPos_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def lookAtPreserveScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_lookAtPreserveScale_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_lookAtPreserveScale_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def setColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColor_ptrNodePath_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 2:
                if isinstance(_args[0], VBase4.VBase4):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setColor_ptrNodePath_ptrConstLVecBase4f_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setColor_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColor_ptrNodePath_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 5:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.IntType):
                                    return self.overloaded_setColor_ptrNodePath_float_float_float_float_int(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.IntType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 5 '

        
        def getSz(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getSz_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getSz_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getSy(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getSy_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getSy_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getSx(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getSx_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getSx_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setZ(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setZ_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setZ_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setY(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setY_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setY_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setX(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setX_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setX_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setRenderModeWireframe(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setRenderModeWireframe_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setRenderModeWireframe_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getScale_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getScale_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setPosHprScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 3:
                if isinstance(_args[0], VBase3.VBase3):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], VBase3.VBase3):
                            return self.overloaded_setPosHprScale_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], VBase3.VBase3):
                            if isinstance(_args[3], VBase3.VBase3):
                                return self.overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <VBase3.VBase3> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 9:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    return self.overloaded_setPosHprScale_ptrNodePath_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8])
                                                else:
                                                    raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 10:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            if isinstance(_args[7], types.FloatType) or isinstance(_args[7], types.IntType):
                                                if isinstance(_args[8], types.FloatType) or isinstance(_args[8], types.IntType):
                                                    if isinstance(_args[9], types.FloatType) or isinstance(_args[9], types.IntType):
                                                        return self.overloaded_setPosHprScale_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6], _args[7], _args[8], _args[9])
                                                    else:
                                                        raise TypeError, 'Invalid argument 9, expected one of: <types.FloatType> '
                                                else:
                                                    raise TypeError, 'Invalid argument 8, expected one of: <types.FloatType> '
                                            else:
                                                raise TypeError, 'Invalid argument 7, expected one of: <types.FloatType> '
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 3 4 9 10 '

        
        def setColorOff(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setColorOff_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setColorOff_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setR(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setR_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setR_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setTransparency(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setTransparency_ptrNodePath_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setTransparency_ptrNodePath_bool_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setP(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setP_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setP_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def printMat(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printMat_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printMat_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getH(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getH_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getH_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setBillboardPointWorld(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setBillboardPointWorld_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setBillboardPointWorld_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setH(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setH_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setH_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def headsUpPreserveScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_headsUpPreserveScale_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_headsUpPreserveScale_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def setSz(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setSz_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setSz_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def printPosHprScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printPosHprScale_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printPosHprScale_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setSx(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setSx_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_setSx_ptrNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def reparentTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_reparentTo_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_reparentTo_ptrNodePath_ptrConstNodePath_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setFogOff(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setFogOff_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setFogOff_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setTextureOff(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setTextureOff_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setTextureOff_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def printScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printScale_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printScale_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def ls(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_ls_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_ls_ptrConstNodePath_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_ls_ptrConstNodePath_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def copyTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_copyTo_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_copyTo_ptrConstNodePath_ptrConstNodePath_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def prepareScene(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], GraphicsStateGuardianBase.GraphicsStateGuardianBase):
                    return self.overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsStateGuardianBase.GraphicsStateGuardianBase> '
            elif numArgs == 2:
                if isinstance(_args[0], GraphicsStateGuardianBase.GraphicsStateGuardianBase):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_prepareScene_ptrNodePath_ptrGraphicsStateGuardianBase_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GraphicsStateGuardianBase.GraphicsStateGuardianBase> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setTexture(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Texture.Texture):
                    return self.overloaded_setTexture_ptrNodePath_ptrTexture(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> '
            elif numArgs == 2:
                if isinstance(_args[0], Texture.Texture):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setTexture_ptrNodePath_ptrTexture_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Texture.Texture> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def shorten(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_shorten_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_shorten_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def printPosHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printPosHpr_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printPosHpr_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setMaterial(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Material.Material):
                    return self.overloaded_setMaterial_ptrNodePath_ptrMaterial(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Material.Material> '
            elif numArgs == 2:
                if isinstance(_args[0], Material.Material):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setMaterial_ptrNodePath_ptrMaterial_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Material.Material> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setTwoSided(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_setTwoSided_ptrNodePath_bool(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setTwoSided_ptrNodePath_bool_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setBin(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setBin_ptrNodePath_atomicstring_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 3:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_setBin_ptrNodePath_atomicstring_int_int(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 '

        
        def flattenMedium(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_flattenMedium_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_flattenMedium_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def instanceTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_instanceTo_ptrConstNodePath_ptrConstNodePath_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setMat(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Mat4.Mat4):
                    return self.overloaded_setMat_ptrNodePath_ptrConstLMatrix4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Mat4.Mat4> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Mat4.Mat4):
                        return self.overloaded_setMat_ptrNodePath_ptrConstNodePath_ptrConstLMatrix4f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Mat4.Mat4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def flattenStrong(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_flattenStrong_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_flattenStrong_ptrNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def printHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_printHpr_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_printHpr_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def asString(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_asString_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_asString_ptrConstNodePath_int(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getR(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getR_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getR_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setPosHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], VBase3.VBase3):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setPosHpr_ptrNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], VBase3.VBase3):
                        if isinstance(_args[2], VBase3.VBase3):
                            return self.overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f_ptrConstLVecBase3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <VBase3.VBase3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 6:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        return self.overloaded_setPosHpr_ptrNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 7:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        if isinstance(_args[6], types.FloatType) or isinstance(_args[6], types.IntType):
                                            return self.overloaded_setPosHpr_ptrNodePath_ptrConstNodePath_float_float_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5], _args[6])
                                        else:
                                            raise TypeError, 'Invalid argument 6, expected one of: <types.FloatType> '
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 3 6 7 '

        
        def getP(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getP_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getP_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setFog(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Fog.Fog):
                    return self.overloaded_setFog_ptrNodePath_ptrFog(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Fog.Fog> '
            elif numArgs == 2:
                if isinstance(_args[0], Fog.Fog):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_setFog_ptrNodePath_ptrFog_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Fog.Fog> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def headsUp(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_headsUp_ptrNodePath_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_headsUp_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_headsUp_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_headsUp_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            return self.overloaded_headsUp_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_headsUp_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def lookAt(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Point3.Point3):
                    return self.overloaded_lookAt_ptrNodePath_ptrConstLPoint3f(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_lookAt_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], Point3.Point3):
                    if isinstance(_args[1], Vec3.Vec3):
                        return self.overloaded_lookAt_ptrNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Vec3.Vec3> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Point3.Point3> <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_lookAt_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                elif isinstance(_args[0], NodePath):
                    if isinstance(_args[1], Point3.Point3):
                        if isinstance(_args[2], Vec3.Vec3):
                            return self.overloaded_lookAt_ptrNodePath_ptrConstNodePath_ptrConstLPoint3f_ptrConstLVector3f(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <Vec3.Vec3> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_lookAt_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def getZ(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getZ_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getZ_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getY(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getY_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getY_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getX(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getX_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getX_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def setScale(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setScale_ptrNodePath_float(_args[0])
                elif isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_setScale_ptrNodePath_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <VBase3.VBase3> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setScale_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setScale_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setScale_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def attachNewNode(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_attachNewNode_ptrConstNodePath_atomicstring(_args[0])
                elif isinstance(_args[0], Node.Node):
                    return self.overloaded_attachNewNode_ptrConstNodePath_ptrNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Node.Node> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_attachNewNode_ptrConstNodePath_atomicstring_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                elif isinstance(_args[0], Node.Node):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_attachNewNode_ptrConstNodePath_ptrNode_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> <Node.Node> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def setHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_setHpr_ptrNodePath_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], VBase3.VBase3):
                        return self.overloaded_setHpr_ptrNodePath_ptrConstNodePath_ptrConstLVecBase3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase3.VBase3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setHpr_ptrNodePath_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setHpr_ptrNodePath_ptrConstNodePath_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 4 '

        
        def setBillboardPointEye(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_setBillboardPointEye_ptrNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_setBillboardPointEye_ptrNodePath_float(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def getPos(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getPos_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_getPos_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '

        
        def wrtReparentTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], NodePath):
                    return self.overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_wrtReparentTo_ptrNodePath_ptrConstNodePath_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        
        def getHpr(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_getHpr_ptrConstNodePath()
            elif numArgs == 1:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    return self.overloaded_getHpr_ptrConstNodePath_float(_args[0])
                elif isinstance(_args[0], NodePath):
                    return self.overloaded_getHpr_ptrConstNodePath_ptrConstNodePath(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> <NodePath> '
            elif numArgs == 2:
                if isinstance(_args[0], NodePath):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_getHpr_ptrConstNodePath_ptrConstNodePath_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <NodePath> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def id(self):
            return self.arc()

        
        def getName(self):
            from PandaModules import *
            name = '<noname>'
            node = self.node()
            if issubclass(node.__class__, NamedNode):
                namedNodeName = node.getName()
                if len(namedNodeName) != 0:
                    name = namedNodeName
                
            
            return name

        
        def setName(self, name = '<noname>'):
            from PandaModules import *
            node = self.node()
            if issubclass(node.__class__, NamedNode):
                node.setName(name)
            

        
        def getChildrenAsList(self):
            if self.isEmpty():
                return []
            else:
                children = self.getChildren()
                childrenList = []
                for childNum in range(self.getNumChildren()):
                    childrenList.append(children[childNum])
                
                return childrenList

        
        def printChildren(self):
            for child in self.getChildrenAsList():
                print child.getName()
            

        
        def toggleVis(self):
            if self.isHidden():
                self.show()
            else:
                self.hide()

        
        def showSiblings(self):
            for sib in self.getParent().getChildrenAsList():
                if sib.node() != self.node():
                    sib.show()
                
            

        
        def hideSiblings(self):
            for sib in self.getParent().getChildrenAsList():
                if sib.node() != self.node():
                    sib.hide()
                
            

        
        def showAllDescendants(self):
            if self.hasArcs():
                self.show()
            
            for child in self.getChildrenAsList():
                child.showAllDescendants()
            

        
        def isolate(self):
            self.showAllDescendants()
            self.hideSiblings()

        
        def remove(self):
            from PandaObject import *
            messenger.send('preRemoveNodePath', [
                self])
            self.removeNode()

        
        def reversels(self):
            ancestry = self.getAncestry()
            indentString = ''
            for nodePath in ancestry:
                type = nodePath.node().getType().getName()
                name = nodePath.getName()
                print indentString + type + '  ' + name
                indentString = indentString + ' '
            

        
        def getAncestry(self):
            from PandaObject import *
            node = self.node()
            if self.hasParent():
                ancestry = self.getParent().getAncestry()
                ancestry.append(self)
                return ancestry
            else:
                return [
                    self]

        
        def pprintPos(self, other = None, sd = 2):
            from PandaObject import *
            formatString = '%0.' + '%d' % sd + 'f'
            if other:
                pos = self.getPos(other)
                otherString = other.getName() + ', '
            else:
                pos = self.getPos()
                otherString = ''
            print self.getName() + '.setPos(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ')\n'

        
        def pprintHpr(self, other = None, sd = 2):
            from PandaObject import *
            formatString = '%0.' + '%d' % sd + 'f'
            if other:
                hpr = self.getHpr(other)
                otherString = other.getName() + ', '
            else:
                hpr = self.getHpr()
                otherString = ''
            print self.getName() + '.setHpr(' + otherString + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'

        
        def pprintScale(self, other = None, sd = 2):
            from PandaObject import *
            formatString = '%0.' + '%d' % sd + 'f'
            if other:
                scale = self.getScale(other)
                otherString = other.getName() + ', '
            else:
                scale = self.getScale()
                otherString = ''
            print self.getName() + '.setScale(' + otherString + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'

        
        def pprintPosHpr(self, other = None, sd = 2):
            from PandaObject import *
            formatString = '%0.' + '%d' % sd + 'f'
            if other:
                pos = self.getPos(other)
                hpr = self.getHpr(other)
                otherString = other.getName() + ', '
            else:
                pos = self.getPos()
                hpr = self.getHpr()
                otherString = ''
            print self.getName() + '.setPosHpr(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ')\n'

        
        def pprintPosHprScale(self, other = None, sd = 2):
            from PandaObject import *
            formatString = '%0.' + '%d' % sd + 'f'
            if other:
                pos = self.getPos(other)
                hpr = self.getHpr(other)
                scale = self.getScale(other)
                otherString = other.getName() + ', '
            else:
                pos = self.getPos()
                hpr = self.getHpr()
                scale = self.getScale()
                otherString = ''
            print self.getName() + '.setPosHprScale(' + otherString + formatString % pos[0] + ', ' + formatString % pos[1] + ', ' + formatString % pos[2] + ', ' + formatString % hpr[0] + ', ' + formatString % hpr[1] + ', ' + formatString % hpr[2] + ', ' + formatString % scale[0] + ', ' + formatString % scale[1] + ', ' + formatString % scale[2] + ')\n'

        
        def iPos(self, other = None):
            if other:
                self.setPos(other, 0, 0, 0)
            else:
                self.setPos(0, 0, 0)

        
        def iHpr(self, other = None):
            if other:
                self.setHpr(other, 0, 0, 0)
            else:
                self.setHpr(0, 0, 0)

        
        def iScale(self, other = None):
            if other:
                self.setScale(other, 1, 1, 1)
            else:
                self.setScale(1, 1, 1)

        
        def iPosHpr(self, other = None):
            if other:
                self.setPosHpr(other, 0, 0, 0, 0, 0, 0)
            else:
                self.setPosHpr(0, 0, 0, 0, 0, 0)

        
        def iPosHprScale(self, other = None):
            if other:
                self.setPosHprScale(other, 0, 0, 0, 0, 0, 0, 1, 1, 1)
            else:
                self.setPosHprScale(0, 0, 0, 0, 0, 0, 1, 1, 1)

        
        def __getBlend(self, blendType):
            import LerpBlendHelpers
            if blendType == 'easeIn':
                return LerpBlendHelpers.easeIn
            elif blendType == 'easeOut':
                return LerpBlendHelpers.easeOut
            elif blendType == 'easeInOut':
                return LerpBlendHelpers.easeInOut
            elif blendType == 'noBlend':
                return LerpBlendHelpers.noBlend
            else:
                raise Exception('Error: NodePath.__getBlend: Unknown blend type')

        
        def __lerp(self, functorFunc, duration, blendType, taskName = None):
            from TaskManagerGlobal import *
            
            def lerpUponDeath(task):
                
                try:
                    del task.functorFunc
                except:
                    pass

                
                try:
                    del task.lerp
                except:
                    pass


            
            def lerpTaskFunc(task):
                import Lerp
                import Task
                import ClockObject
                if task.init == 1:
                    functor = task.functorFunc()
                    task.lerp = Lerp.Lerp(functor, task.duration, task.blendType)
                    task.init = 0
                
                dt = ClockObject.ClockObject.getGlobalClock().getDt()
                task.lerp.setStepSize(dt)
                task.lerp.step()
                if task.lerp.isDone():
                    task.init = 1
                    return Task.done
                else:
                    return Task.cont

            lerpTask = Task.Task(lerpTaskFunc)
            lerpTask.init = 1
            lerpTask.functorFunc = functorFunc
            lerpTask.duration = duration
            lerpTask.blendType = self._NodePath__getBlend(blendType)
            lerpTask.uponDeath = lerpUponDeath
            if taskName == None:
                return lerpTask
            else:
                taskMgr.spawnTaskNamed(lerpTask, taskName)
                return lerpTask

        
        def __autoLerp(self, functorFunc, time, blendType, taskName):
            import AutonomousLerp
            from ShowBaseGlobal import *
            functor = functorFunc()
            lerp = AutonomousLerp.AutonomousLerp(functor, time, self._NodePath__getBlend(blendType), base.eventHandler)
            lerp.start()
            return lerp

        
        def lerpColor(self, *posArgs, **keyArgs):
            if len(posArgs) == 2:
                return apply(self.lerpColorVBase4, posArgs, keyArgs)
            elif len(posArgs) == 3:
                return apply(self.lerpColorVBase4VBase4, posArgs, keyArgs)
            elif len(posArgs) == 5:
                return apply(self.lerpColorRGBA, posArgs, keyArgs)
            elif len(posArgs) == 9:
                return apply(self.lerpColorRGBARGBA, posArgs, keyArgs)
            else:
                raise Exception('Error: NodePath.lerpColor: bad number of args')

        
        def lerpColorRGBA(self, r, g, b, a, time, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, r = r, g = g, b = b, a = a):
                import ColorLerpFunctor
                startColor = self.getColor()
                functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor[0], startColor[1], startColor[2], startColor[3], r, g, b, a)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpColorRGBARGBA(self, sr, sg, sb, sa, er, eg, eb, ea, time, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, sr = sr, sg = sg, sb = sb, sa = sa, er = er, eg = eg, eb = eb, ea = ea):
                import ColorLerpFunctor
                functor = ColorLerpFunctor.ColorLerpFunctor(self, sr, sg, sb, sa, er, eg, eb, ea)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpColorVBase4(self, endColor, time, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, endColor = endColor):
                import ColorLerpFunctor
                startColor = self.getColor()
                functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpColorVBase4VBase4(self, startColor, endColor, time, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, startColor = startColor, endColor = endColor):
                import ColorLerpFunctor
                functor = ColorLerpFunctor.ColorLerpFunctor(self, startColor, endColor)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpHpr(self, *posArgs, **keyArgs):
            if len(posArgs) == 4:
                return apply(self.lerpHprHPR, posArgs, keyArgs)
            elif len(posArgs) == 2:
                return apply(self.lerpHprVBase3, posArgs, keyArgs)
            else:
                raise Exception('Error: NodePath.lerpHpr: bad number of args')

        
        def lerpHprHPR(self, h, p, r, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
            
            def functorFunc(self = self, h = h, p = p, r = r, other = other, shortest = shortest):
                import HprLerpFunctor
                if other != None:
                    startHpr = self.getHpr(other)
                    functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
                    if shortest:
                        functor.takeShortest()
                    
                else:
                    startHpr = self.getHpr()
                    functor = HprLerpFunctor.HprLerpFunctor(self, startHpr[0], startHpr[1], startHpr[2], h, p, r)
                    if shortest:
                        functor.takeShortest()
                    
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpHprVBase3(self, hpr, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
            
            def functorFunc(self = self, hpr = hpr, other = other, shortest = shortest):
                import HprLerpFunctor
                if other != None:
                    functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(other), hpr, other)
                    if shortest:
                        functor.takeShortest()
                    
                else:
                    functor = HprLerpFunctor.HprLerpFunctor(self, self.getHpr(), hpr)
                    if shortest:
                        functor.takeShortest()
                    
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpPos(self, *posArgs, **keyArgs):
            if len(posArgs) == 4:
                return apply(self.lerpPosXYZ, posArgs, keyArgs)
            elif len(posArgs) == 2:
                return apply(self.lerpPosPoint3, posArgs, keyArgs)
            else:
                raise Exception('Error: NodePath.lerpPos: bad number of args')

        
        def lerpPosXYZ(self, x, y, z, time, other = None, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, x = x, y = y, z = z, other = other):
                import PosLerpFunctor
                if other != None:
                    startPos = self.getPos(other)
                    functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, other)
                else:
                    startPos = self.getPos()
                    functor = PosLerpFunctor.PosLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpPosPoint3(self, pos, time, other = None, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, pos = pos, other = other):
                import PosLerpFunctor
                if other != None:
                    functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(other), pos, other)
                else:
                    functor = PosLerpFunctor.PosLerpFunctor(self, self.getPos(), pos)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpPosHpr(self, *posArgs, **keyArgs):
            if len(posArgs) == 7:
                return apply(self.lerpPosHprXYZHPR, posArgs, keyArgs)
            elif len(posArgs) == 3:
                return apply(self.lerpPosHprPoint3VBase3, posArgs, keyArgs)
            else:
                raise Exception('Error: NodePath.lerpPosHpr: bad number of args')

        
        def lerpPosHprPoint3VBase3(self, pos, hpr, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
            
            def functorFunc(self = self, pos = pos, hpr = hpr, other = other, shortest = shortest):
                import PosHprLerpFunctor
                if other != None:
                    startPos = self.getPos(other)
                    startHpr = self.getHpr(other)
                    functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr, other)
                    if shortest:
                        functor.takeShortest()
                    
                else:
                    startPos = self.getPos()
                    startHpr = self.getHpr()
                    functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos, pos, startHpr, hpr)
                    if shortest:
                        functor.takeShortest()
                    
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpPosHprXYZHPR(self, x, y, z, h, p, r, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
            
            def functorFunc(self = self, x = x, y = y, z = z, h = h, p = p, r = r, other = other, shortest = shortest):
                import PosHprLerpFunctor
                if other != None:
                    startPos = self.getPos(other)
                    startHpr = self.getHpr(other)
                    functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r, other)
                    if shortest:
                        functor.takeShortest()
                    
                else:
                    startPos = self.getPos()
                    startHpr = self.getHpr()
                    functor = PosHprLerpFunctor.PosHprLerpFunctor(self, startPos[0], startPos[1], startPos[2], x, y, z, startHpr[0], startHpr[1], startHpr[2], h, p, r)
                    if shortest:
                        functor.takeShortest()
                    
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpPosHprScale(self, pos, hpr, scale, time, other = None, blendType = 'noBlend', auto = None, task = None, shortest = 1):
            
            def functorFunc(self = self, pos = pos, hpr = hpr, scale = scale, other = other, shortest = shortest):
                import PosHprScaleLerpFunctor
                if other != None:
                    startPos = self.getPos(other)
                    startHpr = self.getHpr(other)
                    startScale = self.getScale(other)
                    functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale, other)
                    if shortest:
                        functor.takeShortest()
                    
                else:
                    startPos = self.getPos()
                    startHpr = self.getHpr()
                    startScale = self.getScale()
                    functor = PosHprScaleLerpFunctor.PosHprScaleLerpFunctor(self, startPos, pos, startHpr, hpr, startScale, scale)
                    if shortest:
                        functor.takeShortest()
                    
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpScale(self, *posArgs, **keyArgs):
            if len(posArgs) == 4:
                return apply(self.lerpScaleXYZ, posArgs, keyArgs)
            elif len(posArgs) == 2:
                return apply(self.lerpScaleVBase3, posArgs, keyArgs)
            else:
                raise Exception('Error: NodePath.lerpScale: bad number of args')

        
        def lerpScaleVBase3(self, scale, time, other = None, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, scale = scale, other = other):
                import ScaleLerpFunctor
                if other != None:
                    functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(other), scale, other)
                else:
                    functor = ScaleLerpFunctor.ScaleLerpFunctor(self, self.getScale(), scale)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def lerpScaleXYZ(self, sx, sy, sz, time, other = None, blendType = 'noBlend', auto = None, task = None):
            
            def functorFunc(self = self, sx = sx, sy = sy, sz = sz, other = other):
                import ScaleLerpFunctor
                if other != None:
                    startScale = self.getScale(other)
                    functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz, other)
                else:
                    startScale = self.getScale()
                    functor = ScaleLerpFunctor.ScaleLerpFunctor(self, startScale[0], startScale[1], startScale[2], sx, sy, sz)
                return functor

            if auto != None:
                return self._NodePath__autoLerp(functorFunc, time, blendType, auto)
            elif task != None:
                return self._NodePath__lerp(functorFunc, time, blendType, task)
            else:
                return self._NodePath__lerp(functorFunc, time, blendType)

        
        def place(self):
            base.wantDIRECT = 1
            base.wantTk = 1
            from ShowBaseGlobal import *
            from DirectSession import *
            import TkGlobal
            import Placer
            return Placer.place(self)

        
        def explore(self):
            base.wantDIRECT = 1
            base.wantTk = 1
            from ShowBaseGlobal import *
            import TkGlobal
            import SceneGraphExplorer
            return SceneGraphExplorer.explore(self)

        
        def rgbPanel(self, cb = None):
            base.wantDIRECT = 1
            base.wantTk = 1
            from ShowBaseGlobal import *
            import TkGlobal
            import EntryScale
            return EntryScale.rgbPanel(self, cb)

        
        def select(self):
            base.wantDIRECT = 1
            base.wantTk = 1
            from ShowBaseGlobal import *
            import TkGlobal
            direct.select(self)

        
        def deselect(self):
            base.wantDIRECT = 1
            base.wantTk = 1
            from ShowBaseGlobal import *
            import TkGlobal
            direct.deselect(self)

        
        def setAlphaScale(self, alpha):
            self.setColorScale(1, 1, 1, alpha)

        
        def setAllColorScale(self, color):
            self.setColorScale(color, color, color, 1)

        
        def showCS(self, mask = None):
            npc = self.findAllMatches('**/+CollisionNode')
            for p in range(0, npc.getNumPaths()):
                np = npc[p]
                if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
                    np.show()
                
            

        
        def hideCS(self, mask = None):
            npc = self.findAllMatches('**/+CollisionNode')
            for p in range(0, npc.getNumPaths()):
                np = npc[p]
                if mask == None or (np.node().getIntoCollideMask() & mask).getWord():
                    np.hide()
                
            


    globals()['NodePath'] = NodePath

