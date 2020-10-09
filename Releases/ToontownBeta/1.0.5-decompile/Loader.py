# Source Generated with Decompyle++
# File: Loader.pyo (Python 2.0)

from PandaModules import *
from DirectNotifyGlobal import *
phaseChecker = None

class Loader:
    notify = directNotify.newCategory('Loader')
    
    def __init__(self, base):
        self.base = base
        self.loader = PandaLoader()

    
    def loadModel(self, modelPath):
        Loader.notify.debug('Loading model: %s' % modelPath)
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = self.loader.loadSync(Filename(modelPath))
        if node != None:
            nodePath = self.base.hidden.attachNewNode(node)
        else:
            nodePath = None
        return nodePath

    
    def loadModelOnce(self, modelPath):
        Loader.notify.debug('Loading model once: %s' % modelPath)
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        if node != None:
            nodePath = self.base.hidden.attachNewNode(node)
        else:
            nodePath = None
        return nodePath

    
    def loadModelCopy(self, modelPath):
        Loader.notify.debug('Loading model copy: %s' % modelPath)
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        if node != None:
            return NodePath(node).copyTo(self.base.hidden)
        else:
            return None

    
    def loadModelNode(self, modelPath):
        Loader.notify.debug('Loading model once node: %s' % modelPath)
        if phaseChecker:
            phaseChecker(modelPath)
        
        return ModelPool.loadModel(modelPath)

    
    def unloadModel(self, modelPath):
        Loader.notify.debug('Unloading model: %s' % modelPath)
        ModelPool.releaseModel(modelPath)

    
    def loadFont(self, modelPath, priority = 0):
        Loader.notify.debug('Loading font: %s' % modelPath)
        if phaseChecker:
            phaseChecker(modelPath)
        
        node = ModelPool.loadModel(modelPath)
        nodePath = hidden.attachNewNode(node)
        nodePath.adjustAllPriorities(priority)
        font = TextFont(node)
        nodePath.removeNode()
        return font

    
    def loadTexture(self, texturePath, alphaPath = None):
        if alphaPath == None:
            Loader.notify.debug('Loading texture: %s' % texturePath)
            if phaseChecker:
                phaseChecker(texturePath)
            
            texture = TexturePool.loadTexture(texturePath)
        else:
            Loader.notify.debug('Loading texture: %s %s' % (texturePath, alphaPath))
            if phaseChecker:
                phaseChecker(texturePath)
            
            texture = TexturePool.loadTexture(texturePath, alphaPath)
        return texture

    
    def unloadTexture(self, texture):
        Loader.notify.debug('Unloading texture: %s' % texture)
        TexturePool.releaseTexture(texture)

    
    def loadSound(self, soundPath):
        Loader.notify.debug('Loading sound: %s' % soundPath)
        if phaseChecker:
            phaseChecker(soundPath)
        
        sound = base.sfxManager.getSound(soundPath)
        return sound

    
    def unloadSound(self, sound):
        if sound:
            Loader.notify.debug('Unloading sound: %s' % sound)
            del sound
        


