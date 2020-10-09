# Source Generated with Decompyle++
# File: RenderTraverser.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import GraphicsStateGuardian
import TypeHandle
import Ostream
import TypedObject
import TypeHandle
import ReferenceCount
import TypeHandle
import TypedReferenceCount
import ReferenceCount
import TypeHandle
import TypedObject
classDefined = 0

def generateClass_RenderTraverser():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class RenderTraverser(TypedReferenceCount.TypedReferenceCount, FFIExternalObject.FFIExternalObject):
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
            returnValue = libpanda._inPAJa7yOqU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def getGsg(self):
            returnValue = libpanda._inPAJa72meI(self.this)
            returnObject = GraphicsStateGuardian.GraphicsStateGuardian(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject.setPointer()

        
        def getGraphType(self):
            returnValue = libpanda._inPAJa7pVOB(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def output(self, out):
            returnValue = libpanda._inPAJa7klEi(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstRenderTraverser_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPAJa7rOoo(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstRenderTraverser_ptrOstream(self, out):
            returnValue = libpanda._inPAJa7pA7A(self.this, out.this)
            return returnValue

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstRenderTraverser_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstRenderTraverser_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['RenderTraverser'] = RenderTraverser

