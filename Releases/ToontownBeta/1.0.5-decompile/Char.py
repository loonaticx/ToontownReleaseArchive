# Source Generated with Decompyle++
# File: Char.pyo (Python 2.0)

import Avatar
from PandaModules import *
MickeyDialogueArray = []
MinnieDialogueArray = []
GoofyDialogueArray = []
DonaldDialogueArray = []
AnimDict = {
    'mk': (('walk', '-walk'), ('run', '-run'), ('neutral', '-wait')),
    'mn': (('walk', '-walk'), ('run', '-run'), ('neutral', '-wait')),
    'g': (('walk', 'Walk'), ('run', 'Run'), ('neutral', 'Wait')),
    'd': (('walk', 'Walk'), ('run', 'Run'), ('neutral', 'Wait')) }
ModelDict = {
    'mk': 'phase_3/models/char/mickey',
    'mn': 'phase_4/models/char/minnie',
    'g': 'phase_6/models/char/TT_G',
    'd': 'phase_6/models/char/TT_D' }
LODModelDict = {
    'mk': [
        1200,
        800,
        400],
    'mn': [
        1200,
        800,
        400],
    'g': [
        1500,
        1000,
        500],
    'd': [
        1500,
        1000,
        500] }

def loadDialogue(char):
    if char == 'mk':
        dialogueFile = base.loadSfx('phase_3/audio/dial/mickey.wav')
        for i in range(0, 6):
            MickeyDialogueArray.append(dialogueFile)
        
    elif char == 'mn':
        dialogueFile = base.loadSfx('phase_3/audio/dial/minnie.wav')
        for i in range(0, 6):
            MinnieDialogueArray.append(dialogueFile)
        
    elif char == 'g':
        dialogueFile = base.loadSfx('phase_3/audio/dial/goofy.wav')
        for i in range(0, 6):
            GoofyDialogueArray.append(dialogueFile)
        
    elif char == 'd':
        dialogueFile = base.loadSfx('phase_3/audio/dial/donald.wav')
        for i in range(0, 6):
            DonaldDialogueArray.append(dialogueFile)
        
    else:
        print 'Error: unknown character %s' % char


def unloadDialogue(char):
    global MickeyDialogueArray, MinnieDialogueArray, GoofyDialogueArray, DonaldDialogueArray
    if char == 'mk':
        for sfx in MickeyDialogueArray:
            base.unloadSfx(sfx)
        
        MickeyDialogueArray = []
    elif char == 'mn':
        for sfx in MinnieDialogueArray:
            base.unloadSfx(sfx)
        
        MinnieDialogueArray = []
    elif char == 'g':
        for sfx in GoofyDialogueArray:
            base.unloadSfx(sfx)
        
        GoofyDialogueArray = []
    elif char == 'd':
        for sfx in DonaldDialogueArray:
            base.unloadSfx(sfx)
        
        DonaldDialogueArray = []
    else:
        print 'Error: unknown character %s' % char


