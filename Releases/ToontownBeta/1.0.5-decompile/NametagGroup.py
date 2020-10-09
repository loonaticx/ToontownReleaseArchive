# Source Generated with Decompyle++
# File: NametagGroup.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
import Nametag2d
import Nametag3d
import Nametag
import TextFont
import Node
import MarginManager
classDefined = 0

def generateClass_NametagGroup():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NametagGroup(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        CCNormal = 0
        CCNoChat = 1
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libtoontown._inPPj7bhvyl()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPPj7bmjVz:
                libtoontown._inPPj7bmjVz(self.this)
            

        
        def getNametag2d(self):
            returnValue = libtoontown._inPPj7bKzsx(self.this)
            returnObject = Nametag2d.Nametag2d(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNametag3d(self):
            returnValue = libtoontown._inPPj7bq_Ty(self.this)
            returnObject = Nametag3d.Nametag3d(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def addNametag(self, tag):
            returnValue = libtoontown._inPPj7bS7_6(self.this, tag.this)
            return returnValue

        
        def removeNametag(self, tag):
            returnValue = libtoontown._inPPj7bfMBU(self.this, tag.this)
            return returnValue

        
        def clearAuxNametags(self):
            returnValue = libtoontown._inPPj7bTUDN(self.this)
            return returnValue

        
        def getNumNametags(self):
            returnValue = libtoontown._inPPj7boah_(self.this)
            return returnValue

        
        def getNametag(self, n):
            returnValue = libtoontown._inPPj7bYzB4(self.this, n)
            returnObject = Nametag.Nametag(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def setFont(self, font):
            returnValue = libtoontown._inPPj7bm_7P(self.this, font.this)
            return returnValue

        
        def setNameFont(self, font):
            returnValue = libtoontown._inPPj7bCkcd(self.this, font.this)
            return returnValue

        
        def getNameFont(self):
            returnValue = libtoontown._inPPj7bivcO(self.this)
            returnObject = TextFont.TextFont(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setChatFont(self, font):
            returnValue = libtoontown._inPPj7bEGW_(self.this, font.this)
            return returnValue

        
        def getChatFont(self):
            returnValue = libtoontown._inPPj7bQ1Uw(self.this)
            returnObject = TextFont.TextFont(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setAvatarNode(self, node):
            returnValue = libtoontown._inPPj7btqvF(self.this, node.this)
            return returnValue

        
        def getAvatarNode(self):
            returnValue = libtoontown._inPPj7bT20z(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def setColorCode(self, code):
            returnValue = libtoontown._inPPj7b_lVu(self.this, code)
            return returnValue

        
        def getColorCode(self):
            returnValue = libtoontown._inPPj7b_jPB(self.this)
            return returnValue

        
        def setName(self, name):
            returnValue = libtoontown._inPPj7bpoEf(self.this, name)
            return returnValue

        
        def getName(self):
            returnValue = libtoontown._inPPj7b68hN(self.this)
            return returnValue

        
        def setDisplayName(self, name):
            returnValue = libtoontown._inPPj7bkAmd(self.this, name)
            return returnValue

        
        def getDisplayName(self):
            returnValue = libtoontown._inPPj7bjkNe(self.this)
            return returnValue

        
        def setChat(self, chat, chatFlags):
            returnValue = libtoontown._inPPj7bJb5E(self.this, chat, chatFlags)
            return returnValue

        
        def clearChat(self):
            returnValue = libtoontown._inPPj7bIrZr(self.this)
            return returnValue

        
        def getChat(self):
            returnValue = libtoontown._inPPj7bMxZv(self.this)
            return returnValue

        
        def getChatFlags(self):
            returnValue = libtoontown._inPPj7b4nze(self.this)
            return returnValue

        
        def setUniqueId(self, event):
            returnValue = libtoontown._inPPj7bYufG(self.this, event)
            return returnValue

        
        def getUniqueId(self):
            returnValue = libtoontown._inPPj7bTHXj(self.this)
            return returnValue

        
        def click(self):
            returnValue = libtoontown._inPPj7bLmcI(self.this)
            return returnValue

        
        def manage(self, manager):
            returnValue = libtoontown._inPPj7bN7ks(self.this, manager.this)
            return returnValue

        
        def unmanage(self, manager):
            returnValue = libtoontown._inPPj7b3twc(self.this, manager.this)
            return returnValue

        
        def isManaged(self):
            returnValue = libtoontown._inPPj7bHm3g(self.this)
            return returnValue

        
        def setContents(self, flags):
            returnValue = libtoontown._inPPj7b8Bye(self.this, flags)
            return returnValue

        
        def getContents(self):
            returnValue = libtoontown._inPPj7b6h8E(self.this)
            return returnValue

        
        def setActive(self, active):
            returnValue = libtoontown._inPPj7bPgf_(self.this, active)
            return returnValue

        
        def isActive(self):
            returnValue = libtoontown._inPPj7bXpl9(self.this)
            return returnValue


    globals()['NametagGroup'] = NametagGroup

