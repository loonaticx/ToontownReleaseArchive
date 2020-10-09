# Source Generated with Decompyle++
# File: QuestPage.pyo (Python 2.0)

from ShowBaseGlobal import *
import GuiGlobals
import ShtikerPage
from DirectGui import *
import Quests
import NPCToons

class QuestPage(ShtikerPage.ShtikerPage):
    
    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.quests = { }
        self.textRolloverColor = Vec4(1, 1, 0, 1)
        self.textDownColor = Vec4(0.5, 0.9, 1, 1)
        self.textDisabledColor = Vec4(0.4, 0.8, 0.4, 1)

    
    def load(self):
        self.title = DirectLabel(parent = self, relief = None, text = 'Quests', text_scale = 0.12, pos = (0, 0, 0.6))
        self.gui = loader.loadModel('phase_4/models/gui/friendslist_gui')
        self.scrollList = DirectScrolledList(parent = self, relief = None, pos = (-0.58, 0, 0), incButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), incButton_relief = None, incButton_scale = (1.3, 1.3, -1.3), incButton_pos = (0.1, 0, -0.51), incButton_image3_color = Vec4(1, 1, 1, 0.2), decButton_image = (self.gui.find('**/FndsLst_ScrollUp'), self.gui.find('**/FndsLst_ScrollDN'), self.gui.find('**/FndsLst_ScrollUp_Rllvr'), self.gui.find('**/FndsLst_ScrollUp')), decButton_relief = None, decButton_scale = (1.3, 1.3, 1.3), decButton_pos = (0.1, 0, 0.51), decButton_image3_color = Vec4(1, 1, 1, 0.2), itemFrame_pos = (-0.237, 0, 0.361), itemFrame_scale = 1.0, itemFrame_relief = SUNKEN, itemFrame_frameSize = (-0.05, 0.79, -0.83, 0.1), itemFrame_frameColor = (0.85, 0.95, 1, 1), itemFrame_borderWidth = (0.01, 0.01), numItemsVisible = 10, items = [])

    
    def unload(self):
        del self.title
        del self.scrollList
        del self.quests
        ShtikerPage.ShtikerPage.unload(self)

    
    def makeQuestFrame(self, questDesc):
        (questId, npcId, toNpcId, rewardId, progress) = questDesc
        quest = Quests.getQuest(questId)
        questName = quest.getString()
        npcName = NPCToons.getNPCName(npcId)
        zone = toonbase.tcr.hoodMgr.getSafeZone(npcId)
        locationName = toonbase.tcr.hoodMgr.getFullnameFromId(zone)
        if quest.getType() == Quests.DeliveryQuest:
            toNpcName = NPCToons.getNPCName(toNpcId)
            fullString = '%s to %s\nGiven by: %s\nLocation: %s\nProgress: %s' % (questName, toNpcName, npcName, locationName, progress)
        else:
            fullString = '%s\nGiven by: %s\nLocation: %s\nProgress: %s' % (questName, npcName, locationName, progress)
        frame = DirectFrame(relief = RIDGE, frameSize = (-0.025, 0.77, -0.2, 0.07), frameColor = (0.7, 0.8, 0.9, 1), borderWidth = (0.01, 0.01), pad = (0.01, 0.01), text = fullString, text_scale = 0.05, text_align = TMALIGNLEFT)
        return frame

    
    def updateScrollList(self):
        newQuests = toonbase.localToon.getQuests()
        for questDesc in self.quests.keys():
            if questDesc not in newQuests:
                questFrame = self.quests[questDesc]
                self.scrollList.removeItem(questFrame)
                questFrame.destroy()
                del self.quests[questDesc]
            
        
        for questDesc in newQuests:
            if tuple(questDesc) not in self.quests.keys():
                questFrame = self.makeQuestFrame(tuple(questDesc))
                self.scrollList.addItem(questFrame)
                self.quests[tuple(questDesc)] = questFrame
            
        
        return None

    
    def enter(self):
        self.updateScrollList()
        ShtikerPage.ShtikerPage.enter(self)
        return None

    
    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        return None

    
    def choseQuest(self, questId):
        print 'choose quest', questId
        return None


