# Source Generated with Decompyle++
# File: Suit.pyo (Python 2.0)

import Actor
import Avatar
import AvatarDNA
import ToontownGlobals
from PandaModules import *
aSize = 6.06
bSize = 5.29
cSize = 4.14
SuitDialogArray = []
AllSuits = (('walk', 'walk'), ('neutral', 'neutral'))
AllSuitsMinigame = ()
AllSuitsBattle = (('lose', 'lose'), ('victory', 'victory'), ('drop-react', 'anvil-drop'), ('flatten', 'drop'), ('sidestep-left', 'sidestep-left'), ('sidestep-right', 'sidestep-right'), ('slip-backward', 'slip-backward'), ('slip-forward', 'slip-forward'), ('pie-small-react', 'pie-small'), ('squirt-small-react', 'squirt-small'), ('tug-o-war', 'tug-o-war'), ('landing', 'landing'), ('reach', 'walknreach'), ('rake-react', 'rake'), ('flail', 'flailing'), ('hypnotized', 'hypnotize'))
f = (('throw-paper', 'throw-paper', 5), ('phone', 'phone', 5), ('shredder', 'shredder', 5))
p = (('pencil-sharpener', 'pencil-sharpener', 5), ('pen-squirt', 'pen-squirt', 5), ('hold-eraser', 'hold-eraser', 5), ('finger-wag', 'finger-wag', 5), ('hold-pencil', 'hold-pencil', 5))
ym = (('throw-paper', 'throw-paper', 5), ('golf-club-swing', 'golf-club-swing', 5), ('magic3', 'magic3', 5), ('rubber-stamp', 'rubber-stamp', 5), ('smile', 'smile', 5))
mm = (('speak', 'speak', 5), ('effort', 'effort', 5), ('magic1', 'magic1', 5), ('pen-squirt', 'fountain-pen', 5), ('finger-wag', 'finger-wag', 5))
cc = (('speak', 'speak', 5), ('glower', 'glower', 5), ('phone', 'phone', 5), ('finger-wag', 'finger-wag', 5))
tm = (('speak', 'speak', 5), ('throw-paper', 'throw-paper', 5), ('pickpocket', 'pickpocket', 5), ('roll-o-dex', 'roll-o-dex', 5), ('finger-wag', 'finger-wag', 5))
nd = (('pickpocket', 'pickpocket', 5), ('roll-o-dex', 'roll-o-dex', 5), ('magic3', 'magic3', 5), ('smile', 'smile', 5))
gh = (('speak', 'speak', 5), ('pen-squirt', 'fountain-pen', 5), ('rubber-stamp', 'rubber-stamp', 5))
sc = (('throw-paper', 'throw-paper', 5), ('watercooler', 'watercooler', 5), ('pickpocket', 'pickpocket', 5))
pp = (('throw-paper', 'throw-paper', 5), ('glower', 'glower', 5), ('finger-wag', 'fingerwag', 5))
tw = (('throw-paper', 'throw-paper', 5), ('glower', 'glower', 5), ('magic2', 'magic2', 5), ('finger-wag', 'finger-wag', 5))
bc = (('phone', 'phone', 5), ('hold-pencil', 'hold-pencil', 5))
bf = (('pickpocket', 'pickpocket', 5), ('rubber-stamp', 'rubber-stamp', 5), ('shredder', 'shredder', 5), ('watercooler', 'watercooler', 5))
b = (('effort', 'effort', 5), ('throw-paper', 'throw-paper', 5), ('throw-object', 'throw-object', 5), ('magic1', 'magic1', 5))
dt = (('rubber-stamp', 'rubber-stamp', 5), ('throw-paper', 'throw-paper', 5), ('speak', 'speak', 5), ('finger-wag', 'fingerwag', 5))
ac = (('throw-object', 'throw-object', 5), ('roll-o-dex', 'roll-o-dex', 5), ('stomp', 'stomp', 5), ('phone', 'phone', 5))
ModelDict = {
    'a': '/models/char/suitA-',
    'b': '/models/char/suitB-',
    'c': '/models/char/suitC-' }

def loadSuits(level):
    loadSuitModelsAndAnims(level, flag = 1)
    loadDialog(level)


def unloadSuits(level):
    loadSuitModelsAndAnims(level, flag = 0)
    unloadDialog(level)


def loadSuitModelsAndAnims(level, flag = 0):
    print 'print loading level %d suits...' % level
    for key in ModelDict.keys():
        if flag:
            loader.loadModelNode('phase_4' + ModelDict[key] + 'mod')
            loader.loadModelNode('phase_4' + ModelDict[key] + 'heads')
        else:
            loader.unloadModel('phase_4' + ModelDict[key] + 'mod')
            loader.unloadModel('phase_4' + ModelDict[key] + 'heads')
    


