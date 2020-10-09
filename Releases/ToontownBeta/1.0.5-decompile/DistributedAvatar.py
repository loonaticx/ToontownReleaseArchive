# Source Generated with Decompyle++
# File: DistributedAvatar.pyo (Python 2.0)

from PandaObject import *
import DistributedNode
import DistributedActor
import ToontownGlobals
import Avatar
import AvatarDNA
import ChatGarbler
import ChatManager
import string
import Task
import InventoryNew
import Experience
import QTGraph

class DistributedAvatar(DistributedActor.DistributedActor, Avatar.Avatar):
    LaffNumberGenerator = TextNode()
    LaffNumberGenerator.freeze()
    LaffNumbersEnabled = 1
    
    def __init__(self, cr):
        
        try:
            self.DistributedAvatar_initialized
        except:
            self.DistributedAvatar_initialized = 1
            Avatar.Avatar.__init__(self)
            DistributedActor.DistributedActor.__init__(self, cr)
            self._DistributedAvatar__chatGarbler = ChatGarbler.ChatGarbler()
            self.chatPermission = 0
            self._DistributedAvatar__teleportAvailable = 0
            self.soundChatBubble = base.loadSfx('phase_4/audio/sfx/GUI_balloon_popup.mp3')
            self.laffNumber = None
            self.inventory = None
            self.experience = None
            self.hp = None
            self.maxHp = None

        return None

    
    def disable(self):
        self.reparentTo(hidden)
        self.removeActive()
        self.disableBodyCollisions()
        self.hideLaffNumber()
        self.hp = None
        DistributedActor.DistributedActor.disable(self)

    
    def delete(self):
        
        try:
            self.DistributedAvatar_deleted
        except:
            self.DistributedAvatar_deleted = 1
            del self.experience
            if self.inventory:
                self.inventory.unload()
            
            del self.inventory
            del self._DistributedAvatar__chatGarbler
            base.unloadSfx(self.soundChatBubble)
            del self.soundChatBubble
            DistributedActor.DistributedActor.delete(self)
            Avatar.Avatar.delete(self)


    
    def generate(self):
        DistributedNode.DistributedNode.generate(self)
        self.addActive()
        self.initializeBodyCollisions('distAvatarCollNode-' + str(self.doId))

    
    def b_setHp(self, hitPoints):
        self.setHp(hitPoints)
        self.d_setHp(hitPoints)

    
    def d_setHp(self, hitPoints):
        self.sendUpdate('setHp', [
            hitPoints])

    
    def setHp(self, hitPoints):
        if self.hp != None:
            oldHp = max(self.hp, 0)
            newHp = max(hitPoints, 0)
            hpDisplayDelta = newHp - oldHp
            self.showLaffNumber(hpDisplayDelta)
        
        self.hp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
            
            if oldHp <= 0 and newHp > 0:
                messenger.send(self.uniqueName('positiveHP'))
        except:
            pass


    
    def getHp(self):
        return self.hp

    
    def b_setMaxHp(self, hitPoints):
        self.setMaxHp(hitPoints)
        self.d_setMaxHp(hitPoints)

    
    def d_setMaxHp(self, hitPoints):
        self.sendUpdate('setMaxHp', [
            hitPoints])

    
    def setMaxHp(self, hitPoints):
        self.maxHp = hitPoints
        
        try:
            if self.hp != None and self.maxHp != None:
                messenger.send(self.uniqueName('hpChange'), [
                    self.hp,
                    self.maxHp])
        except AttributeError:
            pass

        if self.inventory:
            self.inventory.updateGUI()
        

    
    def getMaxHp(self):
        return self.hp

    
    def b_setExperience(self, experience):
        self.setExperience(experience)
        self.d_setExperience(experience)

    
    def d_setExperience(self, experience):
        self.sendUpdate('setExperience', [
            experience.makeNetString()])

    
    def setExperience(self, experience):
        self.experience = Experience.Experience(experience)
        if self.inventory:
            self.inventory.updateGUI()
        
        return None

    
    def setInventory(self, inventoryNetString):
        if not (self.inventory):
            self.inventory = InventoryNew.InventoryNew(self, inventoryNetString)
        
        self.inventory.updateInvString(inventoryNetString)
        return None

    
    def setAccountName(self, accountName):
        self.accountName = accountName

    
    def setLastHood(self, lastHood):
        self.lastHood = lastHood

    
    def d_setWhisper(self, chatString, sendToId = None):
        self.sendUpdate('setWhisper', [
            chatString], sendToId)
        return None

    
    def setWhisper(self, chatString):
        self.displayWhisper(chatString)
        return None

    
    def displayWhisper(self, chatString):
        print 'Whisper to %s: %s' % (self.getName(), chatString)

    
    def b_setChat(self, chatString, chatFlags):
        if len(chatString) > 0 and chatString[0] == '~':
            messenger.send('magicWord', [
                chatString])
        else:
            self.setChatAbsolute(chatString, chatFlags)
            self.d_setChat(chatString, chatFlags)
        return None

    
    def d_setChat(self, chatString, chatFlags):
        self.sendUpdate('setChat', [
            chatString,
            chatFlags])

    
    def setChatAbsolute(self, chatString, chatFlags):
        distance = self.getDistance(camera)
        if distance < 100.0:
            self.playDialogueForString(chatString)
            base.playSfx(self.soundChatBubble)
        
        Avatar.Avatar.setChat(self, chatString, chatFlags)

    
    def setChat(self, chatString, chatFlags):
        if toonbase.localToon.chatMgr.chatPermission() != 1:
            chatString = self._DistributedAvatar__chatGarbler.garble(self, chatString)
        
        self.setChatAbsolute(chatString, chatFlags & ~CFQuicktalker)

    
    def b_setQT(self, qtSequence):
        self.setQT(qtSequence)
        self.d_setQT(qtSequence)
        return None

    
    def d_setQT(self, qtSequence):
        self.sendUpdate('setQT', [
            qtSequence])

    
    def setQT(self, qtSequence):
        chatString = QTGraph.decodeQTMessage(qtSequence)
        distance = self.getDistance(camera)
        if distance < 100.0:
            self.playDialogueForString(chatString)
            base.playSfx(self.soundChatBubble)
        
        Avatar.Avatar.setChat(self, chatString, CFSpeech | CFQuicktalker | CFTimeout)

    
    def b_setParentalControl(self, canChat):
        self.setParentalControl(canChat)
        self.d_setParentalControl(canChat)
        return None

    
    def d_setParentalControl(self, canChat):
        self.sendUpdate('setParentalControl', [
            canChat])

    
    def setParentalControl(self, canChat):
        self.chatPermission = canChat
        if canChat:
            self.nametag.setColorCode(NametagGroup.CCNormal)
        else:
            self.nametag.setColorCode(NametagGroup.CCNoChat)

    
    def d_teleportQuery(self, requesterId, sendToId = None):
        self.sendUpdate('teleportQuery', [
            requesterId], sendToId)

    
    def teleportQuery(self, requesterId):
        avatar = None
        if toonbase.tcr.doId2do.has_key(requesterId):
            avatar = toonbase.tcr.doId2do[requesterId]
        elif toonbase.tcr.isFriend(requesterId):
            avatar = toonbase.tcr.identifyFriend(requesterId)
        
        if avatar != None:
            if self._DistributedAvatar__teleportAvailable:
                self.setWhisper('%s is coming to visit you.' % avatar.getName())
                messenger.send('teleportQuery', [
                    avatar,
                    self])
                return None
            
            self.setWhisper('%s tried to visit you.' % avatar.getName())
        
        self.d_teleportResponse(self.doId, 0, 0, 0, 0, sendToId = requesterId)

    
    def d_teleportResponse(self, avId, available, shardId, hoodId, zoneId, sendToId = None):
        self.sendUpdate('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId], sendToId)

    
    def teleportResponse(self, avId, available, shardId, hoodId, zoneId):
        messenger.send('teleportResponse', [
            avId,
            available,
            shardId,
            hoodId,
            zoneId])

    
    def setTeleportAvailable(self, available):
        self._DistributedAvatar__teleportAvailable = available

    
    def getTeleportAvailable(self):
        return self._DistributedAvatar__teleportAvailable

    
    def playDialogueForString(self, chatString):
        searchString = string.lower(chatString)
        if string.find(searchString, 'ooo') >= 0:
            type = 'special'
        elif string.find(searchString, '!') >= 0:
            type = 'exclamation'
        elif string.find(searchString, '?') >= 0:
            type = 'question'
        else:
            animal = self.getStyle().getType()
            if animal == 'dog' and animal == 'horse' or animal == 'duck':
                type = 'statementA'
            else:
                type = 'statementB'
        stringLength = len(chatString)
        if stringLength <= 6:
            length = 1
        elif stringLength <= 12:
            length = 2
        elif stringLength <= 20:
            length = 3
        else:
            length = 4
        self.playDialogue(type, length)
        return None

    
    def getName(self):
        return Avatar.Avatar.getName(self)

    
    def setName(self, name):
        return Avatar.Avatar.setName(self, name)

    
    def showLaffNumber(self, number, bonus = 0):
        if self.LaffNumbersEnabled:
            if number != 0:
                if self.laffNumber:
                    self.hideLaffNumber()
                
                self.LaffNumberGenerator.setFont(ToontownGlobals.getSignFont())
                if number < 0:
                    self.LaffNumberGenerator.setText(str(number))
                else:
                    self.LaffNumberGenerator.setText('+' + str(number))
                self.LaffNumberGenerator.clearShadow()
                self.LaffNumberGenerator.setAlign(TMALIGNCENTER)
                if bonus == 1:
                    r = 1.0
                    g = 1.0
                    b = 0
                    a = 1
                elif bonus == 2:
                    r = 1.0
                    g = 0.5
                    b = 0
                    a = 1
                elif number < 0:
                    r = 0.9
                    g = 0
                    b = 0
                    a = 1
                else:
                    r = 0
                    g = 0.9
                    b = 0
                    a = 1
                self.LaffNumberGenerator.setTextColor(r, g, b, a)
                self.laffNumberNode = self.LaffNumberGenerator.generate()
                self.laffNumber = self.attachNewNode(self.laffNumberNode)
                self.laffNumber.setBillboardAxis()
                self.laffNumber.setPos(0, 0, self.height / 2)
                seq = Task.sequence(self.laffNumber.lerpPos(Point3(0, 0, self.height + 1.5), 1.0, blendType = 'easeOut'), Task.pause(0.85), self.laffNumber.lerpColor(Vec4(r, g, b, a), Vec4(r, g, b, 0), 0.1), Task.Task(self.hideLaffNumberTask))
                taskMgr.spawnTaskNamed(seq, self.uniqueName('laffNumber'))
            
        
        return None

    
    def hideLaffNumberTask(self, task):
        self.hideLaffNumber()
        return Task.done

    
    def hideLaffNumber(self):
        if self.laffNumber:
            taskMgr.removeTasksNamed(self.uniqueName('laffNumber'))
            self.laffNumber.removeNode()
            self.laffNumber = None
        
        return None


