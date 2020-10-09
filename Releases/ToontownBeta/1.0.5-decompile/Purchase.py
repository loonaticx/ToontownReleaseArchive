# Source Generated with Decompyle++
# File: Purchase.pyo (Python 2.0)

from ToontownBattleGlobals import *
import GuiGlobals
import ToonHead
import ToontownTimer
import ToontownGlobals
import StateData
from PurchaseManagerConstants import *
from DirectGui import *
import Task

class Purchase(StateData.StateData):
    
    def __init__(self, toon, points, ids, states, remain, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.oldBgColor = None
        self.points = points
        self.toon = toon
        self.ids = ids
        self.states = states
        self.remain = remain
        return None

    
    def load(self):
        self.purchaseModels = loader.loadModel('phase_4/models/gui/purchase_gui')
        self.frame = DirectFrame(relief = None)
        self.frame.hide()
        self.title = DirectLabel(parent = self.frame, relief = None, pos = (0.0, 0.0, 0.83), scale = 1.2, image = self.purchaseModels.find('**/Goofys_Sign'), text = "Goofy's Gag Shop", text_fg = (0.6, 0.2, 0, 1), text_scale = 0.11, text_pos = (0, -0.02, 0), text_font = ToontownGlobals.getSignFont())
        self.pointDisplay = DirectLabel(parent = self.frame, relief = None, pos = (-1.117, 0.0, 0.045), text = str(self.points), text_scale = 0.2, text_fg = (0, 0.1, 0.07, 1), text_shadow = (0, 0, 0, 1), text_pos = (0, 0, 0), image = self.purchaseModels.find('**/Jar'))
        self.playAgain = DirectButton(parent = self.frame, relief = None, scale = 1.04, pos = (0.64, 0, -0.231), image = (self.purchaseModels.find('**/PurchScrn_BTN_UP'), self.purchaseModels.find('**/PurchScrn_BTN_DN'), self.purchaseModels.find('**/PurchScrn_BTN_RLVR')), text = 'PLAY\nAGAIN', text_fg = (0, 0.1, 0.7, 1), text_scale = 0.05, text_pos = (0, 0.015, 0), command = self._Purchase__handlePlayAgain)
        self.backToPlayground = DirectButton(parent = self.frame, relief = None, scale = 1.04, pos = (0.64, 0, -0.01), image = (self.purchaseModels.find('**/PurchScrn_BTN_UP'), self.purchaseModels.find('**/PurchScrn_BTN_DN'), self.purchaseModels.find('**/PurchScrn_BTN_RLVR')), text = 'BACK TO\nPLAYGROUND', text_fg = (0, 0.1, 0.7, 1), text_scale = 0.05, text_pos = (0, 0.015, 0), command = self._Purchase__handleBackToPlayground)
        self.statusLabel = DirectLabel(parent = self.frame, relief = None, pos = (0, 0, 0.6), text = 'You have %s Jellybeans to spend' % self.points, text_scale = 0.1, text_pos = (0, 0, 0.563), text_fg = (0.9, 0.9, 0, 1))
        if self.points == 1:
            self.statusLabel['text'] = 'You have %s Jellybean to spend' % self.points
        
        self.timer = ToontownTimer.ToontownTimer()
        self.timer.reparentTo(self.frame)
        self.timer.posInTopRightCorner()
        numAvs = 0
        count = 0
        localToonIndex = 0
        for index in range(len(self.ids)):
            avId = self.ids[index]
            if avId == toonbase.localToon.doId:
                localToonIndex = index
            
            if self.states[index] != PURCHASE_NO_CLIENT_STATE and self.states[index] != PURCHASE_DISCONNECTED_STATE:
                numAvs = numAvs + 1
            
        
        layoutList = (None, (0,), (0, 2), (0, 1, 3), (0, 1, 2, 3))
        layout = layoutList[numAvs]
        headFramePosList = (Vec3(0.05, 0, -0.384), Vec3(0.05, 0, -0.776), Vec3(0.8, 0, -0.555), Vec3(-0.704, 0, -0.555))
        AVID_INDEX = 0
        LAYOUT_INDEX = 1
        TOON_INDEX = 2
        self.avInfoArray = [
            (toonbase.localToon.doId, headFramePosList[0], localToonIndex)]
        pos = 1
        for index in range(len(self.ids)):
            avId = self.ids[index]
            if self.states[index] != PURCHASE_NO_CLIENT_STATE and self.states[index] != PURCHASE_DISCONNECTED_STATE:
                av = toonbase.tcr.doId2do[avId]
                if av != toonbase.localToon:
                    self.avInfoArray.append((avId, headFramePosList[layout[pos]], index))
                    pos = pos + 1
                
            
        
        self.headFrames = []
        for avInfo in self.avInfoArray:
            av = toonbase.tcr.doId2do[avInfo[AVID_INDEX]]
            headFrame = PurchaseHeadFrame(av, self.purchaseModels)
            headFrame.setAvatarState(PURCHASE_WAITING_STATE)
            headFrame.setPos(avInfo[LAYOUT_INDEX])
            self.headFrames.append((avInfo[AVID_INDEX], headFrame))
        
        return None

    
    def unload(self):
        self.purchaseModels.removeNode()
        del self.purchaseModels
        for headFrame in self.headFrames:
            headFrame[1].reparentTo(hidden)
            headFrame[1].destroy()
        
        del self.headFrames
        self.frame.destroy()
        del self.frame
        del self.title
        del self.pointDisplay
        del self.playAgain
        del self.backToPlayground
        del self.timer
        return None

    
    def __handleSelection(self, track, level):
        self.handlePurchase(track, level)

    
    def handlePurchase(self, track, level):
        ret = self.toon.inventory.addItem(track, level)
        if ret == -2:
            text = 'Sorry, you have too many props'
        elif ret == -1:
            text = 'Sorry, you have enough %ss already' % AvPropStrings[track][level]
        elif ret == 0:
            text = 'You do not have enough skill for that yet'
        else:
            text = 'You purchased one %s' % AvPropStrings[track][level]
            self.toon.inventory.updateGUI(track, level)
            self.points -= 1
            self.pointDisplay['text'] = str(self.points)
            self.checkForBroke()
        self.showStatusText(text)
        return None

    
    def showStatusText(self, text):
        self.statusLabel['text'] = text
        taskMgr.removeTasksNamed('doLater-resetStatusText')
        taskMgr.removeTasksNamed('resetStatusText')
        taskMgr.doMethodLater(2.0, self.resetStatusText, 'resetStatusText')
        return None

    
    def resetStatusText(self, task):
        self.statusLabel['text'] = ''
        return Task.done

    
    def checkForBroke(self):
        if self.points == 0:
            self.toon.inventory.setActivateMode('broke')
            text = 'Sorry, you are all out of Jellybeans!'
            self.showStatusText(text)
        
        return None

    
    def __handleDone(self, playAgain):
        if playAgain:
            self.doneStatus = {
                'mode': 'minigame' }
        else:
            self.doneStatus = {
                'mode': 'safeZone' }
        messenger.send(self.doneEvent)

    
    def __handlePlayAgain(self):
        for headFrame in self.headFrames:
            headFrame[1].wrtReparentTo(guiTop)
        
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        taskMgr.removeTasksNamed('doLater-resetStatusText')
        taskMgr.removeTasksNamed('resetStatusText')
        self.statusLabel['text'] = 'Waiting for other players...'
        self.statusLabel.setPos(0, 0, 0.1)
        messenger.send('purchasePlayAgain')
        return None

    
    def __handleBackToPlayground(self):
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        messenger.send('purchaseBackToToontown')
        return None

    
    def __timerExpired(self):
        messenger.send('purchaseTimeout')
        return None

    
    def findHeadFrame(self, id):
        for headFrame in self.headFrames:
            if headFrame[0] == id:
                return headFrame[1]
            
        
        return None

    
    def __handleStateChange(self, playerStates):
        print playerStates
        self.states = playerStates
        for avInfo in self.avInfoArray:
            index = avInfo[2]
            headFrame = self.findHeadFrame(avInfo[0])
            state = self.states[index]
            headFrame.setAvatarState(state)
        

    
    def enter(self):
        self.frame.show()
        self.toon.inventory.show()
        self.toon.inventory.reparentTo(self.frame)
        self.toon.inventory.setActivateMode('purchase')
        self.playAgain.reparentTo(self.toon.inventory.purchaseFrame)
        self.backToPlayground.reparentTo(self.toon.inventory.purchaseFrame)
        for headFrame in self.headFrames:
            headFrame[1].reparentTo(self.toon.inventory.purchaseFrame)
        
        self.checkForBroke()
        self.oldBgColor = base.win.getGsg().getColorClearValue()
        base.win.getGsg().setColorClearValue(Vec4(0.05, 0.14, 0.4, 1))
        self.acceptOnce('purchaseOver', self._Purchase__handleDone)
        self.accept('purchaseStateChange', self._Purchase__handleStateChange)
        self.accept('inventory-selection', self._Purchase__handleSelection)
        self.timer.countdown(self.remain, self._Purchase__timerExpired)
        return None

    
    def exit(self):
        self.frame.hide()
        self.playAgain.reparentTo(self.frame)
        self.backToPlayground.reparentTo(self.frame)
        self.toon.inventory.reparentTo(hidden)
        self.toon.inventory.hide()
        self.ignore('purchaseOver')
        self.ignore('purchaseStateChange')
        self.ignore('inventory-selection')
        taskMgr.removeTasksNamed('doLater-resetStatusText')
        taskMgr.removeTasksNamed('resetStatusText')
        base.win.getGsg().setColorClearValue(self.oldBgColor)
        return None



class PurchaseHeadFrame(DirectFrame):
    
    def __init__(self, av, purchaseModels):
        DirectFrame.__init__(self, relief = None, image = purchaseModels.find('**/Char_Pnl'))
        self.initialiseoptions(PurchaseHeadFrame)
        self.statusLabel = DirectLabel(parent = self, relief = None, text = '', text_scale = 0.08, text_fg = (0.6, 0.3, 0.0, 1), text_pos = (0.1, 0, 0))
        self.av = av
        self.head = self.stateNodePath[0].attachNewNode('head', 20)
        self.head.setPosHprScale(-0.22, 10.0, -0.05, 180.0, 0.0, 0.0, 0.1, 0.1, 0.1)
        self.headModel = ToonHead.ToonHead()
        self.headModel.setupHead(self.av.style, forGui = 1)
        self.headModel.reparentTo(self.head)
        self.tagNode = NametagFloat2d()
        self.tagNode.setContents(Nametag.CSpeech | Nametag.CThought)
        self.av.nametag.addNametag(self.tagNode)
        self.tag = self.attachNewNode(self.tagNode.upcastToNamedNode())
        self.tag.setPosHprScale(-0.15, 0, -0.1, 0, 0, 0, 0.046, 0.046, 0.046)

    
    def destroy(self):
        DirectFrame.destroy(self)
        del self.statusLabel
        self.headModel.delete()
        del self.headModel
        self.head.removeNode()
        del self.head
        self.tag.removeNode()
        del self.tag
        del self.tagNode
        del self.av

    
    def setAvatarState(self, state):
        if state == PURCHASE_DISCONNECTED_STATE:
            self.statusLabel['text'] = '%s has\ndisconnected' % self.av.getName()
            self.statusLabel['text_pos'] = (0, 0.04, 0)
            self.head.hide()
            self.tag.hide()
        elif state == PURCHASE_EXIT_STATE:
            self.statusLabel['text'] = '%s has\nexited' % self.av.getName()
            self.statusLabel['text_pos'] = (0, 0.04, 0)
            self.head.hide()
            self.tag.hide()
        elif state == PURCHASE_PLAYAGAIN_STATE:
            self.statusLabel['text'] = 'Play Again'
            self.statusLabel['text_pos'] = (0.14, -0.12, 0)
        elif state == PURCHASE_WAITING_STATE:
            self.statusLabel['text'] = 'Buying'
            self.statusLabel['text_pos'] = (0.14, -0.12, 0)
        else:
            raise StandardError


