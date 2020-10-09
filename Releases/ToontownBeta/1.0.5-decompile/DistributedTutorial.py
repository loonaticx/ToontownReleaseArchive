# Source Generated with Decompyle++
# File: DistributedTutorial.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
from IntervalGlobal import *
import ToontownGlobals
import DistributedObject
import DirectNotifyGlobal
import FSM
import State
import Char
import AvatarDNA
import Toon
import CollisionSphere
import CollisionNode
import DistributedAvatar

class DistributedTutorial(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorial')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.isLoaded = 0
        self.arrow1 = loader.loadModelOnce('phase_3/models/props/arrow')
        self.arrow2 = loader.loadModelOnce('phase_3/models/props/arrow')
        self.fsm = FSM.FSM('DistributedTutorial', [
            State.State('off', self.enterOff, self.exitOff, [
                'waitForToon']),
            State.State('waitForToon', self.enterWaitForToon, self.exitWaitForToon, [
                'navigate',
                'off']),
            State.State('navigate', self.enterNavigate, self.exitNavigate, [
                'flippyIntro',
                'off']),
            State.State('flippyIntro', self.enterFlippyIntro, self.exitFlippyIntro, [
                'qt',
                'chat',
                'off']),
            State.State('qt', self.enterQt, self.exitQt, [
                'bodyClick',
                'off']),
            State.State('chat', self.enterChat, self.exitChat, [
                'bodyClick',
                'off']),
            State.State('bodyClick', self.enterBodyClick, self.exitBodyClick, [
                'friends',
                'off']),
            State.State('friends', self.enterFriends, self.exitFriends, [
                'book',
                'off']),
            State.State('book', self.enterBook, self.exitBook, [
                'laffMeter',
                'off']),
            State.State('laffMeter', self.enterLaffMeter, self.exitLaffMeter, [
                'trolley',
                'off']),
            State.State('trolley', self.enterTrolley, self.exitTrolley, [
                'bye',
                'off']),
            State.State('bye', self.enterBye, self.exitBye, [
                'off'])], 'off', 'off')
        self.fsm.enterInitialState()
        return None

    
    def generate(self):
        self.mickey = Char.Char()
        mickeyDNA = AvatarDNA.AvatarDNA()
        mickeyDNA.newChar('mk')
        self.mickey.setName('Mickey')
        self.mickey.setDNA(mickeyDNA)
        self.mickey.initializeBodyCollisions('tutorialMickey')
        self.mickey.reparentTo(render)
        self.mickey.addActive()
        self.flippyDNA = AvatarDNA.AvatarDNA()
        self.flippyDNA.type = 't'
        self.flippyDNA.head = 'dls'
        self.flippyDNA.torso = 'ms'
        self.flippyDNA.legs = 'm'
        self.flippyDNA.armColor = 6
        self.flippyDNA.legColor = 6
        self.flippyDNA.headColor = 6
        self.flippyDNA.gloveColor = 0
        self.flippyDNA.topTex = 40
        self.flippyDNA.botTex = 8
        self.flippy = Toon.Toon()
        self.flippy.doId = -1
        self.flippy.setName('Flippy')
        self.flippy.setDNA(self.flippyDNA)
        self.flippy.initializeBodyCollisions('tutorialFlippy')
        self.fsm.request('waitForToon')
        return None

    
    def disable(self):
        self.fsm.request('off')
        self.cleanupMickey()
        self.cleanupFlippy()

    
    def delete(self):
        self.fsm.request('off')
        del self.fsm
        self.arrow1.removeNode()
        self.arrow2.removeNode()
        del self.arrow1
        del self.arrow2
        return None

    
    def cleanupMickey(self):
        if hasattr(self, 'mickey'):
            self.mickey.removeActive()
            self.mickey.disableBodyCollisions()
            self.mickey.delete()
            del self.mickey
        
        return None

    
    def cleanupFlippy(self):
        if hasattr(self, 'flippy'):
            self.flippy.disableBodyCollisions()
            self.flippy.delete()
            del self.flippy
            del self.flippyDNA
        
        return None

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterWaitForToon(self):
        self.acceptOnce('toonEntersTutorial', self._DistributedTutorial__waitForToonHandler)
        return None

    
    def __waitForToonHandler(self):
        self.fsm.request('navigate')
        return None

    
    def exitWaitForToon(self):
        self.ignore('toonEntersTutorial')

    
    def enterNavigate(self):
        toonbase.localToon.chatMgr.stop()
        toonbase.localToon.book.hideButton()
        toonbase.localToon.setFriendsListButtonActive(0)
        toonbase.localToon.laffMeter.stop()
        self.collSphere = CollisionSphere.CollisionSphere(0, 0, 0, 12)
        self.collSphereNode = CollisionNode.CollisionNode()
        self.collSphereNode.addSolid(self.collSphere)
        self.collSphereNodePath = self.mickey.attachNewNode(self.collSphereNode)
        self.collSphereBitMask = ToontownGlobals.WallBitmask
        self.collSphereNode.setCollideMask(self.collSphereBitMask)
        self.collSphereNode.setName('mickeyTutorialSphere')
        self.collSphere.setTangible(0)
        self.mickey.hideCollisionSolids()
        self.acceptOnce('enter' + self.collSphereNode.getName(), self._DistributedTutorial__handleNavToMickey)
        self.mickey.setPosHpr(99, -11, -1.3, -77, 0, 0)
        self.mickey.loop('neutral')
        navIntervals = []
        navIntervals.append(FunctionInterval(self.mickey.clearChat))
        navIntervals.append(WaitInterval(3))
        navIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Hi %s!' % toonbase.localToon.getName(),
            CFSpeech]))
        navIntervals.append(WaitInterval(3))
        navIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Hi %s!\nCome over here!' % toonbase.localToon.getName(),
            CFSpeech]))
        navIntervals.append(WaitInterval(3))
        navIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Hi %s!\nCome over here!\nUse the arrow keys!' % toonbase.localToon.getName(),
            CFSpeech]))
        self.navTrack = Track(navIntervals)
        self.navTrack.play()
        return None

    
    def __handleNavToMickey(self, collEntry):
        self.fsm.request('flippyIntro')
        return None

    
    def exitNavigate(self):
        self.mickey.clearChat()
        self.navTrack.stop()
        del self.navTrack
        self.ignore('enter' + self.collSphereNode.getName())
        self.collSphereNodePath.reparentTo(hidden)
        self.collSphereNodePath.removeNode()
        del self.collSphereNodePath
        del self.collSphereNode
        del self.collSphere
        return None

    
    def enterFlippyIntro(self):
        toonbase.localToon.detachCamera()
        toonbase.localToon.stopTrackAnimToSpeed()
        toonbase.localToon.loop('neutral')
        efIntervals = []
        efIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Welcome to Toontown!',
            CFSpeech]))
        efIntervals.append(LerpPosHprInterval(toonbase.localToon, duration = 1.0, pos = Point3(110, -10, -1.3), hpr = Point3(112, 0, 0)))
        efIntervals.append(WaitInterval(2.0))
        efIntervals.append(FunctionInterval(self.chooseChat))
        self.efTrack = Track(efIntervals)
        self.efTrack.play()
        return None

    
    def chooseChat(self):
        if toonbase.localToon.chatMgr.chatPermission():
            self.fsm.request('chat')
        else:
            self.fsm.request('qt')
        return None

    
    def exitFlippyIntro(self):
        self.efTrack.stop()
        del self.efTrack
        return None

    
    def enterQt(self):
        self.accept('chatUpdateQT', self._DistributedTutorial__handleChatUpdateQT)
        chatIntervals = []
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'You can talk by using this.',
            CFSpeech]))
        chatIntervals.append(WaitInterval(0.5))
        chatIntervals.append(FunctionInterval(toonbase.localToon.chatMgr.start))
        chatIntervals.append(FunctionInterval(self.arrowsOn, extraArgs = [
            -1.13,
            0.7,
            90,
            -10.13,
            0.7,
            90]))
        chatIntervals.append(WaitInterval(2.5))
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'You can talk by using this.\nClick it, then choose "Hi".',
            CFSpeech]))
        self.qtTrack = Track(chatIntervals)
        self.qtTrack.play()
        return None

    
    def __handleChatUpdateQT(self, qtList):
        if qtList[0] == 0:
            self.fsm.request('bodyClick')
        
        return None

    
    def exitQt(self):
        self.mickey.clearChat()
        self.qtTrack.stop()
        del self.qtTrack
        self.arrowsOff()
        self.ignore('chatUpdateQT')
        return None

    
    def enterChat(self):
        self.accept('chatUpdateQT', self._DistributedTutorial__handleChatUpdateQT)
        self.accept('chatUpdate', self._DistributedTutorial__handleChatUpdate)
        chatIntervals = []
        chatIntervals.append(WaitInterval(2.5))
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'You can talk using either of these buttons.',
            CFSpeech]))
        chatIntervals.append(WaitInterval(0.5))
        chatIntervals.append(FunctionInterval(toonbase.localToon.chatMgr.start))
        chatIntervals.append(FunctionInterval(self.arrowsOn, extraArgs = [
            -1.28,
            0.7,
            90,
            -1.13,
            0.7,
            90]))
        chatIntervals.append(WaitInterval(4.0))
        chatIntervals.append(FunctionInterval(self.arrowsOn, extraArgs = [
            -1.28,
            0.7,
            90,
            -10.13,
            0.7,
            90]))
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'The blue button lets you chat with the keyboard',
            CFSpeech]))
        chatIntervals.append(WaitInterval(5.0))
        chatIntervals.append(FunctionInterval(self.arrowsOn, extraArgs = [
            -10.28,
            0.7,
            90,
            -1.13,
            0.7,
            90]))
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'The green one opens the ToonTalker',
            CFSpeech]))
        chatIntervals.append(WaitInterval(5.0))
        chatIntervals.append(FunctionInterval(self.arrowsOff))
        chatIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Try typing "Hi".',
            CFSpeech]))
        self.chatTrack = Track(chatIntervals)
        self.chatTrack.play()
        return None

    
    def __handleChatUpdate(self, chatMessage, chatFlags):
        lowerChatMessage = chatMessage.lower()
        if lowerChatMessage.count('hello') and lowerChatMessage.count('hi') and lowerChatMessage.count('howdy') or lowerChatMessage.count('hey'):
            self.fsm.request('bodyClick')
        
        return None

    
    def exitChat(self):
        self.mickey.clearChat()
        self.ignore('chatUpdate')
        self.ignore('chatUpdateQT')
        self.chatTrack.stop()
        del self.chatTrack
        self.arrowsOff()
        return None

    
    def enterBodyClick(self):
        bcIntervals = []
        bcIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Very good!',
            CFSpeech]))
        bcIntervals.append(WaitInterval(3))
        bcIntervals.append(FunctionInterval(self._DistributedTutorial__handleBodyClick))
        self.bcTrack = Track(bcIntervals)
        self.bcTrack.play()
        return None

    
    def __handleBodyClick(self):
        self.fsm.request('friends')
        return None

    
    def exitBodyClick(self):
        self.mickey.clearChat()
        self.bcTrack.stop()
        del self.bcTrack
        return None

    
    def enterFriends(self):
        self.fsm.request('book')
        return None

    
    def exitFriends(self):
        return None

    
    def enterBook(self):
        self.fsm.request('laffMeter')
        return None

    
    def exitBook(self):
        self.mickey.clearChat()
        return None

    
    def enterLaffMeter(self):
        lmIntervals = []
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 0
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'You will also need this...',
            CFSpeech]))
        lmIntervals.append(WaitInterval(0.5))
        lmIntervals.append(FunctionInterval(toonbase.localToon.laffMeter.start))
        lmIntervals.append(FunctionInterval(self.arrowsOn, extraArgs = [
            -1.19,
            -0.63,
            270,
            -0.95,
            -0.87,
            180]))
        lmIntervals.append(WaitInterval(2.5))
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            "You will also need this...\nIt's your Laffmeter.",
            CFSpeech]))
        lmIntervals.append(WaitInterval(4.0))
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'When COGS attack you, it gets lower.',
            CFSpeech]))
        lmIntervals.append(WaitInterval(1.0))
        countdown = range(1, 15)
        countdown.reverse()
        self.originalHp = toonbase.localToon.hp
        for i in countdown:
            lmIntervals.append(FunctionInterval(toonbase.localToon.setHp, extraArgs = [
                i]))
            lmIntervals.append(WaitInterval(0.1))
        
        lmIntervals.append(WaitInterval(3.0))
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'When you are in playgrounds like this one, it goes back up.',
            CFSpeech]))
        lmIntervals.append(WaitInterval(1.0))
        countdown = range(1, 16)
        for i in countdown:
            lmIntervals.append(FunctionInterval(toonbase.localToon.setHp, extraArgs = [
                i]))
            lmIntervals.append(WaitInterval(0.1))
        
        lmIntervals.append(WaitInterval(3.0))
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Be careful! If the COGS defeat you, you will lose all your gags.',
            CFSpeech]))
        countdown = range(0, 1)
        countdown.reverse()
        for i in countdown:
            lmIntervals.append(FunctionInterval(toonbase.localToon.setHp, extraArgs = [
                i]))
            lmIntervals.append(WaitInterval(0.1))
        
        lmIntervals.append(WaitInterval(4.5))
        lmIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'To get more gags, play trolley games.',
            CFSpeech]))
        countdown = range(15, 16)
        for i in countdown:
            lmIntervals.append(FunctionInterval(toonbase.localToon.setHp, extraArgs = [
                i]))
            lmIntervals.append(WaitInterval(0.1))
        
        lmIntervals.append(FunctionInterval(toonbase.localToon.setHp, extraArgs = [
            self.originalHp]))
        lmIntervals.append(WaitInterval(4.5))
        lmIntervals.append(FunctionInterval(self.fsm.request, extraArgs = [
            'trolley']))
        self.lmTrack = Track(lmIntervals)
        self.lmTrack.play()
        return None

    
    def exitLaffMeter(self):
        self.mickey.clearChat()
        self.lmTrack.stop()
        del self.lmTrack
        toonbase.localToon.setHp(self.originalHp)
        DistributedAvatar.DistributedAvatar.LaffNumbersEnabled = 1
        self.arrowsOff()
        return None

    
    def enterTrolley(self):
        self.acceptOnce('entertrolley_sphere', self.handleTrolleyBoard)
        walkIntervals = []
        walkIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Follow me to the trolley!',
            CFSpeech]))
        walkIntervals.append(FunctionInterval(toonbase.localToon.attachCamera))
        walkIntervals.append(FunctionInterval(toonbase.localToon.startTrackAnimToSpeed))
        walkIntervals.append(WaitInterval(1.5))
        walkIntervals.append(FunctionInterval(self.mickey.loop, extraArgs = [
            'walk']))
        pathPoints = [
            Vec3(99, -11, -1.3),
            Vec3(83, -45, -1.3),
            Vec3(58, -52, -1.3),
            Vec3(42, -49, 6.2),
            Vec3(16, -46, 6.692)]
        pathTrack = self.makePathTrack(self.mickey, pathPoints, 7)
        walkIntervals.append(pathTrack)
        walkIntervals.append(FunctionInterval(self.mickey.loop, extraArgs = [
            'neutral']))
        walkIntervals.append(FunctionInterval(self.mickey.setHpr, extraArgs = [
            -60,
            0,
            0]))
        walkIntervals.append(FunctionInterval(self.mickey.clearChat))
        walkIntervals.append(WaitInterval(1))
        walkIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Hop on board!',
            CFSpeech]))
        self.trolleyTrack = Track(walkIntervals)
        self.trolleyTrack.play()
        return None

    
    def makePathTrack(self, nodePath, posPoints, velocity):
        intervals = []
        restOfPosPoints = posPoints[1:]
        for pointIndex in range(len(posPoints) - 1):
            startPoint = posPoints[pointIndex]
            endPoint = posPoints[pointIndex + 1]
            intervals.append(FunctionInterval(nodePath.headsUpPreserveScale, extraArgs = [
                endPoint[0],
                endPoint[1],
                endPoint[2]]))
            distance = Vec3(endPoint - startPoint).length()
            duration = distance / velocity
            intervals.append(LerpPosInterval(nodePath, duration = duration, pos = Point3(endPoint), startPos = Point3(startPoint)))
        
        track = Track(intervals)
        return track

    
    def handleTrolleyBoard(self, collEntry):
        self.fsm.request('bye')
        return None

    
    def exitTrolley(self):
        self.mickey.clearChat()
        self.ignore('entertrolley_sphere')
        self.trolleyTrack.stop()
        del self.trolleyTrack
        return None

    
    def enterBye(self):
        byeIntervals = []
        byeIntervals.append(FunctionInterval(self.mickey.loop, extraArgs = [
            'neutral']))
        byeIntervals.append(FunctionInterval(self.mickey.clearChat))
        byeIntervals.append(FunctionInterval(self.mickey.setPosHpr, extraArgs = [
            16,
            -46,
            6.692,
            -60,
            0,
            0]))
        byeIntervals.append(WaitInterval(2))
        byeIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Play some games!',
            CFSpeech]))
        byeIntervals.append(WaitInterval(3))
        byeIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Play some games!\nBuy some gags!',
            CFSpeech]))
        byeIntervals.append(WaitInterval(3))
        byeIntervals.append(FunctionInterval(self.mickey.setChat, extraArgs = [
            'Play some games!\nBuy some gags!\nSee you later!',
            CFSpeech]))
        self.acceptOnce('trolleyLeaving', self.d_allDone)
        self.byeTrack = Track(byeIntervals)
        self.byeTrack.play()
        return None

    
    def d_allDone(self):
        self.sendUpdate('allDone', [])
        return None

    
    def exitBye(self):
        self.ignore('trolleyLeaving')
        self.mickey.clearChat()
        self.byeTrack.stop()
        del self.byeTrack
        return None

    
    def arrowsOn(self, x1, y1, h1, x2, y2, h2):
        self.stopArrowsFlashing()
        self.arrow1.reparentTo(aspect2d)
        self.arrow2.reparentTo(aspect2d)
        self.arrow1.setScale(0.2)
        self.arrow2.setScale(0.2)
        self.arrow1.setPos(x1, 0, y1)
        self.arrow2.setPos(x2, 0, y2)
        self.arrow1.setR(h1)
        self.arrow2.setR(h2)
        self.startArrowsFlashing()
        return None

    
    def arrowsOff(self):
        self.stopArrowsFlashing()
        self.arrow1.reparentTo(hidden)
        self.arrow2.reparentTo(hidden)
        return None

    
    def startArrowsFlashing(self):
        arrowIntervals = [
            FunctionInterval(self.showArrows),
            WaitInterval(0.5),
            FunctionInterval(self.hideArrows),
            WaitInterval(0.5)]
        self.arrowTrack = Track(arrowIntervals)
        self.arrowTrack.loop()
        return None

    
    def stopArrowsFlashing(self):
        if hasattr(self, 'arrowTrack'):
            self.arrowTrack.stop()
            del self.arrowTrack
        
        self.hideArrows()
        return None

    
    def showArrows(self):
        self.arrow1.show()
        self.arrow2.show()
        return None

    
    def hideArrows(self):
        self.arrow1.hide()
        self.arrow2.hide()
        return None


