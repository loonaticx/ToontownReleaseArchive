# Source Generated with Decompyle++
# File: MovieSquirt.pyo (Python 2.0)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from AvatarDNA import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
import BattleParticles
import Toon
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSquirt')
hitSoundFiles = ('AA_squirt_flowersquirt.mp3', 'AA_squirt_glasswater.mp3', 'AA_squirt_neonwatergun.mp3', 'AA_squirt_seltzer.mp3', 'AA_squirt_seltzer.mp3', 'AA_throw_stormcloud.mp3')
missSoundFiles = ('AA_squirt_flowersquirt_miss.mp3', 'AA_squirt_glasswater_miss.mp3', 'AA_squirt_neonwatergun_miss.mp3', 'AA_squirt_seltzer_miss.mp3', 'AA_squirt_seltzer_miss.mp3', 'AA_throw_stormcloud_miss.mp3')
sprayScales = [
    0.2,
    0.3,
    0.1,
    0.6,
    0.8,
    1.0]

def doSquirts(squirts):
    if len(squirts) == 0:
        return (None, None)
    
    suitSquirtsDict = { }
    for squirt in squirts:
        suitId = squirt['target']['suit'].doId
        if suitSquirtsDict.has_key(suitId):
            suitSquirtsDict[suitId].append(squirt)
        else:
            suitSquirtsDict[suitId] = [
                squirt]
    
    suitSquirts = suitSquirtsDict.values()
    
    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        
        return 0

    suitSquirts.sort(compFunc)
    delay = 0.0
    tracks = []
    for st in suitSquirts:
        if len(st) > 0:
            ival = __doSuitSquirts(st)
            if ival:
                tracks.append(Track([
                    (delay, ival)]))
            
            delay = delay + TOON_SQUIRT_SUIT_DELAY
        
    
    mtrack = MultiTrack(tracks)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSquirtShot(squirts, suitSquirtsDict, camDuration)
    return (mtrack, camTrack)


def __doSuitSquirts(squirts):
    toonTracks = []
    delay = 0.0
    for s in squirts:
        tracks = __doSquirt(s, delay)
        if tracks:
            for track in tracks:
                toonTracks.append(track)
            
        
        delay = delay + TOON_SQUIRT_DELAY
    
    return MultiTrack(toonTracks)


def __doSquirt(squirt, delay):
    notify.debug('toon: %s squirts prop: %d at suit: %d for hp: %d' % (squirt['toon'].getName(), squirt['level'], squirt['target']['suit'].doId, squirt['target']['hp']))
    squirts = [
        __doFlower,
        __doWaterGlass,
        __doWaterGun,
        __doSeltzerBottle,
        __doFireHose,
        __doStormCloud]
    waitTrack = Track([
        WaitInterval(delay)])
    attackMTrack = squirts[squirt['level']](squirt)
    return [
        Track([
            waitTrack,
            attackMTrack])]


def __suitTargetPoint(suit):
    return suit.getPos() + Point3(0, 0, suit.getHeight() * (2.0 / 3.0))


def __getSplashTrack(point, scale, delay):
    
    def prepSplash(splash, point):
        splash.reparentTo(render)
        splash.setPos(point)
        scale = splash.getScale()
        splash.setBillboardPointWorld()
        splash.setScale(scale)

    splash = globalPropPool.getProp('splash-from-splat')
    splash.setScale(scale)
    return Track([
        (delay, FunctionInterval(prepSplash, extraArgs = [
            splash,
            point])),
        ActorInterval(splash, 'splash-from-splat'),
        FunctionInterval(splash.reparentTo, extraArgs = [
            hidden])])


