# Source Generated with Decompyle++
# File: ShtikerBook.pyo (Python 2.0)

from ShowBaseGlobal import *
import ToontownGlobals
import PandaObject
import StateData
import GuiGlobals
import OnscreenPanel
from DirectGui import *

class ShtikerBook(DirectFrame, StateData.StateData):
    
    def __init__(self, doneEvent):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(ShtikerBook)
        StateData.StateData.__init__(self, doneEvent)
        self.pages = []
        self.currPageIndex = None
        self.openSound = None
        self.pageSound = None
        self.hide()

    
    def enter(self):
        base.disableMouse()
        base.render.stash()
        self.oldBgColor = base.win.getGsg().getColorClearValue()
        base.win.getGsg().setColorClearValue(Vec4(0.05, 0.15, 0.4, 1))
        self.oldMin2dAlpha = NametagGlobals.getMin2dAlpha()
        self.oldMax2dAlpha = NametagGlobals.getMax2dAlpha()
        NametagGlobals.setMin2dAlpha(0.8)
        NametagGlobals.setMax2dAlpha(1.0)
        self.bookOpenButton.hide()
        self.bookCloseButton.show()
        self.show()
        self.nextArrow.show()
        self.prevArrow.show()
        self.accept('shtiker-page-done', self._ShtikerBook__pageDone)
        self.accept(ToontownGlobals.StickerBookHotkey, self._ShtikerBook__close)
        self.pages[self.currPageIndex].enter()
        self.accept('right', self._ShtikerBook__pageChange, [
            1])
        self.accept('left', self._ShtikerBook__pageChange, [
            -1])

    
    def exit(self):
        self.pages[self.currPageIndex].exit()
        base.render.unstash()
        base.win.getGsg().setColorClearValue(self.oldBgColor)
        NametagGlobals.setMin2dAlpha(self.oldMin2dAlpha)
        NametagGlobals.setMax2dAlpha(self.oldMax2dAlpha)
        self.hide()
        self.hideButton()
        OnscreenPanel.cleanupPanel('globalDialog')
        self.ignore('shtiker-page-done')
        self.ignore(ToontownGlobals.StickerBookHotkey)
        self.ignore('right')
        self.ignore('left')

    
    def load(self):
        self.bookModel = loader.loadModel('phase_4/models/gui/stickerbook_gui')
        self['image'] = self.bookModel.find('**/big_book')
        self['image_scale'] = (2, 1, 1.5)
        self.resetFrameSize()
        self.bookOpenButton = DirectButton(image = (self.bookModel.find('**/BookIcon_CLSD'), self.bookModel.find('**/BookIcon_OPEN'), self.bookModel.find('**/BookIcon_RLVR')), relief = None, pos = (1.175, 0, -0.854167), scale = 0.305, command = self._ShtikerBook__open)
        self.bookCloseButton = DirectButton(image = (self.bookModel.find('**/BookIcon_OPEN'), self.bookModel.find('**/BookIcon_CLSD'), self.bookModel.find('**/BookIcon_RLVR2')), relief = None, pos = (1.175, 0, -0.854167), scale = 0.305, command = self._ShtikerBook__close)
        self.bookOpenButton.hide()
        self.bookCloseButton.hide()
        self.nextArrow = DirectButton(parent = self, relief = None, image = (self.bookModel.find('**/arrow_button'), self.bookModel.find('**/arrow_down'), self.bookModel.find('**/arrow_rollover')), scale = (0.1, 0.1, 0.1), pos = (0.838, 0, -0.661), command = self._ShtikerBook__pageChange, extraArgs = [
            1])
        self.prevArrow = DirectButton(parent = self, relief = None, image = (self.bookModel.find('**/arrow_button'), self.bookModel.find('**/arrow_down'), self.bookModel.find('**/arrow_rollover')), scale = (-0.1, 0.1, 0.1), pos = (-0.838, 0, -0.661), command = self._ShtikerBook__pageChange, extraArgs = [
            -1])
        self.openSound = base.loadSfx('phase_4/audio/sfx/GUI_stickerbook_open.mp3')
        self.pageSound = base.loadSfx('phase_4/audio/sfx/GUI_stickerbook_turn.mp3')

    
    def unload(self):
        loader.unloadModel('phase_4/models/gui/stickerbook_gui')
        self.bookModel.removeNode()
        del self.bookModel
        self.destroy()
        self.bookOpenButton.destroy()
        del self.bookOpenButton
        self.bookCloseButton.destroy()
        del self.bookCloseButton
        del self.nextArrow
        del self.prevArrow
        for page in self.pages:
            page.unload()
        
        del self.pages
        base.unloadSfx(self.openSound)
        del self.openSound
        base.unloadSfx(self.pageSound)
        del self.pageSound
        return None

    
    def addPage(self, page):
        self.pages.append(page)
        page.setBook(self)
        page.reparentTo(self)
        return None

    
    def setPage(self, page):
        if self.currPageIndex is not None:
            self.pages[self.currPageIndex].exit()
        
        self.currPageIndex = self.pages.index(page)
        page.enter()

    
    def showButton(self):
        self.bookOpenButton.show()
        self.bookCloseButton.hide()

    
    def hideButton(self):
        self.bookOpenButton.hide()
        self.bookCloseButton.hide()

    
    def __open(self):
        base.playSfx(self.openSound)
        messenger.send('enterStickerBook')

    
    def __close(self):
        self.pages[self.currPageIndex].exit()
        self.doneStatus = {
            'mode': 'close' }
        messenger.send(self.doneEvent)

    
    def __pageDone(self):
        page = self.pages[self.currPageIndex]
        pageDoneStatus = page.getDoneStatus()
        if pageDoneStatus['mode'] == 'teleport':
            self.doneStatus = {
                'mode': 'teleport',
                'hood': pageDoneStatus['hood'] }
            messenger.send(self.doneEvent)
            return None
        elif pageDoneStatus['mode'] == 'close':
            self._ShtikerBook__close()
            return None
        
        if pageDoneStatus['mode'] == 'exit':
            self.doneStatus = {
                'mode': 'exit' }
            messenger.send(self.doneEvent)
            return None
        
        return None

    
    def __pageChange(self, offset):
        base.playSfx(self.pageSound)
        self.pages[self.currPageIndex].exit()
        self.currPageIndex = self.currPageIndex + offset
        self.currPageIndex = max(self.currPageIndex, 0)
        self.currPageIndex = min(self.currPageIndex, len(self.pages) - 1)
        if self.currPageIndex == 0:
            self.prevArrow.hide()
        elif self.currPageIndex == len(self.pages) - 1:
            self.nextArrow.hide()
        else:
            self.prevArrow.show()
            self.nextArrow.show()
        self.pages[self.currPageIndex].enter()
        return None


