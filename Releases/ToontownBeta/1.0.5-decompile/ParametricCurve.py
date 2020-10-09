# Source Generated with Decompyle++
# File: ParametricCurve.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import VBase3
import Filename
import Ostream
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
classDefined = 0

def generateClass_ParametricCurve():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ParametricCurve(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inPHc9WrwO8()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def isValid(self):
            returnValue = libpanda._inPHc9WZdM7(self.this)
            return returnValue

        
        def getMaxT(self):
            returnValue = libpanda._inPHc9WTB4O(self.this)
            return returnValue

        
        def setCurveType(self, type):
            returnValue = libpanda._inPHc9WnAfd(self.this, type)
            return returnValue

        
        def getCurveType(self):
            returnValue = libpanda._inPHc9WnpVX(self.this)
            return returnValue

        
        def setNumDimensions(self, num):
            returnValue = libpanda._inPHc9WDI0T(self.this, num)
            return returnValue

        
        def getNumDimensions(self):
            returnValue = libpanda._inPHc9Wed71(self.this)
            return returnValue

        
        def overloaded_calcLength_ptrConstParametricCurve(self):
            returnValue = libpanda._inPHc9WUqeF(self.this)
            return returnValue

        
        def overloaded_calcLength_ptrConstParametricCurve_float_float(self, _from, to):
            returnValue = libpanda._inPHc9W6hNZ(self.this, _from, to)
            return returnValue

        
        def findLength(self, startT, lengthOffset):
            returnValue = libpanda._inPHc9W_LMm(self.this, startT, lengthOffset)
            return returnValue

        
        def getPoint(self, t, point):
            returnValue = libpanda._inPHc9WhTPE(self.this, t, point.this)
            return returnValue

        
        def getTangent(self, t, tangent):
            returnValue = libpanda._inPHc9W_cs0(self.this, t, tangent.this)
            return returnValue

        
        def getPt(self, t, point, tangent):
            returnValue = libpanda._inPHc9WIoPy(self.this, t, point.this, tangent.this)
            return returnValue

        
        def get2ndtangent(self, t, tangent2):
            returnValue = libpanda._inPHc9WIPja(self.this, t, tangent2.this)
            return returnValue

        
        def adjustPoint(self, t, px, py, pz):
            returnValue = libpanda._inPHc9WzJWs(self.this, t, px, py, pz)
            return returnValue

        
        def adjustTangent(self, t, tx, ty, tz):
            returnValue = libpanda._inPHc9WclxE(self.this, t, tx, ty, tz)
            return returnValue

        
        def adjustPt(self, t, px, py, pz, tx, ty, tz):
            returnValue = libpanda._inPHc9Wq0cM(self.this, t, px, py, pz, tx, ty, tz)
            return returnValue

        
        def recompute(self):
            returnValue = libpanda._inPHc9Wgg_o(self.this)
            return returnValue

        
        def stitch(self, a, b):
            returnValue = libpanda._inPHc9WDE8P(self.this, a.this, b.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(self, filename, cs):
            returnValue = libpanda._inPHc9W4EHa(self.this, filename.this, cs)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrFilename(self, filename):
            returnValue = libpanda._inPHc9WqZwA(self.this, filename.this)
            return returnValue

        
        def overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(self, out, filename, cs):
            returnValue = libpanda._inPHc9Wohju(self.this, out.this, filename.this, cs)
            return returnValue

        
        def calcLength(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_calcLength_ptrConstParametricCurve()
            elif numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_calcLength_ptrConstParametricCurve_float_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '

        
        def writeEgg(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Filename.Filename):
                    return self.overloaded_writeEgg_ptrParametricCurve_ptrFilename(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            elif numArgs == 2:
                if isinstance(_args[0], Filename.Filename):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_writeEgg_ptrParametricCurve_ptrFilename___enum__CoordinateSystem(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Filename.Filename> '
            elif numArgs == 3:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], Filename.Filename):
                        if isinstance(_args[2], types.IntType):
                            return self.overloaded_writeEgg_ptrParametricCurve_ptrOstream_ptrConstFilename___enum__CoordinateSystem(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.IntType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Filename.Filename> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 3 '


    globals()['ParametricCurve'] = ParametricCurve

