# Source Generated with Decompyle++
# File: AvatarChoice.pyo (Python 2.0)

from ShowBaseGlobal import *
import ToontownGlobals
import PandaObject
import AvatarDNA
import ToonHead
import DialogBox
import OnscreenPanel
from DirectGui import *

class AvatarChoice(DirectButton):
    
    def __init__(self, av = None, position = 0):
        DirectButton.__init__(self, relief = None, text = '', text_font = ToontownGlobals.getSignFont())
        self.initialiseoptions(AvatarChoice)
        if not av:
            self.create = 1
            self.name = ''
            self.dna = None
        else:
            self.create = 0
            self.name = av.name
            self.dna = AvatarDNA.AvatarDNA(av.dna)
        self.position = position
        self.doneEvent = 'avChoicePanel-' + str(self.position)
        self.pickAToonGui = loader.loadModelOnce('phase_3/models/gui/pick_a_toon_gui')
        self['image'] = self.pickAToonGui.find('**/av-chooser_Square_UP')
        self.setScale(1.01)
        if self.create:
            self['command'] = self._AvatarChoice__handleCreate
            self['text'] = ('Make A\nToon',)
            self['text_pos'] = (0, 0)
            self['text0_scale'] = 0.1
            self['text1_scale'] = 0.12
            self['text2_scale'] = 0.12
            self['text0_fg'] = (0, 1, 0.8, 0.5)
            self['text1_fg'] = (0, 1, 0.8, 1)
            self['text2_fg'] = (0.3, 1, 0.9, 1)
        else:
            self['command'] = self._AvatarChoice__handleChoice
            self['text'] = ('', 'Play\nThis Toon', 'Play\nThis Toon')
            self['text_scale'] = 0.12
            self['text_fg'] = (1, 0.9, 0.1, 1)
            dw = DepthWriteTransition()
            self.setY(100)
            self.arc().setTransition(dw, 1)
            self.nameText = DirectLabel(parent = self, relief = None, scale = 0.1, pos = (0, 0, 0.27), text = self.name, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_font = ToontownGlobals.getToonFont(), state = DISABLED)
            self.head = hidden.attachNewNode('head')
            self.head.setPosHprScale(0, 5, -0.1, 180, 0, 0, 0.24, 0.24, 0.24)
            self.head.reparentTo(self.stateNodePath[0], 20)
            self.head.instanceTo(self.stateNodePath[1], 20)
            self.head.instanceTo(self.stateNodePath[2], 20)
            self.headModel = ToonHead.ToonHead()
            self.headModel.setupHead(self.dna, forGui = 1)
            self.headModel.reparentTo(self.head)
            self.headModel.startBlink()
            self.headModel.startLookAround()
            trashcanGui = loader.loadModelOnce('phase_3/models/gui/trashcan_gui')
            self.deleteButton = DirectButton(parent = self, image = (trashcanGui.find('**/TrashCan_CLSD'), trashcanGui.find('**/TrashCan_OPEN'), trashcanGui.find('**/TrashCan_RLVR')), text = ('', 'Delete', 'Delete'), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.15, text_pos = (0, -0.1), text_font = ToontownGlobals.getInterfaceFont(), relief = None, pos = (0.27, 0, -0.25), scale = 0.45, command = self._AvatarChoice__handleDelete)
        self.resetFrameSize()
        return None

    
    def destroy(self):
        loader.unloadModel('phase_3/models/gui/pick_a_toon_gui')
        self.pickAToonGui.removeNode()
        del self.pickAToonGui
        del self.dna
        if self.create:
            pass
        1
        self.headModel.stopBlink()
        self.headModel.stopLookAroundNow()
        self.headModel.delete()
        self.head.removeNode()
        del self.head
        del self.headModel
        del self.nameText
        del self.deleteButton
        loader.unloadModel('phase_3/models/gui/trashcan_gui')
        DirectFrame.destroy(self)
        return None

    
    def __handleChoice(self):
        OnscreenPanel.cleanupPanel('globalDialog')
        messenger.send(self.doneEvent, [
            'chose',
            self.position])

    
    def __handleCreate(self):
        OnscreenPanel.cleanupPanel('globalDialog')
        messenger.send(self.doneEvent, [
            'create',
            self.position])

    
    def __handleDelete(self):
        OnscreenPanel.cleanupPanel('globalDialog')
        self.verify = DialogBox.DialogBox(doneEvent = 'verifyDone', message = 'This will delete %s forever.' % self.name, style = DialogBox.TwoChoice)
        self.verify.show()
        self.accept('verifyDone', self._AvatarChoice__handleVerify)

    
    def __handleVerify(self):
        status = self.verify.doneStatus
        self.ignore('verifyDone')
        self.verify.cleanup()
        del self.verify
        if status == 'ok':
            messenger.send(self.doneEvent, [
                'delete',
                self.position])
        


