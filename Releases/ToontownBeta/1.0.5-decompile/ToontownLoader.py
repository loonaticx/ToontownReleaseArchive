# Source Generated with Decompyle++
# File: ToontownLoader.pyo (Python 2.0)

from PandaModules import *
from DirectNotifyGlobal import *
import Loader
import LoaderGui

class ToontownLoader(Loader.Loader):
    
    def __init__(self, base):
        Loader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.expectedCount = 0
        self.count = 0
        self.gui = None

    
    def beginBulkLoad(self, name, expected, pos = None, namePos = None):
        Loader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return None
        
        self.inBulkBlock = 1
        self.blockName = name
        self.count = 0
        self.expectedCount = expected
        self.gui = LoaderGui.LoaderGui(expected, name, pos, namePos)
        self.gui.update(self.count)

    
    def endBulkLoad(self, name):
        if not (self.inBulkBlock):
            Loader.Loader.notify.warning("Tried to end a block ('%s'), but not in one" % name)
            return None
        
        if name != self.blockName:
            Loader.Loader.notify.warning("Tried to end a block ('%s'), other then the current one ('%s')" % (name, self.blockName))
            return None
        
        Loader.Loader.notify.info("At end of block '%s', expected %s, loaded %s" % (self.blockName, self.expectedCount, self.count))
        self.inBulkBlock = None
        self.gui.finish()
        del self.gui
        self.gui = None

    
    def tick(self, name):
        if self.inBulkBlock:
            self.count = self.count + 1
            self.gui.update(self.count)
        

    
    def loadModel(self, modelPath):
        ret = Loader.Loader.loadModel(self, modelPath)
        self.tick(modelPath)
        return ret

    
    def loadModelOnce(self, modelPath):
        ret = Loader.Loader.loadModelOnce(self, modelPath)
        self.tick(modelPath)
        return ret

    
    def loadModelCopy(self, modelPath):
        ret = Loader.Loader.loadModelCopy(self, modelPath)
        self.tick(modelPath)
        return ret

    
    def loadModelNode(self, modelPath):
        ret = Loader.Loader.loadModelNode(self, modelPath)
        self.tick(modelPath)
        return ret

    
    def loadFont(self, modelPath, priority = 0):
        ret = Loader.Loader.loadFont(self, modelPath, priority)
        self.tick(modelPath)
        return ret

    
    def loadTexture(self, texturePath, alphaPath = None):
        ret = Loader.Loader.loadTexture(self, texturePath, alphaPath)
        self.tick(texturePath)
        if alphaPath:
            self.tick(alphaPath)
        
        return ret

    
    def loadSound(self, soundPath):
        ret = Loader.Loader.loadSound(self, soundPath)
        self.tick(soundPath)
        return ret


