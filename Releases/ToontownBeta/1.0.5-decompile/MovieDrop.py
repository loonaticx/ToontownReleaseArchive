# Source Generated with Decompyle++
# File: MovieDrop.pyo (Python 2.0)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
notify = DirectNotifyGlobal.directNotify.newCategory('MovieDrop')
hitSoundFiles = ('AA_drop_flowerpot.mp3', 'AA_drop_sandbag.mp3', 'AA_drop_anvil.mp3', 'AA_drop_bigweight.mp3', 'AA_drop_safe.mp3', 'AA_drop_piano.mp3')
missSoundFiles = ('AA_drop_flowerpot_miss.mp3', 'AA_drop_sandbag_miss.mp3', 'AA_drop_anvil_miss.mp3', 'AA_drop_bigweight_miss.mp3', 'AA_drop_safe_miss.mp3', 'AA_drop_piano_miss.mp3')
tSuitDodges = 2.45
tObjectAppears = 3.0
tButtonPressed = 2.44
dShrink = 0.3
dShrinkOnMiss = 0.1
dPropFall = 0.6
objects = ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano')
objZOffsets = (0.75, 0.75, 0.0, 0.0, 0.0, 0.0)
landFrames = (12, 4, 1, 11, 11, 11)
shoulderHeights = {
    'a': 13.28 / 4.0,
    'b': 13.74 / 4.0,
    'c': 10.02 / 4.0 }

def doDrops(drops):
    if len(drops) == 0:
        return (None, None)
    
    suitDropsDict = { }
    for drop in drops:
        suitId = drop['target']['suit'].doId
        if suitDropsDict.has_key(suitId):
            suitDropsDict[suitId].append(drop)
        else:
            suitDropsDict[suitId] = [
                drop]
    
    suitDrops = suitDropsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitDrops.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitDrops:
        if len(st) > 0:
            ival = __doSuitDrops(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_DROP_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks, name = 'toplevel-drop')
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseDropShot(drops, suitDropsDict, camDuration)
    return (mtrack, camTrack)


def __getSoundTrack(level, hitSuit):
    if hitSuit:
        soundEffect = globalSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalSoundCache.getSound(missSoundFiles[level])
    soundIntervals = []
    if soundEffect:
        playSound = SoundInterval(soundEffect)
        soundIntervals.append((tButtonPressed, playSound))
    else:
        soundIntervals.append(WaitInterval(0.1))
    return Track(soundIntervals)


def __doSuitDrops(drops):
    toonTracks = []
    delay = 0.0
    alreadyDodged = 0
    for drop in drops:
        level = drop['level']
        objName = objects[level]
        ivals = __dropObject(drop, delay, objName, level, alreadyDodged)
        if ivals:
            toonTracks += ivals
            delay += TOON_DROP_DELAY
        
        hp = drop['target']['hp']
        if hp <= 0:
            alreadyDodged = 1
        
    
    return MultiTrack(toonTracks)


