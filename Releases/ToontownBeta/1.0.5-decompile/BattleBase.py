# Source Generated with Decompyle++
# File: BattleBase.pyo (Python 2.0)

from PandaModules import *
from ToontownBattleGlobals import *
from Timer import *
import DirectNotifyGlobal
TOON_ID_COL = 0
TOON_TRACK_COL = 1
TOON_LVL_COL = 2
TOON_TGT_COL = 3
TOON_HP_COL = 4
TOON_ACCBONUS_COL = 5
TOON_HPBONUS_COL = 6
TOON_KBBONUS_COL = 7
SUIT_DIED_COL = 8
SUIT_ID_COL = 0
SUIT_ATK_COL = 1
SUIT_TGT_COL = 2
SUIT_HP_COL = 3
TOON_DIED_COL = 4
SUIT_BEFORE_TOONS_COL = 5
SUIT_TAUNT_COL = 6
NO_ID = -1
NO_ATTACK = -1
UN_ATTACK = -2
NO_TRAP = -1
LURE_SUCCEEDED = -1
SOS = 99
HEAL = Tracks.index('toon-up')
TRAP = Tracks.index('trap')
LURE = Tracks.index('lure')
SOUND = Tracks.index('sound')
THROW = Tracks.index('throw')
SQUIRT = Tracks.index('squirt')
DROP = Tracks.index('drop')
TOON_ATTACK_TIME = 12.0
SUIT_ATTACK_TIME = 12.0
TOON_TRAP_DELAY = 0.8
TOON_SOUND_DELAY = 1.0
TOON_THROW_DELAY = 0.5
TOON_THROW_SUIT_DELAY = 1.0
TOON_SQUIRT_DELAY = 0.5
TOON_SQUIRT_SUIT_DELAY = 1.0
TOON_DROP_DELAY = 0.8
TOON_DROP_SUIT_DELAY = 1.0

try:
    debugBattles = base.config.GetBool('debug-battles', 0)
    CLIENT_INPUT_TIMEOUT = base.config.GetFloat('battle-input-timeout', 20.0)
except:
    debugBattles = simbase.config.GetBool('debug-battles', 0)
    CLIENT_INPUT_TIMEOUT = simbase.config.GetFloat('battle-input-timeout', 20.0)


def levelAffectsGroup(level):
    return level % 2


def attackAffectsGroup(track, level):
    if track == HEAL and level % 2:
        return 1
    elif track == LURE and level % 2:
        return 1
    elif track == SOUND:
        return 1
    else:
        return 0


def getToonAttack(id, track = NO_ATTACK, level = -1, target = -1):
    return [
        id,
        track,
        level,
        target,
        [],
        0,
        0,
        [],
        0]


def getDefaultSuitAttacks():
    suitAttacks = [
        [
            NO_ID,
            NO_ATTACK,
            -1,
            [],
            0,
            0,
            0],
        [
            NO_ID,
            NO_ATTACK,
            -1,
            [],
            0,
            0,
            0],
        [
            NO_ID,
            NO_ATTACK,
            -1,
            [],
            0,
            0,
            0],
        [
            NO_ID,
            NO_ATTACK,
            -1,
            [],
            0,
            0,
            0]]
    return suitAttacks


def getDefaultSuitAttack():
    return [
        NO_ID,
        NO_ATTACK,
        -1,
        [],
        0,
        0,
        0]


def findToonAttack(toons, attacks, track):
    p = []
    for t in toons:
        if attacks.has_key(t):
            attack = attacks[t]
            if attack[TOON_TRACK_COL] == track:
                p.append(attack)
            
        
    
    
    def compFunc(a, b):
        if a[TOON_LVL_COL] > b[TOON_LVL_COL]:
            return 1
        elif a[TOON_LVL_COL] < b[TOON_LVL_COL]:
            return -1
        
        return 0

    p.sort(compFunc)
    return p


def estimateRewardTime(toons, expDict):
    rewardTime = 0
    for t in toons:
        if expDict.has_key(t):
            expMat = expDict[t]
            for i in range(7):
                rewardTime += 1.5
                for j in range(6):
                    for k in range(expMat[i][j]):
                        rewardTime += 0.25
                    
                
            
        
    
    return rewardTime

SERVER_BUFFER_TIME = 2.0
SERVER_INPUT_TIMEOUT = CLIENT_INPUT_TIMEOUT + SERVER_BUFFER_TIME
MAX_JOIN_T = 20.0
FACEOFF_TAUNT_T = 3.5
ELEVATOR_T = 4.0
BATTLE_SMALL_VALUE = 1e-007

class BattleBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('BattleBase')
    srow = [
        [
            Point3(0, 5, 0)],
        [
            Point3(2, 5.3, 0),
            Point3(-2, 5.3, 0)],
        [
            Point3(4, 5.2, 0),
            Point3(0, 6, 0),
            Point3(-4, 5.2, 0)],
        [
            Point3(6, 4.4, 0),
            Point3(2, 6.3, 0),
            Point3(-2, 6.3, 0),
            Point3(-6, 4.4, 0)],
        [
            Point3(-4, 8.2, 0),
            Point3(0, 9, 0),
            Point3(4, 8.2, 0)]]
    srowHpr = [
        [
            Vec3(179, 0, 0)],
        [
            Vec3(170, 0, 0),
            Vec3(180, 0, 0)],
        [
            Vec3(170, 0, 0),
            Vec3(179, 0, 0),
            Vec3(190, 0, 0)],
        [
            Vec3(160, 0, 0),
            Vec3(170, 0, 0),
            Vec3(190, 0, 0),
            Vec3(200, 0, 0)],
        [
            Vec3(190, 0, 0),
            Vec3(179, 0, 0),
            Vec3(170, 0, 0)]]
    trow = [
        [
            Point3(0, -6, 0)],
        [
            Point3(1.5, -6.5, 0),
            Point3(-1.5, -6.5, 0)],
        [
            Point3(3, -6.75, 0),
            Point3(0, -7, 0),
            Point3(-3, -6.75, 0)],
        [
            Point3(4.5, -7, 0),
            Point3(1.5, -7.5, 0),
            Point3(-1.5, -7.5, 0),
            Point3(-4.5, -7, 0)],
        [
            Point3(-3, -8, 0),
            Point3(0, -9, 0),
            Point3(3, -8, 0)]]
    trowHpr = [
        [
            Vec3(0, 0, 0)],
        [
            Vec3(5, 0, 0),
            Vec3(-5, 0, 0)],
        [
            Vec3(5, 0, 0),
            Vec3(0, 0, 0),
            Vec3(-5, 0, 0)],
        [
            Vec3(10, 0, 0),
            Vec3(5, 0, 0),
            Vec3(-5, 0, 0),
            Vec3(-10, 0, 0)],
        [
            Vec3(-5, 0, 0),
            Vec3(0, 0, 0),
            Vec3(5, 0, 0)]]
    posA = Point3(0, 10, 0)
    posB = Point3(-7.071, 7.071, 0)
    posC = Point3(-10, 0, 0)
    posD = Point3(-7.071, -7.071, 0)
    posE = Point3(0, -10, 0)
    posF = Point3(7.071, -7.071, 0)
    posG = Point3(10, 0, 0)
    posH = Point3(7.071, 7.071, 0)
    allPoints = (posA, posB, posC, posD, posE, posF, posG, posH)
    toonCwise = [
        posA,
        posB,
        posC,
        posD,
        posE]
    toonCCwise = [
        posH,
        posG,
        posF,
        posE]
    suitCwise = [
        posE,
        posF,
        posG,
        posH,
        posA]
    suitCCwise = [
        posD,
        posC,
        posB,
        posA]
    suitSpeed = 4.8
    toonSpeed = 8.0
    
    def __init__(self):
        self.initialSuitPos = Point3(0, 0, 0)
        self.timer = Timer()
        self.resetLists()

    
    def resetLists(self):
        self.suits = []
        self.pendingSuits = []
        self.joiningSuits = []
        self.activeSuits = []
        self.luredSuits = []
        self.suitGone = 0
        self.toons = []
        self.joiningToons = []
        self.pendingToons = []
        self.activeToons = []
        self.runningToons = []
        self.toonGone = 0

    
    def calcFaceoffTime(self, centerpos, suitpos):
        hpr = Vec3(centerpos - suitpos)
        hpr.normalize()
        suitdest = Point3(centerpos - Point3(hpr * 6.0))
        dist = Vec3(suitdest - suitpos).length()
        return dist / BattleBase.suitSpeed

    
    def calcSuitMoveTime(self, pos0, pos1):
        dist = Vec3(pos0 - pos1).length()
        return dist / BattleBase.suitSpeed

    
    def calcToonMoveTime(self, pos0, pos1):
        dist = Vec3(pos0 - pos1).length()
        return dist / BattleBase.toonSpeed

    
    def buildJoinPointList(self, avPos, destPos, toon = 0):
        minDist = 999999.0
        nearestP = None
        for p in BattleBase.allPoints:
            dist = Vec3(avPos - p).length()
            if dist < minDist:
                nearestP = p
                minDist = dist
            
        
        self.notify.debug('buildJoinPointList() - avp: %s nearp: %s' % (avPos, nearestP))
        dist = Vec3(avPos - destPos).length()
        if dist < minDist:
            self.notify.debug('buildJoinPointList() - destPos is nearest')
            return []
        
        if toon == 1:
            if nearestP == BattleBase.posE:
                self.notify.debug('buildJoinPointList() - posE')
                plist = [
                    BattleBase.posE]
            elif BattleBase.toonCwise.count(nearestP) == 1:
                self.notify.debug('buildJoinPointList() - clockwise')
                index = BattleBase.toonCwise.index(nearestP)
                plist = BattleBase.toonCwise[index + 1:]
            else:
                self.notify.debug('buildJoinPointList() - counter-clockwise')
                index = BattleBase.toonCCwise.index(nearestP)
                plist = BattleBase.toonCCwise[index + 1:]
        elif nearestP == BattleBase.posA:
            self.notify.debug('buildJoinPointList() - posA')
            plist = [
                BattleBase.posA]
        elif BattleBase.suitCwise.count(nearestP) == 1:
            self.notify.debug('buildJoinPointList() - clockwise')
            index = BattleBase.suitCwise.index(nearestP)
            plist = BattleBase.suitCwise[index + 1:]
        else:
            self.notify.debug('buildJoinPointList() - counter-clockwise')
            index = BattleBase.suitCCwise.index(nearestP)
            plist = BattleBase.suitCCwise[index + 1:]
        self.notify.debug('buildJoinPointList() - plist: %s' % plist)
        return plist


