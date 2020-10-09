# Source Generated with Decompyle++
# File: PGEntry.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Node
import TextNode
import ButtonHandle
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
import PGItem
import VBase4
import Node
import ArcChain
import PGFrameStyle
import ButtonHandle
import AudioSound
import TextNode
import TypeHandle
classDefined = 0

def generateClass_PGEntry():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class PGEntry(PGItem.PGItem, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        SFocus = 0
        SNoFocus = 1
        SInactive = 2
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_atomicstring(self, name):
            self.this = libpanda._inPVvimhLDL(name)
            self.userManagesMemory = 1

        
        def overloaded_constructor(self):
            self.this = libpanda._inPVvimQ5nG()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def getAcceptPrefix():
            returnValue = libpanda._inPVvimKnBk()
            return returnValue

        getAcceptPrefix = PandaStatic.PandaStatic(getAcceptPrefix)
        
        def getOverflowPrefix():
            returnValue = libpanda._inPVvimHcNR()
            return returnValue

        getOverflowPrefix = PandaStatic.PandaStatic(getOverflowPrefix)
        
        def getTypePrefix():
            returnValue = libpanda._inPVvimIq4_()
            return returnValue

        getTypePrefix = PandaStatic.PandaStatic(getTypePrefix)
        
        def getErasePrefix():
            returnValue = libpanda._inPVvim_UJQ()
            return returnValue

        getErasePrefix = PandaStatic.PandaStatic(getErasePrefix)
        
        def getClassType():
            returnValue = libpanda._inPVvim76ug()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def setup(self, width, numLines):
            returnValue = libpanda._inPVvimbKuL(self.this, width, numLines)
            return returnValue

        
        def setText(self, text):
            returnValue = libpanda._inPVvim5lDl(self.this, text)
            return returnValue

        
        def getText(self):
            returnValue = libpanda._inPVvim4qSc(self.this)
            return returnValue

        
        def setCursorPosition(self, position):
            returnValue = libpanda._inPVvimeGq8(self.this, position)
            return returnValue

        
        def getCursorPosition(self):
            returnValue = libpanda._inPVvimuatR(self.this)
            return returnValue

        
        def setMaxChars(self, maxChars):
            returnValue = libpanda._inPVvimgpHw(self.this, maxChars)
            return returnValue

        
        def getMaxChars(self):
            returnValue = libpanda._inPVvim4F7z(self.this)
            return returnValue

        
        def setMaxWidth(self, maxWidth):
            returnValue = libpanda._inPVvimDwva(self.this, maxWidth)
            return returnValue

        
        def getMaxWidth(self):
            returnValue = libpanda._inPVvimQLik(self.this)
            return returnValue

        
        def setNumLines(self, numLines):
            returnValue = libpanda._inPVvimMdLT(self.this, numLines)
            return returnValue

        
        def getNumLines(self):
            returnValue = libpanda._inPVvimsx9W(self.this)
            return returnValue

        
        def setBlinkRate(self, blinkRate):
            returnValue = libpanda._inPVvimgrOV(self.this, blinkRate)
            return returnValue

        
        def getBlinkRate(self):
            returnValue = libpanda._inPVvimD58v(self.this)
            return returnValue

        
        def getCursorDef(self):
            returnValue = libpanda._inPVvime56N(self.this)
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def clearCursorDef(self):
            returnValue = libpanda._inPVvimEJxG(self.this)
            return returnValue

        
        def setCursorKeysActive(self, flag):
            returnValue = libpanda._inPVvimdDwF(self.this, flag)
            return returnValue

        
        def getCursorKeysActive(self):
            returnValue = libpanda._inPVvimPryA(self.this)
            return returnValue

        
        def setTextDef(self, state, node):
            returnValue = libpanda._inPVvimFLsH(self.this, state, node.this)
            return returnValue

        
        def getTextDef(self, state):
            returnValue = libpanda._inPVvim__Bt(self.this, state)
            returnObject = TextNode.TextNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getAcceptEvent(self, button):
            returnValue = libpanda._inPVvimp_hs(self.this, button.this)
            return returnValue

        
        def getOverflowEvent(self):
            returnValue = libpanda._inPVvim6DRn(self.this)
            return returnValue

        
        def getTypeEvent(self):
            returnValue = libpanda._inPVvim_3ug(self.this)
            return returnValue

        
        def getEraseEvent(self):
            returnValue = libpanda._inPVvimBesr(self.this)
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


    globals()['PGEntry'] = PGEntry

