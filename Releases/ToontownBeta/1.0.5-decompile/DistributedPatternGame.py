# Source Generated with Decompyle++
# File: DistributedPatternGame.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from IntervalGlobal import *
from DistributedMinigame import *
import FSM
import State
import Button
from GuiGlobals import *
import Sign
import ToontownTimer
from DirectGui import *
import PatternPad
import PatternGameGlobals
import OnscreenText
import ToonHead
import AvatarDNA
import Char
import OnscreenText
import ArrowKeys

class DistributedPatternGame(DistributedMinigame):
    textColor = (0.9, 0.9, 0.9, 1.0)
    bgColor = Vec4(0.01, 0.2, 0.01, 1.0)
    phase3snd = 'phase_3/audio/sfx/'
    phase4snd = 'phase_4/audio/sfx/'
    TEXT_POS_ABOVE = (0, 0.45)
    TEXT_POS_ON = (0, 0)
    TEXT_SCALE_BIG = 0.2
    TEXT_SCALE_NORMAL = 0.15
    TEXT_SCALE_SMALL = 0.12
    ButtonSoundNames = (phase4snd + 'MG_cannon_hit_tower.mp3', phase3snd + 'GUI_create_toon_back.mp3', phase3snd + 'GUI_create_toon_bodyshop.mp3', phase4snd + 'SZ_trolley_bell.mp3')
    strWatch = 'Watch the pattern...'
    strTryAgain = 'Try again...'
    strGo = 'Go!'
    strRight = 'Good!'
    strWrong = 'Oops!'
    strTimeUp = 'You ran out of time!'
    strWin = 'You won!'
    strPerfect = 'That was perfect!'
    strBye = 'Thanks for playing!'
    strWaitingOtherPlayers = 'Waiting for other players...'
    strPleaseWait = 'Please wait...'
    
    def __init__(self, cr):
        DistributedMinigame.__init__(self, cr)
        self.gameFSM = FSM.FSM('DistributedPatternGame', [
            State.State('off', self.enterOff, self.exitOff, [
                'readyForNextRound']),
            State.State('readyForNextRound', self.enterReadyForNextRound, self.exitReadyForNextRound, [
                'waitForServerPattern']),
            State.State('waitForServerPattern', self.enterWaitForServerPattern, self.exitWaitForServerPattern, [
                'showServerPattern']),
            State.State('showServerPattern', self.enterShowServerPattern, self.exitShowServerPattern, [
                'getUserInput']),
            State.State('getUserInput', self.enterGetUserInput, self.exitGetUserInput, [
                'waitForGameOverFlag',
                'finish']),
            State.State('waitForGameOverFlag', self.enterWaitForGameOverFlag, self.exitWaitForGameOverFlag, [
                'readyForNextRound',
                'finish']),
            State.State('finish', self.enterFinish, self.exitFinish, [
                'off'])], 'off', 'off')
        self.frameworkFSM.getStateNamed('game').addChild(self.gameFSM)
        self.oldBgColor = None

    
    def getTitle(self):
        return 'Match Minnie'

    
    def getInstructions(self):
        return 'Minnie will show you a pattern. Try to repeat ' + "Minnie's pattern just the way you see it!"

    
    def generate(self):
        DistributedMinigame.generate(self)

    
    def disable(self):
        DistributedMinigame.disable(self)

    
    def load(self):
        DistributedMinigame.load(self)
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.posInTopRightCorner()
        self.timer.hide()
        self.localPatternPad = PatternPad.PatternPad()
        self.localPatternPad.setPressCallback(self._DistributedPatternGame__pressHandler)
        self.localPatternPad.setReleaseCallback(self._DistributedPatternGame__releaseHandler)
        self.localPatternPad.hide()
        self.buttonSounds = []
        for i in range(0, 4):
            self.buttonSounds.append(base.loadSfx(self.ButtonSoundNames[i]))
        
        self.correctSound = base.loadSfx('phase_4/audio/sfx/MG_pos_buzzer.wav')
        self.winSound = base.loadSfx('phase_4/audio/sfx/MG_win.mp3')
        self.loseSound = base.loadSfx('phase_4/audio/sfx/MG_lose.mp3')
        self.titleText = DirectLabel(text = self.getTitle(), text_fg = (0.9, 0.9, 0.9, 1.0), frameColor = (1, 1, 1, 0), text_font = getSignFont(), pos = (0, 0, 0.8), scale = 0.14)
        self.waitingText = DirectLabel(text = self.strPleaseWait, text_fg = (0.9, 0.9, 0.9, 1.0), frameColor = (1, 1, 1, 0), text_font = getSignFont(), pos = (0, 0, -0.483333), scale = 0.107502)
        self.roundText = DirectLabel(parent = self.localPatternPad, text = '1', text_fg = (0.9, 0.9, 0.9, 1.0), frameColor = (1, 1, 1, 0), text_font = getSignFont(), pos = (0, 0, -0.05), scale = 0.15)
        self.titleText.hide()
        self.waitingText.hide()
        self.roundText.hide()
        self.checkMark = DirectLabel(text = 'OK', text_fg = (0, 1, 0, 1), frameColor = (1, 1, 1, 0), text_font = getSignFont(), pos = (0, 0, -0.15), scale = 0.45)
        self.xMark = DirectLabel(text = 'X', text_fg = (1, 0, 0, 1), frameColor = (1, 1, 1, 0), text_font = getSignFont(), pos = (0, 0, -0.3), scale = 0.8)
        self.checkMark.show()
        self.xMark.show()
        self.checkMark.reparentTo(hidden)
        self.xMark.reparentTo(hidden)
        self.minnie = Char.Char()
        m = self.minnie
        dna = AvatarDNA.AvatarDNA()
        dna.newChar('mn')
        m.setDNA(dna)
        m.setName('Minnie')
        m.reparentTo(hidden)

    
    def unload(self):
        DistributedMinigame.unload(self)
        self.timer.destroy()
        del self.timer
        for i in range(0, 4):
            base.unloadSfx(self.buttonSounds[i])
        
        del self.buttonSounds
        base.unloadSfx(self.correctSound)
        base.unloadSfx(self.winSound)
        base.unloadSfx(self.loseSound)
        del self.correctSound
        del self.winSound
        del self.loseSound
        self.titleText.destroy()
        self.waitingText.destroy()
        self.roundText.destroy()
        del self.titleText
        del self.waitingText
        del self.roundText
        self.checkMark.destroy()
        self.xMark.destroy()
        del self.checkMark
        del self.xMark
        self.localPatternPad.destroy()
        del self.localPatternPad
        del self.minnie
        self.frameworkFSM.getStateNamed('game').removeChild(self.gameFSM)
        del self.gameFSM

    
    def onstage(self):
        DistributedMinigame.onstage(self)
        self.arrowKeys = ArrowKeys.ArrowKeys()
        self.oldBgColor = base.win.getGsg().getColorClearValue()
        base.win.getGsg().setColorClearValue(self.bgColor)
        self.titleText.show()
        pad = self.localPatternPad
        pad.show()
        pad.disable()
        pad.setScale(1.3)
        pad.setPos(0, 0, 0.15)
        self.remotePatternPads = { }
        for i in range(0, len(self.remoteAvIdList)):
            avId = self.remoteAvIdList[i]
            pad = PatternPad.PatternPad()
            pad.show()
            pad.disable()
            pad.setScale(0.4)
            padSpacing = 0.65
            pad.setPos(0.12 + i * padSpacing - (len(self.remoteAvIdList) - 1) * padSpacing / 2.0, 0, -0.7)
            self.remotePatternPads[avId] = pad
        
        self.checkMarks = []
        self.xMarks = []
        self.toonHeadDict = { }
        if self.isSinglePlayer():
            WD = 1.0
            HT = 0.32
            self.chancesLeftFrame = DirectFrame(parent = guiTop, frameColor = (0.1, 0.1, 0.1, 1), frameSize = (-WD / 2.0, WD / 2.0, -HT / 2.0, HT / 2.0), pos = (0, 0, -0.8))
            self.chancesLeftFrame.show()
            self.chancesLeftSlots = []
            self.chancesLeftToonHeads = []
            self.chancesLeftXMarks = []
            xMark = OnscreenText.OnscreenText(parent = hidden, text = 'X', font = getSignFont(), fg = (1, 0, 0, 1), scale = 0.3)
            for i in range(0, PatternGameGlobals.SP_NUM_CHANCES):
                head = ToonHead.ToonHead()
                head.setupHead(self.getAvatar(self.localAvId).style, forGui = 1)
                head.setPos(0, 10, 0)
                head.setScale(0.14)
                head.setHpr(180, 0, 0)
                head.getGeomNode().setHpr(0, 0, 0)
                head.startBlink()
                self.chancesLeftToonHeads.append(head)
                slotSpacing = 0.3
                WD = 0.25
                HT = 0.28
                dummyNode = hidden.attachNewNode('patternGameNullGeomNode')
                slot = DirectLabel(parent = self.chancesLeftFrame, pos = (slotSpacing * (float(i) - float(PatternGameGlobals.SP_NUM_CHANCES - 1) / 2.0), 0, 0), frameColor = (1, 1, 1, 0), frameSize = (-WD / 2.0, WD / 2.0, -HT / 2.0, HT / 2.0), geom = (dummyNode, xMark), numStates = 2)
                head.reparentTo(slot.stateNodePath[0])
                dummyNode.removeNode()
                del dummyNode
                slot['geom1_pos'] = (0, 0, -0.1)
                self.chancesLeftSlots.append(slot)
            
        
        self.lt = Toon.Toon()
        lt = self.lt
        d = toonbase.localToon.getStyle()
        lt.setDNA(d)
        lt.setName(toonbase.localToon.getName())
        lt.reparentTo(camera)
        lt.setPos(-4.8, 12.96, -1.64)
        lt.lookAt(camera)
        lt.setP(0)
        lt.setR(0)
        lt.loop('neutral')
        lt.startBlink()
        lt.startLookAround()
        tag = NametagFloat3d()
        tag.setBillboardOffset(0)
        tag.setAvatarNode(lt.node())
        toonbase.localToon.nametag.addNametag(tag)
        tagPath = lt.attachNewNode(tag.upcastToNamedNode())
        tagPath.setPos(0, 0, lt.getHeight() + 1.0)
        lt.tag = tag
        m = self.minnie
        m.reparentTo(camera)
        m.setPos(4.7, 12.96, -1.64)
        m.lookAt(camera)
        m.setP(0)
        m.setR(0)
        m.loop('neutral')
        m.startBlink()
        self.minnie.nametag.manage(toonbase.marginManager)
        self.minnie.setPickable(0)
        self.minnie.nametag.getNametag3d().setChatWordwrap(5)
        camera.reparentTo(render)

    
    def offstage(self):
        DistributedMinigame.offstage(self)
        self.arrowKeys.destroy()
        del self.arrowKeys
        self.localPatternPad.disable()
        self.localPatternPad.hide()
        self.titleText.hide()
        self._DistributedPatternGame__delMarks(self.checkMarks)
        self._DistributedPatternGame__delMarks(self.xMarks)
        del self.checkMarks
        del self.xMarks
        for avId in self.remotePatternPads.keys():
            self.remotePatternPads[avId].destroy()
            del self.remotePatternPads[avId]
        
        del self.remotePatternPads
        for avId in self.toonHeadDict.keys():
            head = self.toonHeadDict[avId]
            head.stopBlink()
            head.stopLookAroundNow()
            av = self.getAvatar(avId)
            if av:
                av.nametag.removeNametag(head.tag)
            
            head.delete()
        
        del self.toonHeadDict
        if self.isSinglePlayer():
            del self.chancesLeftXMarks
            for head in self.chancesLeftToonHeads:
                head.stopBlink()
                head.delete()
            
            del self.chancesLeftToonHeads
            for slot in self.chancesLeftSlots:
                slot.destroy()
            
            del self.chancesLeftSlots
            self.chancesLeftFrame.destroy()
            del self.chancesLeftFrame
        
        self.minnie.nametag.unmanage(toonbase.marginManager)
        self.minnie.stop()
        self.minnie.stopBlink()
        self.minnie.reparentTo(hidden)
        toonbase.localToon.nametag.removeNametag(self.lt.tag)
        self.lt.stop()
        self.lt.stopBlink()
        self.lt.stopLookAroundNow()
        self.lt.delete()
        del self.lt
        if self.oldBgColor:
            base.win.getGsg().setColorClearValue(self.oldBgColor)
        

    
    def __addCheckMark(self, patternPad):
        mark = self.checkMark.instanceTo(patternPad)
        self.checkMarks.append(mark)

    
    def __addXMark(self, patternPad):
        mark = self.xMark.instanceTo(patternPad)
        self.xMarks.append(mark)

    
    def __delMarks(self, list):
        for mark in list:
            mark.removeNode()
            del mark
        
        list = []

    
    def __updateChancesLeftDisplay(self):
        if not self.isSinglePlayer():
            return None
        
        for i in range(0, PatternGameGlobals.SP_NUM_CHANCES):
            if i < self._DistributedPatternGame__chances:
                state = 0
            else:
                state = 1
            self.chancesLeftSlots[i]['activeState'] = state
        

    
    def setGameReady(self):
        DistributedMinigame.setGameReady(self)
        for i in range(0, len(self.remoteAvIdList)):
            avId = self.remoteAvIdList[i]
            self._DistributedPatternGame__createToonHead(avId, self.remotePatternPads[avId])
        
        if self.isSinglePlayer():
            self.waitingText['text'] = self.strPleaseWait
        else:
            self.waitingText['text'] = self.strWaitingOtherPlayers

    
    def setGameStart(self):
        DistributedMinigame.setGameStart(self)
        self._DistributedPatternGame__initGameVars()
        self.gameFSM.request('readyForNextRound')

    
    def __initGameVars(self):
        self._DistributedPatternGame__round = 0
        self._DistributedPatternGame__madeAMistake = 0
        if self.isSinglePlayer():
            self._DistributedPatternGame__chances = PatternGameGlobals.SP_NUM_CHANCES
            self._DistributedPatternGame__updateChancesLeftDisplay()
        
        self._DistributedPatternGame__sitOut = 0

    
    def __createToonHead(self, avId, patternPad):
        head = ToonHead.ToonHead()
        head.setupHead(self.getAvatar(avId).style, forGui = 1)
        head.reparentTo(patternPad)
        head.setPos(-0.7, 10, -0.25)
        head.getGeomNode().setHpr(180, 0, 0)
        head.setScale(0.25)
        head.startBlink()
        head.startLookAround()
        self.toonHeadDict[avId] = head
        toon = self.getAvatar(avId)
        tag = NametagFloat2d()
        toon.nametag.addNametag(tag)
        tagPath = head.attachNewNode(tag.upcastToNamedNode())
        tagPath.setPos(0, 0, 1)
        tagPath.setScale(0.5)
        head.tag = tag

    
    def __setMinnieChat(self, string, giggle):
        self.minnie.setChat(string, CFSpeech)
        if giggle:
            self.minnie.playDialogue('statementA', 1)
        

    
    def __clearMinnieChat(self):
        self.minnie.clearChat()

    
    def enterOff(self):
        self.notify.debug('enterOff')

    
    def exitOff(self):
        pass

    
    def enterReadyForNextRound(self):
        self.notify.debug('enterReadyForNextRound')
        self._DistributedPatternGame__delMarks(self.checkMarks)
        self.sendUpdate('clientReadyForNextRound', [
            self.localAvId])
        self.gameFSM.request('waitForServerPattern')

    
    def exitReadyForNextRound(self):
        pass

    
    def enterWaitForServerPattern(self):
        self.notify.debug('enterWaitForServerPattern')
        if self.isSinglePlayer():
            pass
        if not (self._DistributedPatternGame__madeAMistake):
            self._DistributedPatternGame__round += 1
        
        self.roundText.show()
        self.roundText['text'] = str(self._DistributedPatternGame__round)

    
    def setPattern(self, pattern):
        self.notify.debug('setPattern: ' + str(pattern))
        self._DistributedPatternGame__serverPattern = pattern
        self.gameFSM.request('showServerPattern')

    
    def exitWaitForServerPattern(self):
        pass

    
    def enterShowServerPattern(self):
        self.notify.debug('enterShowServerPattern')
        text = self.strWatch
        if self.isSinglePlayer() and self._DistributedPatternGame__madeAMistake:
            text = self.strTryAgain
        
        showIntervals = [
            FunctionInterval(self._DistributedPatternGame__setMinnieChat, extraArgs = [
                text,
                1]),
            WaitInterval(0.5)]
        for buttonIndex in self._DistributedPatternGame__serverPattern:
            showIntervals.append(self._DistributedPatternGame__createShowButtonPressInterval(buttonIndex))
        
        showIntervals.append(Track([
            WaitInterval(0.2),
            FunctionInterval(self._DistributedPatternGame__clearMinnieChat),
            WaitInterval(0.2),
            FunctionInterval(self._DistributedPatternGame__doneShowingPattern),
            WaitInterval(0.001)]))
        self.showTrack = Track(showIntervals)
        self.showTrack.play()

    
    def __createShowButtonPressInterval(self, index):
        longest = 0.65
        shortest = 0.3
        r = float(min(self._DistributedPatternGame__round, 10) - 1) / 9.0
        buttonPeriod = shortest * r + longest * (1.0 - r)
        buttonLitPercent = 0.85
        return MultiTrack([
            Track([
                FunctionInterval(self.localPatternPad.simButtonPress, extraArgs = [
                    index]),
                FunctionInterval(base.playSfx, extraArgs = [
                    self._DistributedPatternGame__getButtonSound(index)]),
                WaitInterval(buttonPeriod * buttonLitPercent),
                FunctionInterval(self.localPatternPad.simButtonRelease, extraArgs = [
                    index]),
                WaitInterval(buttonPeriod * (1 - buttonLitPercent))])])

    
    def __doneShowingPattern(self):
        self.gameFSM.request('getUserInput')

    
    def exitShowServerPattern(self):
        self.showTrack.stop()
        del self.showTrack

    
    def enterGetUserInput(self):
        self.notify.debug('enterGetUserInput')
        self.setupTrack = None
        self.resultTrack = None
        if self._DistributedPatternGame__sitOut:
            self.gameFSM.request('waitForGameOverFlag', enterArgList = [
                0])
        else:
            
            def startTimer(self = self):
                time = 10
                self.timer.show()
                self.timer.setTime(time)
                self.timer.countdown(time, self._DistributedPatternGame__handleInputTimeout)

            
            def enableKeys(self = self):
                
                def keyPress(self, index):
                    self.localPatternPad.simButtonPress(index)
                    self._DistributedPatternGame__pressHandler(index)

                
                def keyRelease(self, index):
                    self.localPatternPad.simButtonRelease(index)
                    self._DistributedPatternGame__releaseHandler(index)

                self.arrowKeys.setPressHandlers([
                    (lambda self = self, keyPress = keyPress: keyPress(self, 0)),
                    (lambda self = self, keyPress = keyPress: keyPress(self, 2)),
                    (lambda self = self, keyPress = keyPress: keyPress(self, 3)),
                    (lambda self = self, keyPress = keyPress: keyPress(self, 1))])
                self.arrowKeys.setReleaseHandlers([
                    (lambda self = self, keyRelease = keyRelease: keyRelease(self, 0)),
                    (lambda self = self, keyRelease = keyRelease: keyRelease(self, 2)),
                    (lambda self = self, keyRelease = keyRelease: keyRelease(self, 3)),
                    (lambda self = self, keyRelease = keyRelease: keyRelease(self, 1))])

            self._DistributedPatternGame__localPattern = []
            self.setupTrack = Track([
                FunctionInterval(self._DistributedPatternGame__setMinnieChat, extraArgs = [
                    self.strGo,
                    0]),
                FunctionInterval(self.localPatternPad.enable),
                FunctionInterval(enableKeys),
                FunctionInterval(startTimer),
                WaitInterval(0.8),
                FunctionInterval(self._DistributedPatternGame__clearMinnieChat)])
            self.setupTrack.play()

    
    def __handleInputTimeout(self):
        self._DistributedPatternGame__doneGettingInput(0, 1)

    
    def __pressHandler(self, index):
        self._DistributedPatternGame__buttonPressed(index)
        self.sendUpdate('announceButtonPressed', [
            self.localAvId,
            index])

    
    def __releaseHandler(self, index):
        self.sendUpdate('announceButtonReleased', [
            self.localAvId,
            index])

    
    def announceButtonPressed(self, avId, button):
        if avId != self.localAvId:
            self.remotePatternPads[avId].simButtonPress(button)
        

    
    def announceButtonReleased(self, avId, button):
        if avId != self.localAvId:
            self.remotePatternPads[avId].simButtonRelease(button)
        

    
    def __getButtonSound(self, index):
        return self.buttonSounds[index]

    
    def __doneGettingInput(self, success, timeup = 0):
        self.localPatternPad.disable()
        self.arrowKeys.setPressHandlers(self.arrowKeys.NULL_HANDLERS)
        self.timer.stop()
        self._DistributedPatternGame__madeAMistake = 0
        if not success:
            if self.isSinglePlayer():
                self._DistributedPatternGame__madeAMistake = 1
                self._DistributedPatternGame__chances -= 1
            else:
                self._DistributedPatternGame__sitOut = 1
        
        
        def proceed(self = self, success = success):
            self.sendUpdate('reportPlayerResult', [
                self.localAvId,
                success])
            self.timer.hide()
            self.gameFSM.request('waitForGameOverFlag', enterArgList = [
                success])

        if success:
            sound = self.correctSound
        else:
            sound = self.loseSound
        soundTrack = Track([
            FunctionInterval(base.playSfx, extraArgs = [
                sound]),
            WaitInterval(1.6)])
        delay = 1.5
        
        markFunc = lambda x: x
        if success:
            text = self.strRight
        elif timeup:
            text = self.strTimeUp
            delay = 2.0
        else:
            text = self.strWrong
        if not self.isSinglePlayer():
            markFunc = self._DistributedPatternGame__addXMark
        
        textTrack = Track([
            WaitInterval(0.2),
            FunctionInterval(self._DistributedPatternGame__setMinnieChat, extraArgs = [
                text,
                0]),
            WaitInterval(delay - 0.2),
            FunctionInterval(self._DistributedPatternGame__clearMinnieChat),
            FunctionInterval(self._DistributedPatternGame__updateChancesLeftDisplay),
            FunctionInterval(markFunc, extraArgs = [
                self.localPatternPad])])
        self.resultTrack = Track([
            MultiTrack([
                soundTrack,
                textTrack]),
            FunctionInterval(proceed)])
        self.resultTrack.play()

    
    def __validPattern(self, fullPattern, partialPattern):
        for i in range(0, len(partialPattern)):
            if partialPattern[i] != fullPattern[i]:
                return 0
            
        
        return 1

    
    def __buttonPressed(self, index):
        base.playSfx(self._DistributedPatternGame__getButtonSound(index))
        self._DistributedPatternGame__localPattern.append(index)
        if 0 == self._DistributedPatternGame__validPattern(self._DistributedPatternGame__serverPattern, self._DistributedPatternGame__localPattern):
            self._DistributedPatternGame__doneGettingInput(0)
        elif len(self._DistributedPatternGame__localPattern) == len(self._DistributedPatternGame__serverPattern):
            self._DistributedPatternGame__doneGettingInput(1)
        

    
    def exitGetUserInput(self):
        self.arrowKeys.setPressHandlers(self.arrowKeys.NULL_HANDLERS)
        self.arrowKeys.setReleaseHandlers(self.arrowKeys.NULL_HANDLERS)
        if self.setupTrack:
            self.setupTrack.stop()
        
        if self.resultTrack:
            self.resultTrack.stop()
        
        del self.setupTrack
        del self.resultTrack
        self._DistributedPatternGame__clearMinnieChat()

    
    def setPlayerResult(self, avId, success):
        self.notify.debug('setPlayerResult: ' + str(avId) + ' ' + str(success))
        if avId != self.localAvId:
            pp = self.remotePatternPads[avId]
            if success:
                self._DistributedPatternGame__addCheckMark(pp)
            else:
                self._DistributedPatternGame__addXMark(pp)
        

    
    def enterWaitForGameOverFlag(self, success):
        self.notify.debug('enterWaitForGameOverFlag')
        self._DistributedPatternGame__success = success
        self._DistributedPatternGame__winTrack = None
        self.waitingText.show()

    
    def setGameOver(self, flag):
        self.waitingText.hide()
        if flag:
            
            def proceed(self = self):
                self.gameFSM.request('finish')

            intervals = []
            if self._DistributedPatternGame__success:
                if self.isSinglePlayer() and self._DistributedPatternGame__chances == PatternGameGlobals.SP_NUM_CHANCES:
                    text = self.strPerfect
                else:
                    text = self.strWin
                sound = self.winSound
            else:
                text = self.strBye
                sound = None
            intervals.extend([
                FunctionInterval(self._DistributedPatternGame__setMinnieChat, extraArgs = [
                    text,
                    1]),
                FunctionInterval(base.playSfx, extraArgs = [
                    sound]),
                WaitInterval(2),
                FunctionInterval(self._DistributedPatternGame__clearMinnieChat)])
            intervals.append(FunctionInterval(proceed))
            self._DistributedPatternGame__winTrack = Track(intervals)
            self._DistributedPatternGame__winTrack.play()
        else:
            self.gameFSM.request('readyForNextRound')

    
    def exitWaitForGameOverFlag(self):
        if self._DistributedPatternGame__winTrack:
            self._DistributedPatternGame__winTrack.stop()
        
        del self._DistributedPatternGame__winTrack

    
    def enterFinish(self):
        self.notify.debug('enterFinish')
        self.gameOver()
        self.gameFSM.request('off')

    
    def exitFinish(self):
        pass