class Char(Avatar.Avatar):
    
    def __init__(self):
        
        try:
            self.Char_initialized
        except:
            self.Char_initialized = 1
            Avatar.Avatar.__init__(self)

        return None

    
    def delete(self):
        
        try:
            self.Char_deleted
        except:
            self.Char_deleted = 1
            unloadDialogue(self.style.name)
            filePrefix = ModelDict[self.style.name]
            loader.unloadModel(filePrefix + '-' + str(LODModelDict[self.style.name][0]))
            loader.unloadModel(filePrefix + '-' + str(LODModelDict[self.style.name][1]))
            loader.unloadModel(filePrefix + '-' + str(LODModelDict[self.style.name][2]))
            animList = AnimDict[self.style.name]
            for anim in animList:
                loader.unloadModel(filePrefix + anim[1])
            
            Avatar.Avatar.delete(self)

        return None

    
    def updateCharDNA(self, newDNA):
        if newDNA.name != self.style.name:
            self.swapCharModel(newDNA)
        

    
    def setLODs(self):
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 50)
        levelOneOut = base.config.GetInt('lod1-out', 1)
        levelTwoIn = base.config.GetInt('lod2-in', 100)
        levelTwoOut = base.config.GetInt('lod2-out', 50)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 100)
        self.addLOD(LODModelDict[self.style.name][2], levelThreeIn, levelThreeOut)
        self.addLOD(LODModelDict[self.style.name][1], levelTwoIn, levelTwoOut)
        self.addLOD(LODModelDict[self.style.name][0], levelOneIn, levelOneOut)

    
    def generateChar(self):
        self.setLODs()
        dna = self.style
        name = dna.getCharName()
        if name == 'mickey':
            filePrefix = ModelDict[dna.name]
            height = 3.0
        elif name == 'minnie':
            filePrefix = ModelDict[dna.name]
            height = 3.0
        elif name == 'goofy':
            filePrefix = ModelDict[dna.name]
            height = 6.0
        elif name == 'donald':
            filePrefix = ModelDict[dna.name]
            height = 4.5
        
        lod1 = str(LODModelDict[self.style.name][0])
        lod2 = str(LODModelDict[self.style.name][1])
        lod3 = str(LODModelDict[self.style.name][2])
        loader.loadModel(filePrefix + '-' + lod1)
        loader.loadModel(filePrefix + '-' + lod2)
        loader.loadModel(filePrefix + '-' + lod3)
        self.loadModel(filePrefix + '-' + lod1, lodName = lod1)
        self.loadModel(filePrefix + '-' + lod2, lodName = lod2)
        self.loadModel(filePrefix + '-' + lod3, lodName = lod3)
        animDict = { }
        animList = AnimDict[self.style.name]
        for anim in animList:
            animDict[anim[0]] = filePrefix + anim[1]
        
        self.loadAnims(animDict, lodName = lod1)
        self.loadAnims(animDict, lodName = lod2)
        self.loadAnims(animDict, lodName = lod3)
        self.setHeight(height)
        loadDialogue(dna.name)
        if name == 'mickey' or name == 'minnie':
            earCollection = self.findAllMatches('**/sphere3')
            numEars = earCollection.getNumPaths()
            for earNum in range(0, numEars):
                earCollection.getPath(earNum).setHpr(0, 0, 0)
            
        

    
    def swapCharModel(self, charStyle):
        lod1 = str(LODModelDict[self.style.name][0])
        lod2 = str(LODModelDict[self.style.name][1])
        lod3 = str(LODModelDict[self.style.name][2])
        self.removePart('modelRoot', lodName = lod1)
        self.removePart('modelRoot', lodName = lod2)
        self.removePart('modelRoot', lodName = lod3)
        self.setStyle(charStyle)
        self.generateChar()

    
    def playDialogue(self, type, length):
        animalType = self.style.getType()
        if animalType == 'mickey':
            dialogueArray = MickeyDialogueArray
        elif animalType == 'minnie':
            dialogueArray = MinnieDialogueArray
        elif animalType == 'goofy':
            dialogueArray = GoofyDialogueArray
        elif animalType == 'donald':
            dialogueArray = DonaldDialogueArray
        
        if type == 'statementA' or type == 'statementB':
            if length == 1:
                if dialogueArray[0] != None:
                    base.playSfx(dialogueArray[0])
                
            
            if length == 2:
                if dialogueArray[1] != None:
                    base.playSfx(dialogueArray[1])
                
            
            if length >= 3:
                if dialogueArray[2] != None:
                    base.playSfx(dialogueArray[2])
                
            
        elif type == 'question':
            if dialogueArray[3] != None:
                base.playSfx(dialogueArray[3])
            
        elif type == 'exclamation':
            if dialogueArray[4] != None:
                base.playSfx(dialogueArray[4])
            
        elif type == 'special':
            if dialogueArray[5] != None:
                base.playSfx(dialogueArray[5])
            
        else:
            notify.error('unrecognized dialogue type: ', type)

    
    def getShadowJoints(self):
        return [
            self.getGeomNode()]

    
    def getNametagJoints(self):
        return [
            self.getGeomNode()]

    
    def startBlink(self):
        pass

    
    def stopBlink(self):
        pass


