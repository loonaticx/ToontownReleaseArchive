# Source Generated with Decompyle++
# File: GeomBinTransition.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
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
import NodeTransition
import Ostream
import TypeHandle
import OnOffTransition
import TypeHandle
classDefined = 0

def generateClass_GeomBinTransition():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomBinTransition(OnOffTransition.OnOffTransition, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor(self):
            self.this = libpanda._inPspg2nx4L()
            self.userManagesMemory = 1

        
        def overloaded_constructor_atomicstring_int(self, bin, drawOrder):
            self.this = libpanda._inPspg28VhU(bin, drawOrder)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPspg24tRl:
                libpanda._inPspg24tRl(self.this)
            

        
        def off():
            returnValue = libpanda._inPspg2R50h()
            returnObject = GeomBinTransition(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        off = PandaStatic.PandaStatic(off)
        
        def getClassType():
            returnValue = libpanda._inPspg25GEU()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setOn(self, bin, drawOrder):
            returnValue = libpanda._inPspg2Flhl(self.this, bin, drawOrder)
            return returnValue

        
        def getBin(self):
            returnValue = libpanda._inPspg2ERLr(self.this)
            return returnValue

        
        def getDrawOrder(self):
            returnValue = libpanda._inPspg2EOD_(self.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_constructor_atomicstring_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 2 '


    globals()['GeomBinTransition'] = GeomBinTransition

