# Source Generated with Decompyle++
# File: DistributedRaceGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DistributedMinigame import *
import FSM
import State
import Button
import Task
from ToontownGlobals import *
from GuiGlobals import *
import Sign
import ToontownTimer

class DistributedRaceGame(DistributedMinigame):
    NumberToWin = 14
    InputTimeout = 10
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = FSM.FSM('DistributedRaceGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'inputChoice']),
            State.State('inputChoice', self.enterInputChoice, self.exitInputChoice, [
                'waitServerChoices']),
            State.State('waitServerChoices', self.enterWaitServerChoices, self.exitWaitServerChoices, [
                'moveAvatars']),
            State.State('moveAvatars', self.enterMoveAvatars, self.exitMoveAvatars, [
                'inputChoice',
                'finish']),
            State.State('finish', self.enterFinish, self.exitFinish, [
                'off'])], 'off', 'off')
        self.frameworkFSM.getStateNamed('game').addChild(self.gameFSM)
        self.posHprArray = (((-9.03, 0.06, 0.025, -152.9), (-7.43, -2.76, 0.025, -152.68), (-6.02, -5.48, 0.025, -157.54), (-5.01, -8.32, 0.025, -160.66), (-4.05, -11.36, 0.025, -170.22), (-3.49, -14.18, 0.025, -175.76), (-3.12, -17.15, 0.025, -177.73), (-3.0, -20.32, 0.025, 178.49), (-3.09, -23.44, 0.025, 176.59), (-3.43, -26.54, 0.025, 171.44), (-4.07, -29.44, 0.025, 163.75), (-5.09, -32.27, 0.025, 158.2), (-6.11, -35.16, 0.025, 154.98), (-7.57, -37.78, 0.025, 154.98), (-9.28, -40.65, 0.025, 150.41)), ((-6.12, 1.62, 0.025, -152.9), (-4.38, -1.35, 0.025, -150.92), (-3.08, -4.3, 0.025, -157.9), (-1.85, -7.26, 0.025, -162.54), (-0.93, -10.49, 0.025, -167.71), (-0.21, -13.71, 0.025, -171.79), (0.21, -17.08, 0.025, -174.92), (0.31, -20.2, 0.025, 177.1), (0.17, -23.66, 0.025, 174.82), (-0.23, -26.91, 0.025, 170.51), (-0.99, -30.2, 0.025, 162.54), (-2.02, -33.28, 0.025, 160.48), (-3.28, -36.38, 0.025, 157.96), (-4.67, -39.17, 0.025, 154.13), (-6.31, -42.15, 0.025, 154.13)), ((-2.99, 3.09, 0.025, -154.37), (-1.38, -0.05, 0.025, -154.75), (-0.19, -3.29, 0.025, -159.22), (1.17, -6.51, 0.025, -162.74), (2.28, -9.8, 0.025, -168.73), (3.09, -13.28, 0.025, -173.49), (3.46, -16.63, 0.025, -176.81), (3.69, -20.38, 0.025, 179.14), (3.61, -24.12, 0.025, 175.78), (3.0, -27.55, 0.025, 170.87), (2.15, -30.72, 0.025, 167.41), (1.04, -34.26, 0.025, 162.11), (-0.15, -37.44, 0.025, 158.59), (-1.64, -40.52, 0.025, 153.89), (-3.42, -43.63, 0.025, 153.89)), ((0.0, 4.35, 0.025, -154.37), (1.52, 1.3, 0.025, -155.67), (3.17, -2.07, 0.025, -155.67), (4.47, -5.41, 0.025, -163.0), (5.56, -9.19, 0.025, -168.89), (6.22, -12.66, 0.025, -171.67), (6.67, -16.56, 0.025, -176.53), (6.93, -20.33, 0.025, 179.87), (6.81, -24.32, 0.025, 175.19), (6.22, -27.97, 0.025, 170.81), (5.59, -31.73, 0.025, 167.54), (4.48, -35.42, 0.025, 161.92), (3.06, -38.82, 0.025, 158.56), (1.4, -42.0, 0.025, 154.32), (-0.71, -45.17, 0.025, 153.27)))
        self.avatarPositions = { }
        self.modelCount = 8
        self.cameraPosHprs = ((-31.3527, -18.1425, 34.0543, -88.218, 11.0438, -58.5021), (-22.78, -41.65, 31.53, -51.55, -42.68, -2.96), (-29.7037, 0.757536, 31.5399, -122.51, -56.5493, 11.4299))

    
    def getTitle(self):
        return 'Race Game'

    
    def getInstructions(self):
        return 'Click a number. Choose wisely! You only advance if no one else picked the same number.'

    
    def generate(self):
        DistributedMinigame.generate(self)

    
    def disable(self):
        DistributedMinigame.disable(self)
        self.raceBoard.reparentTo(hidden)

    
    def load(self):
        DistributedMinigame.load(self)
        self.raceBoard = loader.loadModel('phase_4/models/minigames/race')
        self.raceBoard.setPosHpr(0, 0, 0, 0, 0, 0)
        self.raceBoard.setScale(0.8)
        self.dice = loader.loadModelOnce('phase_4/models/minigames/dice')
        self.dice1 = self.dice.find('**/dice_button1')
        self.dice2 = self.dice.find('**/dice_button2')
        self.dice3 = self.dice.find('**/dice_button3')
        self.dice4 = self.dice.find('**/dice_button4')
        self.diceList = [
            self.dice1,
            self.dice2,
            self.dice3,
            self.dice4]
        self.music = base.loadMusic('phase_4/audio/bgm/minigame_race.mid')
        self.posBuzzer = base.loadSfx('phase_4/audio/sfx/MG_pos_buzzer.wav')
        self.negBuzzer = base.loadSfx('phase_4/audio/sfx/MG_neg_buzzer.wav')
        self.winSting = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')
        self.loseSting = base.loadSfx('phase_4/audio/sfx/MG_lose.mp3')
        self.dice = loader.loadModelOnce('phase_4/models/minigames/dice')
        self.diceButtonList = []
        for i in range(1, 5):
            model = self.dice.find('**/dice_button' + str(i))
            np = NodePath(NamedNode('diceButton' + str(i)))
            model.instanceTo(np)
            diceReadyLabel = GuiLabel.makeModelLabel(np.node(), 0.2, 0.2)
            model = self.dice.find('**/dice_button' + str(i) + '_down')
            np = NodePath(NamedNode('diceButton' + str(i) + '_down'))
            model.instanceTo(np)
            diceDownLabel = GuiLabel.makeModelLabel(np.node(), 0.2, 0.2)
            model = self.dice.find('**/dice_button' + str(i) + '_ro')
            np = NodePath(NamedNode('diceButton' + str(i) + '_ro'))
            model.instanceTo(np)
            diceRolloverLabel = GuiLabel.makeModelLabel(np.node(), 0.2, 0.2)
            diceInactiveLabel = GuiLabel.makeNullLabel()
            diceButton = GuiButton('diceButton' + str(i), diceReadyLabel, diceRolloverLabel, diceDownLabel, diceDownLabel, diceInactiveLabel)
            diceButton.setPos(Vec3(-0.9 + (i - 1) * 0.2, 0.0, -0.85))
            diceButton.setScale(0.25)
            diceButton.setBehaviorEvent('diceButton')
            diceButton.setBehaviorEventParameter(i)
            diceButton.setRolloverFunctor(getNewRolloverFunctor(None))
            diceButton.setBehaviorFunctor(getNewClickFunctor(None))
            self.diceButtonList.append(diceButton)
        
        self.waitingChoicesSign = Sign.Sign('waitingChoicesSign', 'Waiting for other players to choose...')
        self.waitingChoicesSign.setPos(-0.3, -0.9)
        self.waitingChoicesSign.label.setForegroundColor(1, 1, 1, 1)

    
    def unload(self):
        DistributedMinigame.unload(self)
        self.raceBoard.removeNode()
        del self.raceBoard
        self.dice.removeNode()
        del self.dice
        del self.waitingChoicesSign
        base.unloadMusic(self.music)
        del self.music
        base.unloadSfx(self.posBuzzer)
        base.unloadSfx(self.negBuzzer)
        base.unloadSfx(self.winSting)
        base.unloadSfx(self.loseSting)
        del self.posBuzzer
        del self.negBuzzer
        del self.winSting
        del self.loseSting
        del self.diceButtonList
        self.frameworkFSM.getStateNamed('game').removeChild(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        DistributedMinigame.onstage(self)
        base.playMusic(self.music, looping = 1, volume = 0.8)
        self.raceBoard.reparentTo(render)
        camera.reparentTo(render)
        camera.setPosHpr(-22.78, -41.65, 31.53, -51.55, -42.68, -2.96)
        base.transitions.irisIn(0.4)

    
    def offstage(self):
        DistributedMinigame.offstage(self)
        base.stopMusic(self.music)

    
    def setGameReady(self):
        DistributedMinigame.setGameReady(self)
        self.resetPositions()
        for i in range(len(self.avIdList)):
            avId = self.avIdList[i]
            avatar = self.getAvatar(avId)
            if avatar:
                avatar.reparentTo(render)
                avatar.loop('neutral')
                self.positionInPlace(avatar, i, 0)
            
        

    
    def setGameStart(self):
        DistributedMinigame.setGameStart(self)
        self.gameFSM.request('inputChoice')

    
    def enterOff(self):
        pass

    
    def exitOff(self):
        pass

    
    def enterInputChoice(self):
        self.accept('diceButton', self.handleInputChoice)
        for i in range(len(self.diceButtonList)):
            button = self.diceButtonList[i]
            button.manage(guiMgr, base.eventMgr.eventHandler, aspect2d.node())
            button.startBehavior()
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.setTime(self.InputTimeout)
        self.timer.countdown(self.InputTimeout, self.handleChoiceTimeout)

    
    def exitInputChoice(self):
        self.timer.destroy()
        del self.timer
        self.ignore('diceButton')
        for button in self.diceButtonList:
            button.stopBehavior()
            button.unmanage()
        

    
    def handleChoiceTimeout(self):
        self.sendUpdate('setAvatarChoice', [
            self.localAvId,
            0])
        self.gameFSM.request('waitServerChoices')

    
    def handleInputChoice(self, item, choice):
        if item in self.diceButtonList:
            self.sendUpdate('setAvatarChoice', [
                self.localAvId,
                choice])
            self.gameFSM.request('waitServerChoices')
        

    
    def enterWaitServerChoices(self):
        self.waitingChoicesSign.manage()

    
    def exitWaitServerChoices(self):
        self.waitingChoicesSign.unmanage()

    
    def localToonWon(self):
        localToonPosition = self.avatarPositions[self.localAvId]
        if localToonPosition >= self.NumberToWin:
            self.notify.debug('localToon won')
            return 1
        else:
            return 0

    
    def anyAvatarWon(self):
        for position in self.avatarPositions.values():
            if position >= self.NumberToWin:
                self.notify.debug('anyAvatarWon: Somebody won')
                return 1
            
        
        self.notify.debug('anyAvatarWon: Nobody won')
        return 0

    
    def showNumbers(self, task):
        self.diceInstanceList = []
        for i in range(len(self.choiceList)):
            avId = self.avIdList[i]
            choice = self.choiceList[i]
            if choice == 0:
                self.diceInstanceList.append(None)
            else:
                diceInstance = self.diceList[choice - 1].instanceTo(self.raceBoard)
                self.diceInstanceList.append(diceInstance)
                dicePosition = self.avatarPositions[avId] + 1
                diceInstance.setScale(4.0)
                self.positionInPlace(diceInstance, i, dicePosition)
                diceInstance.setP(-90)
        
        return Task.done

    
    def showMatches(self, task):
        for i in range(len(self.choiceList)):
            avId = self.avIdList[i]
            choice = self.choiceList[i]
            if choice != 0:
                diceInstance = self.diceInstanceList[i]
                freq = self.choiceList.count(choice)
                if freq == 1:
                    diceInstance.setColor(0.2, 1, 0.2, 1)
                    if avId == self.localAvId:
                        base.playSfx(self.posBuzzer)
                    
                else:
                    diceInstance.setColor(1, 0.2, 0.2, 1)
                    if avId == self.localAvId:
                        base.playSfx(self.negBuzzer)
                    
            
        
        return Task.done

    
    def hideNumbers(self, task):
        for dice in self.diceInstanceList:
            if dice:
                dice.removeNode()
            
        
        self.diceInstanceList = []
        return Task.done

    
    def enterMoveAvatars(self, choiceList, positionList):
        self.choiceList = choiceList
        self.positionList = positionList
        longestLerpTime = self.getLongestLerpTime()
        if longestLerpTime > 0.0:
            moveTask = Task.sequence(Task.Task(self.showNumbers), Task.pause(0.5), Task.Task(self.showMatches), Task.pause(0.75), Task.Task(self.moveAvatars), Task.pause(0.75), Task.Task(self.hideNumbers), Task.pause(longestLerpTime - 0.5), Task.Task(self.walkDone))
        else:
            moveTask = Task.sequence(Task.Task(self.showNumbers), Task.pause(0.5), Task.Task(self.showMatches), Task.pause(1.0), Task.Task(self.hideNumbers), Task.Task(self.walkDone))
        taskMgr.spawnTaskNamed(moveTask, 'moveAvatars')

    
    def walkDone(self, task):
        self.choiceList = []
        if self.anyAvatarWon():
            self.gameFSM.request('finish')
        else:
            self.gameFSM.request('inputChoice')
        return Task.done

    
    def getLongestLerpTime(self):
        longestTime = 0.0
        for choice in self.choiceList:
            freq = self.choiceList.count(choice)
            if freq == 1:
                longestTime = max(longestTime, choice / 1.2)
            
        
        return longestTime

    
    def moveAvatars(self, task):
        for i in range(len(self.choiceList)):
            avId = self.avIdList[i]
            choice = self.choiceList[i]
            position = self.positionList[i]
            self.avatarPositions[avId] = position
            if choice != 0 and self.choiceList.count(choice) == 1:
                avatar = self.getAvatar(avId)
                if avatar:
                    walkDuration = choice / 1.2
                    self.lerpInPlace(avatar, i, position, walkDuration)
                
            
        
        return Task.done

    
    def exitMoveAvatars(self):
        taskMgr.removeTasksNamed('moveAvatars')
        for lane in range(len(self.avIdList)):
            taskMgr.removeTasksNamed('startWalk-' + str(lane))
            taskMgr.removeTasksNamed('startNeutral-' + str(lane))
            taskMgr.removeTasksNamed('walkAvatar-' + str(lane))
        
        return None

    
    def gameOverCallback(self, task):
        self.gameOver()
        return Task.done

    
    def enterFinish(self):
        if self.localToonWon():
            base.playSfx(self.winSting)
        else:
            base.playSfx(self.loseSting)
        taskMgr.doMethodLater(4.0, self.gameOverCallback, 'playMovie')

    
    def exitFinish(self):
        taskMgr.removeTasksNamed('playMovie')
        taskMgr.removeTasksNamed('doLater-playMovie')
        base.stopSfx(self.winSting)
        base.stopSfx(self.loseSting)

    
    def positionInPlace(self, avatar, lane, place):
        place = min(place, len(self.posHprArray[lane]) - 1)
        posH = self.posHprArray[lane][place]
        avatar.setPosHpr(self.raceBoard, posH[0], posH[1], posH[2], posH[3], 0, 0)

    
    def lerpInPlace(self, avatar, lane, place, time):
        place = min(place, len(self.posHprArray[lane]) - 1)
        posH = self.posHprArray[lane][place]
        
        def startWalk(task):
            task.avatar.setPlayRate(1.0, 'walk')
            task.avatar.loop('walk')
            return Task.done

        startWalkTask = Task.Task(startWalk, 'startWalk-' + str(lane))
        startWalkTask.avatar = avatar
        
        def uponDeath(task):
            task.avatar.loop('neutral')
            task.avatar.setPosHpr(task.raceBoard, task.posH[0], task.posH[1], task.posH[2], task.posH[3], 0, 0)
            return Task.done

        walkTask = Task.sequence(startWalkTask, avatar.lerpPosHpr(posH[0], posH[1], posH[2], posH[3], 0, 0, time, other = self.raceBoard))
        walkTask.avatar = avatar
        walkTask.posH = posH
        walkTask.raceBoard = self.raceBoard
        walkTask.uponDeath = uponDeath
        taskMgr.spawnTaskNamed(walkTask, 'walkAvatar-' + str(lane))

    
    def setAvatarChoice(self, avId, choice):
        self.notify.error('setAvatarChoice should not be called on the client')

    
    def setAvatarChose(self, avId):
        self.notify.debug('setAvatarChose: avatar: ' + str(avId) + ' choose a number')

    
    def setServerChoices(self, choices, positions):
        self.notify.debug('setServerChoices: %s positions: %s' % (choices, positions))
        self.gameFSM.request('moveAvatars', [
            choices,
            positions])

    
    def resetPositions(self):
        for avId in self.avIdList:
            self.avatarPositions[avId] = 0
        


