# Source Generated with Decompyle++
# File: Quests.pyo (Python 2.0)

import ToontownBattleGlobals
import ToontownGlobals
import SuitBattleGlobals
import whrandom

class Quest:
    
    def __init__(self, id, quest):
        self.id = id
        self.quest = quest

    
    def getId(self):
        return self.id

    
    def getType(self):
        return self.quest[0]

    
    def __repr__(self):
        return 'Quest type: %s id: %s params: %s' % (self.__class__.__name__, self.id, self.quest[1:])



class CogQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCogType(self):
        return self.quest[2]

    
    def getNumCogs(self):
        return self.quest[1]

    
    def getString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            cogName = SuitBattleGlobals.SuitAttributes[self.getCogType()]['name']
        else:
            cogName = SuitBattleGlobals.SuitAttributes[self.getCogType()]['pluralname']
        return 'Defeat %s %s' % (numCogs, cogName)



class CogTrackQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCogTrack(self):
        return self.quest[2]

    
    def getNumCogs(self):
        return self.quest[1]

    
    def getString(self):
        numCogs = self.getNumCogs()
        cogTrack = self.getCogTrack()
        if numCogs == 1:
            cogText = 'Cog'
        else:
            cogText = 'Cogs'
        return 'Defeat %s %s %s' % (numCogs, cogTrack, cogText)



class CogLevelQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getCogLevel(self):
        return self.quest[2]

    
    def getNumCogs(self):
        return self.quest[1]

    
    def getString(self):
        numCogs = self.getNumCogs()
        cogLevel = self.getCogLevel()
        if numCogs == 1:
            cogText = 'Cog'
        else:
            cogText = 'Cogs'
        return 'Defeat %s Level %s %s' % (numCogs, cogLevel, cogText)



class BuildingQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getBuildingType(self):
        return self.quest[2]

    
    def getNumBuildings(self):
        return self.quest[1]

    
    def getString(self):
        num = self.getNumBuildings()
        if num == 1:
            buildingText = 'Building'
        else:
            buildingText = 'Buildings'
        return 'Defeat %s %s %s' % (num, self.getBuildingType(), buildingText)



class DeliveryQuest(Quest):
    
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    
    def getGagType(self):
        return (self.quest[2], self.quest[3])

    
    def getNumGags(self):
        return self.quest[1]

    
    def getString(self):
        (track, item) = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            gagName = ToontownBattleGlobals.AvPropStrings[track][item]
        else:
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
        return 'Deliver %s %s' % (num, gagName)


QuestDict = {
    1001: (CogQuest, 1, 'f'),
    1002: (CogQuest, 1, 'p'),
    1003: (CogQuest, 2, 'f'),
    1004: (CogQuest, 2, 'p'),
    1005: (CogQuest, 3, 'f'),
    1006: (CogQuest, 3, 'p'),
    1007: (CogQuest, 4, 'f'),
    1008: (CogQuest, 4, 'p'),
    1009: (CogQuest, 5, 'f'),
    1010: (CogQuest, 5, 'p'),
    1020: (CogLevelQuest, 1, 1),
    1021: (CogLevelQuest, 2, 1),
    1022: (CogLevelQuest, 3, 1),
    1023: (CogLevelQuest, 1, 2),
    1024: (CogLevelQuest, 2, 2),
    1025: (CogLevelQuest, 3, 2),
    1026: (CogLevelQuest, 1, 3),
    1027: (CogLevelQuest, 2, 3),
    1028: (CogLevelQuest, 3, 3),
    1029: (CogLevelQuest, 4, 3),
    2001: (BuildingQuest, 1, 'Legal'),
    3001: (DeliveryQuest, 1, ToontownBattleGlobals.THROW_TRACK, 0),
    3002: (DeliveryQuest, 1, ToontownBattleGlobals.SQUIRT_TRACK, 0) }
QuestTierDict = {
    1: {
        1: (1001, 1002, 1020, 1021),
        2: (1003, 1004, 1022, 1023, 1024, 1026, 1027),
        3: (1005, 1025, 1028, 1029) },
    2: {
        1: (1006, 1007),
        2: (1008, 1009),
        3: (1010,) } }

def getRandomQuestTierDiff(tier, diff):
    return whrandom.choice(QuestTierDict[tier][diff])


def getQuest(id):
    questDesc = QuestDict.get(id)
    if questDesc:
        questClass = questDesc[0]
        return questClass(id, questDesc)
    else:
        return None


class Reward:
    
    def __init__(self, id, reward):
        self.id = id
        self.reward = reward

    
    def getId(self):
        return self.id

    
    def getType(self):
        return self.reward[0]



class MaxHpReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[1]



class MaxCarryReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getAmount(self):
        return self.reward[1]



class TeleportReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getZone(self):
        return self.reward[1]



class TrackReward(Reward):
    
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    
    def getTrack(self):
        return self.reward[1]


RewardDict = {
    101: (MaxHpReward, 1),
    102: (MaxHpReward, 2),
    103: (MaxHpReward, 3),
    104: (MaxHpReward, 4),
    105: (MaxHpReward, 5),
    106: (MaxHpReward, 6),
    107: (MaxHpReward, 7),
    108: (MaxHpReward, 8),
    109: (MaxHpReward, 9),
    110: (MaxHpReward, 10),
    201: (MaxCarryReward, 1),
    202: (MaxCarryReward, 2),
    203: (MaxCarryReward, 3),
    204: (MaxCarryReward, 4),
    205: (MaxCarryReward, 5),
    206: (MaxCarryReward, 6),
    207: (MaxCarryReward, 7),
    208: (MaxCarryReward, 8),
    209: (MaxCarryReward, 9),
    210: (MaxCarryReward, 10),
    300: (TeleportReward, ToontownGlobals.ToontownCentral),
    301: (TeleportReward, ToontownGlobals.DonaldsDock),
    302: (TeleportReward, ToontownGlobals.TheBrrrgh),
    303: (TeleportReward, ToontownGlobals.MinniesMelodyland),
    304: (TeleportReward, ToontownGlobals.DaisyGardens),
    305: (TeleportReward, ToontownGlobals.ConstructionZone),
    306: (TeleportReward, ToontownGlobals.FunnyFarm),
    307: (TeleportReward, ToontownGlobals.GoofyStadium),
    308: (TeleportReward, ToontownGlobals.DonaldsDreamland),
    400: (TrackReward, ToontownBattleGlobals.HEAL_TRACK),
    401: (TrackReward, ToontownBattleGlobals.TRAP_TRACK),
    402: (TrackReward, ToontownBattleGlobals.LURE_TRACK),
    403: (TrackReward, ToontownBattleGlobals.SOUND_TRACK),
    404: (TrackReward, ToontownBattleGlobals.THROW_TRACK),
    405: (TrackReward, ToontownBattleGlobals.SQUIRT_TRACK),
    406: (TrackReward, ToontownBattleGlobals.DROP_TRACK) }

def getReward(id):
    reward = RewardDict.get(id)
    if reward:
        rewardClass = reward[0]
        return rewardClass(id, reward)
    else:
        return None

