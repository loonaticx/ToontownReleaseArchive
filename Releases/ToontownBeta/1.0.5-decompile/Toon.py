# Source Generated with Decompyle++
# File: Toon.pyo (Python 2.0)

import Avatar
import Actor
import string
from ToonHead import *
from PandaModules import *
import DirectNotifyGlobal
DogDialogueArray = []
CatDialogueArray = []
HorseDialogueArray = []
RabbitDialogueArray = []
MouseDialogueArray = []
DuckDialogueArray = []
LegsAnimDict = { }
TorsoAnimDict = { }
HeadAnimDict = { }
ShirtTextures = []
ShirtSleeveTextures = []
ShortTextures = []
SkirtTextures = []
Preloaded = []
Phase3AnimList = (('neutral', 'neutral'),)
Phase4AnimList = (('walk', 'walk'), ('run', 'run'), ('swim', 'swim'), ('teleport', 'teleport'), ('book', 'book'), ('tug-o-war', 'tug-o-war'), ('jump', 'jump'))
Phase5AnimList = (('pushbutton', 'press-button'), ('water-gun', 'water-gun'), ('hold-bottle', 'hold-bottle'), ('firehose', 'firehose'), ('spit', 'spit'), ('throw', 'pie-throw'), ('tickle', 'tickle'), ('smooch', 'smooch'), ('happy-dance', 'happy-dance'), ('sprinkle-dust', 'sprinkle-dust'), ('juggle', 'juggle'), ('sound', 'shout'), ('toss', 'toss'), ('cast', 'fish'), ('hold-magnet', 'hold-magnet'), ('hypnotize', 'hypnotize'), ('conked', 'conked'), ('cringe', 'cringe'), ('duck', 'duck'), ('sidestep-left', 'sidestep-left'), ('slip-forward', 'slip-forward'), ('slip-backward', 'slip-backward'), ('struggle', 'struggle'), ('victory', 'victory-dance'), ('lose', 'lose'), ('sad-walk', 'losewalk'), ('sad-neutral', 'sad-neutral'), ('think', 'think'))
LegDict = {
    's': '/models/char/dogSS_Shorts-legs-',
    'm': '/models/char/dogMM_Shorts-legs-',
    'l': '/models/char/dogLL_Shorts-legs-' }
TorsoDict = {
    'ss': '/models/char/dogSS_Shorts-torso-',
    'ms': '/models/char/dogMM_Shorts-torso-',
    'ls': '/models/char/dogLL_Shorts-torso-',
    'sd': '/models/char/dogSS_Skirt-torso-',
    'md': '/models/char/dogMM_Skirt-torso-',
    'ld': '/models/char/dogLL_Skirt-torso-' }
ShirtList = [
    'phase_3/maps/desat_shirt_1.jpg',
    'phase_3/maps/desat_shirt_2.jpg',
    'phase_3/maps/desat_shirt_3.jpg',
    'phase_3/maps/desat_shirt_4.jpg',
    'phase_3/maps/desat_shirt_5.jpg',
    'phase_3/maps/desat_shirt_6.jpg',
    'phase_3/maps/desat_shirt_7.jpg',
    'phase_3/maps/desat_shirt_8.jpg',
    'phase_3/maps/desat_shirt_9.jpg']
ShirtSleeveList = [
    'phase_3/maps/desat_sleeve_1.jpg',
    'phase_3/maps/desat_sleeve_2.jpg',
    'phase_3/maps/desat_sleeve_3.jpg',
    'phase_3/maps/desat_sleeve_4.jpg',
    'phase_3/maps/desat_sleeve_5.jpg',
    'phase_3/maps/desat_sleeve_6.jpg',
    'phase_3/maps/desat_sleeve_7.jpg',
    'phase_3/maps/desat_sleeve_8.jpg',
    'phase_3/maps/desat_sleeve_9.jpg']
ShortList = [
    'phase_3/maps/desat_shorts_1.jpg',
    'phase_3/maps/desat_shorts_2.jpg',
    'phase_3/maps/desat_shorts_3.jpg',
    'phase_3/maps/desat_shorts_4.jpg',
    'phase_3/maps/desat_shorts_5.jpg',
    'phase_3/maps/desat_shorts_6.jpg']
