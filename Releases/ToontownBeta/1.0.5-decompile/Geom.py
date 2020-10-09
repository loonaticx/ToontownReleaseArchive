# Source Generated with Decompyle++
# File: Geom.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import DDrawable
import Ostream
import PTAVertexf
import PTANormalf
import PTAColorf
import PTATexCoordf
import PTAUshort
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedObject
import TypeHandle
import Writable
import TypedWritable
import Writable
import TypeHandle
import TypedObject
import WritableConfigurable
import TypeHandle
import BoundedObject
import BoundingVolume
import TypeHandle
import DDrawable
import WritableConfigurable
import BoundedObject
import TypeHandle
import ReferenceCount
import BoundingVolume
classDefined = 0

def generateClass_Geom():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Geom(DDrawable.DDrawable, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPMAKP_dZJ:
                libpanda._inPMAKP_dZJ(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPMAKPrqKN()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def overloaded_write_ptrConstGeom_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPMAKP7P2S(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstGeom_ptrOstream(self, out):
            returnValue = libpanda._inPMAKPtIjX(self.this, out.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPMAKPkxR3(self.this, out.this)
            return returnValue

        
        def writeVerbose(self, out, indentLevel):
            returnValue = libpanda._inPMAKPYE4D(self.this, out.this, indentLevel)
            return returnValue

        
        def getBinding(self, attr):
            returnValue = libpanda._inPMAKPw7es(self.this, attr)
            return returnValue

        
        def getCoordsArray(self):
            returnValue = libpanda._inPMAKPjfPn(self.this)
            returnObject = PTAVertexf.PTAVertexf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNormalsArray(self):
            returnValue = libpanda._inPMAKPmArp(self.this)
            returnObject = PTANormalf.PTANormalf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getColorsArray(self):
            returnValue = libpanda._inPMAKP0qeS(self.this)
            returnObject = PTAColorf.PTAColorf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getTexcoordsArray(self):
            returnValue = libpanda._inPMAKPhsNd(self.this)
            returnObject = PTATexCoordf.PTATexCoordf(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getCoordsIndex(self):
            returnValue = libpanda._inPMAKPDMVk(self.this)
            returnObject = PTAUshort.PTAUshort(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getNormalsIndex(self):
            returnValue = libpanda._inPMAKPnn_L(self.this)
            returnObject = PTAUshort.PTAUshort(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getColorsIndex(self):
            returnValue = libpanda._inPMAKPmojP(self.this)
            returnObject = PTAUshort.PTAUshort(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getTexcoordsIndex(self):
            returnValue = libpanda._inPMAKPlXca(self.this)
            returnObject = PTAUshort.PTAUshort(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstGeom_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstGeom_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['Geom'] = Geom

