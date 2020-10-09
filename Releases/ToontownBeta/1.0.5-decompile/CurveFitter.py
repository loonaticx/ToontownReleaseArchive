# Source Generated with Decompyle++
# File: CurveFitter.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase3
import ParametricCurveCollection
import Ostream
import TypeHandle
classDefined = 0

def generateClass_CurveFitter():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CurveFitter(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPHc9WFJyy()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPHc9WMi_c:
                libpanda._inPHc9WMi_c(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPHc9WLXsR()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def reset(self):
            returnValue = libpanda._inPHc9WEeBv(self.this)
            return returnValue

        
        def addXyz(self, t, xyz):
            returnValue = libpanda._inPHc9WNZs2(self.this, t, xyz.this)
            return returnValue

        
        def addHpr(self, t, hpr):
            returnValue = libpanda._inPHc9WPMH0(self.this, t, hpr.this)
            return returnValue

        
        def addXyzHpr(self, t, xyz, hpr):
            returnValue = libpanda._inPHc9W1tgF(self.this, t, xyz.this, hpr.this)
            return returnValue

        
        def getNumSamples(self):
            returnValue = libpanda._inPHc9Wqrbc(self.this)
            return returnValue

        
        def getSampleT(self, n):
            returnValue = libpanda._inPHc9WUzg8(self.this, n)
            return returnValue

        
        def getSampleXyz(self, n):
            returnValue = libpanda._inPHc9WXdCE(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getSampleHpr(self, n):
            returnValue = libpanda._inPHc9WiaDi(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def getSampleTangent(self, n):
            returnValue = libpanda._inPHc9Wz1To(self.this, n)
            returnObject = VBase3.VBase3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def removeSamples(self, begin, end):
            returnValue = libpanda._inPHc9WTerD(self.this, begin, end)
            return returnValue

        
        def sample(self, curves, count):
            returnValue = libpanda._inPHc9WmYF2(self.this, curves.this, count)
            return returnValue

        
        def wrapHpr(self):
            returnValue = libpanda._inPHc9WGQ6m(self.this)
            return returnValue

        
        def sortPoints(self):
            returnValue = libpanda._inPHc9WNLWM(self.this)
            return returnValue

        
        def desample(self, factor):
            returnValue = libpanda._inPHc9WXRBy(self.this, factor)
            return returnValue

        
        def computeTangents(self, scale):
            returnValue = libpanda._inPHc9WlLxM(self.this, scale)
            return returnValue

        
        def makeHermite(self):
            returnValue = libpanda._inPHc9WMJIh(self.this)
            returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def makeNurbs(self):
            returnValue = libpanda._inPHc9WiDGN(self.this)
            returnObject = ParametricCurveCollection.ParametricCurveCollection(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def output(self, out):
            returnValue = libpanda._inPHc9WYdRp(self.this, out.this)
            return returnValue

        
        def write(self, out):
            returnValue = libpanda._inPHc9WQViW(self.this, out.this)
            return returnValue


    globals()['CurveFitter'] = CurveFitter

