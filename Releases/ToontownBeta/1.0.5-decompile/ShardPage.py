# Source Generated with Decompyle++
# File: ShardPage.pyo (Python 2.0)

from ShowBaseGlobal import *
import GuiGlobals
import ShtikerPage
from DirectGui import *

class ShardPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.prevShard = -1
        self.shards = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)

    
    def load(self):
        self.title = DirectLabel(parent = self, relief = None, text = 'Districts', text_scale = 0.12, pos = (0, 0, 0.6))
        self.helpText = DirectLabel(parent = self, relief = None, text = 'Each District is a copy of the Toontown world.', text_scale = 0.08, text_wordwrap = 10, text_align = TMALIGNLEFT, pos = (0.058, 0, 0.303))
        self.youAreHereText = DirectLabel(parent = self, relief = None, text = 'You are currently in the "Sillyville" District', text_scale = 0.08, text_wordwrap = 10, text_align = TMALIGNLEFT, pos = (0.058, 0, 0.045))
        self.gui = loader.loadModel('phase_4/models/gui/friendslist_gui')
        self.scrollList = DirectScrolledList(parent = self, relief = None, pos = (-0.5, 0, 0), incButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.3, 1.3, -1.3), incButton_pos = (0, 0, -0.51), incButton_image3_color = Vec4(1, 1, 1, 0.2), decButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (1.3, 1.3, 1.3), decButton_pos = (0, 0, 0.51), decButton_image3_color = Vec4(1, 1, 1, 0.2), itemFrame_pos = (-0.237, 0, 0.361), itemFrame_scale = 1.0, itemFrame_relief = SUNKEN, itemFrame_frameSize = (-0.05, 0.55, -0.83, 0.1), itemFrame_frameColor = (0.85, 0.95, 1, 1), itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 10, items = [])

    
    def unload(self):
        del self.title
        del self.scrollList
        del self.shards
        ShtikerPage.ShtikerPage.unload(self)

    
    def makeShardButton(self, shardPair):
        (shardId, shardName) = shardPair
        return DirectButton(relief = None, text = shardName, text_scale = 0.08, text_align = TMALIGNLEFT, text1_bg = self.textDownColor, text2_bg = self.textRolloverColor, text3_fg = self.textDisabledColor, command = self.choseShard, extraArgs = [
            shardId])

    
    def updateScrollList(self):
        newShards = toonbase.tcr.listAvailableShards()
        for shardPair in self.shards.keys():
            if shardPair not in newShards:
                shardButton = self.shards[shardPair]
                self.scrollList.removeItem(shardButton)
                shardButton.destroy()
                del self.shards[shardPair]
            
        
        for shardPair in newShards:
            if shardPair not in self.shards.keys():
                shardButton = self.makeShardButton(shardPair)
                self.scrollList.addItem(shardButton)
                self.shards[shardPair] = shardButton
            
        
        currentShard = toonbase.localToon.defaultShard
        if self.prevShard != currentShard:
            for shardPair in self.shards.keys():
                (shardId, shardName) = shardPair
                if currentShard == shardId:
                    self.youAreHereText['text'] = 'You are currently in the "%s" District' % shardName
                    shardButton = self.shards[shardPair]
                    shardButton['state'] = DISABLED
                elif self.prevShard == shardId:
                    shardButton = self.shards[shardPair]
                    shardButton['state'] = NORMAL
                
            
            self.prevShard = currentShard
        
        return None

    
    def enter(self):
        self.updateScrollList()
        ShtikerPage.ShtikerPage.enter(self)
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        return None

    
    def choseShard(self, shardId):
        if shardId == toonbase.localToon.defaultShard:
            return None
        else:
            toonbase.tcr.gameFSM.request('waitOnEnterResponses', [
                shardId,
                toonbase.localToon.defaultZone,
                toonbase.localToon.defaultZone,
                -1])
        return None


