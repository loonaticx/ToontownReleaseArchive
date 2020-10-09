# Source Generated with Decompyle++
# File: Elevator.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
from DirectGui import *
from IntervalGlobal import *
import PandaObject
import FSM
import State
import StateData
import DialogBox

class Elevator(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.fsm = FSM.FSM('Elevator', [
            State.State('start', self.enterStart, self.exitStart, [
                'requestBoard']),
            State.State('requestBoard', self.enterRequestBoard, self.exitRequestBoard, [
                'boarding']),
            State.State('boarding', self.enterBoarding, self.exitBoarding, [
                'boarded']),
            State.State('boarded', self.enterBoarded, self.exitBoarded, [
                'requestExit',
                'elevatorClosing',
                'final']),
            State.State('requestExit', self.enterRequestExit, self.exitRequestExit, [
                'exiting',
                'elevatorClosing']),
            State.State('elevatorClosing', self.enterElevatorClosing, self.exitElevatorClosing, [
                'final']),
            State.State('exiting', self.enterExiting, self.exitExiting, [
                'final']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')
        self.parentFSM = parentFSM
        return None

    
    def load(self):
        self.parentFSM.getStateNamed('elevator').addChild(self.fsm)
        self.buttonModels = loader.loadModel('phase_4/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**//InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')
        return None

    
    def unload(self):
        self.parentFSM.getStateNamed('elevator').removeChild(self.fsm)
        del self.fsm
        del self.parentFSM
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton
        return None

    
    def enter(self):
        self.fsm.enterInitialState()
        self.fsm.request('requestBoard')
        return None

    
    def exit(self):
        self.ignoreAll()
        return None

    
    def enterStart(self):
        return None

    
    def exitStart(self):
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
            LerpPosHprInterval(camera, 1.5, Point3(0, -16, 5.5), Point3(0, 0, 0))])
        self.cameraBoardTrack.play()
        return None

    
    def exitBoarding(self):
        self.ignore('boardedElevator')
        return None

    
    def enterBoarded(self):
        self.enableExitButton()
        return None

    
    def exitBoarded(self):
        self.cameraBoardTrack.stop()
        self.disableExitButton()
        return None

    
    def enableExitButton(self):
        self.exitButton = DirectButton(relief = None, text = 'Hop off', text_fg = (0.9, 0.9, 0.9, 1), text_pos = (0, -0.23), text_scale = 0.8, image = (self.upButton, self.downButton, self.rolloverButton), image_color = (0.5, 0.5, 0.5, 1), image_scale = (20, 1, 11), pos = (0, 0, 0.8), scale = 0.15, command = (lambda self = self: self.fsm.request('requestExit')))
        return None

    
    def disableExitButton(self):
        self.exitButton.destroy()
        return None

    
    def enterRequestExit(self):
        messenger.send('elevatorExitButton')
        return None

    
    def exitRequestExit(self):
        return None

    
    def enterElevatorClosing(self):
        return None

    
    def exitElevatorClosing(self):
        return None

    
    def enterExiting(self):
        return None

    
    def handleOffElevator(self):
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