def __dropObject(drop, delay, objName, level, alreadyDodged):
    toon = drop['toon']
    hpbonus = drop['hpbonus']
    target = drop['target']
    suit = target['suit']
    hp = target['hp']
    hitSuit = hp > 0
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    kbbonus = target['kbbonus']
    battle = drop['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    majorObject = level >= 3
    button = globalPropPool.getProp('button')
    buttonType = globalPropPool.getPropType('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    object = globalPropPool.getProp(objName)
    objectType = globalPropPool.getPropType(objName)
    arc = object.arc()
    arc.setBound(OmniBoundingVolume())
    arc.setFinal(1)
    soundTrack = __getSoundTrack(level, hitSuit)
    toonIntervals = []
    toonFace = FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos])
    toonIntervals.append((delay, toonFace))
    toonIntervals.append(ActorInterval(toon, 'pushbutton'))
    toonIntervals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIntervals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    toonTrack = Track(toonIntervals)
    buttonIntervals = []
    buttonShow = FunctionInterval(MovieUtil.showProps, extraArgs = [
        buttons,
        hands])
    buttonScaleUp = LerpScaleInterval(button, 1.0, button.getScale(), startScale = Point3(0.0, 0.0, 0.0))
    buttonScaleDown = LerpScaleInterval(button, 1.0, Point3(0.0, 0.0, 0.0), startScale = button.getScale())
    buttonHide = FunctionInterval(MovieUtil.removeProps, extraArgs = [
        buttons])
    buttonIntervals.append((delay, buttonShow))
    buttonIntervals.append(buttonScaleUp)
    buttonIntervals.append(WaitInterval(2.5))
    buttonIntervals.append(buttonScaleDown)
    buttonIntervals.append(buttonHide)
    buttonTrack = Track(buttonIntervals)
    objIntervals = []
    
    def posObject(object, suit, level, majorObject, miss, battle = battle):
        object.reparentTo(render)
        if battle.isSuitLured(suit):
            object.reparentTo(battle)
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            object.setPos(suitPos)
            object.setHpr(suitHpr)
            object.wrtReparentTo(render)
        else:
            object.setPos(suit.getPos())
            object.setHpr(suit.getHpr())
        if not majorObject:
            if not miss:
                shoulderHeight = shoulderHeights[suit.style.body] * suit.scale
                object.setZ(object.getPos()[2] + shoulderHeight)
            
        
        object.setZ(object.getPos()[2] + objZOffsets[level])
        if level == 5:
            object.setX(object.getPos()[0] - suit.getHeight() * (1.0 / 5.0))
        

    
    def hideObject(object, propPool):
        object.reparentTo(hidden)

    objInit = FunctionInterval(posObject, extraArgs = [
        object,
        suit,
        level,
        majorObject,
        hp <= 0])
    objIntervals.append((delay + tObjectAppears, objInit))
    if hp > 0 and level == 1 or level == 2:
        animProp = ActorInterval(object, objName)
        trackObjAnimate = Track([
            animProp])
        shrinkProp = LerpScaleInterval(object, dShrink, Point3(0, 0, 0), startScale = object.getScale())
        trackObjShrink = Track([
            (animProp.getDuration() - dShrink, shrinkProp)])
        objAnimShrink = MultiTrack([
            trackObjAnimate,
            trackObjShrink])
        objIntervals.append(objAnimShrink)
    else:
        animProp = ActorInterval(object, objName, duration = landFrames[level] / 24.0)
        
        def poseProp(prop, animName, level):
            prop.pose(animName, landFrames[level])

        poseProp = FunctionInterval(poseProp, extraArgs = [
            object,
            objName,
            level])
        wait = WaitInterval(1.0)
        shrinkProp = LerpScaleInterval(object, dShrinkOnMiss, Point3(0, 0, 0), startScale = object.getScale())
        objIntervals.append(animProp)
        objIntervals.append(poseProp)
        objIntervals.append(wait)
        objIntervals.append(shrinkProp)
    objHide = FunctionInterval(hideObject, extraArgs = [
        object,
        globalPropPool])
    objIntervals.append(objHide)
    objectTrack = Track(objIntervals)
    if kbbonus == 0:
        suitTrack = Track([
            FunctionInterval(suit.loop, extraArgs = [
                'neutral'])])
    elif hp > 0:
        suitIntervals = []
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        if majorObject:
            anim = 'flatten'
        else:
            anim = 'drop-react'
        suitReact = ActorInterval(suit, anim)
        suitIntervals.append((delay + tObjectAppears, showDamage))
        suitIntervals.append(suitReact)
        bonusTrack = None
        if hpbonus > 0:
            bonusTrack = Track([
                (delay + tObjectAppears + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]))])
        
        if died != 0:
            suitIntervals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIntervals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            suitTrack = Track(suitIntervals)
        else:
            suitTrack = MultiTrack([
                Track(suitIntervals),
                bonusTrack])
    elif alreadyDodged == 0:
        suitTrack = MovieUtil.createSuitDodgeMultitrack(delay + tSuitDodges, suit, leftSuits, rightSuits)
    else:
        return [
            toonTrack,
            soundTrack,
            buttonTrack,
            objectTrack]
    return [
        toonTrack,
        soundTrack,
        buttonTrack,
        objectTrack,
        suitTrack]

