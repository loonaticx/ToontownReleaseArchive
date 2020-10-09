# Source Generated with Decompyle++
# File: Avatar.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from PandaModules import *
import ToontownGlobals
import Actor
import AvatarDNA
import Point3
import NamedNode
import TextNode

class Avatar(Actor.Actor):
    notify = Actor.directNotify.newCategory('Avatar')
    ActiveAvatars = []
    
    def __init__(self):
        
        try:
            self.Avatar_initialized
        except:
            self.Avatar_initialized = 1
            Actor.Actor.__init__(self)
            self._Avatar__font = ToontownGlobals.getToonFont()
            self._Avatar__nameVisible = 1
            self.nametag = NametagGroup()
            self.nametag.setAvatarNode(self.node())
            self.nametag.setFont(ToontownGlobals.getInterfaceFont())
            self.nametag3ds = []
            self.dropShadows = []
            self.scale = 1.0
            self.nametagScale = 1.0
            self.height = 0.0
            self.name = ''
            self.style = None

        return None

    
    def delete(self):
        
        try:
            self.Avatar_deleted
        except:
            self.Avatar_deleted = 1
            del self._Avatar__font
            del self.style
            self.deleteNametag3d()
            del self.nametag
            self.deleteDropShadow()
            Actor.Actor.delete(self)


    
    def setDNAString(self, dnaString):
        newDNA = AvatarDNA.AvatarDNA()
        newDNA.makeFromNetString(dnaString)
        self.setDNA(newDNA)

    
    def setDNA(self, dna):
        if self.style:
            type = dna.type
            if type == AvatarDNA.toonType:
                self.updateToonDNA(dna)
            elif type == AvatarDNA.charType:
                self.updateCharDNA(dna)
            
        else:
            self.style = dna
            type = dna.type
            if type == AvatarDNA.toonType:
                self.generateToon()
            elif type == AvatarDNA.suitType:
                self.generateSuit()
            elif type == AvatarDNA.charType:
                self.generateChar()
            else:
                Avatar.notify.error('unknown DNA type: %s' % type)
            self.initializeDropShadow()
            self.initializeNametag3d()
        return None

    
    def getAvatarScale(self):
        return self.scale

    
    def setAvatarScale(self, scale):
        if self.scale != scale:
            self.scale = scale
            self.getGeomNode().setScale(scale)
            self.setNametagScale(self.nametagScale)
            self.setHeight(self.height)
        

    
    def getNametagScale(self):
        return self.nametagScale

    
    def setNametagScale(self, scale):
        self.nametagScale = scale
        for n in self.nametag3ds:
            n.setScale(scale / self.scale)
        

    
    def getHeight(self):
        return self.height

    
    def setHeight(self, height):
        self.height = height
        for n in self.nametag3ds:
            n.setPos(0, 0, (height + 0.5) / self.scale)
        

    
    def getName(self):
        return self.name

    
    def setName(self, name):
        self.name = name
        self.nametag.setName(name)

    
    def getFont(self):
        return self._Avatar__font

    
    def setFont(self, font):
        self._Avatar__font = font
        self.nametag.setFont(font)

    
    def getStyle(self):
        return self.style

    
    def setStyle(self, style):
        self.style = style

    
    def setChat(self, message, chatFlags):
        self.nametag.setChat(message, chatFlags)

    
    def clearChat(self):
        self.nametag.clearChat()

    
    def isInView(self):
        pos = self.getPos(camera)
        eyePos = Point3.Point3(pos[0], pos[1], pos[2] + self.getHeight())
        return base.cam.node().isInView(eyePos)

    
    def getNameVisible(self):
        return self._Avatar__nameVisible

    
    def setNameVisible(self, bool):
        self._Avatar__nameVisible = bool
        if bool:
            self.showName()
        
        if not bool:
            self.hideName()
        

    
    def hideName(self):
        self.nametag.getNametag3d().setContents(Nametag.CSpeech | Nametag.CThought)

    
    def showName(self):
        if self._Avatar__nameVisible:
            self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)
        

    
    def hideNametag2d(self):
        self.nametag.getNametag2d().setContents(0)

    
    def showNametag2d(self):
        self.nametag.getNametag2d().setContents(Nametag.CName | Nametag.CSpeech)

    
    def hideNametag3d(self):
        self.nametag.getNametag3d().setContents(0)

    
    def showNametag3d(self):
        self.nametag.getNametag3d().setContents(Nametag.CName | Nametag.CSpeech | Nametag.CThought)

    
    def setPickable(self, flag):
        self.nametag.setActive(flag)

    
    def clickedNametag(self):
        messenger.send('clickedNametag', [
            self])

    
    def initializeDropShadow(self):
        self.deleteDropShadow()
        self.getGeomNode().setZ(0.025)
        dropShadow = loader.loadModelOnce('phase_3/models/props/drop_shadow')
        dropShadow.setScale(0.45)
        dropShadow.setColor(0.0, 0.0, 0.0, 0.5)
        self.dropShadows = []
        for shadowJoint in self.getShadowJoints():
            instance = dropShadow.instanceTo(shadowJoint)
            instance.flattenMedium()
            self.dropShadows.append(instance)
        
        dropShadow.removeNode()

    
    def deleteDropShadow(self):
        for shadow in self.dropShadows:
            shadow.removeNode()
        
        self.dropShadows = []

    
    def initializeNametag3d(self):
        self.deleteNametag3d()
        nametagNode = self.nametag.getNametag3d().upcastToNamedNode()
        self.nametag3ds = []
        for nametagJoint in self.getNametagJoints():
            self.nametag3ds.append(nametagJoint.attachNewNode(nametagNode))
        
        self.setNametagScale(self.nametagScale)
        self.setHeight(self.height)

    
    def deleteNametag3d(self):
        for shadow in self.nametag3ds:
            shadow.removeNode()
        
        self.nametag3ds = []

    
    def initializeBodyCollisions(self, collIdStr):
        self.collSphere = CollisionSphere(0, 0, 0.5, 1.0)
        self.collNode = CollisionNode(collIdStr)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.collNode.setCollideMask(ToontownGlobals.WallBitmask)
        return None

    
    def disableBodyCollisions(self):
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode
        del self.collSphere

    
    def addActive(self):
        self.notify.info('Adding avatar %s' % self.getName())
        
        try:
            Avatar.ActiveAvatars.remove(self)
        except ValueError:
            pass

        Avatar.ActiveAvatars.append(self)
        self.nametag.manage(toonbase.marginManager)
        self.accept(self.nametag.getUniqueId(), self.clickedNametag)

    
    def removeActive(self):
        self.notify.info('Removing avatar %s' % self.getName())
        
        try:
            Avatar.ActiveAvatars.remove(self)
        except ValueError:
            self.notify.warning('%s was not present...' % self)

        self.nametag.unmanage(toonbase.marginManager)
        self.ignore(self.nametag.getUniqueId())


