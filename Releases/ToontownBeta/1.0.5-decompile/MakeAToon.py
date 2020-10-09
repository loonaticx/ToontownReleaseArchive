# Source Generated with Decompyle++
# File: MakeAToon.pyo (Python 2.0)

from ShowBaseGlobal import *
import PandaObject
import Char
import Avatar
import Toon
import LocalToon
import AvatarDNA
import BodyShop
import ColorShop
import ClothesShop
import NameShop
import FSM
import State
import StateData
import ToontownGlobals
import OnscreenText
import Label
import whrandom
import Task
from DirectGui import *
BODYSHOP = 1
COLORSHOP = 2
CLOTHESSHOP = 3
NAMESHOP = 4

class MakeAToon(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.phase = 3
        self.name = None
        self.dnastring = None
        self.dna = None
        self.fsm = FSM.FSM('MakeAToon', [
            State.State('Init', self.enterInit, self.exitInit, [
                'BodyShop']),
            State.State('BodyShop', self.enterBodyShop, self.exitBodyShop, [
                'ClothesShop',
                'ColorShop',
                'NameShop']),
            State.State('ClothesShop', self.enterClothesShop, self.exitClothesShop, [
                'ColorShop',
                'NameShop',
                'BodyShop']),
            State.State('ColorShop', self.enterColorShop, self.exitColorShop, [
                'NameShop',
                'BodyShop',
                'ClothesShop']),
            State.State('NameShop', self.enterNameShop, self.exitNameShop, [
                'ClothesShop',
                'ColorShop',
                'BodyShop']),
            State.State('Done', self.enterDone, self.exitDone, [])], 'Init', 'Done')
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('createAvatar').addChild(self.fsm)
        self.bs = BodyShop.BodyShop('BodyShop-done')
        self.cos = ColorShop.ColorShop('ColorShop-done')
        self.cls = ClothesShop.ClothesShop('ClothesShop-done')
        self.ns = NameShop.NameShop(self.fsm, 'NameShop-done')
        self.shop = BODYSHOP
        self.shopsVisited = []
        self.music = None
        self.soundBack = None
        self.fsm.enterInitialState()
        return None

    
    def getToon(self):
        return self.toon

    
    def enter(self):
        base.camNode.setFov(ToontownGlobals.MakeAToonCameraFov)
        base.playMusic(self.music, looping = 1, volume = 0.9)
        self.toon.startBlink()
        self.toon.startLookAround()
        self.toon.reparentTo(render)
        self.toon.setPosHprScale(-1.5, -2.0, 0, 200, 0, 0, 1.2, 1.2, 1.2)
        self.toon.loop('neutral')
        self.room.reparentTo(render)
        camera.setPosHpr(0.75, -22, 5.35, 0, -7.12, 0)
        self.mickey.reparentTo(render)
        self.mickey.loop('neutral')
        self.mickey.setPosHpr(4.2, -1.9, 0, 160, 0, 0)
        self.guiTopBar.show()
        self.guiBottomBar.show()
        self.guiCancelButton.show()
        self.guiNextButton.show()
        self.fsm.request('BodyShop')
        return None

    
    def exit(self):
        base.cam.node().setFov(ToontownGlobals.DefaultCameraFov)
        self.guiTopBar.hide()
        self.guiBottomBar.hide()
        base.stopMusic(self.music)
        self.fsm.request('Done')
        self.toon.stopBlink()
        self.toon.stopLookAroundNow()
        self.toon.reparentTo(hidden)
        self.room.reparentTo(hidden)
        self.mickey.reparentTo(hidden)
        self.mickey.stop()
        return None

    
    def load(self):
        self.gui = loader.loadModelOnce('phase_3/models/gui/create_a_toon_gui')
        self.guiTopBar = DirectFrame(relief = None, image = self.gui.find('**/CrtATn_TopBar'), text = 'Create Your Toon', text_font = ToontownGlobals.getSignFont(), text_fg = (0.0, 0.65, 0.35, 1), text_scale = 0.18, text_pos = (0, -0.03), pos = (0, 0, 0.86))
        self.guiTopBar.hide()
        self.guiBottomBar = DirectFrame(relief = None, image = self.gui.find('**/CrtATn_BtmBar'), pos = (0, 0, -0.86))
        self.guiBottomBar.hide()
        self.guiBodyButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtATn_BodyBtn_UP'), self.gui.find('**/CrtATn_BodyBtn_DN'), self.gui.find('**/CrtATn_BodyBtn_SEL'), self.gui.find('**/CrtATn_BodyBtn_SEL')), pos = (-0.7, 0, 0.054), command = self._MakeAToon__handleBodyShop, text = ('', 'Body', 'Body', ''), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.06), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiBodyButton.hide()
        self.guiClothesButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtATn_ClthBtn_UP'), self.gui.find('**/CrtATn_ClthBtn_DN'), self.gui.find('**/CrtATn_ClthBtn_SEL'), self.gui.find('**/CrtATn_ClthBtn_SEL')), pos = (0, 0, 0.0418), command = self._MakeAToon__handleClothesShop, text = ('', 'Clothes', 'Clothes', ''), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.06), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiClothesButton.hide()
        self.guiPaintButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtATn_PntBtn_UP'), self.gui.find('**/CrtATn_PntBtn_DN'), self.gui.find('**/CrtATn_PntBtn_SEL'), self.gui.find('**/CrtATn_PntBtn_SEL')), pos = (0.7, 0, 0.0501), command = self._MakeAToon__handleColorShop, text = ('', 'Paint', 'Paint', ''), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.06), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiPaintButton.hide()
        self.guiCheckButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtAtoon_Btn1_UP'), self.gui.find('**/CrtAtoon_Btn1_DOWN'), self.gui.find('**/CrtAtoon_Btn1_RLLVR')), pos = (1.165, 0, -0.018), command = self._MakeAToon__handleNext, text = ('', 'Done', 'Done'), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.03), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiCheckButton.hide()
        self.guiCancelButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtAtoon_Btn2_UP'), self.gui.find('**/CrtAtoon_Btn2_DOWN'), self.gui.find('**/CrtAtoon_Btn2_RLLVR')), pos = (-1.179, 0, -0.011), command = self._MakeAToon__handleCancel, text = ('', 'Cancel', 'Cancel'), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.03), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiCancelButton.hide()
        self.guiNextButton = DirectButton(parent = self.guiBottomBar, relief = None, image = (self.gui.find('**/CrtAtoon_Btn3_UP'), self.gui.find('**/CrtAtoon_Btn3_DN'), self.gui.find('**/CrtAtoon_Btn3_RLVR')), pos = (1.165, 0, -0.018), command = self._MakeAToon__handleNext, text = ('', 'Next', 'Next'), text_font = ToontownGlobals.getInterfaceFont(), text_scale = 0.08, text_pos = (0, -0.03), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1))
        self.guiNextButton.hide()
        self.room = loader.loadModel('phase_3/models/gui/create_a_toon')
        self.draftingTable = self.room.find('**/drafting_table')
        self.easel = self.room.find('**/easel')
        self.sewingMachine = self.room.find('**/sewing_machine')
        self.stool = self.room.find('**/stool')
        self.stool.hide()
        self.draftingTable.hide()
        self.easel.hide()
        self.sewingMachine.hide()
        self.dna = AvatarDNA.AvatarDNA()
        self.dna.newToonRandom()
        self.toon = Toon.Toon()
        self.toon.setDNA(self.dna)
        self.toon.useLOD(1000)
        self.toon.setNameVisible(0)
        self.toon.startBlink()
        self.toon.startLookAround()
        self.mickey = Char.Char()
        mickeyDNA = AvatarDNA.AvatarDNA()
        mickeyDNA.newChar('mk')
        self.mickey.setDNA(mickeyDNA)
        self.mickey.nametag.manage(toonbase.marginManager)
        self.mickey.setNametagScale(0.8)
        self.mickey.hideName()
        self.mickey.setPickable(0)
        self.mickey.nametag.getNametag3d().setChatWordwrap(8)
        self.bs.load()
        self.cos.load()
        self.cls.load()
        self.ns.load()
        self.music = base.loadMusic('phase_3/audio/bgm/create_a_toon.mid')
        self.soundBack = base.loadSfx('phase_3/audio/sfx/GUI_create_toon_back.mp3')
        return None

    
    def unload(self):
        self.exit()
        del self.stool
        del self.draftingTable
        del self.easel
        del self.sewingMachine
        self.room.removeNode()
        del self.room
        self.toon.stopBlink()
        self.toon.stopLookAroundNow()
        self.bs.unload()
        self.cos.unload()
        self.cls.unload()
        self.ns.unload()
        del self.bs
        del self.cos
        del self.cls
        del self.ns
        self.guiTopBar.destroy()
        del self.guiTopBar
        self.guiBottomBar.destroy()
        del self.guiBottomBar
        del self.guiBodyButton
        del self.guiClothesButton
        del self.guiPaintButton
        del self.guiCancelButton
        del self.guiCheckButton
        del self.guiNextButton
        del self.name
        del self.dnastring
        base.unloadMusic(self.music)
        del self.music
        base.unloadSfx(self.soundBack)
        del self.soundBack
        del self.dna
        self.toon.delete()
        del self.toon
        self.mickey.nametag.unmanage(toonbase.marginManager)
        self.mickey.delete()
        del self.mickey
        self.gui.removeNode()
        del self.gui
        self.parentFSM.getStateNamed('createAvatar').removeChild(self.fsm)
        del self.parentFSM
        del self.fsm
        self.ignoreAll()
        loader.unloadModel('phase_3/models/gui/create_a_toon_gui')
        loader.unloadModel('phase_3/models/gui/create_a_toon')
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        return None

    
    def getDNA(self):
        return self.dnastring

    
    def getName(self):
        return self.name

    
    def __handleBodyShop(self):
        self.fsm.request('BodyShop')
        return None

    
    def __handleClothesShop(self):
        self.fsm.request('ClothesShop')
        return None

    
    def __handleColorShop(self):
        self.fsm.request('ColorShop')
        return None

    
    def __handleNameShop(self):
        self.fsm.request('NameShop')
        return None

    
    def __handleCancel(self):
        self.doneStatus = 'cancel'
        
        def sendDoneTask(self):
            messenger.send(self.doneEvent)
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        base.transitions.fadeOutTask(sdt)

    
    def updateButtons(self):
        if BODYSHOP in self.shopsVisited:
            self.guiBodyButton.show()
        
        if CLOTHESSHOP in self.shopsVisited:
            self.guiClothesButton.show()
        
        if COLORSHOP in self.shopsVisited:
            self.guiPaintButton.show()
        

    
    def goToNextShop(self):
        if CLOTHESSHOP not in self.shopsVisited:
            self.fsm.request('ClothesShop')
        elif COLORSHOP not in self.shopsVisited:
            self.fsm.request('ColorShop')
        else:
            self.fsm.request('NameShop')
        return None

    
    def mickeySez(self, stringList):
        self.mickey.setChat(whrandom.choice(stringList), CFSpeech)
        self.mickey.playDialogue('statementA', 1)
        return None

    
    def enterInit(self):
        pass

    
    def exitInit(self):
        pass

    
    def bodyShopOpening(self, task):
        self.mickeySez([
            'Click the arrows to create your toon.'])
        self.bs.showButtons()
        self.updateButtons()
        return Task.done

    
    def enterBodyShop(self):
        self.shop = BODYSHOP
        if BODYSHOP not in self.shopsVisited:
            self.shopsVisited.append(BODYSHOP)
        
        self.guiTopBar['text'] = 'Create Your Toon'
        self.guiTopBar['text_fg'] = (1, 0.9, 0, 1)
        self.guiTopBar['text_scale'] = 0.18
        base.transitions.fadeIn()
        self.accept('BodyShop-done', self._MakeAToon__handleBodyShopDone)
        self.draftingTable.show()
        self.guiNextButton.show()
        self.guiBodyButton['state'] = DISABLED
        self.bs.enter(self.toon)
        taskMgr.doMethodLater(0.8, self.bodyShopOpening, 'bodyShopOpeningTask')
        taskMgr.doMethodLater(16.0, self.bodyShopDialogTask, 'bodyShopDialogTask')
        return None

    
    def bodyShopDialogTask(self, task):
        self.mickeySez([
            'Click the arrow below to go to the next screen.'])
        return Task.done

    
    def exitBodyShop(self):
        self.bs.exit()
        self.mickey.clearChat()
        self.ignore('BodyShop-done')
        taskMgr.removeTasksNamed('doLater-bodyShopDialogTask')
        taskMgr.removeTasksNamed('bodyShopDialogTask')
        taskMgr.removeTasksNamed('doLater-bodyShopOpeningTask')
        taskMgr.removeTasksNamed('bodyShopOpeningTask')
        self.draftingTable.hide()
        self.guiBodyButton['state'] = NORMAL
        self.guiNextButton.hide()
        return None

    
    def __handleBodyShopDone(self):
        self.goToNextShop()

    
    def clothesShopOpening(self, task):
        self.mickeySez([
            'Click the arrows to pick clothes!'])
        self.cls.showButtons()
        self.updateButtons()
        return Task.done

    
    def enterClothesShop(self):
        self.shop = CLOTHESSHOP
        if CLOTHESSHOP not in self.shopsVisited:
            self.shopsVisited.append(CLOTHESSHOP)
        
        self.guiTopBar['text'] = 'Choose Your Clothes'
        self.guiTopBar['text_fg'] = (0.15, 0.4, 0.8, 1)
        self.guiTopBar['text_scale'] = 0.16
        base.transitions.fadeIn()
        self.accept('ClothesShop-done', self._MakeAToon__handleClothesShopDone)
        self.sewingMachine.show()
        self.guiClothesButton['state'] = DISABLED
        self.guiNextButton.show()
        self.cls.enter(self.toon)
        taskMgr.doMethodLater(0.8, self.clothesShopOpening, 'clothesShopOpeningTask')
        return None

    
    def exitClothesShop(self):
        self.cls.exit()
        taskMgr.removeTasksNamed('doLater-clothesShopOpeningTask')
        taskMgr.removeTasksNamed('clothesShopOpeningTask')
        self.mickey.clearChat()
        self.ignore('ClothesShop-done')
        self.sewingMachine.hide()
        self.guiClothesButton['state'] = NORMAL
        self.guiNextButton.hide()
        return None

    
    def __handleClothesShopDone(self):
        self.goToNextShop()

    
    def colorShopOpening(self, task):
        self.mickeySez([
            'Click the arrows to paint your toon!'])
        self.cos.showButtons()
        self.updateButtons()
        return Task.done

    
    def enterColorShop(self):
        self.shop = COLORSHOP
        if COLORSHOP not in self.shopsVisited:
            self.shopsVisited.append(COLORSHOP)
        
        self.guiTopBar['text'] = 'Paint Your Toon'
        self.guiTopBar['text_fg'] = (0.0, 0.65, 0.35, 1)
        self.guiTopBar['text_scale'] = 0.18
        base.transitions.fadeIn()
        self.accept('ColorShop-done', self._MakeAToon__handleColorShopDone)
        self.easel.show()
        self.guiPaintButton['state'] = DISABLED
        self.guiNextButton.show()
        self.cos.enter(self.toon)
        taskMgr.doMethodLater(0.8, self.colorShopOpening, 'colorShopOpeningTask')
        taskMgr.doMethodLater(8.0, self.colorShopDialogTask, 'colorShopDialogTask')
        return None

    
    def colorShopDialogTask(self, task):
        self.mickeySez([
            'You can go back to change your clothes or body, too!'])
        return Task.done

    
    def exitColorShop(self):
        self.cos.exit()
        self.mickey.clearChat()
        self.ignore('ColorShop-done')
        taskMgr.removeTasksNamed('doLater-colorShopOpeningTask')
        taskMgr.removeTasksNamed('colorShopOpeningTask')
        taskMgr.removeTasksNamed('doLater-colorShopDialogTask')
        taskMgr.removeTasksNamed('colorShopDialogTask')
        self.easel.hide()
        self.guiPaintButton['state'] = NORMAL
        self.guiNextButton.hide()
        return None

    
    def __handleColorShopDone(self):
        self.goToNextShop()

    
    def nameShopOpening(self, task):
        self.ns.enter(self.toon)
        self.updateButtons()
        return Task.done

    
    def enterNameShop(self):
        self.shop = NAMESHOP
        if NAMESHOP not in self.shopsVisited:
            self.shopsVisited.append(NAMESHOP)
            self.mickeySez([
                "Don't use your real name... make up a funny one!"])
        else:
            self.mickeySez([
                'Last step before going to Toontown!',
                'Pick a name you like!'])
        self.guiTopBar['text'] = 'Name Your Toon'
        self.guiTopBar['text_fg'] = (1, 0.9, 0, 1)
        self.guiTopBar['text_scale'] = 0.18
        base.transitions.fadeIn()
        self.accept('NameShop-name', self._MakeAToon__checkToon)
        self.accept('NameShop-done', self._MakeAToon__handleNameShopDone)
        taskMgr.doMethodLater(0.8, self.nameShopOpening, 'nameShopOpeningTask')
        self.guiCheckButton.show()
        return None

    
    def exitNameShop(self):
        self.ns.exit()
        self.mickey.clearChat()
        self.ignore('NameShop-name')
        self.ignore('NameShop-done')
        taskMgr.removeTasksNamed('doLater-nameShopOpeningTask')
        taskMgr.removeTasksNamed('nameShopOpeningTask')
        self.guiCheckButton.hide()
        return None

    
    def rejectName(self):
        self.ns.rejectName('That name is not allowed. Please try again.')

    
    def acceptName(self):
        self.ns.acceptName()

    
    def __checkToon(self, name):
        self.name = name
        style = self.toon.getStyle()
        self.dnastring = style.makeNetString()
        self.doneStatus = 'check'
        messenger.send(self.doneEvent)

    
    def __handleNameShopDone(self):
        self.doneStatus = 'create'
        
        def sendDoneTask(self):
            messenger.send(self.doneEvent)
            return Task.done

        sdt = Task.Task(sendDoneTask)
        sdt.doneEvent = self.doneEvent
        base.transitions.fadeOutTask(sdt)

    
    def __handleNext(self):
        messenger.send('next')

    
    def enterDone(self):
        return None

    
    def exitDone(self):
        return None


