# Source Generated with Decompyle++
# File: Nametag.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import NametagGroup
import Node
import TypeHandle
import ReferenceCount
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_Nametag():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Nametag(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        CName = 1
        CSpeech = 2
        CThought = 4
        
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
            if libtoontown and libtoontown._inPPj7bKHI6:
                libtoontown._inPPj7bKHI6(self.this)
            

        
        def getClassType():
            returnValue = libtoontown._inPPj7brgKv()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setContents(self, flags):
            returnValue = libtoontown._inPPj7bEeaT(self.this, flags)
            return returnValue

        
        def getContents(self):
            returnValue = libtoontown._inPPj7bCegG(self.this)
            return returnValue

        
        def setActive(self, active):
            returnValue = libtoontown._inPPj7bLFzD(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libtoontown._inPPj7bhm1i(self.this)
            return returnValue

        
        def hasGroup(self):
            returnValue = libtoontown._inPPj7bMiee(self.this)
            return returnValue

        
        def getGroup(self):
            returnValue = libtoontown._inPPj7bU9Np(self.this)
            returnObject = NametagGroup.NametagGroup(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def setDrawOrder(self, drawOrder):
            returnValue = libtoontown._inPPj7batHf(self.this, drawOrder)
            return returnValue

        
        def clearDrawOrder(self):
            returnValue = libtoontown._inPPj7b_Mq7(self.this)
            return returnValue

        
        def setChatWordwrap(self, wordwrap):
            returnValue = libtoontown._inPPj7bfcNR(self.this, wordwrap)
            return returnValue

        
        def getChatWordwrap(self):
            returnValue = libtoontown._inPPj7bb3ZX(self.this)
            return returnValue

        
        def setAvatarNode(self, node):
            returnValue = libtoontown._inPPj7bnq5m(self.this, node.this)
            return returnValue

        
        def clearAvatarNode(self):
            returnValue = libtoontown._inPPj7bBm0m(self.this)
            return returnValue

        
        def getAvatarNode(self):
            returnValue = libtoontown._inPPj7bTt6d(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getType(self):
            returnValue = libtoontown._inPPj7bK3Xg(self.this)
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def upcastToReferenceCount(self):
            returnValue = libtoontown._inPPj7bd6q5(self.this)
            returnObject = ReferenceCount.ReferenceCount(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject


    globals()['Nametag'] = Nametag

