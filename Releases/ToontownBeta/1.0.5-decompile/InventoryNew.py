# Source Generated with Decompyle++
# File: InventoryNew.pyo (Python 2.0)

from DirectGui import *
from ToontownBattleGlobals import *
import InventoryBase

class InventoryNew(InventoryBase.InventoryBase, DirectFrame):
    PressableTextColor = Vec4(1, 1, 1, 1)
    PressableGeomColor = Vec4(1, 1, 1, 1)
    PressableImageColor = Vec4(0, 0.6, 1, 1)
    DeletePressableImageColor = Vec4(0, 0.6, 1, 1)
    UnpressableTextColor = Vec4(1, 1, 1, 0.3)
    UnpressableGeomColor = Vec4(1, 1, 1, 0.3)
    UnpressableImageColor = Vec4(0.3, 0.3, 0.3, 0.8)
    BookUnpressableTextColor = Vec4(1, 1, 1, 1)
    BookUnpressableGeomColor = Vec4(1, 1, 1, 1)
    BookUnpressableImage0Color = Vec4(0, 0.6, 1, 1)
    BookUnpressableImage2Color = Vec4(0.1, 0.7, 1, 1)
    
    def __init__(self, toon, invStr = None):
        InventoryBase.InventoryBase.__init__(self, toon, invStr)
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(InventoryNew)
        self.activateMode = 'book'
        self.load()
        self.hide()
        return None

    
    def updateTotalPropsText(self):
        self.totalLabel['text'] = 'Total Gags\n%d / %d' % (self.totalProps, self.getMaxTotalProps())
        return None

    
    def unload(self):
        self.invModel.removeNode()
        del self.invModel
        del self.invModels
        self.buttonModels.removeNode()
        del self.buttonModels
        del self.upButton
        del self.downButton
        del self.rolloverButton
        del self.flatButton
        self.trashcanGui.removeNode()
        del self.trashcanGui
        del self.invFrame
        del self.battleFrame
        del self.purchaseFrame
        del self.deleteEnterButton
        del self.deleteExitButton
        del self.detailFrame
        del self.detailNameLabel
        del self.detailAmountLabel
        del self.detailDataLabel
        del self.totalLabel
        del self.trackRows
        del self.trackNameLabels
        del self.trackScoreLabels
        del self.trackNextLabels
        del self.buttons
        if self.purchaseModels:
            self.purchaseModels.removeNode()
        
        del self.purchaseModels
        if self.battleModels:
            self.battleModels.removeNode()
        
        del self.battleModels
        DirectFrame.destroy(self)
        return None

    
    def load(self):
        self.invModel = loader.loadModelOnce('phase_4/models/gui/inventory_icons')
        self.invModels = []
        for track in range(len(AvPropsNew)):
            itemList = []
            for item in range(len(AvPropsNew[track])):
                itemList.append(self.invModel.find('**/' + AvPropsNew[track][item]))
            
            self.invModels.append(itemList)
        
        self.buttonModels = loader.loadModelOnce('phase_4/models/gui/inventory_gui')
        self.rowModel = self.buttonModels.find('**/InventoryRow')
        self.upButton = self.buttonModels.find('**/InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')
        self.flatButton = self.buttonModels.find('**/InventoryButtonFlat')
        self.invFrame = DirectFrame(relief = None, parent = self)
        self.battleModels = None
        self.battleFrame = None
        self.purchaseModels = None
        self.purchaseFrame = None
        self.trashcanGui = loader.loadModelOnce('phase_3/models/gui/trashcan_gui')
        self.deleteEnterButton = DirectButton(parent = self.invFrame, image = (self.trashcanGui.find('**/TrashCan_CLSD'), self.trashcanGui.find('**/TrashCan_OPEN'), self.trashcanGui.find('**/TrashCan_RLVR')), text = ('', 'DELETE', 'DELETE'), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.1, text_pos = (0, -0.1), text_font = getInterfaceFont(), relief = None, pos = (-1, 0, -0.35), scale = 1.0)
        self.deleteExitButton = DirectButton(parent = self.invFrame, image = (self.trashcanGui.find('**/TrashCan_OPEN'), self.trashcanGui.find('**/TrashCan_CLSD'), self.trashcanGui.find('**/TrashCan_RLVR')), text = ('', 'DONE', 'DONE'), text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_scale = 0.1, text_pos = (0, -0.1), text_font = getInterfaceFont(), relief = None, pos = (-1, 0, -0.35), scale = 1.0)
        self.deleteHelpText = DirectLabel(parent = self.invFrame, relief = None, pos = (0.272, 0.3, -0.907), text = 'Click on a gag to DELETE it.', text_fg = (0, 0, 0, 1), text_scale = 0.08)
        self.deleteHelpText.hide()
        self.detailFrame = DirectFrame(parent = self.invFrame, relief = None, pos = (1.05, 0, -0.08))
        self.detailNameLabel = DirectLabel(parent = self.detailFrame, text = '', text_fg = (0, 0, 0, 1), scale = 0.05, pos = (0, 0, 0), text_font = getInterfaceFont(), relief = None, image = self.invModels[0][0])
        self.detailAmountLabel = DirectLabel(parent = self.detailFrame, text = '', text_fg = (1, 1, 1, 1), scale = 0.05, pos = (0.15, 0, -0.2), text_font = getInterfaceFont(), text_align = TMALIGNRIGHT, relief = None)
        self.detailDataLabel = DirectLabel(parent = self.detailFrame, text = '', text_fg = (0, 0, 0, 1), scale = 0.05, pos = (0, 0, -0.27), text_font = getInterfaceFont(), relief = None)
        self.totalLabel = DirectLabel(text = '', parent = self.detailFrame, pos = (0.005, 0, -0.12), scale = 0.065, text_fg = (0, 0, 0, 1), text_font = getInterfaceFont(), relief = None)
        self.updateTotalPropsText()
        self.trackRows = []
        self.trackNameLabels = []
        self.trackScoreLabels = []
        self.trackNextLabels = []
        self.buttons = []
        for track in range(0, len(Tracks)):
            self.trackRows.append(DirectFrame(parent = self.invFrame, image = self.rowModel, pos = (0, 0, track * -0.12), image_color = (TrackColors[track][0], TrackColors[track][1], TrackColors[track][2], 1), relief = None))
            self.trackNameLabels.append(DirectLabel(text = Tracks[track].upper(), parent = self.trackRows[track], pos = (-0.72, 0, 0.01), scale = 0.06, relief = None, text_fg = (0.2, 0.2, 0.2, 1), text_font = getInterfaceFont(), text_align = TMALIGNLEFT))
            self.trackScoreLabels.append(DirectLabel(text = '0', parent = self.trackRows[track], pos = (-0.44, 0, -0.04), scale = 0.05, relief = None, text_fg = (0.3, 0.3, 0.3, 1), text_font = getInterfaceFont(), text_align = TMALIGNRIGHT))
            self.trackNextLabels.append(DirectLabel(text = '0', parent = self.trackRows[track], pos = (-0.31, 0, -0.02), scale = 0.05, relief = None, text_fg = (0, 0, 0, 1), text_font = getInterfaceFont(), text_align = TMALIGNCENTER))
            self.buttons.append([])
            for item in range(0, len(Levels)):
                button = DirectButton(parent = self.trackRows[track], image = (self.upButton, self.downButton, self.rolloverButton, self.flatButton), geom = self.invModels[track][item], text = '50', text_scale = 0.04, text_align = TMALIGNRIGHT, geom_scale = 0.75, geom_pos = (-0.01, 0, 0), text_fg = Vec4(1, 1, 1, 1), text_pos = (0.07, -0.04), relief = None, image_color = (0, 0.6, 1, 1), pos = (-0.31 + item * 0.193, 0, 0), command = self._InventoryNew__handleSelection, extraArgs = [
                    track,
                    item])
                button.bind(ENTER, (lambda x, track = track, item = item, button = button, self = self: self.showDetail(track, item, button)))
                button.bind(EXIT, (lambda x, track = track, item = item, button = button, self = self: self.hideDetail(track, item, button)))
                self.buttons[track].append(button)
            
        
        return None

    
    def __handleSelection(self, track, level):
        if self.activateMode == 'purchaseDelete' or self.activateMode == 'bookDelete':
            if self.numItem(track, level):
                self.useItem(track, level)
                self.updateGUI(track, level)
                messenger.send('inventory-deletion', [
                    track,
                    level])
            
        else:
            messenger.send('inventory-selection', [
                track,
                level])
        return None

    
    def __handleRun(self):
        messenger.send('inventory-run')
        return None

    
    def __handleSOS(self):
        messenger.send('inventory-sos')
        return None

    
    def __handlePass(self):
        messenger.send('inventory-pass')
        return None

    
    def showDetail(self, track, level, button):
        self.totalLabel.hide()
        self.detailNameLabel.show()
        self.detailNameLabel.configure(text = AvPropStrings[track][level], image_image = self.invModels[track][level])
        self.detailNameLabel.configure(image_scale = 25, image_pos = (-0.2, 0, -2.6))
        self.detailAmountLabel.show()
        self.detailAmountLabel.configure(text = '%d / %d' % (self.numItem(track, level), self.getMax(track, level)))
        self.detailDataLabel.show()
        self.detailDataLabel.configure(text = 'Accuracy: %s\n%s: %d\n%s' % (AvTrackAccStrings[track], self.getToonupDmgStr(track, level), getAvPropDamage(track, level, self.toon.experience.getExp(track)), self.getSingleGroupStr(track, level)))
        return None

    
    def hideDetail(self, track, level, button):
        self.totalLabel.show()
        self.detailNameLabel.hide()
        self.detailAmountLabel.hide()
        self.detailDataLabel.hide()
        return None

    
    def setActivateMode(self, mode, heal = 1, trap = 1, lure = 1):
        self.notify.info('setActivateMode() mode:%s heal:%s trap:%s lure:%s' % (mode, heal, trap, lure))
        self.previousActivateMode = self.activateMode
        self.activateMode = mode
        self.deactivateButtons()
        self.heal = heal
        self.trap = trap
        self.lure = lure
        self._InventoryNew__activateButtons()
        return None

    
    def deactivateButtons(self):
        if self.previousActivateMode == 'book':
            self.bookDeactivateButtons()
        elif self.previousActivateMode == 'bookDelete':
            self.bookDeleteDeactivateButtons()
        elif self.previousActivateMode == 'purchaseDelete':
            self.purchaseDeleteDeactivateButtons()
        elif self.previousActivateMode == 'purchase':
            self.purchaseDeactivateButtons()
        elif self.previousActivateMode == 'broke':
            self.brokeDeactivateButtons()
        elif self.previousActivateMode == 'battle':
            self.battleDeactivateButtons()
        else:
            self.notify.error('No such mode as %s' % self.previousActivateMode)
        return None

    
    def __activateButtons(self):
        if hasattr(self, 'activateMode'):
            if self.activateMode == 'book':
                self.bookActivateButtons()
            elif self.activateMode == 'bookDelete':
                self.bookDeleteActivateButtons()
            elif self.activateMode == 'purchaseDelete':
                self.purchaseDeleteActivateButtons()
            elif self.activateMode == 'purchase':
                self.purchaseActivateButtons()
            elif self.activateMode == 'broke':
                self.brokeActivateButtons()
            elif self.activateMode == 'battle':
                self.battleActivateButtons()
            else:
                self.notify.error('No such mode as %s' % self.activateMode)
        
        return None

    
    def bookActivateButtons(self):
        self.setPos(-0.2, 0, 0.4)
        self.setScale(0.8)
        self.deleteEnterButton.hide()
        self.deleteEnterButton.setPos(1.029, 0, -0.639)
        self.deleteEnterButton.setScale(0.75)
        self.deleteExitButton.hide()
        self.deleteExitButton.setPos(1.029, 0, -0.639)
        self.deleteExitButton.setScale(0.75)
        self.invFrame.reparentTo(self)
        self.invFrame.setPos(0, 0, 0)
        self.invFrame.setScale(1)
        self.deleteEnterButton['command'] = self.setActivateMode
        self.deleteEnterButton['extraArgs'] = [
            'bookDelete']
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        self.makeBookUnpressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def bookDeactivateButtons(self):
        self.deleteEnterButton['command'] = None
        return None

    
    def bookDeleteActivateButtons(self):
        messenger.send('enterBookDelete')
        self.setPos(-0.2, 0, 0.4)
        self.setScale(0.8)
        self.deleteEnterButton.hide()
        self.deleteEnterButton.setPos(1.029, 0, -0.639)
        self.deleteEnterButton.setScale(0.75)
        self.deleteExitButton.show()
        self.deleteExitButton.setPos(1.029, 0, -0.639)
        self.deleteExitButton.setScale(0.75)
        self.deleteHelpText.show()
        self.invFrame.reparentTo(self)
        self.invFrame.setPos(0, 0, 0)
        self.invFrame.setScale(1)
        self.deleteExitButton['command'] = self.setActivateMode
        self.deleteExitButton['extraArgs'] = [
            self.previousActivateMode]
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        if self.numItem(track, level) <= 0:
                            self.makeUnpressable(button)
                        else:
                            self.makeDeletePressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def bookDeleteDeactivateButtons(self):
        messenger.send('exitBookDelete')
        self.deleteHelpText.hide()
        self.deleteDeactivateButtons()
        return None

    
    def purchaseDeleteActivateButtons(self):
        self.reparentTo(guiTop)
        self.setPos(0, 0, -0.04)
        self.setScale(1)
        if self.purchaseFrame == None:
            self.loadPurchaseFrame()
        
        self.purchaseFrame.show()
        self.invFrame.reparentTo(self.purchaseFrame)
        self.invFrame.setPos(-0.23, 0, 0.50756)
        self.invFrame.setScale(0.793894)
        self.detailFrame.setPos(1.08, 0, 0)
        self.detailFrame.setScale(1.25)
        self.deleteEnterButton.hide()
        self.deleteEnterButton.setPos(-0.441, 0, -0.917)
        self.deleteEnterButton.setScale(0.75)
        self.deleteExitButton.show()
        self.deleteExitButton.setPos(-0.441, 0, -0.917)
        self.deleteExitButton.setScale(0.75)
        self.deleteExitButton['command'] = self.setActivateMode
        self.deleteExitButton['extraArgs'] = [
            self.previousActivateMode]
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        if self.numItem(track, level) <= 0:
                            self.makeUnpressable(button)
                        else:
                            self.makeDeletePressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def purchaseDeleteDeactivateButtons(self):
        self.invFrame.reparentTo(self)
        self.purchaseFrame.hide()
        self.deleteDeactivateButtons()
        return None

    
    def deleteActivateButtons(self):
        self.reparentTo(guiTop)
        self.setPos(0, 0, 0)
        self.setScale(1)
        self.deleteEnterButton.hide()
        self.deleteExitButton.show()
        self.deleteExitButton['command'] = self.setActivateMode
        self.deleteExitButton['extraArgs'] = [
            self.previousActivateMode]
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        if self.numItem(track, level) <= 0:
                            self.makeUnpressable(button)
                        else:
                            self.makePressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def deleteDeactivateButtons(self):
        self.deleteExitButton['command'] = None
        return None

    
    def purchaseActivateButtons(self):
        self.reparentTo(guiTop)
        self.setPos(0, 0, -0.04)
        self.setScale(1)
        if self.purchaseFrame == None:
            self.loadPurchaseFrame()
        
        self.purchaseFrame.show()
        self.invFrame.reparentTo(self.purchaseFrame)
        self.invFrame.setPos(-0.23, 0, 0.50756)
        self.invFrame.setScale(0.793894)
        self.detailFrame.setPos(1.08, 0, 0)
        self.detailFrame.setScale(1.25)
        totalProps = self.totalProps
        maxProps = self.getMaxTotalProps()
        self.deleteEnterButton.show()
        self.deleteEnterButton.setPos(-0.441, 0, -0.917)
        self.deleteEnterButton.setScale(0.75)
        self.deleteExitButton.hide()
        self.deleteExitButton.setPos(-0.441, 0, -0.917)
        self.deleteExitButton.setScale(0.75)
        self.deleteEnterButton['command'] = self.setActivateMode
        self.deleteEnterButton['extraArgs'] = [
            'purchaseDelete']
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        if self.numItem(track, level) >= self.getMax(track, level) or totalProps == maxProps:
                            self.makeUnpressable(button)
                        else:
                            self.makePressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def purchaseDeactivateButtons(self):
        self.invFrame.reparentTo(self)
        self.purchaseFrame.hide()
        return None

    
    def brokeActivateButtons(self):
        self.reparentTo(guiTop)
        self.setPos(0, 0, -0.04)
        self.setScale(1)
        if self.purchaseFrame == None:
            self.loadPurchaseFrame()
        
        self.purchaseFrame.show()
        self.invFrame.reparentTo(self.purchaseFrame)
        self.invFrame.setPos(-0.23, 0, 0.50756)
        self.invFrame.setScale(0.793894)
        self.detailFrame.setPos(1.08, 0, 0)
        self.detailFrame.setScale(1.25)
        self.deleteEnterButton.show()
        self.deleteEnterButton.setPos(-0.441, 0, -0.917)
        self.deleteEnterButton.setScale(0.75)
        self.deleteExitButton.hide()
        self.deleteExitButton.setPos(-0.441, 0, -0.917)
        self.deleteExitButton.setScale(0.75)
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        self.makeUnpressable(button)
                    else:
                        button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def brokeDeactivateButtons(self):
        self.invFrame.reparentTo(self)
        self.purchaseFrame.hide()
        return None

    
    def battleActivateButtons(self):
        self.reparentTo(guiTop)
        self.setPos(0, 0, 0.02)
        self.setScale(1)
        if self.battleFrame == None:
            self.loadBattleFrame()
        
        self.battleFrame.show()
        self.invFrame.reparentTo(self.battleFrame)
        self.invFrame.setPos(-0.25, 0, 0.33)
        self.invFrame.setScale(1)
        self.detailFrame.setPos(1.05, 0, -0.08)
        self.detailFrame.setScale(1)
        self.deleteEnterButton.hide()
        self.deleteExitButton.hide()
        for track in range(len(Tracks)):
            if TrackZones[track] in self.toon.safeZonesVisited:
                self.showTrack(track)
                for level in range(len(Levels)):
                    button = self.buttons[track][level]
                    if self.itemIsUsable(track, level):
                        button.show()
                        if not self.numItem(track, level) <= 0:
                            if not track == HEAL_TRACK and not (self.heal):
                                if track == TRAP_TRACK and not (self.trap) and track == LURE_TRACK and not (self.lure):
                                    self.makeUnpressable(button)
                                else:
                                    self.makePressable(button)
                            else:
                                button.hide()
                
            else:
                self.hideTrack(track)
        
        return None

    
    def battleDeactivateButtons(self):
        self.invFrame.reparentTo(self)
        self.battleFrame.hide()
        return None

    
    def itemIsUsable(self, track, level):
        curSkill = self.toon.experience.getExp(track)
        if curSkill < Levels[level]:
            return 0
        else:
            return 1

    
    def getNextExpValue(self, track):
        curSkill = self.toon.experience.getExp(track)
        retVal = MaxSkill
        for amount in Levels:
            if curSkill < amount:
                retVal = amount
                return retVal
            
        
        return retVal

    
    def makePressable(self, button):
        button.configure(image0_image = self.upButton, image2_image = self.rolloverButton, text_color = self.PressableTextColor, geom_color = self.PressableGeomColor, image_color = self.PressableImageColor, commandButtons = (LMB,))
        return None

    
    def makeDeletePressable(self, button):
        button.configure(image0_image = self.upButton, image2_image = self.rolloverButton, text_color = self.PressableTextColor, geom_color = self.PressableGeomColor, image_color = self.DeletePressableImageColor, commandButtons = (LMB,))
        return None

    
    def makeUnpressable(self, button):
        button.configure(text_color = self.UnpressableTextColor, geom_color = self.UnpressableGeomColor, image_image = self.flatButton, image_color = self.UnpressableImageColor, commandButtons = ())
        return None

    
    def makeBookUnpressable(self, button):
        button.configure(text_color = self.BookUnpressableTextColor, geom_color = self.BookUnpressableGeomColor, image_image = self.flatButton, image0_color = self.BookUnpressableImage0Color, image2_color = self.BookUnpressableImage2Color, commandButtons = ())
        return None

    
    def hideTrack(self, trackIndex):
        self.trackNameLabels[trackIndex].show()
        self.trackScoreLabels[trackIndex].show()
        self.trackNextLabels[trackIndex].hide()
        for levelIndex in range(0, len(Levels)):
            self.buttons[trackIndex][levelIndex].hide()
        

    
    def showTrack(self, trackIndex):
        self.trackNameLabels[trackIndex].show()
        self.trackScoreLabels[trackIndex].show()
        nextLabel = self.trackNextLabels[trackIndex]
        nextLabel.show()
        for levelIndex in range(0, len(Levels)):
            self.buttons[trackIndex][levelIndex].show()
        
        expVal = self.getNextExpValue(trackIndex)
        if expVal == MaxSkill:
            nextLabel.hide()
        else:
            nextLabel['text'] = str(expVal)
            index = Levels.index(expVal)
            nextLabel.setPos(-0.31 + index * 0.193, 0, -0.02)
        return None

    
    def updateInvString(self, invString):
        InventoryBase.InventoryBase.updateInvString(self, invString)
        self.updateGUI()
        return None

    
    def updateButtonText(self, track, level):
        button = self.buttons[track][level]
        button['text'] = str(self.numItem(track, level))
        return None

    
    def updateGUI(self, track = None, level = None):
        self.updateTotalPropsText()
        if track == None and level == None:
            for track in range(len(Tracks)):
                expStr = str(toonbase.localToon.experience.getExp(track))
                self.trackScoreLabels[track]['text'] = expStr
                for level in range(0, len(Levels)):
                    self.updateButtonText(track, level)
                
            
        elif track != None and level != None:
            self.updateButtonText(track, level)
        else:
            self.notify.error('Invalid use of updateGUI')
        self._InventoryNew__activateButtons()
        return None

    
    def getSingleGroupStr(self, track, level):
        if track == HEAL_TRACK:
            obj = 'Toon'
        else:
            obj = 'Cog'
        if isGroup(track, level):
            adj = 'All'
            plural = 's'
        else:
            adj = 'One'
            plural = ''
        return 'Affects: ' + adj + ' ' + obj + plural

    
    def getToonupDmgStr(self, track, level):
        if track == HEAL_TRACK:
            return 'Toon-up'
        else:
            return 'Damage'

    
    def deleteItem(self, track, level):
        if self.numItem(track, level) > 0:
            self.useItem(track, level)
            self.updateGUI(track, level)
        
        return None

    
    def loadBattleFrame(self):
        self.battleModels = loader.loadModelOnce('phase_5/models/gui/battle_gui')
        self.battleFrame = DirectFrame(relief = None, text = 'BATTLE MENU', text_pos = (-0.13, 0.43), text_scale = 0.1, text_fg = (1, 1, 1, 1), image = self.battleModels.find('**/BATTLE_Menu'), parent = self)
        self.runButton = DirectButton(parent = self.battleFrame, relief = None, pos = (0.695, 0, -0.416), text = 'RUN', text_scale = 0.06, text_pos = (0, -0.02), text_fg = Vec4(1, 1, 1, 1), image = (self.upButton, self.downButton, self.rolloverButton), image_scale = 1.05, image_color = (0, 0.6, 1, 1), command = self._InventoryNew__handleRun)
        self.sosButton = DirectButton(parent = self.battleFrame, relief = None, pos = (0.9175, 0, -0.416), text = 'SOS', text_scale = 0.06, text_pos = (0, -0.02), text_fg = Vec4(1, 1, 1, 1), image = (self.upButton, self.downButton, self.rolloverButton), image_scale = 1.05, image_color = (0, 0.6, 1, 1), command = self._InventoryNew__handleSOS)
        self.passButton = DirectButton(parent = self.battleFrame, relief = None, pos = (0.901, 0, -0.257), text = 'PASS', text_scale = 0.06, text_pos = (0, -0.02), text_fg = Vec4(1, 1, 1, 1), image = (self.upButton, self.downButton, self.rolloverButton), image_scale = 1.05, image_color = (0, 0.6, 1, 1), command = self._InventoryNew__handlePass)
        self.battleFrame.hide()
        return None

    
    def loadPurchaseFrame(self):
        self.purchaseModels = loader.loadModelOnce('phase_4/models/gui/purchase_gui')
        self.purchaseFrame = DirectFrame(relief = None, image = self.purchaseModels.find('**/PurchasePanel'), parent = self)
        self.purchaseFrame.hide()
        return None

    
    def buttonLookup(self, track, level):
        return self.invModels[track][level]


