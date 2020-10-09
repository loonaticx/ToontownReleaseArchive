# Source Generated with Decompyle++
# File: NodeTransition.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
import TypeHandle
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
classDefined = 0

def generateClass_NodeTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NodeTransition(TypedWritableReferenceCount.TypedWritableReferenceCount, FFIExternalObject.FFIExternalObject):
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
            if libpanda and libpanda._inPs9JIDqzZ:
                libpanda._inPs9JIDqzZ(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPs9JI4DXI()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setPriority(self, priority):
            returnValue = libpanda._inPs9JIyAah(self.this, priority)
            return returnValue

        
        def getPriority(self):
            returnValue = libpanda._inPs9JIW86b(self.this)
            return returnValue

        
        def output(self, out):
            returnValue = libpanda._inPs9JI7_ww(self.this, out.this)
            return returnValue

        
        def overloaded_write_ptrConstNodeTransition_ptrOstream_int(self, out, indentLevel):
            returnValue = libpanda._inPs9JIWI7e(self.this, out.this, indentLevel)
            return returnValue

        
        def overloaded_write_ptrConstNodeTransition_ptrOstream(self, out):
            returnValue = libpanda._inPs9JIWFtx(self.this, out.this)
            return returnValue

        
        def write(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], Ostream.Ostream):
                    return self.overloaded_write_ptrConstNodeTransition_ptrOstream(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            elif numArgs == 2:
                if isinstance(_args[0], Ostream.Ostream):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_write_ptrConstNodeTransition_ptrOstream_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <Ostream.Ostream> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['NodeTransition'] = NodeTransition