def __getSuitTrack(suit, tContact, tDodge, hp, hpbonus, kbbonus, anim, died, leftSuits, rightSuits, battle, toon):
    if hp > 0:
        suitIvals = []
        sival = ActorInterval(suit, anim)
        sival = []
        if kbbonus > 0:
            (suitPos, suitHpr) = battle.getActorPosHpr(suit)
            suitType = getSuitBodyType(suit.getStyleName())
            animIvals = []
            animIvals.append(ActorInterval(suit, anim, duration = 0.2))
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
            sival = ActorInterval(suit, anim)
        showDamage = FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
            -hp])
        suitIvals.append((tContact, showDamage))
        suitIvals.append(sival)
        bonusTrack = None
        bonusIvals = []
        if kbbonus > 0:
            bonusIvals.append((tContact + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                -kbbonus,
                2])))
        
        if hpbonus > 0:
            if kbbonus > 0:
                bonusIvals.append((0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1]), PREVIOUS_END))
            else:
                bonusIvals.append((tContact + 0.75, FunctionInterval(suit.showLaffNumber, openEnded = 0, extraArgs = [
                    -hpbonus,
                    1])))
        
        if len(bonusIvals) > 0:
            bonusTrack = Track(bonusIvals)
        
        if died != 0:
            suitIvals.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitIvals.append(FunctionInterval(suit.loop, extraArgs = [
                'neutral']))
        if bonusTrack == None:
            return Track(suitIvals)
        else:
            return MultiTrack([
                Track(suitIvals),
                bonusTrack])
    else:
        return MovieUtil.createSuitDodgeMultitrack(tDodge, suit, leftSuits, rightSuits)


def __getSoundTrack(level, hitSuit, delay):
    if hitSuit:
        soundEffect = globalSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalSoundCache.getSound(missSoundFiles[level])
    soundIntervals = []
    if soundEffect:
        playSound = SoundInterval(soundEffect)
        soundIntervals.append((delay, playSound))
    else:
        soundIntervals.append(WaitInterval(0.1))
    return Track(soundIntervals)


def __doFlower(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tFlower = 2.5
    dFlowerScale = 0.5
    dFlowerHold = 1.0
    tSpray = tFlower + dFlowerScale
    dSprayScale = 0.2
    dSprayHold = 0.1
    tContact = tSpray + dSprayScale
    tSuitDodges = tFlower
    tracks = []
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
    hands = toon.getLeftHands()
    toonIvals = []
    toonIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs = [
        buttons,
        hands]))
    toonIvals.append(FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        suitPos]))
    toonIvals.append(ActorInterval(toon, 'pushbutton'))
    toonIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs = [
        buttons]))
    toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
        'neutral']))
    toonIvals.append(FunctionInterval(toon.setHpr, extraArgs = [
        battle,
        origHpr]))
    tracks.append(Track(toonIvals))
    tracks.append(__getSoundTrack(level, hitSuit, tFlower))
    flower = globalPropPool.getProp('squirting-flower')
    flower.setScale(1.5, 1.5, 1.5)
    targetPoint = __suitTargetPoint(suit)
    
    def getSprayStartPos(flower = flower):
        return flower.getPos(render)

    sprayIvals = MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    flowerIntervals = [
        WaitInterval(tFlower),
        FunctionInterval(flower.reparentTo, extraArgs = [
            toon.find('**/joint-attachFlower')]),
        LerpScaleInterval(flower, dFlowerScale, flower.getScale(), startScale = Point3(0, 0, 0))]
    flowerIntervals.extend(sprayIvals)
    flowerIntervals.append(LerpScaleInterval(flower, dFlowerScale, Point3(0, 0, 0)))
    flowerIntervals.append(FunctionInterval(flower.reparentTo, extraArgs = [
        hidden]))
    tracks.append(Track(flowerIntervals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale))
    
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)


def __doWaterGlass(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    dGlassHold = 5.0
    dGlassScale = 0.5
    tSpray = 82.0 / toon.getFrameRate('spit')
    sprayPoseFrame = 88
    dSprayScale = 0.1
    dSprayHold = 0.1
    tContact = tSpray + dSprayScale
    tSuitDodges = max(tSpray - 0.5, 0.0)
    tracks = []
    toonIntervals = [
        ActorInterval(toon, 'spit')]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, 2)
    tracks.append(soundTrack)
    glass = globalPropPool.getProp('glass')
    glass2 = MovieUtil.copyProp(glass)
    glasses = [
        glass,
        glass2]
    hands = toon.getRightHands()
    glassIntervals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            glasses,
            hands]),
        MovieUtil.getActorIntervals(glasses, 'glass'),
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            glasses])]
    tracks.append(Track(glassIntervals))
    targetPoint = __suitTargetPoint(suit)
    
    def getSprayStartPos(toon = toon, sprayPoseFrame = sprayPoseFrame):
        toon.pose('spit', sprayPoseFrame)
        toon.update(0)
        lod0 = toon.getLOD(toon.getLODNames()[0])
        joint = lod0.find('**/joint-head')
        n = hidden.attachNewNode('pointInFrontOfHead')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, 0.3, -0.2))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    tracks.append(Track([
        WaitInterval(tSpray)] + sprayIvals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale))
    
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)