SkirtList = [
    'phase_3/maps/desat_skirt_1.jpg',
    'phase_3/maps/desat_skirt_2.jpg',
    'phase_3/maps/desat_skirt_3.jpg',
    'phase_3/maps/desat_skirt_4.jpg',
    'phase_3/maps/desat_skirt_5.jpg']
ClothesColors = [
    (173, 154, 255),
    (217, 255, 107),
    (120, 51, 4),
    (255, 217, 207),
    (228, 255, 215),
    (255, 223, 88),
    (123, 57, 181),
    (115, 180, 158),
    (255, 196, 138),
    (181, 57, 181),
    (170, 163, 221),
    (214, 221, 163),
    (185, 0, 18),
    (255, 113, 4),
    (54, 96, 85),
    (144, 70, 34),
    (143, 91, 157),
    (170, 211, 248),
    (228, 243, 103),
    (209, 249, 255),
    (255, 232, 25),
    (243, 67, 3),
    (137, 155, 255),
    (138, 230, 165),
    (255, 40, 1),
    (248, 210, 0),
    (0, 126, 226),
    (247, 139, 133),
    (209, 201, 255),
    (255, 103, 213),
    (180, 255, 145),
    (255, 173, 159),
    (102, 194, 255),
    (255, 140, 13),
    (111, 89, 17),
    (35, 125, 211),
    (255, 171, 75),
    (57, 189, 132),
    (205, 255, 54),
    (148, 255, 247),
    (235, 116, 255),
    (254, 216, 221),
    (185, 178, 255),
    (197, 237, 255),
    (131, 255, 130),
    (255, 231, 82),
    (171, 82, 255),
    (173, 29, 0),
    (0, 167, 67),
    (246, 255, 145),
    (255, 78, 85),
    (0, 238, 42),
    (255, 136, 194),
    (120, 51, 4),
    (64, 59, 150),
    (115, 180, 158),
    (255, 196, 138),
    (181, 57, 115),
    (123, 57, 181),
    (214, 221, 163),
    (170, 163, 221),
    (255, 217, 207),
    (186, 19, 23),
    (184, 243, 255),
    (8, 177, 255),
    (248, 84, 255),
    (2, 255, 178),
    (2, 58, 255),
    (32, 255, 2),
    (25, 197, 154),
    (192, 132, 33),
    (74, 82, 189),
    (226, 97, 38),
    (154, 64, 200),
    (255, 236, 111),
    (118, 184, 112),
    (165, 0, 7),
    (120, 150, 175),
    (175, 165, 120),
    (252, 214, 255),
    (255, 248, 214),
    (223, 254, 255),
    (232, 255, 227),
    (132, 255, 186),
    (184, 132, 255),
    (255, 145, 132),
    (255, 247, 156),
    (255, 195, 241),
    (195, 205, 255),
    (255, 213, 198),
    (222, 255, 204),
    (255, 242, 17),
    (255, 103, 17),
    (255, 224, 16),
    (255, 119, 66),
    (169, 255, 66),
    (126, 255, 215),
    (202, 126, 255),
    (255, 175, 221),
    (175, 184, 255),
    (0, 125, 246),
    (128, 144, 239),
    (255, 197, 254),
    (158, 255, 171),
    (193, 227, 255),
    (255, 95, 34),
    (252, 255, 13),
    (203, 212, 255),
    (203, 255, 221),
    (239, 203, 255),
    (255, 212, 203),
    (255, 251, 203),
    (255, 170, 122),
    (255, 255, 255)]
