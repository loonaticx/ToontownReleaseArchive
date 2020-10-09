# Source Generated with Decompyle++
# File: QuestManagerAI.pyo (Python 2.0)

from AIBaseGlobal import *
import Task
import DirectNotifyGlobal
import Quests
import NPCToons
import whrandom

class QuestManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('QuestManagerAI')
    notify.setDebug(1)
    
    def __init__(self, air):
        self.air = air

    
    def requestInteract(self, avId, npc):
        self.notify.debug('requestInteract: avId: %s npcId: %s' % (avId, npc.getNpcId()))
        av = self.air.doId2do[avId]
        if npc.isBusy():
            self.rejectAvatar(av, npc)
        else:
            questId = self.hasQuest(av, npc)
            if questId >= 0:
                if self.isQuestComplete(av, npc, questId):
                    self.completeQuest(av, npc, questId)
                else:
                    self.incompleteQuest(av, npc, questId)
            elif self.needsQuest(av):
                self.assignQuest(av, npc)
            else:
                self.rejectAvatar(av, npc)

    
    def rejectAvatar(self, av, npc):
        self.notify.debug('rejecting avatar: avId: %s' % av.getDoId())
        npc.rejectAvatar(av.getDoId())
        return None

    
    def hasQuest(self, av, npc):
        quests = av.getQuests()
        for quest in quests:
            questId = quest[0]
            npcId = quest[1]
            toNpcId = quest[2]
            if npcId == npc.getNpcId() or toNpcId == npc.getNpcId():
                self.notify.debug('hasQuest: found quest: %s avId: %s npcId: %s toNpcId %s' % (questId, av.getDoId(), npcId, toNpcId))
                return questId
            
        
        self.notify.debug('hasQuest: did not find quest for avId: %s npcId: %s' % (av.getDoId(), npc.getNpcId()))
        return -1

    
    def isQuestComplete(self, av, npc, questId):
        quest = Quests.getQuest(questId)
        avQuest = av.getQuest(questId)
        self.notify.debug('isQuestComplete: avId: %s quest: %s avQuest: %s' % (av.getDoId(), quest, avQuest))
        if quest.getType() == Quests.DeliveryQuest:
            toNpcId = avQuest[2]
            gag = quest.getGagType()
            num = quest.getNumGags()
            if toNpcId == npc.getNpcId() and av.getInventory().numItem(gag[0], gag[1]) >= num:
                return 1
            else:
                return 0
        elif quest.getType() == Quests.CogQuest:
            num = quest.getNumCogs()
            progress = avQuest[4]
            if progress >= num:
                return 1
            else:
                return 0
        elif quest.getType() == Quests.BuildingQuest:
            num = quest.getNumBuildings()
            progress = avQuest[4]
            if progress >= num:
                return 1
            else:
                return 0
        else:
            self.notify.error('Quest type unknown')
            return 0

    
    def completeQuest(self, av, npc, questId):
        self.notify.debug('compelteQuest: avId: %s questId: %s' % (av.getDoId(), questId))
        if not av.removeQuest(questId):
            self.notify.error('completeQuest: could not remove quest from av')
        
        npc.completeQuest(av.getDoId(), questId)
        return None

    
    def incompleteQuest(self, av, npc, questId):
        self.notify.debug('incompleteQuest: avId: %s questId: %s' % (av.getDoId(), questId))
        npc.incompleteQuest(av.getDoId(), questId)
        return None

    
    def needsQuest(self, av):
        quests = av.getQuests()
        if len(quests) > 2:
            self.notify.debug('needsQuest: avId: %s already has %s quest(s)' % (av.getDoId(), len(quests)))
            return 0
        else:
            self.notify.debug('needsQuest: avId: %s only has %s quest(s), needs one' % (av.getDoId(), len(quests)))
            return 1

    
    def chooseQuest(self, av):
        return Quests.getRandomQuestTierDiff(1, 1)

    
    def chooseReward(self, av, quest):
        return Quests.getReward(100)

    
    def assignQuest(self, av, npc):
        quests = av.getQuests()
        self.notify.debug('assignQuest: avId: %s oldQuests: %s' % (av.getDoId(), quests))
        quest = self.chooseQuest(av)
        if quest.getType() == Quests.DeliveryQuest:
            toNpcId = NPCToons.getNPCInSameHood(npc.getNpcId())
        else:
            toNpcId = 0
        reward = self.chooseReward(av, quest)
        initialProgress = 0
        av.addQuest((quest.getId(), npc.getNpcId(), toNpcId, reward.getId(), initialProgress))
        av.b_setQuests(quests)
        npc.assignQuest(av.getDoId(), quest, toNpcId)
        return None

    
    def toonKilledCogs(self, av, cogList):
        avQuests = av.getQuests()
        changed = 0
        for questDesc in avQuests:
            quest = Quests.getQuest(questDesc[0])
            if quest.getType() == Quests.CogQuest:
                questCogType = quest.getCogType()
                for cogType in cogList:
                    if questCogType == cogType:
                        questDesc[4] += 1
                        changed = 1
                    
                
            
        
        if changed:
            av.b_setQuests(avQuests)
        
        return None