def __doWaterGun(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tPistol = 0.0
    dPistolScale = 0.5
    dPistolHold = 1.8
    tSpray = 48.0 / toon.getFrameRate('water-gun')
    sprayPoseFrame = 63
    dSprayScale = 0.1
    dSprayHold = 0.3
    tContact = tSpray + dSprayScale
    tSuitDodges = 1.1
    tracks = []
    toonIntervals = [
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'water-gun'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, 1.8)
    tracks.append(soundTrack)
    pistol = globalPropPool.getProp('water-gun')
    pistol2 = MovieUtil.copyProp(pistol)
    pistols = [
        pistol,
        pistol2]
    hands = toon.getRightHands()
    targetPoint = __suitTargetPoint(suit)
    
    def getSprayStartPos(pistol = pistol, toon = toon, sprayPoseFrame = sprayPoseFrame, tSpray = tSpray):
        curFrame = toon.getCurrentFrame('water-gun')
        toon.pose('water-gun', sprayPoseFrame)
        toon.update(0)
        joint = pistol.find('**/joint-nozzle')
        p = joint.getPos(render)
        toon.pose('water-gun', curFrame)
        toon.update(0)
        return p

    sprayIvals = MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    pistolPos = Point3(0.28, 0.1, 0.08)
    pistolHpr = Point3(-4.76, -85.6, -85.91)
    
    def getPistolIvals(pistol, hand, pos = pistolPos, hpr = pistolHpr, dPistolScale = dPistolScale, dPistolHold = dPistolHold, sprayIvals = sprayIvals, tSpray = tSpray, useSpray = 1):
        ivals = [
            FunctionInterval(MovieUtil.showProp, extraArgs = [
                pistol,
                hand,
                pos,
                hpr]),
            LerpScaleInterval(pistol, dPistolScale, pistol.getScale(), startScale = Point3(1e-005, 1e-005, 1e-005)),
            WaitInterval(tSpray - dPistolScale)]
        if useSpray == 1:
            ivals.extend(sprayIvals)
        
        ivals.append(WaitInterval(dPistolHold))
        ivals.append(LerpScaleInterval(pistol, dPistolScale, Point3(0, 0, 0)))
        ivals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            pistol]))
        return ivals

    tracks.append(Track(getPistolIvals(pistol, hands[0], useSpray = 1)))
    tracks.append(Track(getPistolIvals(pistol2, hands[1], useSpray = 0)))
    if hp > 0:
        splashScale = 0.3
        tSplash = 2
        
        def prepSplash(splash, targetPoint, splashScale = splashScale):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(splashScale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setScale(splashScale)
        tracks.append(Track([
            (tSplash, FunctionInterval(prepSplash, extraArgs = [
                splash,
                targetPoint])),
            ActorInterval(splash, 'splash-from-splat'),
            FunctionInterval(splash.reparentTo, extraArgs = [
                hidden])]))
    
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)