ShirtPairs = [
    (1, 1),
    (1, 2),
    (1, 3),
    (1, 4),
    (1, 5),
    (1, 6),
    (1, 7),
    (1, 8),
    (1, 9),
    (1, 10),
    (1, 11),
    (1, 12),
    (1, 13),
    (1, 14),
    (1, 15),
    (2, 1),
    (2, 2),
    (2, 3),
    (2, 4),
    (2, 5),
    (2, 6),
    (2, 7),
    (2, 8),
    (2, 9),
    (2, 10),
    (2, 11),
    (2, 12),
    (2, 13),
    (2, 14),
    (2, 15),
    (3, 16),
    (3, 17),
    (3, 18),
    (3, 19),
    (4, 20),
    (4, 21),
    (4, 22),
    (4, 23),
    (4, 24),
    (5, 25),
    (5, 26),
    (5, 27),
    (5, 28),
    (5, 29),
    (5, 30),
    (6, 31),
    (6, 32),
    (6, 33),
    (6, 34),
    (6, 35),
    (7, 36),
    (7, 37),
    (7, 38),
    (7, 39),
    (7, 40),
    (7, 41),
    (8, 42),
    (8, 43),
    (8, 44),
    (8, 45),
    (8, 46),
    (8, 47),
    (8, 48),
    (8, 49),
    (9, 114),
    (9, 50),
    (9, 51),
    (9, 52),
    (9, 53)]
ShortPairs = [
    (1, 54),
    (1, 55),
    (1, 56),
    (1, 57),
    (1, 58),
    (1, 61),
    (1, 62),
    (1, 63),
    (1, 65),
    (1, 66),
    (2, 54),
    (2, 55),
    (2, 56),
    (2, 57),
    (2, 58),
    (2, 60),
    (2, 61),
    (2, 62),
    (2, 63),
    (2, 64),
    (2, 65),
    (2, 66),
    (3, 67),
    (3, 69),
    (3, 71),
    (4, 72),
    (4, 73),
    (4, 74),
    (4, 75),
    (4, 76),
    (4, 77),
    (4, 78),
    (4, 79),
    (4, 80),
    (4, 81),
    (5, 114),
    (5, 84),
    (5, 85),
    (5, 86),
    (5, 87),
    (5, 88),
    (5, 89),
    (5, 90),
    (5, 91),
    (5, 91),
    (5, 92),
    (5, 93),
    (6, 114),
    (6, 50),
    (6, 51),
    (6, 52),
    (6, 53)]
SkirtPairs = [
    (1, 94),
    (1, 95),
    (1, 96),
    (1, 97),
    (1, 98),
    (1, 99),
    (1, 100),
    (1, 101),
    (2, 94),
    (2, 95),
    (2, 96),
    (2, 97),
    (2, 98),
    (2, 99),
    (2, 100),
    (2, 101),
    (3, 102),
    (3, 103),
    (3, 104),
    (3, 105),
    (3, 106),
    (3, 107),
    (4, 114),
    (4, 108),
    (4, 109),
    (4, 110),
    (4, 113),
    (5, 36),
    (5, 37),
    (5, 38),
    (5, 39),
    (5, 40),
    (5, 41)]
toonBodyScales = {
    'mouse': 0.6,
    'cat': 0.73,
    'fowl': 0.66,
    'rabbit': 0.74,
    'horse': 0.85,
    'dog': 0.85 }
toonHeadScales = {
    'mouse': Vec3(1.3078, 1.1274, 1.1274),
    'cat': Vec3(1.125),
    'fowl': Vec3(1.345, 1.1298, 1.3292),
    'rabbit': Vec3(1.0),
    'horse': Vec3(1.0),
    'dog': Vec3(1.0857) }
legHeightDict = {
    's': 1.5,
    'm': 2.0,
    'l': 2.75 }
torsoHeightDict = {
    'ss': 1.5,
    'ms': 1.75,
    'ls': 2.25,
    'sd': 1.5,
    'md': 1.75,
    'ld': 2.25 }
headHeightDict = {
    'dls': 0.75,
    'dss': 0.5,
    'dsl': 0.5,
    'dll': 0.75,
    'cls': 0.75,
    'css': 0.5,
    'csl': 0.5,
    'cll': 0.75,
    'hls': 0.75,
    'hss': 0.5,
    'hsl': 0.5,
    'hll': 0.75,
    'mls': 0.75,
    'mss': 0.5,
    'rls': 0.75,
    'rss': 0.5,
    'rsl': 0.5,
    'rll': 0.75,
    'fls': 0.75,
    'fss': 0.5,
    'fsl': 0.5,
    'fll': 0.75 }

