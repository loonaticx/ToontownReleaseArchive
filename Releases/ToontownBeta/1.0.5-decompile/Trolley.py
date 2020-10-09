# Source Generated with Decompyle++
# File: Trolley.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from IntervalGlobal import *
import PandaObject
import FSM
import State
import StateData
import DialogBox

class Trolley(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, safeZone, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Trolley', [
            State.State('start', self.enterStart, self.exitStart, [
                'requestBoard',
                'trolleyFA']),
            State.State('trolleyFA', self.enterTrolleyFA, self.exitTrolleyFA, [
                'final']),
            State.State('requestBoard', self.enterRequestBoard, self.exitRequestBoard, [
                'boarding']),
            State.State('boarding', self.enterBoarding, self.exitBoarding, [
                'boarded']),
            State.State('boarded', self.enterBoarded, self.exitBoarded, [
                'requestExit',
                'trolleyLeaving',
                'final']),
            State.State('requestExit', self.enterRequestExit, self.exitRequestExit, [
                'exiting',
                'trolleyLeaving']),
            State.State('trolleyLeaving', self.enterTrolleyLeaving, self.exitTrolleyLeaving, [
                'final']),
            State.State('exiting', self.enterExiting, self.exitExiting, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        return None

    
    def load(self):
        self.parentFSM.getStateNamed('trolley').addChild(self.fsm)
        self.buttonModels = loader.loadModel('phase_4/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**//InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')
        return None

    
    def unload(self):
        self.parentFSM.getStateNamed('trolley').removeChild(self.fsm)
        del self.fsm
        del self.parentFSM
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton
        return None

    
    def enter(self):
        self.fsm.enterInitialState()
        if toonbase.localToon.hp > 0:
            self.fsm.request('requestBoard')
        else:
            self.fsm.request('trolleyFA')
        return None

    
    def exit(self):
        self.ignoreAll()
        return None

    
    def enterStart(self):
        return None

    
    def exitStart(self):
        return None

    
    def enterTrolleyFA(self):
        self.noTrolleyBox = DialogBox.DialogBox(message = 'You may not board the trolley until your laffmeter is smiling.', doneEvent = 'noTrolleyAck', style = DialogBox.Acknowledge)
        self.noTrolleyBox.show()
        toonbase.localToon.b_setAnimState('neutral', 1)
        self.accept('noTrolleyAck', self._Trolley__handleNoTrolleyAck)
        return None

    
    def __handleNoTrolleyAck(self):
        ntbDoneStatus = self.noTrolleyBox.doneStatus
        if ntbDoneStatus == 'ok':
            doneStatus = { }
            doneStatus['mode'] = 'reject'
            messenger.send(self.doneEvent, [
                doneStatus])
        else:
            self.notify.error('Unrecognized doneStatus: ' + str(ntbDoneStatus))
        return None

    
    def exitTrolleyFA(self):
        self.ignore('noTrolleyAck')
        self.noTrolleyBox.cleanup()
        del self.noTrolleyBox
        return None

    
    def enterRequestBoard(self):
        return None

    
    def handleRejectBoard(self):
        doneStatus = { }
        doneStatus['mode'] = 'reject'
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def exitRequestBoard(self):
        return None

    
    def enterBoarding(self, nodePath):
        camera.wrtReparentTo(nodePath)
        self.cameraBoardTrack = Track([
            LerpPosHprInterval(camera, 1.5, Point3(-35, 0, 8), Point3(-90, 0, 0))])
        self.cameraBoardTrack.play()
        return None

    
    def exitBoarding(self):
        self.ignore('boardedTrolley')
        return None

    
    def enterBoarded(self):
        self.enableExitButton()
        return None

    
    def exitBoarded(self):
        self.cameraBoardTrack.stop()
        self.disableExitButton()
        return None

    
    def enableExitButton(self):
        self.exitButton = DirectButton(relief = None, text = 'Hop off', text_fg = (1, 1, 0.65, 1), text_pos = (0, -0.23), text_scale = 0.8, image = (self.upButton, self.downButton, self.rolloverButton), image_color = (1, 0, 0, 1), image_scale = (20, 1, 11), pos = (0, 0, 0.8), scale = 0.15, command = (lambda self = self: self.fsm.request('requestExit')))
        return None

    
    def disableExitButton(self):
        self.exitButton.destroy()
        return None

    
    def enterRequestExit(self):
        messenger.send('trolleyExitButton')
        return None

    
    def exitRequestExit(self):
        return None

    
    def enterTrolleyLeaving(self):
        messenger.send('trolleyLeaving')
        camera.lerpPosHprXYZHPR(0, 18.55, 3.75, -180, 0, 0, 3, blendType = 'easeInOut', task = 'leavingCamera')
        self.acceptOnce('playMinigame', self.handlePlayMinigame)
        return None

    
    def handlePlayMinigame(self, zoneId, minigameId):
        doneStatus = { }
        doneStatus['mode'] = 'minigame'
        doneStatus['zoneId'] = zoneId
        doneStatus['minigameId'] = minigameId
        messenger.send(self.doneEvent, [
            doneStatus])

    
    def exitTrolleyLeaving(self):
        self.ignore('playMinigame')
        taskMgr.removeTasksNamed('leavingCamera')
        return None

    
    def enterExiting(self):
        return None

    
    def handleOffTrolley(self):
        doneStatus = { }
        doneStatus['mode'] = 'exit'
        messenger.send(self.doneEvent, [
            doneStatus])
        return None

    
    def exitExiting(self):
        return None

    
    def enterFinal(self):
        return None

    
    def exitFinal(self):
        return None


