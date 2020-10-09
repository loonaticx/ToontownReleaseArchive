# Source Generated with Decompyle++
# File: Movie.pyo (Python 2.0)

from ToontownBattleGlobals import *
from BattleBase import *
from IntervalGlobal import *
import MovieSOS
import MovieHeal
import MovieTrap
import MovieLure
import MovieSound
import MovieThrow
import MovieSquirt
import MovieDrop
import MovieSuitAttacks
import MovieToonVictory
import PlayByPlayText
from SuitBattleGlobals import *
import DirectNotifyGlobal
import RewardPanel
import whrandom
import MovieUtil
camPos = Point3(14, 0, 10)
camHpr = Vec3(89, -30, 0)
randomBattleTimestamp = base.config.GetBool('random-battle-timestamp', 0)
debugIntervals = base.config.GetBool('debug-movie-intervals', 0)
globalMovieTrack = None

class Movie:
    notify = DirectNotifyGlobal.directNotify.newCategory('Movie')
    
    def __init__(self, battle):
        self.battle = battle
        self.track = None
        self.camTrack = None
        self.rewardPanel = None
        self.playByPlayText = PlayByPlayText.PlayByPlayText()
        self.playByPlayText.hide()
        self.hasBeenReset = 0
        self.reset()
        self.rewardHasBeenReset = 0
        self.resetReward()

    
    def cleanup(self):
        self.reset()
        self.resetReward()
        self.battle = None
        if self.playByPlayText != None:
            self.playByPlayText.cleanup()
        
        self.playByPlayText = None
        if self.rewardPanel != None:
            self.rewardPanel.cleanup()
        
        self.rewardPanel = None

    
    def needRestoreColor(self):
        self.restoreColor = 1

    
    def needRestoreHips(self):
        self.restoreHips = 1

    
    def needRestoreParticleEffect(self, effect):
        self.specialParticleEffects.append(effect)

    
    def clearRestoreParticleEffect(self, effect):
        if self.specialParticleEffects.count(effect) > 0:
            self.specialParticleEffects.remove(effect)
        

    
    def restore(self):
        for toon in self.battle.activeToons:
            toon.loop('neutral')
            (origPos, origHpr) = self.battle.getActorPosHpr(toon)
            toon.setPosHpr(self.battle, origPos, origHpr)
            hands = toon.getRightHands()
            hands += toon.getLeftHands()
            for hand in hands:
                props = hand.getChildrenAsList()
                for prop in props:
                    MovieUtil.removeProp(prop)
                
            
            if self.restoreColor == 1:
                headParts = toon.getHeadParts()
                torsoParts = toon.getTorsoParts()
                legsParts = toon.getLegsParts()
                partsList = [
                    headParts,
                    torsoParts,
                    legsParts]
                for parts in partsList:
                    for partNum in range(0, parts.getNumPaths()):
                        nextPart = parts.getPath(partNum)
                        nextPart.clearColorScale()
                        nextPart.clearTransparency()
                    
                
            
            if self.restoreHips == 1:
                parts = toon.getHipsParts()
                for partNum in range(0, parts.getNumPaths()):
                    nextPart = parts.getPath(partNum)
                    props = nextPart.getChildrenAsList()
                    for prop in props:
                        if prop.getName() == 'redtape-tube.egg':
                            MovieUtil.removeProp(prop)
                        
                    
                
            
        
        for suit in self.battle.activeSuits:
            suit.loop('neutral')
            (origPos, origHpr) = self.battle.getActorPosHpr(suit)
            suit.setPosHpr(self.battle, origPos, origHpr)
            hands = [
                suit.getRightHand(),
                suit.getLeftHand()]
            for hand in hands:
                props = hand.getChildrenAsList()
                for prop in props:
                    prop.reparentTo(hidden)
                
            
        
        for effect in self.specialParticleEffects:
            if effect != None:
                BattleParticles.cleanupParticleEffect(effect)
            
        
        self.specialParticleEffects = []

    
    def reset(self, finish = 0):
        if self.hasBeenReset == 1:
            self.notify.debug('reset() - movie was previously reset')
            return None
        
        self.hasBeenReset = 1
        if finish == 1 and self.track != None:
            self.restore()
            if self.battle.localToonPendingOrActive() and self.camTrack != None:
                self.camTrack.setFinalT()
            
        
        self.stop()
        self.track = None
        self.camTrack = None
        self.toonAttackDicts = []
        self.suitAttackDicts = []
        self.restoreColor = 0
        self.restoreHips = 0
        self.specialParticleEffects = []

    
    def resetReward(self, finish = 0):
        if self.rewardHasBeenReset == 1:
            self.notify.debug('resetReward() - movie was previously reset')
            return None
        
        self.rewardHasBeenReset = 1
        if finish == 1 and self.track != None:
            self.restore()
            if self.battle.localToonPendingOrActive() and self.camTrack != None:
                self.camTrack.setFinalT()
            
        
        self.stop()
        self.track = None
        self.camTrack = None
        self.toonRewardDicts = []
        if self.rewardPanel != None:
            self.rewardPanel.cleanup()
        
        self.rewardPanel = None

    
    def play(self, ts, callback):
        global globalMovieTrack
        self.hasBeenReset = 0
        plist = []
        camlist = []
        (tattacks, tcam) = self._Movie__doToonAttacks()
        if tattacks:
            plist.append(tattacks)
            camlist.append(tcam)
        
        (sattacks, scam) = self._Movie__doSuitAttacks()
        if sattacks:
            plist.append(sattacks)
            camlist.append(scam)
        
        plist.append(FunctionInterval(callback))
        self.track = Track(plist, name = 'movie-track-%d' % self.battle.doId)
        if debugIntervals == 1:
            globalMovieTrack = self.track
        
        self.camTrack = Track(camlist, name = 'movie-track-cam-%d' % self.battle.doId)
        dur = self.track.getDuration()
        if randomBattleTimestamp == 1:
            randNum = whrandom.randint(0, 99)
            ts = (float(randNum) / 100.0) * dur
            self.notify.debug('play() - random timestamp: %f' % ts)
        
        if ts <= dur:
            self.track.play(ts)
            if self.battle.localToonPendingOrActive():
                self.playCamera(ts)
            
        else:
            self.notify.debug('play() - ts: %f dur: %f' % (ts, dur))
            self.track.setT(dur, event = IVAL_INIT)
        return None

    
    def playCamera(self, ts):
        self.notify.debug('playCamera(%f)' % ts)
        if self.camTrack != None:
            dur = self.camTrack.getDuration()
            if ts <= dur:
                self.camTrack.play(ts)
            
        
        return None

    
    def playReward(self, ts, name, callback):
        self.rewardHasBeenReset = 0
        plist = []
        camlist = []
        self.rewardPanel = RewardPanel.RewardPanel(name)
        (victory, camVictory) = MovieToonVictory.doToonVictory(self.battle.localToonActive(), self.battle.activeToons, self.toonRewardDicts, self.rewardPanel)
        if victory:
            plist.append(victory)
            camlist.append(camVictory)
        
        plist.append(FunctionInterval(callback))
        self.track = Track(plist, name = 'movie-reward-track-%d' % self.battle.doId)
        self.camTrack = Track(camlist, name = 'movie-reward-track-cam-%d' % self.battle.doId)
        dur = self.track.getDuration()
        if ts <= dur:
            self.track.play(ts)
            if self.battle.localToonActive():
                self.playCamera(ts)
            
        else:
            self.notify.debug('playReward() - ts: %f dur: %f' % (ts, dur))
            self.track.setT(dur, event = IVAL_INIT)
        return None

    
    def stop(self):
        if self.track:
            if self.track.isPlaying():
                self.notify.debug('stop() - track was playing!')
            
            self.track.stop()
        
        if self.camTrack:
            self.camTrack.stop()
        
        if self.rewardPanel:
            self.rewardPanel.hide()
        
        if self.playByPlayText:
            self.playByPlayText.hide()
        

    
    def __doToonAttacks(self):
        if base.config.GetBool('want-toon-attack-anims', 1):
            ivals = []
            camIvals = []
            (ival, camIval) = MovieSOS.doSOSs(self._Movie__findToonAttack(SOS))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieHeal.doHeals(self._Movie__findToonAttack(HEAL))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieTrap.doTraps(self._Movie__findToonAttack(TRAP))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieLure.doLures(self._Movie__findToonAttack(LURE))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieSound.doSounds(self._Movie__findToonAttack(SOUND))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieThrow.doThrows(self._Movie__findToonAttack(THROW))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieSquirt.doSquirts(self._Movie__findToonAttack(SQUIRT))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            (ival, camIval) = MovieDrop.doDrops(self._Movie__findToonAttack(DROP))
            if ival:
                ivals.append(ival)
                camIvals.append(camIval)
            
            if len(ivals) == 0:
                return (None, None)
            else:
                return (Track(ivals, name = 'toon-attacks'), Track(camIvals, name = 'toon-attacks-cam'))
        else:
            return (None, None)

    
    def genRewardDicts(self, id0, exp0, nentries0, entries0, id1, exp1, nentries1, entries1, id2, exp2, nentries2, entries2, id3, exp3, nentries3, entries3):
        entries = [
            [
                id0,
                exp0,
                nentries0,
                entries0],
            [
                id1,
                exp1,
                nentries1,
                entries1],
            [
                id2,
                exp2,
                nentries2,
                entries2],
            [
                id3,
                exp3,
                nentries3,
                entries3]]
        self.toonRewardDicts = []
        for e in entries:
            toonId = e[0]
            if toonId != -1:
                dict = { }
                toon = self.battle.findToon(toonId)
                if toon == None:
                    continue
                
                dict['toon'] = toon
                dict['exp'] = e[1]
                invMat = [
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0],
                    [
                        0,
                        0,
                        0,
                        0,
                        0,
                        0]]
                index = 0
                for i in range(e[2]):
                    track = e[3][index]
                    level = e[3][index + 1]
                    value = e[3][index + 2]
                    invMat[track][level] = value
                    index += 3
                
                dict['inv'] = invMat
                self.toonRewardDicts.append(dict)
            
        

    
    def genAttackDicts(self, toons, suits, id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0, id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1, id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2, id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3, sid0, at0, stg0, dm0, sd0, sb0, st0, sid1, at1, stg1, dm1, sd1, sb1, st1, sid2, at2, stg2, dm2, sd2, sb2, st2, sid3, at3, stg3, dm3, sd3, sb3, st3):
        self.notify.debug('genAttackDicts()')
        if self.track and self.track.isPlaying():
            self.notify.warning('genAttackDicts() - track is playing!')
        
        toonAttacks = ((id0, tr0, le0, tg0, hp0, ac0, hpb0, kbb0, died0), (id1, tr1, le1, tg1, hp1, ac1, hpb1, kbb1, died1), (id2, tr2, le2, tg2, hp2, ac2, hpb2, kbb2, died2), (id3, tr3, le3, tg3, hp3, ac3, hpb3, kbb3, died3))
        self._Movie__genToonAttackDicts(toons, suits, toonAttacks)
        suitAttacks = ((sid0, at0, stg0, dm0, sd0, sb0, st0), (sid1, at1, stg1, dm1, sd1, sb1, st1), (sid2, at2, stg2, dm2, sd2, sb2, st2), (sid3, at3, stg3, dm3, sd3, sb3, st3))
        self._Movie__genSuitAttackDicts(toons, suits, suitAttacks)

    
    def __genToonAttackDicts(self, toons, suits, toonAttacks):
        self.notify.debug('genToonAttackDicts() - toons: %s suits: %s toon attacks: %s' % (toons, suits, toonAttacks))
        for ta in toonAttacks:
            targetGone = 0
            track = ta[TOON_TRACK_COL]
            if track != NO_ATTACK:
                adict = { }
                toonIndex = ta[TOON_ID_COL]
                toonId = toons[toonIndex]
                toon = self.battle.findToon(toonId)
                if toon == None:
                    continue
                
                level = ta[TOON_LVL_COL]
                adict['toon'] = toon
                adict['track'] = track
                adict['level'] = level
                hps = ta[TOON_HP_COL]
                kbbonuses = ta[TOON_KBBONUS_COL]
                if track == SOS:
                    targetId = ta[TOON_TGT_COL]
                    if targetId == toonbase.localToon.doId:
                        target = toonbase.localToon
                        adict['targetType'] = 'callee'
                    elif toon == toonbase.localToon:
                        target = toonbase.tcr.identifyFriend(targetId)
                        adict['targetType'] = 'caller'
                    else:
                        target = None
                        adict['targetType'] = 'observer'
                    adict['target'] = target
                elif track == HEAL:
                    if levelAffectsGroup(level):
                        targets = []
                        for t in toons:
                            if t != toonId and t != -1:
                                target = self.battle.findToon(t)
                                if target == None:
                                    continue
                                
                                tdict = { }
                                tdict['toon'] = target
                                tdict['hp'] = hps[toons.index(t)]
                                targets.append(tdict)
                            
                        
                        if len(targets) > 0:
                            adict['target'] = targets
                        else:
                            targetGone = 1
                    else:
                        targetIndex = ta[TOON_TGT_COL]
                        targetId = toons[targetIndex]
                        target = self.battle.findToon(targetId)
                        if target != None:
                            tdict = { }
                            tdict['toon'] = target
                            tdict['hp'] = hps[targetIndex]
                            adict['target'] = tdict
                        else:
                            targetGone = 1
                elif attackAffectsGroup(track, level):
                    targets = []
                    for s in suits:
                        if s != -1:
                            target = self.battle.findSuit(s)
                            targetIndex = suits.index(s)
                            sdict = { }
                            sdict['suit'] = target
                            sdict['hp'] = hps[targetIndex]
                            sdict['kbbonus'] = kbbonuses[targetIndex]
                            sdict['died'] = ta[SUIT_DIED_COL] & 1 << targetIndex
                            if sdict['died'] != 0:
                                self.notify.debug('suit: %d died' % target.doId)
                            
                            targets.append(sdict)
                        
                    
                    adict['target'] = targets
                else:
                    targetIndex = ta[TOON_TGT_COL]
                    targetId = suits[targetIndex]
                    target = self.battle.findSuit(targetId)
                    sdict = { }
                    sdict['suit'] = target
                    suitIndex = self.battle.activeSuits.index(target)
                    leftSuits = []
                    for si in range(0, suitIndex):
                        asuit = self.battle.activeSuits[si]
                        if self.battle.isSuitLured(asuit) == 0:
                            leftSuits.append(asuit)
                        
                    
                    lenSuits = len(self.battle.activeSuits)
                    rightSuits = []
                    if lenSuits > suitIndex + 1:
                        for si in range(suitIndex + 1, lenSuits):
                            asuit = self.battle.activeSuits[si]
                            if self.battle.isSuitLured(asuit) == 0:
                                rightSuits.append(asuit)
                            
                        
                    
                    sdict['leftSuits'] = leftSuits
                    sdict['rightSuits'] = rightSuits
                    sdict['hp'] = hps[targetIndex]
                    sdict['kbbonus'] = kbbonuses[targetIndex]
                    sdict['died'] = ta[SUIT_DIED_COL] & 1 << targetIndex
                    if sdict['died'] != 0:
                        self.notify.debug('suit: %d died' % targetId)
                    
                    adict['target'] = sdict
                adict['hpbonus'] = ta[TOON_HPBONUS_COL]
                adict['sidestep'] = ta[TOON_ACCBONUS_COL]
                adict['battle'] = self.battle
                adict['playByPlayText'] = self.playByPlayText
                if targetGone == 0:
                    self.toonAttackDicts.append(adict)
                else:
                    self.notify.warning('genToonAttackDicts() - target gone!')
            
        
        
        def compFunc(a, b):
            alevel = a['level']
            blevel = b['level']
            if alevel > blevel:
                return 1
            elif alevel < blevel:
                return -1
            
            return 0

        self.toonAttackDicts.sort(compFunc)

    
    def __findToonAttack(self, track):
        p = []
        for ta in self.toonAttackDicts:
            if ta['track'] == track:
                p.append(ta)
            
        
        return p

    
    def __genSuitAttackDicts(self, toons, suits, suitAttacks):
        self.notify.debug('genSuitAttackDicts() - toons: %s suits: %s suit attacks: %s' % (toons, suits, suitAttacks))
        for sa in suitAttacks:
            targetGone = 0
            attack = sa[SUIT_ATK_COL]
            if attack != NO_ATTACK:
                suitIndex = sa[SUIT_ID_COL]
                suitId = suits[suitIndex]
                suit = self.battle.findSuit(suitId)
                if suit == None:
                    self.notify.error('suit: %d not in battle!' % suitId)
                
                adict = getSuitAttack(suit.getStyleName(), suit.getLevel(), attack)
                adict['suit'] = suit
                adict['battle'] = self.battle
                adict['playByPlayText'] = self.playByPlayText
                adict['taunt'] = sa[SUIT_TAUNT_COL]
                hps = sa[SUIT_HP_COL]
                if adict['group'] == ATK_TGT_GROUP:
                    self.notify.debug('genSuitAttackDicts() - group: %s' % toons)
                    targets = []
                    for t in toons:
                        if t != -1:
                            target = self.battle.findToon(t)
                            if target == None:
                                continue
                            
                            targetIndex = toons.index(t)
                            tdict = { }
                            tdict['toon'] = target
                            tdict['hp'] = hps[targetIndex]
                            toonDied = sa[TOON_DIED_COL] & 1 << targetIndex
                            tdict['died'] = toonDied
                            targets.append(tdict)
                        
                    
                    if len(targets) > 0:
                        adict['target'] = targets
                    else:
                        targetGone = 1
                elif adict['group'] == ATK_TGT_SINGLE:
                    targetIndex = sa[SUIT_TGT_COL]
                    targetId = toons[targetIndex]
                    target = self.battle.findToon(targetId)
                    if target == None:
                        targetGone = 1
                        break
                    
                    tdict = { }
                    tdict['toon'] = target
                    tdict['hp'] = hps[targetIndex]
                    toonDied = sa[TOON_DIED_COL] & 1 << targetIndex
                    tdict['died'] = toonDied
                    toonIndex = self.battle.activeToons.index(target)
                    rightToons = []
                    for ti in range(0, toonIndex):
                        rightToons.append(self.battle.activeToons[ti])
                    
                    lenToons = len(self.battle.activeToons)
                    leftToons = []
                    if lenToons > toonIndex + 1:
                        for ti in range(toonIndex + 1, lenToons):
                            leftToons.append(self.battle.activeToons[ti])
                        
                    
                    tdict['leftToons'] = leftToons
                    tdict['rightToons'] = rightToons
                    adict['target'] = tdict
                else:
                    self.notify.warning('got suit attack not group or single!')
                if targetGone == 0:
                    self.suitAttackDicts.append(adict)
                else:
                    self.notify.warning('genSuitAttackDicts() - target gone!')
            
        
        
        def compFunc(a, b):
            alevel = a['suit'].getActualLevel()
            blevel = b['suit'].getActualLevel()
            if alevel > blevel:
                return 1
            elif alevel < blevel:
                return -1
            
            return 0

        self.suitAttackDicts.sort(compFunc)

    
    def __doSuitAttacks(self):
        if base.config.GetBool('want-suit-anims', 1):
            ivals = []
            camIvals = []
            for a in self.suitAttackDicts:
                (ival, camIval) = MovieSuitAttacks.doSuitAttack(a)
                if ival:
                    ivals.append(ival)
                    camIvals.append(camIval)
                
            
            if len(ivals) == 0:
                return (None, None)
            
            return (Track(ivals), Track(camIvals))
        else:
            return (None, None)