def loadModels():
    preloadAvatars = base.config.GetBool('preload-avatars', 1)
    if preloadAvatars:
        for shirt in ShirtList:
            tex = loader.loadTexture(shirt)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)
        
        for sleeve in ShirtSleeveList:
            tex = loader.loadTexture(sleeve)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)
        
        for short in ShortList:
            tex = loader.loadTexture(short)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)
        
        for skirt in SkirtList:
            tex = loader.loadTexture(skirt)
            tex.setMinfilter(Texture.FTLinearMipmapLinear)
            tex.setMagfilter(Texture.FTLinear)
            Preloaded.append(tex)
        
        for key in LegDict.keys():
            model = loader.loadModelNode('phase_3' + LegDict[key] + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + LegDict[key] + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + LegDict[key] + '250')
            Preloaded.append(model)
        
        for key in TorsoDict.keys():
            model = loader.loadModelNode('phase_3' + TorsoDict[key] + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + TorsoDict[key] + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + TorsoDict[key] + '250')
            Preloaded.append(model)
        
        for key in HeadDict.keys():
            model = loader.loadModelNode('phase_3' + HeadDict[key] + '1000')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + HeadDict[key] + '500')
            Preloaded.append(model)
            model = loader.loadModelNode('phase_3' + HeadDict[key] + '250')
            Preloaded.append(model)
        
    


def loadBasicAnims():
    loadPhaseAnims()


def unloadBasicAnims():
    loadPhaseAnims(0)


def loadMinigameAnims():
    loadPhaseAnims('phase_4')


def unloadMinigameAnims():
    loadPhaseAnims('phase_4', 0)


def loadBattleAnims():
    loadPhaseAnims('phase_5')


def unloadBattleAnims():
    loadPhaseAnims('phase_5', 0)


def loadPhaseAnims(phaseStr = 'phase_3', loadFlag = 1):
    if loadFlag:
        print 'loading anims for ', phaseStr
    else:
        print 'unloading anims for ', phaseStr
    if phaseStr == 'phase_3':
        animList = Phase3AnimList
    elif phaseStr == 'phase_4':
        animList = Phase4AnimList
    elif phaseStr == 'phase_5':
        animList = Phase5AnimList
    else:
        self.notify.error('Unknown phase string %s' % phaseStr)
    for key in LegDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if LegsAnimDict[key].has_key(anim[0]):
                if toonbase.localToon.style.legs == key:
                    toonbase.localToon.unloadAnims([
                        anim[0]], 'legs', None)
                
            
        
    
    for key in TorsoDict.keys():
        for anim in animList:
            if loadFlag:
                pass
            1
            if TorsoAnimDict[key].has_key(anim[0]):
                if toonbase.localToon.style.torso == key:
                    toonbase.localToon.unloadAnims([
                        anim[0]], 'torso', None)
                
            
        
    
    for key in HeadDict.keys():
        if string.find(key, 'd') >= 0:
            for anim in animList:
                if loadFlag:
                    pass
                1
                if HeadAnimDict[key].has_key(anim[0]):
                    if toonbase.localToon.style.head == key:
                        toonbase.localToon.unloadAnims([
                            anim[0]], 'head', None)
                    
                
            
        
    


def compileGlobalAnimList():
    phaseList = [
        Phase3AnimList,
        Phase4AnimList,
        Phase5AnimList]
    phaseStrList = [
        'phase_3',
        'phase_4',
        'phase_5']
    for animList in phaseList:
        phaseStr = phaseStrList[phaseList.index(animList)]
        for key in LegDict.keys():
            if not LegsAnimDict.has_key(key):
                LegsAnimDict[key] = { }
            
            for anim in animList:
                file = phaseStr + LegDict[key] + anim[1]
                LegsAnimDict[key][anim[0]] = file
            
        
        for key in TorsoDict.keys():
            if not TorsoAnimDict.has_key(key):
                TorsoAnimDict[key] = { }
            
            for anim in animList:
                file = phaseStr + TorsoDict[key] + anim[1]
                TorsoAnimDict[key][anim[0]] = file
            
        
        for key in HeadDict.keys():
            if string.find(key, 'd') >= 0:
                if not HeadAnimDict.has_key(key):
                    HeadAnimDict[key] = { }
                
                for anim in animList:
                    file = phaseStr + HeadDict[key] + anim[1]
                    HeadAnimDict[key][anim[0]] = file
                
            
        
    


