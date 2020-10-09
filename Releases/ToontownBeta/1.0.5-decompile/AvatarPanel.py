# Source Generated with Decompyle++
# File: AvatarPanel.pyo (Python 2.0)

from ShowBaseGlobal import *
import PandaObject
import ToonHead
import Button
import FriendHandle
import LaffMeter
import Avatar
import DistributedObject
import FriendsListPanel
import ToontownGlobals
import GuiGlobals
from DirectGui import *

class AvatarPanel(PandaObject.PandaObject):
    currentAvatarPanel = None
    
    def __init__(self, avatar):
        if AvatarPanel.currentAvatarPanel:
            AvatarPanel.currentAvatarPanel.cleanup()
        
        AvatarPanel.currentAvatarPanel = self
        if FriendsListPanel.FriendsListPanel.currentFriendsListPanel:
            FriendsListPanel.FriendsListPanel.currentFriendsListPanel.cleanup()
            FriendsListPanel.FriendsListPanel.currentFriendsListPanel = None
        
        self.laffMeter = None
        self.avName = avatar.getName()
        if isinstance(avatar, DistributedObject.DistributedObject) or isinstance(avatar, FriendHandle.FriendHandle):
            self.avId = avatar.doId
            self.avDisableName = avatar.uniqueName('disable')
            self.avGenerateName = avatar.uniqueName('generate')
            self.avHpChangeName = avatar.uniqueName('hpChange')
            if toonbase.tcr.doId2do.has_key(self.avId):
                avatar = toonbase.tcr.doId2do[self.avId]
            
        else:
            self.avDisableName = None
            self.avGenerateName = None
            self.avHpChangeName = None
            self.avId = None
        import Toon
        if not isinstance(avatar, Toon.Toon):
            pass
        self.isToon = isinstance(avatar, FriendHandle.FriendHandle)
        wantsLaffMeter = isinstance(avatar, Toon.Toon)
        toonbase.localToon.obscureFriendsListButton(1)
        gui = loader.loadModelOnce('phase_4/models/gui/avatar_panel_gui')
        disabledImageColor = Vec4(1, 1, 1, 0.4)
        text0Color = Vec4(1, 1, 1, 1)
        text1Color = Vec4(0.5, 1, 0.5, 1)
        text2Color = Vec4(1, 1, 0.5, 1)
        text3Color = Vec4(1, 1, 1, 0.2)
        self.frame = DirectFrame(image = gui.find('**/avatar_panel'), relief = None, pos = (1.1, 100, 0.525))
        dw = DepthWriteTransition()
        self.frame.setY(100)
        self.frame.arc().setTransition(dw, 1)
        self.closeButton = DirectButton(parent = self.frame, image = (gui.find('**/CloseBtn_UP'), gui.find('**/CloseBtn_DN'), gui.find('**/CloseBtn_Rllvr')), relief = None, pos = (0.157644, 0, -0.379167), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleClose)
        if self.isToon:
            self.friendButton = DirectButton(parent = self.frame, image = (gui.find('**/Frnds_Btn_UP'), gui.find('**/Frnds_Btn_DN'), gui.find('**/Frnds_Btn_RLVR'), gui.find('**/Frnds_Btn_UP')), image3_color = disabledImageColor, relief = None, text = 'Friends', text_scale = 0.06, pos = (-0.103, 0, 0.096), text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_pos = (0.06, -0.02), text_align = TMALIGNLEFT, text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleFriend)
            self.whisperButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_ChtBtn_UP'), gui.find('**/ChtBx_ChtBtn_DN'), gui.find('**/ChtBx_ChtBtn_RLVR'), gui.find('**/ChtBx_ChtBtn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103, 0, -0.1875), text = 'Whisper', text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.06, text_pos = (0.06, -0.02), text_align = TMALIGNLEFT, text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleWhisper)
            self.toonUpButton = DirectButton(parent = self.frame, image = (gui.find('**/Amuse_Btn_UP'), gui.find('**/Amuse_Btn_DN'), gui.find('**/Amuse_Btn_RLVR'), gui.find('**/Amuse_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103, 0, -0.0905), text = 'Toon-up', text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.06, text_pos = (0.06, -0.02), text_align = TMALIGNLEFT, text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleFun)
            self.goToButton = DirectButton(parent = self.frame, image = (gui.find('**/Go2_Btn_UP'), gui.find('**/Go2_Btn_DN'), gui.find('**/Go2_Btn_RLVR'), gui.find('**/Go2_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103, 0, 0.00294), text = 'Go To', text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.06, text_pos = (0.06, -0.02), text_align = TMALIGNLEFT, text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleGoto)
            self.ignoreButton = DirectButton(parent = self.frame, image = (gui.find('**/Ignore_Btn_UP'), gui.find('**/Ignore_Btn_DN'), gui.find('**/Ignore_Btn_RLVR'), gui.find('**/Ignore_Btn_UP')), image3_color = disabledImageColor, relief = None, pos = (-0.103697, 0, -0.274875), text = 'Ignore', text0_fg = text0Color, text1_fg = text1Color, text2_fg = text2Color, text3_fg = text3Color, text_scale = 0.06, text_pos = (0.06, -0.02), text_align = TMALIGNLEFT, text_font = ToontownGlobals.getInterfaceFont(), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleIgnore)
            self.whisperButton.hide()
            self.toonUpButton.hide()
            self.ignoreButton.hide()
            self.detailButton = DirectButton(parent = self.frame, image = (gui.find('**/ChtBx_BackBtn_UP'), gui.find('**/ChtBx_BackBtn_DN'), gui.find('**/ChtBx_BackBtn_Rllvr')), relief = None, pos = (-0.133773, 0, -0.387132), clickSound = GuiGlobals.getDefaultClickSound(), rolloverSound = GuiGlobals.getDefaultRolloverSound(), command = self._AvatarPanel__handleDetails)
        
        self.nameLabel = DirectLabel(parent = self.frame, pos = (0.0125, 0, 0.385), relief = None, text = self.avName, text_font = avatar.getFont(), text_fg = Vec4(0, 0, 0, 1), text_pos = (0, 0), text_scale = 0.06, text_wordwrap = 6.0)
        self.head = self.frame.attachNewNode('head')
        self.head.setPosHprScale(0.01, 5, 0.26, 180, 0, 0, 0.11, 0.11, 0.11)
        if self.isToon:
            self.headModel = ToonHead.ToonHead()
            self.headModel.setupHead(avatar.style, forGui = 1)
            self.headModel.reparentTo(self.head)
            self.headModel.startBlink()
            self.headModel.startLookAround()
        
        self.healthText = DirectLabel(parent = self.frame, text = '', pos = (0.06, 0, 0.165), text_pos = (0, 0), text_scale = 0.05)
        self.healthText.hide()
        if wantsLaffMeter:
            self._AvatarPanel__makeLaffMeter(avatar)
            self._AvatarPanel__updateHp(avatar.hp, avatar.maxHp)
            self.healthText.show()
            self.laffMeter.show()
        
        menuX = -0.05
        menuScale = 0.064
        if self.isToon:
            self.accept(self.avDisableName, self._AvatarPanel__handleDisableAvatar)
            self.accept(self.avGenerateName, self._AvatarPanel__handleGenerateAvatar)
            self.accept(self.avHpChangeName, self._AvatarPanel__updateHp)
        
        self.frame.show()

    
    def cleanup(self):
        if AvatarPanel.currentAvatarPanel != self:
            return None
        
        self.frame.destroy()
        del self.frame
        self.head.removeNode()
        del self.head
        if self.isToon:
            self.headModel.stopBlink()
            self.headModel.stopLookAroundNow()
            self.headModel.delete()
            del self.headModel
        
        toonbase.localToon.obscureFriendsListButton(-1)
        self.laffMeter = None
        if self.avDisableName:
            self.ignore(self.avDisableName)
        
        if self.avGenerateName:
            self.ignore(self.avGenerateName)
        
        if self.avHpChangeName:
            self.ignore(self.avHpChangeName)
        
        AvatarPanel.currentAvatarPanel = None

    
    def __handleGoto(self):
        messenger.send('gotoAvatar', [
            self.avId,
            self.avName,
            self.avDisableName])

    
    def __handleWhisper(self):
        print 'Whisper.'

    
    def __handleFun(self):
        print 'Fun.'

    
    def __handleFriend(self):
        messenger.send('friendAvatar', [
            self.avId,
            self.avName,
            self.avDisableName])

    
    def __handleIgnore(self):
        print 'Ignore.'

    
    def __handleDetails(self):
        messenger.send('avatarDetails', [
            self.avId,
            self.avName])

    
    def __handleClose(self):
        self.cleanup()
        AvatarPanel.currentAvatarPanel = None

    
    def __handleDisableAvatar(self):
        if not toonbase.tcr.isFriend(self.avId):
            self.cleanup()
            AvatarPanel.currentAvatarPanel = None
        else:
            self.healthText.hide()
            if self.laffMeter != None:
                self.laffMeter.destroy()
                self.laffMeter = None
            

    
    def __handleGenerateAvatar(self, avatar):
        if self.laffMeter == None:
            self._AvatarPanel__makeLaffMeter(avatar)
        
        self._AvatarPanel__updateHp(avatar.hp, avatar.maxHp)
        self.laffMeter.show()
        self.healthText.show()

    
    def __makeLaffMeter(self, avatar):
        self.laffMeter = LaffMeter.LaffMeter(avatar.style, avatar.hp, avatar.maxHp)
        self.laffMeter.reparentTo(self.frame)
        self.laffMeter.setPos(-0.1, 0, 0.205)
        self.laffMeter.setScale(0.03)

    
    def __updateHp(self, hp, maxHp):
        if self.laffMeter != None:
            self.laffMeter.adjustFace(hp, maxHp)
            self.healthText['text'] = '%d / %d' % (hp, maxHp)
        


