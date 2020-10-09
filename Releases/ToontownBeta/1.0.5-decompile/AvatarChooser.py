# Source Generated with Decompyle++
# File: AvatarChooser.pyo (Python 2.0)

from ShowBaseGlobal import *
import ToontownGlobals
import GuiGlobals
import PandaObject
import OnscreenText
import AvatarChoice
import Label
import StateData
import FSM
import State
import DownloadForceAcknowledge
import OnscreenPanel
from DirectGui import *
MAX_AVATARS = 6
POSITIONS = [
    Vec3(-0.82, 0, 0.35),
    Vec3(0, 0, 0.35),
    Vec3(0.82, 0, 0.35),
    Vec3(-0.82, 0, -0.47),
    Vec3(0, 0, -0.47),
    Vec3(0.82, 0, -0.47)]
COLORS = [
    Vec4(0.917, 0.164, 0.164, 1),
    Vec4(0.152, 0.75, 0.258, 1),
    Vec4(0.598, 0.402, 0.875, 1),
    Vec4(0.133, 0.59, 0.977, 1),
    Vec4(0.895, 0.348, 0.602, 1),
    Vec4(0.977, 0.816, 0.133, 1)]

class AvatarChooser(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, avatarList, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.choice = None
        self.avatarList = avatarList
        self.fsm = FSM.FSM('AvatarChooser', [
            State.State('Choose', self.enterChoose, self.exitChoose, [
                'CheckDownload']),
            State.State('CheckDownload', self.enterCheckDownload, self.exitCheckDownload, [
                'Choose'])], 'Choose', 'Choose')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getCurrentState().addChild(self.fsm)
        self.nextPhase = 4
        return None

    
    def enter(self):
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        self.pickAToonBG.reparentTo(base.camera)
        for panel in self.panelList:
            panel.show()
            self.accept(panel.doneEvent, self._AvatarChooser__handlePanelDone)
        
        return None

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        for panel in self.panelList:
            panel.hide()
        
        self.ignoreAll()
        self.title.reparentTo(hidden)
        self.quitButton.hide()
        self.pickAToonBG.reparentTo(hidden)
        return None

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.pickAToonGui = loader.loadModelOnce('phase_3/models/gui/pick_a_toon_gui')
        self.pickAToonBG = self.pickAToonGui.find('**/av-chooser_FnlBG')
        self.pickAToonBG.setPos(0.0, 2.74, 0.0)
        self.title = OnscreenText.OnscreenText('Pick  A  Toon  To  Play', scale = 0.17, parent = hidden, font = ToontownGlobals.getSignFont(), fg = (1, 0.9, 0.1, 1), pos = (0.0, 0.82))
        self.quitButton = DirectButton(image = (self.pickAToonGui.find('**/QuitBtn_UP'), self.pickAToonGui.find('**/QuitBtn_DN'), self.pickAToonGui.find('**/QuitBtn_RLVR')), relief = None, text = 'Quit', text_font = ToontownGlobals.getSignFont(), text0_fg = (0.152, 0.75, 0.258, 1), text1_fg = (0.152, 0.75, 0.258, 1), text2_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -0.035), text_scale = 0.1, scale = 1.05, pos = (0.008, 0, -0.924), command = self._AvatarChooser__handleQuit)
        self.panelList = []
        positions = []
        for av in self.avatarList:
            panel = AvatarChoice.AvatarChoice(av, position = av.position)
            positions.append(av.position)
            panel.setPos(POSITIONS[av.position])
            panel['image_color'] = COLORS[av.position]
            self.panelList.append(panel)
        
        for panelNum in range(0, MAX_AVATARS):
            if panelNum not in positions:
                panel = AvatarChoice.AvatarChoice(position = panelNum)
                panel.setPos(POSITIONS[panelNum])
                panel['image_color'] = COLORS[panelNum]
                self.panelList.append(panel)
            
        
        self.isLoaded = 1
        return None

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        OnscreenPanel.cleanupPanel('globalDialog')
        for panel in self.panelList:
            panel.destroy()
        
        del self.panelList
        self.title.removeNode()
        del self.title
        self.quitButton.destroy()
        del self.quitButton
        del self.pickAToonBG
        loader.unloadModel('phase_3/models/gui/pick_a_toon_gui')
        self.pickAToonGui.removeNode()
        del self.pickAToonGui
        del self.avatarList
        self.parentFSM.getCurrentState().removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        self.isLoaded = 0
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        return None

    
    def __handlePanelDone(self, panelDoneStatus, panelChoice = 0):
        self.doneStatus = { }
        self.doneStatus['mode'] = panelDoneStatus
        self.choice = panelChoice
        if panelDoneStatus == 'chose':
            self._AvatarChooser__handleChoice()
        elif panelDoneStatus == 'delete':
            self._AvatarChooser__handleDelete()
        elif panelDoneStatus == 'create':
            self._AvatarChooser__handleCreate()
        
        return None

    
    def getChoice(self):
        return self.choice

    
    def __handleChoice(self):
        self.fsm.request('CheckDownload')

    
    def __handleCreate(self):
        
        def sendDoneTask(task):
            messenger.send(task.doneEvent, [
                task.doneStatus])
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        sdt.doneStatus = self.doneStatus
        base.transitions.fadeOutTask(sdt)

    
    def __handleDelete(self):
        messenger.send(self.doneEvent, [
            self.doneStatus])

    
    def __handleQuit(self):
        OnscreenPanel.cleanupPanel('globalDialog')
        toonbase.exitShow()

    
    def enterChoose(self):
        return None

    
    def exitChoose(self):
        return None

    
    def enterCheckDownload(self):
        self.accept('downloadAck-response', self._AvatarChooser__handleDownloadAck)
        self.downloadAck = DownloadForceAcknowledge.DownloadForceAcknowledge('downloadAck-response')
        self.downloadAck.enter(self.nextPhase)
        return None

    
    def exitCheckDownload(self):
        self.downloadAck.exit()
        self.downloadAck.cleanup()
        self.downloadAck = None
        self.ignore('downloadAck-response')
        return None

    
    def __handleDownloadAck(self, doneStatus):
        
        def sendDoneTask(task):
            messenger.send(task.doneEvent, [
                task.doneStatus])
            return Task.done

        if doneStatus['mode'] == 'complete':
            sdt = Task.Task(sendDoneTask)
            sdt.doneEvent = self.doneEvent
            sdt.doneStatus = self.doneStatus
            base.transitions.fadeOutTask(sdt)
        else:
            self.fsm.request('Choose')


