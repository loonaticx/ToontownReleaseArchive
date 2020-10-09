# Source Generated with Decompyle++
# File: GeomParticleRenderer.pyo (Python 2.0)

import PandaStatic
import types
import libpandaphysics
import libpandaphysicsDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Node
import BaseParticleRenderer
import ReferenceCount
import TypeHandle
import BaseParticleRenderer
import GeomNode
classDefined = 0

def generateClass_GeomParticleRenderer():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class GeomParticleRenderer(BaseParticleRenderer.BaseParticleRenderer, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaphysicsDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode_ptrNode(self, am, geomNode):
            self.this = libpandaphysics._inPKBUAi7YN(am, geomNode.this)
            self.userManagesMemory = 1

        
        def overloaded_constructor___enum__ParticleRendererAlphaMode(self, am):
            self.this = libpandaphysics._inPKBUAJH4X(am)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpandaphysics._inPKBUAjDgG()
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrConstGeomParticleRenderer(self, copy):
            self.this = libpandaphysics._inPKBUAYTd7(copy.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpandaphysics and libpandaphysics._inPKBUAVz5b:
                libpandaphysics._inPKBUAVz5b(self.this)
            

        
        def setGeomNode(self, node):
            returnValue = libpandaphysics._inPKBUAfZ3z(self.this, node.this)
            return returnValue

        
        def getGeomNode(self):
            returnValue = libpandaphysics._inPKBUAPlyT(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_constructor()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_constructor___enum__ParticleRendererAlphaMode(_args[0])
                elif isinstance(_args[0], GeomParticleRenderer):
                    return self.overloaded_constructor_ptrConstGeomParticleRenderer(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <GeomParticleRenderer> '
            elif numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Node.Node):
                        return self.overloaded_constructor___enum__ParticleRendererAlphaMode_ptrNode(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Node.Node> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '


    globals()['GeomParticleRenderer'] = GeomParticleRenderer

