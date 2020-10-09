# Source Generated with Decompyle++
# File: GeomBin.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import CullTraverser
import Ostream
import Namable
import TypeHandle
import ReferenceCount
import TypedReferenceCount
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import Namable
import Ostream
import TypeHandle
classDefined = 0

def generateClass_GeomBin():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomBin(TypedReferenceCount.TypedReferenceCount, Namable.Namable, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPspg2zd2_:
                libpanda._inPspg2zd2_(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPspg2jdUw()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setName(self, name):
            returnValue = libpanda._inPspg2RktU(self.this, name)
            return returnValue

        
        def clearName(self):
            returnValue = libpanda._inPspg2hlBk(self.this)
            return returnValue

        
        def getSort(self):
            returnValue = libpanda._inPspg2RcfH(self.this)
            return returnValue

        
        def setSort(self, sort):
            returnValue = libpanda._inPspg2fco1(self.this, sort)
            return returnValue

        
        def setActive(self, active):
            returnValue = libpanda._inPspg2bC9E(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libpanda._inPspg2F1_j(self.this)
            return returnValue

        
        def setTraverser(self, traverser):
            returnValue = libpanda._inPspg2Nty7(self.this, traverser.this)
            return returnValue

        
        def hasTraverser(self):
            returnValue = libpanda._inPspg27z_e(self.this)
            return returnValue

        
        def getTraverser(self):
            returnValue = libpanda._inPspg2Klvp(self.this)
            returnObject = CullTraverser.CullTraverser(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def clearTraverser(self):
            returnValue = libpanda._inPspg2Oc_P(self.this)
            returnObject = GeomBin(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def hasParent(self):
            returnValue = libpanda._inPspg20gyy(self.this)
            return returnValue

        
        def getParent(self):
            returnValue = libpanda._inPspg28Hh9(self.this)
            returnObject = GeomBin(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def output(self, out):
            returnValue = libpanda._inPspg20gnp(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstGeomBin_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPspg2Fzpx(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstGeomBin_ptrOstream(self, out):
            returnValue = libpanda._inPspg2vyy9(self.this, out.this)
            return returnValue

        
        def upcastToNamable(self):
            returnValue = libpanda._inPspg2Sm3E(self.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def upcastToReferenceCount(self):
            upcastSelf = self
            returnValue = libpandaexpress._inPKoxtDe8f(upcastSelf.this)
            returnObject = ReferenceCount.ReferenceCount(None)
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

        
        def assign(self, other):
            upcastSelf = self
            upcastSelf = upcastSelf.upcastToNamable()
            returnValue = libpandaexpress._inPKoxtiPcI(upcastSelf.this, other.this)
            returnObject = Namable.Namable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
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

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstGeomBin_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstGeomBin_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['GeomBin'] = GeomBin