def __doSeltzerBottle(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tBottle = 0.0
    dBottleScale = 0.5
    dBottleHold = 3.0
    tSpray = 53 / toon.getFrameRate('hold-bottle') + 0.05
    dSprayScale = 0.2
    dSprayHold = 0.1
    tContact = tSpray + dSprayScale
    tSuitDodges = max(tContact - 0.7, 0.0)
    tracks = []
    toonIntervals = [
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'hold-bottle'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, tSpray)
    tracks.append(soundTrack)
    bottle = globalPropPool.getProp('bottle')
    bottle2 = MovieUtil.copyProp(bottle)
    bottles = [
        bottle,
        bottle2]
    hands = toon.getRightHands()
    bottleIntervals = [
        FunctionInterval(MovieUtil.showProps, extraArgs = [
            bottles,
            hands]),
        LerpScaleInterval(bottle, dBottleScale, bottle.getScale(), startScale = Point3(0, 0, 0)),
        WaitInterval(dBottleHold),
        LerpScaleInterval(bottle, dBottleScale, Point3(0, 0, 0))]
    bottleDeleteIntervals = [
        FunctionInterval(MovieUtil.removeProps, extraArgs = [
            bottles])]
    targetPoint = __suitTargetPoint(suit)
    
    def getSprayStartPos(bottle = bottle, toon = toon):
        joint = bottle.find('**/joint-toSpray')
        n = hidden.attachNewNode('pointBehindSprayProp')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, -0.4, 0))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = [
        WaitInterval(tSpray)] + MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale)
    bottleAndSprayIntervals = [
        MultiTrack([
            Track(bottleIntervals),
            Track(sprayIvals)]),
        Track(bottleDeleteIntervals)]
    tracks.append(Track(bottleAndSprayIntervals))
    if hp > 0:
        tracks.append(__getSplashTrack(targetPoint, scale, tSpray + dSprayScale))
    
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)


