# Source Generated with Decompyle++
# File: DistributedTagGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DistributedMinigame import *
import FSM
import State
from ToontownGlobals import *
import Walk
import ToontownTimer
import OnscreenText
import MinigameAvatarScorePanel

class DistributedTagGame(DistributedMinigame):
    DURATION = 60
    IT_SPEED_INCREASE = 1.3
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = FSM.FSM('DistributedTagGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'play']),
            State.State('play', self.enterPlay, self.exitPlay, [
                'finish']),
            State.State('finish', self.enterFinish, self.exitFinish, [
                'off'])], 'off', 'off')
        self.frameworkFSM.getStateNamed('game').addChild(self.gameFSM)
        self.walkStateData = Walk.Walk('walkDone')
        self.scorePanels = []
        self.initialPositions = ((0, 10, 0, 180, 0, 0), (10, 0, 0, 90, 0, 0), (0, -10, 0, 0, 0, 0), (-10, 0, 0, -90, 0, 0))
        toonbase.localToon.isIt = 0
        self.modelCount = 4

    
    def getTitle(self):
        return 'Tag Game'

    
    def getInstructions(self):
        return 'Collect the treasures. You cannot collect treasure when you are IT!'

    
    def generate(self):
        DistributedMinigame.generate(self)

    
    def disable(self):
        DistributedMinigame.disable(self)

    
    def load(self):
        DistributedMinigame.load(self)
        self.itText = OnscreenText.OnscreenText('itText', fg = (0.95, 0.95, 0.65, 1), scale = 0.14, font = getSignFont(), pos = (0.0, -0.8), mayChange = 1)
        self.itText.hide()
        self.sky = loader.loadModel('phase_4/models/props/TT_sky')
        self.ground = loader.loadModel('phase_4/models/minigames/tag_arena')
        self.music = base.loadMusic('phase_4/audio/bgm/MG_toontag.mid')
        self.tagSfx = base.loadSfx('phase_4/audio/sfx/MG_tag.mp3')
        self.itPointer = loader.loadModel('phase_4/models/minigames/bboard-pointer')

    
    def unload(self):
        DistributedMinigame.unload(self)
        self.ignoreAll()
        toonbase.localToon.stopSky(self.sky)
        self.sky.removeNode()
        del self.sky
        self.itPointer.removeNode()
        del self.itPointer
        self.ground.removeNode()
        del self.ground
        base.unloadMusic(self.music)
        del self.music
        base.unloadSfx(self.tagSfx)
        del self.tagSfx
        self.itText.cleanup()
        del self.itText
        self.frameworkFSM.getStateNamed('game').removeChild(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        DistributedMinigame.onstage(self)
        self.ground.reparentTo(render)
        self.sky.reparentTo(render)
        toonbase.localToon.startSky(self.sky)
        toonbase.localToon.b_setParent('render')
        toonbase.localToon.setPos(0, 0, 0)
        camera.reparentTo(render)
        camera.setPosHpr(toonbase.localToon, 0, -24, 16, 0, -30, 0)
        base.transitions.irisIn(0.4)
        NametagGlobals.setMasterArrowsOn(1)

    
    def offstage(self):
        NametagGlobals.setMasterArrowsOn(0)
        DistributedMinigame.offstage(self)
        toonbase.localToon.stopSky(self.sky)
        self.ground.reparentTo(hidden)

    
    def setGameReady(self):
        DistributedMinigame.setGameReady(self)
        for avId in self.avIdList:
            self.acceptTagEvent(avId)
        
        i = self.avIdList.index(self.localAvId)
        toonbase.localToon.setPosHpr(*self.initialPositions[i])
        toonbase.localToon.d_setPosHpr(*self.initialPositions[i])

    
    def setGameStart(self):
        DistributedMinigame.setGameStart(self)
        self.gameFSM.request('play')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterPlay(self):
        for i in range(len(self.avIdList)):
            avId = self.avIdList[i]
            avName = self.getAvatarName(avId)
            scorePanel = MinigameAvatarScorePanel.MinigameAvatarScorePanel(avId, avName)
            scorePanel.setPos(1.12, 0, 0.25 * i)
            self.scorePanels.append(scorePanel)
        
        self.walkStateData.enter()
        self.walkStateData.fsm.request('walking')
        if toonbase.localToon.isIt:
            base.mouseInterfaceNode.setForwardSpeed(ToonForwardSpeed * self.IT_SPEED_INCREASE)
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.setTime(self.DURATION)
        self.timer.countdown(self.DURATION, self.timerExpired)
        base.playMusic(self.music, looping = 1, volume = 0.9)
        toonbase.localToon.setIdealCameraPos(Point3(0, -24, 8))

    
    def exitPlay(self):
        self.walkStateData.exit()
        base.stopMusic(self.music)
        self.timer.destroy()
        del self.timer
        for panel in self.scorePanels:
            panel.cleanup()
        
        self.scorePanels = []
        base.mouseInterfaceNode.setForwardSpeed(ToonForwardSpeed)
        self.itPointer.reparentTo(hidden)
        toonbase.localToon.cameraIndex = 0
        toonbase.localToon.setIdealCameraPosByIndex(0)

    
    def timerExpired(self):
        self.notify.debug('local timer expired')
        self.gameFSM.request('finish')

    
    def enterFinish(self):
        self.gameOver()

    
    def exitFinish(self):
        pass

    
    def setIt(self, avId):
        self.itText.show()
        self.notify.debug(str(avId) + ' is now it')
        if avId == self.localAvId:
            self.itText.setText('You Are IT!')
            toonbase.localToon.isIt = 1
            base.mouseInterfaceNode.setForwardSpeed(ToonForwardSpeed * self.IT_SPEED_INCREASE)
        else:
            self.itText.setText(self.getAvatarName(avId) + ' is IT!')
            toonbase.localToon.isIt = 0
            base.mouseInterfaceNode.setForwardSpeed(ToonForwardSpeed)
        avatar = self.getAvatar(avId)
        if avatar:
            self.itPointer.reparentTo(avatar)
            self.itPointer.setZ(avatar.getHeight())
        
        base.playSfx(self.tagSfx)

    
    def acceptTagEvent(self, avId):
        self.accept('enterdistAvatarCollNode-' + str(avId), self.sendTagIfIt, [
            avId])

    
    def sendTagIfIt(self, avId, collisionEntry):
        if toonbase.localToon.isIt:
            self.notify.debug('Tagging ' + str(avId))
            self.sendUpdate('tag', [
                self.localAvId,
                avId])
        else:
            self.notify.debug('Bumped ' + str(avId))

    
    def setTreasureScore(self, scores):
        self.notify.debug('setTreasureScore: %s' % scores)
        for i in range(len(self.scorePanels)):
            self.scorePanels[i].setScore(scores[i])
        


