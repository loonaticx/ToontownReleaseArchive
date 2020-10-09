# Source Generated with Decompyle++
# File: ChatBalloon.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import Node
import ReferenceCount
import TypeHandle
classDefined = 0

def generateClass_ChatBalloon():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ChatBalloon(ReferenceCount.ReferenceCount, FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts,
            libpandaexpressDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self, rootNode):
            self.this = libtoontown._inPPj7b470x(rootNode.this)
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libtoontown and libtoontown._inPPj7b3a4o:
                libtoontown._inPPj7b3a4o(self.this)
            


    globals()['ChatBalloon'] = ChatBalloon