def loadDialog():
    loadPath = 'phase_4/audio/dial/'
    DogDialogueFiles = ('AV_dog_short', 'AV_dog_med', 'AV_dog_long', 'AV_dog_question', 'AV_dog_exclaim', 'AV_dog_howl')
    for file in DogDialogueFiles:
        DogDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    catDialogueFiles = ('AV_cat_short', 'AV_cat_med', 'AV_cat_long', 'AV_cat_question', 'AV_cat_exclaim', 'AV_cat_howl')
    for file in catDialogueFiles:
        CatDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    horseDialogueFiles = ('AV_horse_short', 'AV_horse_med', 'AV_horse_long', 'AV_horse_question', 'AV_horse_exclaim', 'AV_horse_howl')
    for file in horseDialogueFiles:
        HorseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    rabbitDialogueFiles = ('AV_rabbit_short', 'AV_rabbit_med', 'AV_rabbit_long', 'AV_rabbit_question', 'AV_rabbit_exclaim', 'AV_rabbit_howl')
    for file in rabbitDialogueFiles:
        RabbitDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    mouseDialogueFiles = ('AV_mouse_short', 'AV_mouse_med', 'AV_mouse_long', 'AV_mouse_question', 'AV_mouse_exclaim', 'AV_mouse_howl')
    for file in mouseDialogueFiles:
        MouseDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    
    duckDialogueFiles = ('AV_duck_short', 'AV_duck_med', 'AV_duck_long', 'AV_duck_question', 'AV_duck_exclaim', 'AV_duck_howl')
    for file in duckDialogueFiles:
        DuckDialogueArray.append(base.loadSfx(loadPath + file + '.mp3'))
    


def unloadDialog():
    global DogDialogueArray, CatDialogueArray, HorseDialogueArray, RabbitDialogueArray, MouseDialogueArray, DuckDialogueArray
    for sfx in DogDialogueArray:
        base.unloadSfx(sfx)
    
    for sfx in CatDialogueArray:
        base.unloadSfx(sfx)
    
    for sfx in HorseDialogueArray:
        base.unloadSfx(sfx)
    
    for sfx in RabbitDialogueArray:
        base.unloadSfx(sfx)
    
    for sfx in MouseDialogueArray:
        base.unloadSfx(sfx)
    
    for sfx in DuckDialogueArray:
        base.unloadSfx(sfx)
    
    DogDialogueArray = []
    CatDialogueArray = []
    HorseDialogueArray = []
    RabbitDialogueArray = []
    MouseDialogueArray = []
    DuckDialogueArray = []


