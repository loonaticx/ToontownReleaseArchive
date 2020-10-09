# Source Generated with Decompyle++
# File: Settings.pyo (Python 2.0)

import PandaStatic
import types
import libtoontown
import libtoontownDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_Settings():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class Settings(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libtoontownDowncasts]
        GL = 0
        DX = 1
        DNONE = 2
        RNONE = 2
        R800x600 = 1
        R640x480 = 0
        SNONE = 3
        DEVELOPMENT = 1
        PRODUCTION = 0
        DEBUG = 2
        
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
            if libtoontown and libtoontown._inPvzzk6nGO:
                libtoontown._inPvzzk6nGO(self.this)
            

        
        def wantSfx():
            returnValue = libtoontown._inPvzzkJoR_()
            return returnValue

        wantSfx = PandaStatic.PandaStatic(wantSfx)
        
        def wantMusic():
            returnValue = libtoontown._inPvzzkBFle()
            return returnValue

        wantMusic = PandaStatic.PandaStatic(wantMusic)
        
        def wantChatLog():
            returnValue = libtoontown._inPvzzknSsU()
            return returnValue

        wantChatLog = PandaStatic.PandaStatic(wantChatLog)
        
        def masterSfxVolume():
            returnValue = libtoontown._inPvzzkC7Ne()
            return returnValue

        masterSfxVolume = PandaStatic.PandaStatic(masterSfxVolume)
        
        def masterMusicVolume():
            returnValue = libtoontown._inPvzzkNrH0()
            return returnValue

        masterMusicVolume = PandaStatic.PandaStatic(masterMusicVolume)
        
        def displayDriver():
            returnValue = libtoontown._inPvzzkbCbR()
            return returnValue

        displayDriver = PandaStatic.PandaStatic(displayDriver)
        
        def resolution():
            returnValue = libtoontown._inPvzzkbRV5()
            return returnValue

        resolution = PandaStatic.PandaStatic(resolution)
        
        def serverType():
            returnValue = libtoontown._inPvzzkcZBc()
            return returnValue

        serverType = PandaStatic.PandaStatic(serverType)
        
        def setSfx(parameter0):
            returnValue = libtoontown._inPvzzkn2U5(parameter0)
            return returnValue

        setSfx = PandaStatic.PandaStatic(setSfx)
        
        def setMusic(parameter0):
            returnValue = libtoontown._inPvzzkmtiE(parameter0)
            return returnValue

        setMusic = PandaStatic.PandaStatic(setMusic)
        
        def setChatLog(parameter0):
            returnValue = libtoontown._inPvzzkPmX_(parameter0)
            return returnValue

        setChatLog = PandaStatic.PandaStatic(setChatLog)
        
        def setSfxVolume(parameter0):
            returnValue = libtoontown._inPvzzkPxyv(parameter0)
            return returnValue

        setSfxVolume = PandaStatic.PandaStatic(setSfxVolume)
        
        def setMusicVolume(parameter0):
            returnValue = libtoontown._inPvzzkNr8p(parameter0)
            return returnValue

        setMusicVolume = PandaStatic.PandaStatic(setMusicVolume)
        
        def setDisplayDriver(parameter0):
            returnValue = libtoontown._inPvzzkaRug(parameter0)
            return returnValue

        setDisplayDriver = PandaStatic.PandaStatic(setDisplayDriver)
        
        def setResolution(parameter0):
            returnValue = libtoontown._inPvzzklpdA(parameter0)
            return returnValue

        setResolution = PandaStatic.PandaStatic(setResolution)
        
        def setServerType(parameter0):
            returnValue = libtoontown._inPvzzkU2gR(parameter0)
            return returnValue

        setServerType = PandaStatic.PandaStatic(setServerType)
        
        def writeSettings():
            returnValue = libtoontown._inPvzzkA7MG()
            return returnValue

        writeSettings = PandaStatic.PandaStatic(writeSettings)

    globals()['Settings'] = Settings