def __doFireHose(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = 0.3
    tAppearDelay = 0.7
    dHoseHold = 0.7
    dAnimHold = 5.1
    tSprayDelay = 2.8
    tSpray = 0.2
    dSprayScale = 0.1
    dSprayHold = 1.8
    tContact = 2.9
    tSuitDodges = 2.1
    tracks = []
    toonIntervals = [
        WaitInterval(tAppearDelay),
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'firehose'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, tSprayDelay)
    tracks.append(soundTrack)
    hose = globalPropPool.getProp('firehose')
    hydrant = globalPropPool.getProp('hydrant')
    hands = toon.getRightHands()
    scale = Toon.toonBodyScales[toon.style.getAnimal()]
    hydrantPos = toon.getPos()
    hosePos = hydrantPos
    hydrantHpr = toon.getHpr()
    hoseHpr = hydrantHpr
    baseHeight = 0
    bases = hydrant.findAllMatches('**/base')
    
    def moveZ(num, hydrantPos = hydrantPos):
        hydrantPos.setZ(hydrantPos.getZ() + num)
        return hydrantPos

    animal = toon.style.getAnimal()
    legs = toon.style.legs
    torso = toon.style.torso
    torso = torso[0]
    if legs == 's':
        if torso == 's':
            pass
        1
        if torso == 'm':
            hydrantPos = moveZ(-0.25)
            baseHeight = baseHeight + 0.25
        elif torso == 'l':
            pass
        
    elif legs == 'm':
        if torso == 's':
            if animal == 'dog' or animal == 'horse':
                hydrantPos = moveZ(0.4)
                baseHeight = baseHeight - 0.4
            elif animal == 'cat' or animal == 'rabbit':
                hydrantPos = moveZ(0.32)
                baseHeight = baseHeight - 0.32
            elif animal == 'mouse' or animal == 'fowl':
                hydrantPos = moveZ(0.26)
                baseHeight = baseHeight - 0.26
            
        elif torso == 'm':
            pass
        elif torso == 'l':
            if animal == 'dog' or animal == 'horse':
                hydrantPos = moveZ(0.36)
                baseHeight = baseHeight - 0.36
            elif animal == 'cat' or animal == 'rabbit':
                hydrantPos = moveZ(0.32)
                baseHeight = baseHeight - 0.32
            elif animal == 'mouse' or animal == 'fowl':
                hydrantPos = moveZ(0.29)
                baseHeight = baseHeight - 0.29
            
        
    elif legs == 'l':
        if torso == 's':
            if animal == 'dog' or animal == 'horse':
                hydrantPos = moveZ(1.06)
                baseHeight = baseHeight - 1.06
            elif animal == 'cat' or animal == 'rabbit':
                hydrantPos = moveZ(0.94)
                baseHeight = baseHeight - 0.94
            elif animal == 'mouse' or animal == 'fowl':
                hydrantPos = moveZ(0.79)
                baseHeight = baseHeight - 0.79
            
        elif torso == 'm':
            if animal == 'dog' or animal == 'horse':
                hydrantPos = moveZ(0.74)
                baseHeight = baseHeight - 0.74
            elif animal == 'cat' or animal == 'rabbit':
                hydrantPos = moveZ(0.64)
                baseHeight = baseHeight - 0.64
            elif animal == 'mouse' or animal == 'fowl':
                hydrantPos = moveZ(0.51)
                baseHeight = baseHeight - 0.51
            
        elif torso == 'l':
            if animal == 'dog' or animal == 'horse':
                hydrantPos = moveZ(1.06)
                baseHeight = baseHeight - 1.06
            elif animal == 'cat' or animal == 'rabbit':
                hydrantPos = moveZ(0.91)
                baseHeight = baseHeight - 0.91
            elif animal == 'mouse' or animal == 'fowl':
                hydrantPos = moveZ(0.76)
                baseHeight = baseHeight - 0.76
            
        
    
    targetPoint = __suitTargetPoint(suit)
    
    def getSprayStartPos(hose = hose, toon = toon, targetPoint = targetPoint):
        toon.update(0)
        if hose.isEmpty() == 1:
            return targetPoint
        
        joint = hose.find('**/joint-water_stream')
        n = hidden.attachNewNode('pointBehindSprayProp')
        n.reparentTo(toon)
        n.setPos(joint.getPos(toon) + Point3(0, -0.55, 0))
        p = n.getPos(render)
        n.removeNode()
        del n
        return p

    sprayIvals = []
    sprayIvals.append(WaitInterval(tSprayDelay))
    sprayIvals.extend(MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale = scale, vertScale = scale))
    tracks.append(Track(sprayIvals))
    propIvals = [
        FunctionInterval(hydrant.setPos, extraArgs = [
            hydrantPos]),
        FunctionInterval(hydrant.setHpr, extraArgs = [
            hydrantHpr]),
        FunctionInterval(hydrant.setScale, extraArgs = [
            scale]),
        FunctionInterval(hydrant.reparentTo, extraArgs = [
            render]),
        FunctionInterval(hydrant.wrtReparentTo, extraArgs = [
            battle]),
        FunctionInterval(hydrant.headsUp, extraArgs = [
            battle,
            suitPos]),
        FunctionInterval(hydrant.setScale, extraArgs = [
            scale]),
        FunctionInterval(hose.setPos, extraArgs = [
            hosePos]),
        FunctionInterval(hose.setHpr, extraArgs = [
            hoseHpr]),
        FunctionInterval(hose.setScale, extraArgs = [
            scale]),
        FunctionInterval(hose.reparentTo, extraArgs = [
            render]),
        FunctionInterval(hose.wrtReparentTo, extraArgs = [
            battle]),
        FunctionInterval(hose.headsUp, extraArgs = [
            battle,
            suitPos]),
        FunctionInterval(hose.setScale, extraArgs = [
            scale]),
        FunctionInterval(bases[0].wrtReparentTo, extraArgs = [
            render]),
        FunctionInterval(bases[1].wrtReparentTo, extraArgs = [
            render]),
        FunctionInterval(bases[0].setZ, extraArgs = [
            battle.getZ()]),
        FunctionInterval(bases[1].setZ, extraArgs = [
            battle.getZ()]),
        FunctionInterval(hose.pose, extraArgs = [
            'firehose',
            2]),
        WaitInterval(tAppearDelay),
        ActorInterval(hose, 'firehose', duration = dAnimHold),
        WaitInterval(dHoseHold),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            hydrant]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            hose]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            bases[0]]),
        FunctionInterval(MovieUtil.removeProp, extraArgs = [
            bases[1]])]
    tracks.append(Track(propIvals))
    if hp > 0:
        splashScale = 0.3
        tSplash = 2.7
        splashHold = 1.5
        
        def prepSplash(splash, targetPoint, splashScale = splashScale):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(splashScale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setScale(splashScale)
        tracks.append(Track([
            (tSplash, FunctionInterval(prepSplash, extraArgs = [
                splash,
                targetPoint])),
            ActorInterval(splash, 'splash-from-splat'),
            WaitInterval(splashHold),
            FunctionInterval(splash.reparentTo, extraArgs = [
                hidden])]))
    
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)