class Toon(Avatar.Avatar, ToonHead):
    notify = DirectNotifyGlobal.directNotify.newCategory('Toon')
    
    def __init__(self):
        
        try:
            self.Toon_initialized
        except:
            self.Toon_initialized = 1
            Avatar.Avatar.__init__(self)
            ToonHead.__init__(self)

        return None

    
    def delete(self):
        
        try:
            self.Toon_deleted
        except:
            self.Toon_deleted = 1
            del self.rightHands
            del self.leftHands
            del self.headParts
            del self.torsoParts
            del self.hipsParts
            del self.legsParts
            Avatar.Avatar.delete(self)
            ToonHead.delete(self)
            for bookActor in self.bookActors:
                bookActor.cleanup()
            
            self.bookActors = []
            for holeActor in self.holeActors:
                holeActor.cleanup()
            
            self.holeActors = []
            for cloudActor in self.cloudActors:
                cloudActor.cleanup()
            
            self.cloudActors = []


    
    def updateToonDNA(self, newDNA):
        oldDNA = self.style
        if newDNA.head != oldDNA.head:
            self.swapToonHead(newDNA.head)
        
        if newDNA.torso != oldDNA.torso:
            self.swapToonTorso(newDNA.torso)
        
        if newDNA.legs != oldDNA.legs:
            self.swapToonLegs(newDNA.legs)
        
        self.swapToonColor(newDNA)

    
    def parentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.attach('head', 'torso', 'joint-head', lodName)
                self.attach('torso', 'legs', 'joint-hips', lodName)
            
        else:
            self.attach('head', 'torso', 'joint-head')
            self.attach('torso', 'legs', 'joint-hips')

    
    def unparentToonParts(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                self.getPart('head', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('torso', lodName).reparentTo(self.getLOD(lodName))
                self.getPart('legs', lodName).reparentTo(self.getLOD(lodName))
            
        else:
            self.getPart('head').reparentTo(self.getGeomNode())
            self.getPart('torso').reparentTo(self.getGeomNode())
            self.getPart('legs').reparentTo(self.getGeomNode())

    
    def setLODs(self):
        self.setLODNode()
        levelOneIn = base.config.GetInt('lod1-in', 20)
        levelOneOut = base.config.GetInt('lod1-out', 0)
        levelTwoIn = base.config.GetInt('lod2-in', 80)
        levelTwoOut = base.config.GetInt('lod2-out', 20)
        levelThreeIn = base.config.GetInt('lod3-in', 280)
        levelThreeOut = base.config.GetInt('lod3-out', 80)
        self.addLOD(250, levelThreeIn, levelThreeOut)
        self.addLOD(500, levelTwoIn, levelTwoOut)
        self.addLOD(1000, levelOneIn, levelOneOut)

    
    def generateToon(self):
        self.setLODs()
        self.generateToonLegs()
        self.generateToonTorso()
        self.generateToonHead()
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.rightHands = []
        self.leftHands = []
        for lodName in self.getLODNames():
            hand = self.getPart('torso', lodName).find('**/joint-Rhold')
            self.rightHands.append(hand)
            hand = self.getPart('torso', lodName).find('**/joint-Lhold')
            self.leftHands.append(hand)
        
        self.headParts = self.findAllMatches('**/__Actor_head')
        self.hipsParts = self.findAllMatches('**/joint-hips')
        self.torsoParts = self.findAllMatches('**/__Actor_torso')
        self.legsParts = self.findAllMatches('**/__Actor_legs')
        if not launcher and launcher and launcher.getPhaseComplete(4):
            bookActor = Actor.Actor('phase_4/models/props/book-mod', {
                'book': 'phase_4/models/props/book-chan' })
            bookActor2 = Actor.Actor(other = bookActor)
            bookActor3 = Actor.Actor(other = bookActor)
            self.bookActors = [
                bookActor,
                bookActor2,
                bookActor3]
            hands = self.getRightHands()
            index = 0
            for bookActor in self.bookActors:
                bookActor.reparentTo(hands[index])
                bookActor.hide()
                index += 1
            
            holeActor = Actor.Actor('phase_4/models/props/portal-mod', {
                'hole': 'phase_4/models/props/portal-chan' })
            holeActor2 = Actor.Actor(other = holeActor)
            holeActor3 = Actor.Actor(other = holeActor)
            self.holeActors = [
                holeActor,
                holeActor2,
                holeActor3]
            cloudActor = Actor.Actor('phase_4/models/props/stormcloud-mod', {
                'cloud': 'phase_4/models/props/stormcloud-chan' })
            cloudActor2 = Actor.Actor(other = cloudActor)
            cloudActor3 = Actor.Actor(other = cloudActor)
            self.cloudActors = [
                cloudActor,
                cloudActor2,
                cloudActor3]
        else:
            self.bookActors = []
            self.holeActors = []
            self.cloudActors = []

    
    def rescaleToon(self):
        animalStyle = self.style.getAnimal()
        bodyScale = toonBodyScales[animalStyle]
        headScale = toonHeadScales[animalStyle]
        self.setAvatarScale(bodyScale)
        for lod in self.getLODNames():
            self.getPart('head', lod).setScale(headScale)
        

    
    def resetHeight(self):
        animal = self.style.getAnimal()
        bodyScale = toonBodyScales[animal]
        headScale = toonHeadScales[animal][2]
        shoulderHeight = legHeightDict[self.style.legs] * bodyScale + torsoHeightDict[self.style.torso] * bodyScale
        height = shoulderHeight + headHeightDict[self.style.head] * headScale
        self.shoulderHeight = shoulderHeight
        self.setHeight(height)

    
    def generateToonLegs(self, copy = 1):
        legStyle = self.style.legs
        if LegDict.has_key(legStyle):
            filePrefix = LegDict[legStyle]
        else:
            self.notify.error('unknown leg style: %s' % legStyle)
        self.loadModel('phase_3' + filePrefix + '1000', 'legs', '1000', copy)
        self.loadModel('phase_3' + filePrefix + '500', 'legs', '500', copy)
        self.loadModel('phase_3' + filePrefix + '250', 'legs', '250', copy)
        if not copy:
            self.showPart('legs', '1000')
            self.showPart('legs', '500')
            self.showPart('legs', '250')
        
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '1000')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '500')
        self.loadAnims(LegsAnimDict[legStyle], 'legs', '250')

    
    def swapToonLegs(self, legStyle, copy = 1):
        self.unparentToonParts()
        self.removePart('legs', '1000')
        self.removePart('legs', '500')
        self.removePart('legs', '250')
        self.style.legs = legStyle
        self.generateToonLegs(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.initializeDropShadow()
        self.initializeNametag3d()

    
    def generateToonTorso(self, copy = 1):
        torsoStyle = self.style.torso
        if TorsoDict.has_key(torsoStyle):
            filePrefix = TorsoDict[torsoStyle]
        else:
            self.notify.error('unknown torso style: %s' % torsoStyle)
        self.loadModel('phase_3' + filePrefix + '1000', 'torso', '1000', copy)
        self.loadModel('phase_3' + filePrefix + '500', 'torso', '500', copy)
        self.loadModel('phase_3' + filePrefix + '250', 'torso', '250', copy)
        if not copy:
            self.showPart('torso', '1000')
            self.showPart('torso', '500')
            self.showPart('torso', '250')
        
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '1000')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '500')
        self.loadAnims(TorsoAnimDict[torsoStyle], 'torso', '250')
        self.generateToonClothes()

    
    def swapToonTorso(self, torsoStyle, copy = 1):
        self.unparentToonParts()
        self.removePart('torso', '1000')
        self.removePart('torso', '500')
        self.removePart('torso', '250')
        self.style.torso = torsoStyle
        self.generateToonTorso(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()

    
    def generateToonHead(self, copy = 1):
        headHeight = ToonHead.generateToonHead(self, copy, self.style, ('1000', '500', '250'))
        if self.style.getAnimal() == 'dog':
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '1000')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '500')
            self.loadAnims(HeadAnimDict[self.style.head], 'head', '250')
        

    
    def swapToonHead(self, headStyle, copy = 1):
        self.stopLookAroundNow()
        self.eyelids.request('open')
        self.unparentToonParts()
        self.removePart('head', '1000')
        self.removePart('head', '500')
        self.removePart('head', '250')
        self.style.head = headStyle
        self.generateToonHead(copy)
        self.generateToonColor()
        self.parentToonParts()
        self.rescaleToon()
        self.resetHeight()
        self.startLookAround()

    
    def generateToonColor(self):
        ToonHead.generateToonColor(self, self.style)
        dna = self.style
        parts = self.findAllMatches('**/arms')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getArmColor())
        
        parts = self.findAllMatches('**/neck')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getArmColor())
        
        parts = self.findAllMatches('**/hands')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getGloveColor())
        
        parts = self.findAllMatches('**/legs')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getLegColor())
        
        parts = self.findAllMatches('**/feet')
        for partNum in range(0, parts.getNumPaths()):
            parts.getPath(partNum).setColor(dna.getLegColor())
        

    
    def swapToonColor(self, dna):
        self.setStyle(dna)
        self.generateToonColor()

    
    def generateToonClothes(self):
        if self.hasLOD():
            for lodName in self.getLODNames():
                thisPart = self.getPart('torso', lodName)
                texName = ShirtList[ShirtPairs[self.style.topTex][0] - 1]
                shirtTex = loader.loadTexture(texName)
                shirtTex.setMinfilter(Texture.FTLinear)
                shirtTex.setMagfilter(Texture.FTLinear)
                top = thisPart.find('**/torso-top')
                top.setTexture(shirtTex)
                color = ClothesColors[ShirtPairs[self.style.topTex][1] - 1]
                top.setColor(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
                texName = ShirtSleeveList[ShirtPairs[self.style.topTex][0] - 1]
                sleeveTex = loader.loadTexture(texName)
                sleeveTex.setMinfilter(Texture.FTLinear)
                sleeveTex.setMagfilter(Texture.FTLinear)
                sleeves = thisPart.find('**/sleeves')
                sleeves.setTexture(sleeveTex)
                sleeves.setColor(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
                if self.style.torso[1] == 's':
                    list = ShortList
                    pairs = ShortPairs
                else:
                    list = SkirtList
                    pairs = SkirtPairs
                texName = list[pairs[self.style.botTex][0] - 1]
                bottomTex = loader.loadTexture(texName)
                bottomTex.setMinfilter(Texture.FTLinear)
                bottomTex.setMagfilter(Texture.FTLinear)
                bottoms = thisPart.findAllMatches('**/torso-bot')
                for bottomNum in range(0, bottoms.getNumPaths()):
                    bottom = bottoms.getPath(bottomNum)
                    color = ClothesColors[pairs[self.style.botTex][1] - 1]
                    if bottomNum == 0:
                        bottom.setTexture(bottomTex)
                        bottom.setColor(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0)
                    else:
                        bottom.setColor(color[0] / 510.0, color[1] / 510.0, color[2] / 510.0)
                
            
        

    
    def playDialogue(self, type, length):
        animalType = self.style.getType()
        if animalType == 'dog':
            dialogueArray = DogDialogueArray
        elif animalType == 'cat':
            dialogueArray = CatDialogueArray
        elif animalType == 'horse':
            dialogueArray = HorseDialogueArray
        elif animalType == 'mouse':
            dialogueArray = MouseDialogueArray
        elif animalType == 'rabbit':
            dialogueArray = RabbitDialogueArray
        elif animalType == 'fowl':
            dialogueArray = DuckDialogueArray
        
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
            self.notify.error('unrecognized dialogue type: ', type)
        return None

    
    def getShadowJoints(self):
        shadows = []
        for lodName in self.getLODNames():
            shadow = self.getPart('legs', lodName).find('**/joint-shadow')
            shadows.append(shadow)
        
        return shadows

    
    def getNametagJoints(self):
        nametags = []
        for lodName in self.getLODNames():
            nametag = self.getPart('legs', lodName).find('**/joint-nameTag')
            nametags.append(nametag)
        
        return nametags

    
    def getRightHands(self):
        return self.rightHands

    
    def getLeftHands(self):
        return self.leftHands

    
    def getHeadParts(self):
        return self.headParts

    
    def getHipsParts(self):
        return self.hipsParts

    
    def getTorsoParts(self):
        return self.torsoParts

    
    def getLegsParts(self):
        return self.legsParts

    
    def setupPickTrigger(self):
        Avatar.Avatar.setupPickTrigger(self)
        torso = self.getPart('torso', '1000')
        if torso == None:
            return 0
        
        self.pickTriggerNp.reparentTo(torso)
        size = self.style.getTorsoSize()
        if size == 'short':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1.5, 1.5, 2)
        elif size == 'medium':
            self.pickTriggerNp.setPosHprScale(0, 0, 0.5, 0, 0, 0, 1, 1, 2)
        else:
            self.pickTriggerNp.setPosHprScale(0, 0, 1, 0, 0, 0, 1, 1, 2)
        return 1

    
    def showBooks(self):
        for bookActor in self.bookActors:
            bookActor.show()
        

    
    def hideBooks(self):
        for bookActor in self.bookActors:
            bookActor.hide()
        


loadModels()
compileGlobalAnimList()