def loadSuitAnims(suit, flag = 1):
    if suit in AvatarDNA.suitHeadTypes:
        
        try:
            animList = eval(suit)
        except NameError:
            animList = ()

    else:
        print 'Invalid suit name: ', suit
        return -1
    for anim in animList:
        phase = 'phase_' + str(anim[2])
        filePrefix = ModelDict[bodyType]
        animName = phase + filePrefix + anim[1]
        if flag:
            loader.loadModelNode(animName)
        else:
            loader.unloadModel(animName)
    


def loadDialog(level):
    loadPath = 'phase_4/audio/dial/'
    SuitDialogFiles = [
        'COG_VO_grunt',
        'COG_VO_murmur',
        'COG_VO_statement',
        'COG_VO_question']
    for file in SuitDialogFiles:
        SuitDialogArray.append(base.loadSfx(loadPath + file + '.mp3'))
    


def unloadDialog(level):
    global SuitDialogArray
    for sfx in SuitDialogArray:
        base.unloadSfx(sfx)
    
    SuitDialogArray = []


class Suit(Avatar.Avatar):
    
    def __init__(self):
        
        try:
            self.Suit_initialized
        except:
            self.Suit_initialized = 1
            Avatar.Avatar.__init__(self)
            self.setFont(ToontownGlobals.getSuitFont())

        return None

    
    def delete(self):
        
        try:
            self.Suit_deleted
        except:
            self.Suit_deleted = 1
            Avatar.Avatar.delete(self)

        return None

    
    def setHeight(self, height):
        self.height = height
        for n in self.nametag3ds:
            n.setPos(0, 0, (height + 1.5) / self.scale)
        
        return None

    
    def generateSuit(self):
        dna = self.style
        self.headParts = []
        self.headColor = None
        self.headTexture = None
        self.loseActor = None
        if dna.name == 'f':
            self.scale = 4.0 / cSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('flunky')
            self.generateHead('glasses')
            self.setHeight(4.5)
            self.setName('Flunky')
        elif dna.name == 'p':
            self.scale = 3.35 / bSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('pencilpusher')
            self.setHeight(4.95)
            self.setName('Pencil Pusher')
        elif dna.name == 'ym':
            self.scale = 4.125 / aSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(5.5)
            self.setName('Yesman')
        elif dna.name == 'mm':
            self.scale = 2.5 / cSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('micromanager')
            self.setHeight(3.0)
            self.setName('Micromanager')
        elif dna.name == 'ds':
            self.scale = 4.5 / bSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(6.0)
            self.setName('Downsizer')
        elif dna.name == 'hh':
            self.scale = 6.5 / aSize
            self.handColor = AvatarDNA.corpPolyColor
            self.generateBody()
            self.generateHead('headhunter')
            self.setHeight(7.45)
            self.setName('Head Hunter')
        elif dna.name == 'cr':
            self.scale = 6.75 / cSize
            self.handColor = VBase4(0.85, 0.55, 0.55, 1.0)
            self.generateBody()
            self.headTexture = 'corporate-raider.jpg'
            self.generateHead('flunky')
            self.setHeight(7.85)
            self.setName('Corporate Raider')
        elif dna.name == 'tbc':
            self.scale = 7.0 / aSize
            self.handColor = VBase4(0.75, 0.95, 0.75, 1.0)
            self.generateHead('bigcheese')
            self.setHeight(9.0)
            self.setName('The Big Cheese')
        elif dna.name == 'bf':
            self.scale = 4.0 / cSize
            self.handColor = AvatarDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'bottom-feeder.jpg'
            self.generateHead('tightwad')
            self.setHeight(4.5)
            self.setName('Bottom Feeder')
        elif dna.name == 'b':
            self.scale = 4.375 / bSize
            self.handColor = VBase4(0.95, 0.95, 1.0, 1.0)
            self.generateBody()
            self.headTexture = 'blood-sucker.jpg'
            self.generateHead('movershaker')
            self.setHeight(5.0)
            self.setName('Blood Sucker')
        elif dna.name == 'dt':
            self.scale = 4.25 / aSize
            self.handColor = AvatarDNA.legalPolyColor
            self.generateBody()
            self.headTexture = 'double-talker.jpg'
            self.generateHead('twoface')
            self.setHeight(5.5)
            self.setName('Double Talker')
        elif dna.name == 'ac':
            self.scale = 4.35 / bSize
            self.handColor = AvatarDNA.legalPolyColor
            self.generateBody()
            self.generateHead('ambulancechaser')
            self.setHeight(6.0)
            self.setName('Ambulance Chaser')
        elif dna.name == 'bs':
            self.scale = 4.5 / aSize
            self.handColor = AvatarDNA.legalPolyColor
            self.generateBody()
            self.generateHead('backstabber')
            self.setHeight(7.0)
            self.setName('Back Stabber')
        elif dna.name == 'sd':
            self.scale = 5.65 / bSize
            self.handColor = VBase4(0.5, 0.8, 0.75, 1.0)
            self.generateBody()
            self.headTexture = 'spin-doctor.jpg'
            self.generateHead('telemarketer')
            self.setHeight(7.5)
            self.setName('Spin Doctor')
        elif dna.name == 'le':
            self.scale = 7.125 / aSize
            self.handColor = VBase(0.25, 0.25, 0.5, 1.0)
            self.generateBody()
            self.generateHead('legaleagle')
            self.setHeight(8.33)
            self.setName('Legal Eagle')
        elif dna.name == 'bw':
            self.scale = 7.0 / aSize
            self.handColor = AvatarDNA.legalPolyColor
            self.generateBody()
            self.generateHead('bigwig')
            self.setHeight(9.0)
            self.setName('Bigwig')
        elif dna.name == 'sc':
            self.scale = 3.6 / cSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.2)
            self.setName('Short Change')
        elif dna.name == 'pp':
            self.scale = 3.55 / aSize
            self.handColor = VBase4(1.0, 0.5, 0.6, 1.0)
            self.generateBody()
            self.generateHead('pennypincher')
            self.setHeight(4.8)
            self.setName('Penny Pincher')
        elif dna.name == 'tw':
            self.scale = 4.5 / cSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('tightwad')
            self.setHeight(5.2)
            self.setName('Tightwad')
        elif dna.name == 'bc':
            self.scale = 4.4 / bSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('beancounter')
            self.setHeight(6.0)
            self.setName('Bean Counter')
        elif dna.name == 'nc':
            self.scale = 5.25 / aSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('numbercruncher')
            self.setHeight(7.0)
            self.setName('Number Cruncher')
        elif dna.name == 'mb':
            self.scale = 5.3 / cSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.generateHead('moneybags')
            self.setHeight(6.95)
            self.setName('Money Bags')
        elif dna.name == 'ls':
            self.scale = 6.5 / bSize
            self.handColor = VBase4(0.5, 0.85, 0.75, 1.0)
            self.generateBody()
            self.generateHead('loanshark')
            self.setHeight(8.25)
            self.setName('Loan Shark')
        elif dna.name == 'rb':
            self.scale = 7.0 / aSize
            self.handColor = AvatarDNA.moneyPolyColor
            self.generateBody()
            self.headTexture = 'robber-baron.jpg'
            self.generateHead('yesman')
            self.setHeight(9.0)
            self.setName('Robber Baron')
        elif dna.name == 'cc':
            self.scale = 3.5 / cSize
            self.handColor = VBase4(0.55, 0.65, 1.0, 1.0)
            self.headColor = VBase4(0.25, 0.35, 1.0, 1.0)
            self.generateBody()
            self.generateHead('coldcaller')
            self.setHeight(4.5)
            self.setName('Cold Caller')
        elif dna.name == 'tm':
            self.scale = 3.75 / bSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.generateHead('telemarketer')
            self.setHeight(5.0)
            self.setName('Telemarketer')
        elif dna.name == 'nd':
            self.scale = 4.35 / aSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'name-dropper.jpg'
            self.generateHead('numbercruncher')
            self.setHeight(5.8)
            self.setName('Name Dropper')
        elif dna.name == 'gh':
            self.scale = 4.75 / cSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.generateHead('gladhander')
            self.setHeight(6.0)
            self.setName('Glad Hander')
        elif dna.name == 'ms':
            self.scale = 4.75 / bSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.generateHead('movershaker')
            self.setHeight(7.0)
            self.setName('Mover & Shaker')
        elif dna.name == 'tf':
            self.scale = 5.25 / aSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.generateHead('twoface')
            self.setHeight(7.5)
            self.setName('Two-Face')
        elif dna.name == 'm':
            self.scale = 5.75 / aSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.headTexture = 'mingler.jpg'
            self.generateHead('twoface')
            self.setHeight(8.15)
            self.setName('The Mingler')
        elif dna.name == 'mh':
            self.scale = 7.0 / aSize
            self.handColor = AvatarDNA.salesPolyColor
            self.generateBody()
            self.generateHead('yesman')
            self.setHeight(9.0)
            self.setName('Mr. Hollywood')
        
        self.getGeomNode().setScale(self.scale)

    
    def generateBody(self):
        filePrefix = ModelDict[self.style.body]
        animDict = { }
        for anim in AllSuits:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]
        
        for anim in AllSuitsMinigame:
            animDict[anim[0]] = 'phase_4' + filePrefix + anim[1]
        
        for anim in AllSuitsBattle:
            animDict[anim[0]] = 'phase_5' + filePrefix + anim[1]
        
        
        try:
            animList = eval(self.style.name)
        except NameError:
            0
            AllSuitsBattle
            0
            animList = ()
        except:
            0

        for anim in animList:
            phase = 'phase_' + str(anim[2])
            animDict[anim[0]] = phase + filePrefix + anim[1]
        
        self.loadModel('phase_4' + filePrefix + 'mod')
        self.loadAnims(animDict)
        self.setSuitClothes()

    
    def setSuitClothes(self, modelRoot = None):
        if not modelRoot:
            modelRoot = self
        
        torsoTex = loader.loadTexture('phase_4/maps/' + self.style.dept + '_blazer.jpg')
        torsoTex.setMinfilter(Texture.FTLinearMipmapLinear)
        torsoTex.setMagfilter(Texture.FTLinear)
        legTex = loader.loadTexture('phase_4/maps/' + self.style.dept + '_leg.jpg')
        legTex.setMinfilter(Texture.FTLinearMipmapLinear)
        legTex.setMagfilter(Texture.FTLinear)
        armTex = loader.loadTexture('phase_4/maps/' + self.style.dept + '_sleeve.jpg')
        armTex.setMinfilter(Texture.FTLinearMipmapLinear)
        armTex.setMagfilter(Texture.FTLinear)
        modelRoot.find('**/torso').setTexture(torsoTex)
        modelRoot.find('**/arms').setTexture(armTex)
        modelRoot.find('**/legs').setTexture(legTex)
        modelRoot.leftHand = self.find('**/joint-Lhold')
        modelRoot.rightHand = self.find('**/joint-Rhold')
        modelRoot.shadowNull = self.find('**/joint-shadow')
        modelRoot.nametagNull = self.find('**/joint-nameTag')
        modelRoot.find('**/hands').setColor(self.handColor)

    
    def generateHead(self, headType):
        filePrefix = ModelDict[self.style.body]
        headModel = loader.loadModelOnce('phase_4' + filePrefix + 'heads')
        headReferences = headModel.findAllMatches('**/' + headType)
        for i in range(0, headReferences.getNumPaths()):
            headPart = self.instance(headReferences.getPath(i), 'modelRoot', 'joint-head')
            if self.headTexture:
                headTex = loader.loadTexture('phase_4/maps/' + self.headTexture)
                headTex.setMinfilter(Texture.FTLinearMipmapLinear)
                headTex.setMagfilter(Texture.FTLinear)
                headPart.setTexture(headTex)
            
            if self.headColor:
                headPart.setColor(self.headColor)
            
            self.headParts.append(headPart)
        
        headModel.removeNode()

    
    def getLoseActor(self):
        if self.loseActor == None:
            filePrefix = ModelDict[self.style.body]
            loseModel = 'phase_5' + filePrefix + 'lose-mod'
            loseAnim = 'phase_5' + filePrefix + 'lose'
            self.loseActor = Actor.Actor(loseModel, {
                'lose': loseAnim })
            loseNeck = self.loseActor.find('**/joint-head')
            for part in self.headParts:
                part.instanceTo(loseNeck)
            
            self.setSuitClothes(self.loseActor)
        
        self.loseActor.setScale(self.scale)
        self.loseActor.setPos(self.getPos())
        self.loseActor.setHpr(self.getHpr())
        shadowJoint = self.loseActor.find('**/joint-shadow')
        dropShadow = loader.loadModelOnce('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        dropShadow.instanceTo(shadowJoint)
        return self.loseActor

    
    def cleanupLoseActor(self):
        self.notify.debug('cleanupLoseActor()')
        if self.loseActor != None:
            self.notify.debug('cleanupLoseActor() - got one')
            self.loseActor.cleanup()
        
        self.loseActor = None

    
    def getHeadParts(self):
        return self.headParts

    
    def getRightHand(self):
        return self.rightHand

    
    def getLeftHand(self):
        return self.leftHand

    
    def getShadowJoints(self):
        return [
            self.shadowNull]

    
    def getNametagJoints(self):
        return [
            self.nametagNull]

    
    def playDialogue(self, type, length):
        dialogueArray = SuitDialogArray
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
            if dialogueArray[2] != None:
                base.playSfx(dialogueArray[2])
            
        elif type == 'special':
            if dialogueArray[2] != None:
                base.playSfx(dialogueArray[2])
            
        else:
            self.notify.error('unrecognized dialogue type: ', type)
        return None