def __doStormCloud(squirt):
    toon = squirt['toon']
    level = squirt['level']
    hpbonus = squirt['hpbonus']
    target = squirt['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = squirt['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tButton = 0.0
    dButtonScale = 0.5
    dButtonHold = 3.0
    tContact = 2.9
    tSpray = 1
    tSuitDodges = 1.8
    tracks = []
    toonIntervals = [
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            suitPos]),
        ActorInterval(toon, 'pushbutton'),
        FunctionInterval(toon.loop, extraArgs = [
            'neutral']),
        FunctionInterval(toon.setHpr, extraArgs = [
            battle,
            origHpr])]
    tracks.append(Track(toonIntervals))
    soundTrack = __getSoundTrack(level, hitSuit, 2.3)
    tracks.append(soundTrack)
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    hands = toon.getLeftHands()
    
    def getButtonIvals(button, hand, pos = Point3(0, 0, 0), hpr = Point3(0, -90, 0), dButtonScale = dButtonScale, dButtonHold = dButtonHold):
        return [
            FunctionInterval(MovieUtil.showProp, extraArgs = [
                button,
                hand,
                pos,
                hpr]),
            LerpScaleInterval(button, dButtonScale, button.getScale(), startScale = Point3(0, 0, 0)),
            WaitInterval(dButtonHold),
            LerpScaleInterval(button, dButtonScale, Point3(0, 0, 0)),
            FunctionInterval(MovieUtil.removeProp, extraArgs = [
                button])]

    tracks.append(Track(getButtonIvals(button, hands[0])))
    tracks.append(Track(getButtonIvals(button2, hands[1])))
    cloud = MovieUtil.copyProp(toon.cloudActors[0])
    cloud2 = MovieUtil.copyProp(toon.cloudActors[1])
    BattleParticles.loadParticles()
    rainEffect = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect2 = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect3 = BattleParticles.createParticleEffect(file = 'liquidate')
    cloudHeight = suit.height + 3
    cloudPosPoint = Point3(0, 0, cloudHeight)
    scaleUpPoint = Point3(3, 3, 3)
    rainEffects = [
        rainEffect,
        rainEffect2,
        rainEffect3]
    rainDelay = 1
    effectDelay = 0.3
    cloudHold = 1.7
    
    def getCloudIvals(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect):
        ivals = [
            FunctionInterval(MovieUtil.showProp, extraArgs = [
                cloud,
                suit,
                cloudPosPoint]),
            FunctionInterval(cloud.pose, extraArgs = [
                'cloud',
                0]),
            LerpScaleInterval(cloud, 1.5, scaleUpPoint, startScale = Point3(1e-005, 1e-005, 1e-005)),
            WaitInterval(rainDelay)]
        if useEffect == 1:
            pivals = []
            delay = 0
            for i in range(0, 3):
                dur = effectDelay * (3 - i) + cloudHold
                pivals.append(Track([
                    (delay, ParticleInterval(rainEffects[i], cloud, worldRelative = 0, duration = dur))]))
                delay += effectDelay
            
            pivals.append(Track([
                (3 * effectDelay, ActorInterval(cloud, 'cloud', startTime = 1, duration = cloudHold))]))
            ivals.append(MultiTrack(pivals))
        else:
            ivals.append(ActorInterval(cloud, 'cloud', startTime = 1, duration = cloudHold))
        ivals.append(LerpScaleInterval(cloud, 0.5, Point3(1e-005, 1e-005, 1e-005)))
        ivals.append(FunctionInterval(MovieUtil.removeProp, extraArgs = [
            cloud]))
        return Track(ivals)

    tracks.append(getCloudIvals(cloud, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 1))
    tracks.append(getCloudIvals(cloud2, suit, cloudPosPoint, scaleUpPoint, rainEffects, rainDelay, effectDelay, cloudHold, useEffect = 0))
    tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'squirt-small-react', died, leftSuits, rightSuits, battle, toon))
    return MultiTrack(tracks)

