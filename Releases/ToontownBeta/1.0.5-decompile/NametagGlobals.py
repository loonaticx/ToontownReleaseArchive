# Source Generated with Decompyle++
# File: NametagGlobals.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
import Camera
import Node
import VBase4
import AudioSound
import MouseWatcher
import ChatBalloon
classDefined = 0

def generateClass_NametagGlobals():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class NametagGlobals(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        
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
            if libtoontown and libtoontown._inPPj7bObF8:
                libtoontown._inPPj7bObF8(self.this)
            

        
        def setCamera(node):
            returnValue = libtoontown._inPPj7bETTK(node.this)
            return returnValue

        setCamera = PandaStatic.PandaStatic(setCamera)
        
        def getCamera():
            returnValue = libtoontown._inPPj7bYeEo()
            returnObject = Camera.Camera(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getCamera = PandaStatic.PandaStatic(getCamera)
        
        def setToonNode(node):
            returnValue = libtoontown._inPPj7bMBpj(node.this)
            return returnValue

        setToonNode = PandaStatic.PandaStatic(setToonNode)
        
        def getToonNode():
            returnValue = libtoontown._inPPj7b9LKa()
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getToonNode = PandaStatic.PandaStatic(getToonNode)
        
        def setArrowModel(node):
            returnValue = libtoontown._inPPj7b4ET1(node.this)
            return returnValue

        setArrowModel = PandaStatic.PandaStatic(setArrowModel)
        
        def getArrowModel():
            returnValue = libtoontown._inPPj7bXH4M()
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getArrowModel = PandaStatic.PandaStatic(getArrowModel)
        
        def setNametagCard(node, frame):
            returnValue = libtoontown._inPPj7bjX4m(node.this, frame.this)
            return returnValue

        setNametagCard = PandaStatic.PandaStatic(setNametagCard)
        
        def getNametagCard():
            returnValue = libtoontown._inPPj7bTEer()
            returnObject = Node.Node(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getNametagCard = PandaStatic.PandaStatic(getNametagCard)
        
        def getNametagCardFrame():
            returnValue = libtoontown._inPPj7bkOLj()
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        getNametagCardFrame = PandaStatic.PandaStatic(getNametagCardFrame)
        
        def setRolloverSound(sound):
            returnValue = libtoontown._inPPj7bjSN4(sound.this)
            return returnValue

        setRolloverSound = PandaStatic.PandaStatic(setRolloverSound)
        
        def getRolloverSound():
            returnValue = libtoontown._inPPj7b9T7T()
            returnObject = AudioSound.AudioSound(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getRolloverSound = PandaStatic.PandaStatic(getRolloverSound)
        
        def setClickSound(sound):
            returnValue = libtoontown._inPPj7bUrDq(sound.this)
            return returnValue

        setClickSound = PandaStatic.PandaStatic(setClickSound)
        
        def getClickSound():
            returnValue = libtoontown._inPPj7bKGg2()
            returnObject = AudioSound.AudioSound(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getClickSound = PandaStatic.PandaStatic(getClickSound)
        
        def setMouseWatcher(watcher):
            returnValue = libtoontown._inPPj7bI_gS(watcher.this)
            return returnValue

        setMouseWatcher = PandaStatic.PandaStatic(setMouseWatcher)
        
        def getMouseWatcher():
            returnValue = libtoontown._inPPj7bcgmX()
            returnObject = MouseWatcher.MouseWatcher(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        getMouseWatcher = PandaStatic.PandaStatic(getMouseWatcher)
        
        def setSpeechBalloon2d(balloon):
            returnValue = libtoontown._inPPj7bo269(balloon.this)
            return returnValue

        setSpeechBalloon2d = PandaStatic.PandaStatic(setSpeechBalloon2d)
        
        def getSpeechBalloon2d():
            returnValue = libtoontown._inPPj7b8YzZ()
            returnObject = ChatBalloon.ChatBalloon(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getSpeechBalloon2d = PandaStatic.PandaStatic(getSpeechBalloon2d)
        
        def setThoughtBalloon2d(balloon):
            returnValue = libtoontown._inPPj7bv4hI(balloon.this)
            return returnValue

        setThoughtBalloon2d = PandaStatic.PandaStatic(setThoughtBalloon2d)
        
        def getThoughtBalloon2d():
            returnValue = libtoontown._inPPj7bXNHc()
            returnObject = ChatBalloon.ChatBalloon(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getThoughtBalloon2d = PandaStatic.PandaStatic(getThoughtBalloon2d)
        
        def setSpeechBalloon3d(balloon):
            returnValue = libtoontown._inPPj7bnIYA(balloon.this)
            return returnValue

        setSpeechBalloon3d = PandaStatic.PandaStatic(setSpeechBalloon3d)
        
        def getSpeechBalloon3d():
            returnValue = libtoontown._inPPj7b8iRc()
            returnObject = ChatBalloon.ChatBalloon(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getSpeechBalloon3d = PandaStatic.PandaStatic(getSpeechBalloon3d)
        
        def setThoughtBalloon3d(balloon):
            returnValue = libtoontown._inPPj7bu4mW(balloon.this)
            return returnValue

        setThoughtBalloon3d = PandaStatic.PandaStatic(setThoughtBalloon3d)
        
        def getThoughtBalloon3d():
            returnValue = libtoontown._inPPj7bSNOq()
            returnObject = ChatBalloon.ChatBalloon(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        getThoughtBalloon3d = PandaStatic.PandaStatic(getThoughtBalloon3d)
        
        def setMasterNametagsActive(active):
            returnValue = libtoontown._inPPj7bpQDt(active)
            return returnValue

        setMasterNametagsActive = PandaStatic.PandaStatic(setMasterNametagsActive)
        
        def getMasterNametagsActive():
            returnValue = libtoontown._inPPj7b35_m()
            return returnValue

        getMasterNametagsActive = PandaStatic.PandaStatic(getMasterNametagsActive)
        
        def setMasterArrowsOn(active):
            returnValue = libtoontown._inPPj7bNmYq(active)
            return returnValue

        setMasterArrowsOn = PandaStatic.PandaStatic(setMasterArrowsOn)
        
        def getMasterArrowsOn():
            returnValue = libtoontown._inPPj7bkjpy()
            return returnValue

        getMasterArrowsOn = PandaStatic.PandaStatic(getMasterArrowsOn)
        
        def setMax2dAlpha(alpha):
            returnValue = libtoontown._inPPj7bJt8N(alpha)
            return returnValue

        setMax2dAlpha = PandaStatic.PandaStatic(setMax2dAlpha)
        
        def getMax2dAlpha():
            returnValue = libtoontown._inPPj7bYaRF()
            return returnValue

        getMax2dAlpha = PandaStatic.PandaStatic(getMax2dAlpha)
        
        def setMin2dAlpha(alpha):
            returnValue = libtoontown._inPPj7bZsrn(alpha)
            return returnValue

        setMin2dAlpha = PandaStatic.PandaStatic(setMin2dAlpha)
        
        def getMin2dAlpha():
            returnValue = libtoontown._inPPj7bIh_e()
            return returnValue

        getMin2dAlpha = PandaStatic.PandaStatic(getMin2dAlpha)

    globals()['NametagGlobals'] = NametagGlobals

