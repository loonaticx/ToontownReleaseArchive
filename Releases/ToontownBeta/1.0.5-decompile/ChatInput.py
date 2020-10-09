# Source Generated with Decompyle++
# File: ChatInput.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import TextNode
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
import DataNode
import TypeHandle
classDefined = 0

def generateClass_ChatInput():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ChatInput(DataNode.DataNode, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def overloaded_constructor_ptrTextNode_atomicstring(self, textNode, name):
            self.this = libpanda._inPnD0ToPUK(textNode.this, name)
            self.userManagesMemory = 1

        
        def overloaded_constructor_ptrTextNode(self, textNode):
            self.this = libpanda._inPnD0T53Up(textNode.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPnD0TuG0q:
                libpanda._inPnD0TuG0q(self.this)
            

        
        def getClassType():
            returnValue = libpanda._inPnD0T19ZI()
            returnObject = TypeHandle.TypeHandle(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClassType = PandaStatic.PandaStatic(getClassType)
        
        def reset(self):
            returnValue = libpanda._inPnD0TVtiy(self.this)
            return returnValue

        
        def setMaxChars(self, maxChars):
            returnValue = libpanda._inPnD0Ttp_h(self.this, maxChars)
            return returnValue

        
        def clearMaxChars(self):
            returnValue = libpanda._inPnD0TNEY7(self.this)
            return returnValue

        
        def hasMaxChars(self):
            returnValue = libpanda._inPnD0T35Hd(self.this)
            return returnValue

        
        def getMaxChars(self):
            returnValue = libpanda._inPnD0TDmnW(self.this)
            return returnValue

        
        def setMaxLines(self, maxLines):
            returnValue = libpanda._inPnD0T59oj(self.this, maxLines)
            return returnValue

        
        def clearMaxLines(self):
            returnValue = libpanda._inPnD0TolbB(self.this)
            return returnValue

        
        def hasMaxLines(self):
            returnValue = libpanda._inPnD0TQPxe(self.this)
            return returnValue

        
        def getMaxLines(self):
            returnValue = libpanda._inPnD0T8_QY(self.this)
            return returnValue

        
        def setMaxWidth(self, maxWidth):
            returnValue = libpanda._inPnD0TKh9P(self.this, maxWidth)
            return returnValue

        
        def clearMaxWidth(self):
            returnValue = libpanda._inPnD0TYCba(self.this)
            return returnValue

        
        def hasMaxWidth(self):
            returnValue = libpanda._inPnD0TIkxR(self.this)
            return returnValue

        
        def getMaxWidth(self):
            returnValue = libpanda._inPnD0TsyRL(self.this)
            return returnValue

        
        def getString(self):
            returnValue = libpanda._inPnD0Tr7YY(self.this)
            return returnValue

        
        def append(self, str):
            returnValue = libpanda._inPnD0TDu7P(self.this, str)
            return returnValue

        
        def appendCharacter(self, ch):
            returnValue = libpanda._inPnD0TIpJa(self.this, ch)
            return returnValue

        
        def constructor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], TextNode.TextNode):
                    return self.overloaded_constructor_ptrTextNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <TextNode.TextNode> '
            elif numArgs == 2:
                if isinstance(_args[0], TextNode.TextNode):
                    if isinstance(_args[1], types.StringType):
                        return self.overloaded_constructor_ptrTextNode_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <TextNode.TextNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '


    globals()['ChatInput'] = ChatInput

