# Source Generated with Decompyle++
# File: CullTraverser.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GeomBin
import Ostream
import TraverserVisitorNullTransitionWrapperCullLevelState
import TypeHandle
import GraphicsStateGuardian
import RenderTraverser
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
import RenderTraverser
import GraphicsStateGuardian
import TypeHandle
import Ostream
import TraverserVisitorNullTransitionWrapperCullLevelState
classDefined = 0

def generateClass_CullTraverser():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class CullTraverser(RenderTraverser.RenderTraverser, TraverserVisitorNullTransitionWrapperCullLevelState.TraverserVisitorNullTransitionWrapperCullLevelState, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPspg2AHzC:
                libpanda._inPspg2AHzC(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPspg2QPEh()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def hasBin(self, name):
            returnValue = libpanda._inPspg2XIXK(self.this, name)
            return returnValue

        
        def getBin(self, name):
            returnValue = libpanda._inPspg2NJ95(self.this, name)
            returnObject = GeomBin.GeomBin(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearBins(self):
            returnValue = libpanda._inPspg2ebDr(self.this)
            return returnValue

        
        def clearState(self):
            returnValue = libpanda._inPspg2iUbt(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPspg2j0R2(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstCullTraverser_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPspg2EIu5(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstCullTraverser_ptrOstream(self, out):
            returnValue = libpanda._inPspg2FlUC(self.this, out.this)
            return returnValue

        
        def upcastToTraverserVisitorNullTransitionWrapperCullLevelState(self):
            returnValue = libpanda._inPspg2kq51(self.this)
            returnObject = TraverserVisitorNullTransitionWrapperCullLevelState.TraverserVisitorNullTransitionWrapperCullLevelState(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def getGsg(self):
            upcastSelf = self
            returnValue = libpanda._inPAJa72meI(upcastSelf.this)
            returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getGraphType(self):
            upcastSelf = self
            returnValue = libpanda._inPAJa7pVOB(upcastSelf.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
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

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstCullTraverser_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstCullTraverser_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['CullTraverser'] = CullTraverser

