# Source Generated with Decompyle++
# File: MovieThrow.pyo (Python 2.0)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from AvatarDNA import *
import DirectNotifyGlobal
import whrandom
import MovieCamera
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieThrow')
hitSoundFiles = ('AA_throw_fruitpie.mp3', 'AA_throw_fruitpie.mp3', 'AA_throw_creampie.mp3', 'AA_throw_wfruitpie.mp3', 'AA_throw_wcreampie.mp3', 'AA_throw_bdaycake.mp3')
missSoundFiles = ('AA_throw_fruitpie_miss.mp3', 'AA_throw_fruitpie_miss.mp3', 'AA_throw_creampie_miss.mp3', 'AA_throw_wfruitpie_miss.mp3', 'AA_throw_wcreampie_miss.mp3', 'AA_throw_bdaycake_miss.mp3')
tPieLeavesHand = 2.7
tPieHitsSuit = 3.0
tSuitDodges = 2.45
ratioMissToHit = 1.5
tPieShrink = 0.7
pieFlyTaskName = 'MovieThrow-pieFly'
pieNames = ('tart', 'fruitpie-slice', 'creampie-slice', 'fruitpie', 'creampie', 'birthday-cake')

def doThrows(throws):
    if len(throws) == 0:
        return (None, None)
    
    suitThrowsDict = { }
    for throw in throws:
        suitId = throw['target']['suit'].doId
        if suitThrowsDict.has_key(suitId):
            suitThrowsDict[suitId].append(throw)
        else:
            suitThrowsDict[suitId] = [
                throw]
    
    suitThrows = suitThrowsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitThrows.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitThrows:
        if len(st) > 0:
            ival = __doSuitThrows(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_THROW_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseThrowShot(throws, suitThrowsDict, camDuration)
    return (mtrack, camTrack)


def __doSuitThrows(throws):
    toonTracks = []
    delay = 0.0
    for throw in throws:
        tracks = __throwPie(throw, delay)
        if tracks:
            for track in tracks:
                toonTracks.append(track)
            
        
        delay = delay + TOON_THROW_DELAY
    
    return MultiTrack(toonTracks)


def __showProp(prop, parent, pos):
    prop.reparentTo(parent)
    prop.setPos(pos)


def __animProp(props, propName, propType):
    if 'actor' == propType:
        for prop in props:
            prop.play(propName)
        
    elif 'model' == propType:
        pass
    else:
        self.notify.error('No such propType as: %s' % propType)


def __billboardProp(prop):
    scale = prop.getScale()
    prop.setBillboardPointWorld()
    prop.setScale(scale)


def __hideProp(prop, propPool):
    prop.reparentTo(hidden)


def __suitMissPoint(suit):
    pnt = suit.getPos()
    pnt.setZ(pnt[2] + suit.getHeight() * 1.3)
    return pnt


def __propPreflight(props, suit, toon):
    prop = props[0]
    toon.update()
    prop.wrtReparentTo(render)
    props[1].reparentTo(hidden)
    pos = prop.getPos()
    prop.setPosHpr(0, 0, 0, 0, -90, 0)
    prop.flattenMedium()
    prop.setPos(pos)
    targetPnt = MovieUtil.avatarFacePoint(suit)
    prop.lookAt(targetPnt)


def __piePreMiss(missDict, pie, suitPoint):
    missDict['pie'] = pie
    missDict['startScale'] = pie.getScale()
    missDict['startPos'] = pie.getPos()
    v = Vec3(suitPoint - missDict['startPos'])
    endPos = missDict['startPos'] + v * ratioMissToHit
    missDict['endPos'] = endPos


def __pieMissLerpCallback(t, missDict):
    pie = missDict['pie']
    newPos = missDict['startPos'] * (1.0 - t) + missDict['endPos'] * t
    if t < tPieShrink:
        tScale = 0.0
    else:
        tScale = (t - tPieShrink) / (1.0 - tPieShrink)
    newScale = missDict['startScale'] * (1.0 - tScale)
    pie.setPos(newPos)
    pie.setScale(newScale)


def __getSoundTrack(level, hitSuit):
    if hitSuit:
        soundEffect = globalSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalSoundCache.getSound(missSoundFiles[level])
    soundIntervals = []
    if soundEffect:
        playSound = SoundInterval(soundEffect)
        soundIntervals.append((tPieLeavesHand, playSound))
    else:
        soundIntervals.append(WaitInterval(0.1))
    return Track(soundIntervals)


def __throwPie(throw, delay):
    toon = throw['toon']
    hpbonus = throw['hpbonus']
    target = throw['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    sidestep = throw['sidestep']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    level = throw['level']
    battle = throw['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    notify.debug('toon: %s throws tart at suit: %d for hp: %d died: %d' % (toon.getName(), suit.doId, hp, died))
    pieName = pieNames[level]
    hitSuit = hp > 0
    pie = globalPropPool.getProp(pieName)
    pieType = globalPropPool.getPropType(pieName)
    pie2 = MovieUtil.copyProp(pie)
    pies = [
        pie,
        pie2]
    hands = toon.getRightHands()
    splatName = 'splat-' + pieName
    splat = globalPropPool.getProp(splatName)
    splatType = globalPropPool.getPropType(splatName)
    toonIvals = []
    toonFace = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos])
    toonIvals.append((delay, toonFace))
    toonIvals.append(ActorInterval(toon, 'throw'))
    toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    toonTrack = Track(toonIvals)
    pieIntervals = []
    pieShow = FunctionInterval(MovieUtil.showProps, extraArgs = [
        pies,
        hands])
    pieAnim = FunctionInterval(__animProp, extraArgs = [
        pies,
        pieName,
        pieType])
    pieScale1 = LerpScaleInterval(pie, 1.0, pie.getScale(), startScale = Point3(0.0, 0.0, 0.0))
    pieScale2 = LerpScaleInterval(pie2, 1.0, pie2.getScale(), startScale = Point3(0.0, 0.0, 0.0))
    pieScale = MultiTrack([
        Track([
            pieScale1]),
        Track([
            pieScale2])])
    piePreflight = FunctionInterval(__propPreflight, extraArgs = [
        pies,
        suit,
        toon])
    pieIntervals.append((delay, pieShow))
    pieIntervals.append(pieAnim)
    pieIntervals.append(pieScale)
    pieIntervals.append((delay + tPieLeavesHand, piePreflight))
    soundTrack = __getSoundTrack(level, hitSuit)
    if hitSuit:
        pieFly = LerpPosInterval(pie, tPieHitsSuit - tPieLeavesHand, pos = MovieUtil.avatarFacePoint(suit), name = pieFlyTaskName)
        pieHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
            pies])
        splatShow = FunctionInterval(__showProp, extraArgs = [
            splat,
            suit,
            Point3(0, 0, suit.getHeight())])
        splatBillboard = FunctionInterval(__billboardProp, extraArgs = [
            splat])
        splatAnim = ActorInterval(splat, splatName)
        splatHide = FunctionInterval(__hideProp, extraArgs = [
            splat,
            globalPropPool])
        pieIntervals.append((delay + tPieLeavesHand, pieFly))
        pieIntervals.append(pieHide)
        pieIntervals.append(splatShow)
        pieIntervals.append(splatBillboard)
        pieIntervals.append(splatAnim)
        pieIntervals.append(splatHide)
    else:
        missDict = { }
        if sidestep:
            suitPoint = MovieUtil.avatarFacePoint(suit)
        else:
            suitPoint = __suitMissPoint(suit)
        piePreMiss = FunctionInterval(__piePreMiss, extraArgs = [
            missDict,
            pie,
            suitPoint])
        pieMiss = LerpFunctionInterval(__pieMissLerpCallback, extraArgs = [
            missDict], duration = (tPieHitsSuit - tPieLeavesHand) * ratioMissToHit)
        pieHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
            pies])
        pieIntervals.append((delay + tPieLeavesHand, piePreMiss))
        pieIntervals.append(pieMiss)
        pieIntervals.append(pieHide)
    pieTrack = Track(pieIntervals)
    if hitSuit:
        suitIntervals = []
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        sival = []
        if kbbonus > 0:
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            suitType = getSuitBodyType(suit.getStyleName())
            animIvals = []
            animIvals.append(ActorInterval(suit, 'pie-small-react', duration = 0.2))
            if suitType == 'a':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 2.43))
            elif suitType == 'b':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 1.94, duration = 1.03))
            elif suitType == 'c':
                animIvals.append(ActorInterval(suit, 'slip-forward', startTime = 2.58))
            
            battle.unlureSuit(suit)
            animTrack = Track(animIvals)
            moveTrack = Track([
                WaitInterval(0.2),
                LerpPosInterval(suit, 0.6, pos = suitPos, other = battle)])
            sival = MultiTrack([
                animTrack,
                moveTrack])
        else:
            sival = ActorInterval(suit, 'pie-small-react')
        suitIntervals.append((delay + tPieHitsSuit, showDamage))
        suitIntervals.append(sival)
        bonusTrack = None
        bonusIvals = []
        if kbbonus > 0:
            bonusIvals.append((delay + tPieHitsSuit + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                -kbbonus,
                2])))
        
        if hpbonus > 0:
            if kbbonus > 0:
                bonusIvals.append((0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]), PREVIOUS_END))
            else:
                bonusIvals.append((delay + tPieHitsSuit + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1])))
        
        if len(bonusIvals) > 0:
            bonusTrack = Track(bonusIvals)
        
        if died != 0:
            suitIntervals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIntervals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            suitResponseTrack = Track(suitIntervals)
        else:
            suitResponseTrack = MultiTrack([
                Track(suitIntervals),
                bonusTrack])
    else:
        suitResponseTrack = MovieUtil.createSuitDodgeMultitrack(delay + tSuitDodges, suit, leftSuits, rightSuits)
    return [
        toonTrack,
        soundTrack,
        pieTrack,
        suitResponseTrack]

