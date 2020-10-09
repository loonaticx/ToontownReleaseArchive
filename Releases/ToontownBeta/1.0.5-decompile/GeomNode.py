# Source Generated with Decompyle++
# File: GeomNode.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Ostream
import DDrawable
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

def generateClass_GeomNode():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomNode(NamedNode.NamedNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPAJa7w4FF(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPAJa7tj9V()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getClassType():
            returnValue = libpanda._inPAJa7gvK5()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def writeVerbose(self, out, indentLevel):
            returnValue = libpanda._inPAJa7L_iE(self.this, out.this, indentLevel)
            return returnValue

        
        def getNumGeoms(self):
            returnValue = libpanda._inPAJa7BOZs(self.this)
            return returnValue

        
        def getGeom(self, n):
            returnValue = libpanda._inPAJa755Fb(self.this, n)
            returnObject = DDrawable.DDrawable(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def removeGeom(self, n):
            returnValue = libpanda._inPAJa7OXc7(self.this, n)
            return returnValue

        
        def clear(self):
            returnValue = libpanda._inPAJa70R8s(self.this)
            return returnValue

        
        def addGeom(self, geom):
            returnValue = libpanda._inPAJa7kF44(self.this, geom.this)
            return returnValue

        
        def addGeomsFrom(self, other):
            returnValue = libpanda._inPAJa7tUeu(self.this, other.this)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return self.overloaded_constructor_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 '


    globals()['GeomNode'] = GeomNode

