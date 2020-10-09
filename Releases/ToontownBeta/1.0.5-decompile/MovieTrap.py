# Source Generated with Decompyle++
# File: MovieTrap.pyo (Python 2.0)

from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
import MovieUtil
import MovieCamera
import DirectNotifyGlobal
import ToontownBattleGlobals
import Actor
import BattleParticles
notify = DirectNotifyGlobal.directNotify.newCategory('MovieTrap')

def doTraps(traps):
    if len(traps) == 0:
        return (None, None)
    
    suitTrapsDict = { }
    for trap in traps:
        suitId = trap['target']['suit'].doId
        if suitTrapsDict.has_key(suitId):
            suitTrapsDict[suitId].append(trap)
        else:
            suitTrapsDict[suitId] = [
                trap]
    
    suitTrapLists = suitTrapsDict.values()
    ivals = []
    for trapList in suitTrapLists:
        trapPropList = []
        for i in range(len(trapList)):
            trap = trapList[i]
            level = trap['level']
            if level == 0:
                banana = globalPropPool.getProp('banana')
                banana2 = MovieUtil.copyProp(banana)
                trapPropList.append([
                    banana,
                    banana2])
            elif level == 1:
                rake = globalPropPool.getProp('rake')
                rake2 = MovieUtil.copyProp(rake)
                rake.pose('rake', 0)
                rake2.pose('rake', 0)
                trapPropList.append([
                    rake,
                    rake2])
            elif level == 2:
                marbles = globalPropPool.getProp('marbles')
                marbles2 = MovieUtil.copyProp(marbles)
                trapPropList.append([
                    marbles,
                    marbles2])
            elif level == 3:
                trapPropList.append([
                    globalPropPool.getProp('quicksand')])
            elif level == 4:
                trapPropList.append([
                    globalPropPool.getProp('trapdoor')])
            elif level == 5:
                tnt = globalPropPool.getProp('tnt')
                tnt2 = MovieUtil.copyProp(tnt)
                trapPropList.append([
                    tnt,
                    tnt2])
            else:
                notify.warning('__doTraps() - Incorrect trap level:                 %d' % level)
        
        if len(trapList) == 1:
            ival = __doTrapLevel(trapList[0], trapPropList[0])
            if ival:
                ivals.append(Track([
                    ival]))
            
        else:
            subIvals = []
            for i in range(len(trapList)):
                trap = trapList[i]
                trapProps = trapPropList[i]
                ival = __doTrapLevel(trap, trapProps, explode = 1)
                if ival:
                    subIvals.append(Track([
                        ival]))
                
            
            ivals.append(MultiTrack(subIvals))
    
    mtrack = MultiTrack(ivals)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseTrapShot(traps, camDuration)
    return (mtrack, camTrack)


def __doTrapLevel(trap, trapProps, explode = 0):
    level = trap['level']
    if level == 0:
        return __trapBanana(trap, trapProps, explode)
    elif level == 1:
        return __trapRake(trap, trapProps, explode)
    elif level == 2:
        return __trapMarbles(trap, trapProps, explode)
    elif level == 3:
        return __trapQuicksand(trap, trapProps, explode)
    elif level == 4:
        return __trapTrapdoor(trap, trapProps, explode)
    elif level == 5:
        return __trapTNT(trap, trapProps, explode)
    
    return None


def __createThrownTrapMultiTrack(trap, propList, propName, propPos = None, propHpr = None, anim = 0, explode = 0):
    toon = trap['toon']
    level = trap['level']
    battle = trap['battle']
    target = trap['target']
    suit = target['suit']
    targetPos = suit.getPos(battle)
    thrownProp = propList[0]
    unthrownProp = propList[1]
    torso = toon.style.torso
    torso = torso[0]
    if torso == 'l':
        throwDelay = 2.3
    elif torso == 'm':
        throwDelay = 2.3
    else:
        throwDelay = 1.9
    throwDuration = 0.9
    animBreakPoint = throwDelay + throwDuration
    animDelay = 3.1
    trapTrack = ToontownBattleGlobals.TRAP_TRACK
    trapTrackNames = ToontownBattleGlobals.AvProps[trapTrack]
    trapName = trapTrackNames[level]
    hands = toon.getRightHands()
    propIvals = []
    if propPos and propHpr:
        propIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs = [
            propList,
            hands,
            propPos,
            propHpr]))
    else:
        propIvals.append(FunctionInterval(MovieUtil.showProps, extraArgs = [
            propList,
            hands]))
    if anim == 1:
        pTracks = []
        for prop in propList:
            pTracks.append(Track([
                ActorInterval(prop, propName, duration = animBreakPoint)]))
        
        propIvals.append(MultiTrack(pTracks))
    
    throwIvals = []
    throwIvals.append(WaitInterval(throwDelay))
    throwIvals.append(FunctionInterval(unthrownProp.reparentTo, extraArgs = [
        hidden]))
    throwIvals.append(FunctionInterval(toon.update))
    if suit.battleTrap != NO_TRAP:
        notify.debug('trapSuit() - trap: %d destroyed existing trap: %d' % (level, suit.battleTrap))
        battle.removeTrap(suit)
    
    if trapName == 'rake':
        trapProp = globalPropPool.getProp('rake-react')
    else:
        trapProp = MovieUtil.copyProp(thrownProp)
    suit.battleTrapProp = trapProp
    suit.battleTrap = level
    if trapName == 'banana':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_DISTANCE)
        slidePoint = Vec3(trapPoint.getX(), trapPoint.getY() - 2, trapPoint.getZ())
        throwingTrack = Track(createThrowIvals(thrownProp, slidePoint, duration = 0.9, parent = battle))
        moveTrack = Track([
            LerpPosInterval(thrownProp, 0.8, pos = trapPoint, other = battle)])
        animTrack = Track([
            ActorInterval(thrownProp, propName, startTime = animBreakPoint)])
        slideTrack = MultiTrack([
            moveTrack,
            animTrack])
        motionTrack = Track([
            throwingTrack,
            slideTrack])
        hprTrack = Track([
            LerpHprInterval(thrownProp, 1.7, hpr = Point3(0, 0, 0))])
        scaleTrack = Track([
            LerpScaleInterval(thrownProp, 1.7, scale = Point3(1, 1, 1))])
        throwIvals.append(WaitInterval(0.25))
        throwIvals.append(FunctionInterval(thrownProp.wrtReparentTo, extraArgs = [
            suit]))
        throwIvals.append(MultiTrack([
            motionTrack,
            hprTrack,
            scaleTrack]))
    elif trapName == 'tnt':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_TNT_DISTANCE - 3.9)
        trapPoint.setZ(trapPoint.getZ() + 0.4)
        throwingTrack = Track(createThrowIvals(thrownProp, trapPoint, duration = throwDuration, parent = battle))
        hprTrack = Track([
            LerpHprInterval(thrownProp, 0.9, hpr = Point3(0, 90, 0))])
        scaleTrack = Track([
            LerpScaleInterval(thrownProp, 0.9, scale = Point3(1, 1, 1))])
        throwIvals.append(WaitInterval(0.2))
        throwIvals.append(MultiTrack([
            throwingTrack,
            hprTrack,
            scaleTrack]))
    elif trapName == 'marbles':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_MARBLES_DISTANCE)
        flingDuration = 0.2
        rollDuration = 1.0
        throwDuration = flingDuration + rollDuration
        landPoint = Point3(0, trapPoint.getY() + 2, trapPoint.getZ())
        throwPoint = Point3(0, trapPoint.getY(), trapPoint.getZ())
        moveTrack = Track([
            FunctionInterval(thrownProp.wrtReparentTo, extraArgs = [
                suit]),
            FunctionInterval(thrownProp.setHpr, extraArgs = [
                Point3(94, 0, 0)]),
            LerpPosInterval(thrownProp, flingDuration, pos = landPoint, other = suit),
            LerpPosInterval(thrownProp, rollDuration, pos = throwPoint, other = suit)])
        animTrack = Track([
            ActorInterval(thrownProp, propName, startTime = throwDelay + 0.9)])
        scaleTrack = Track([
            LerpScaleInterval(thrownProp, throwDuration, scale = Point3(1, 1, 1))])
        throwIvals.append(WaitInterval(0.2))
        throwIvals.append(MultiTrack([
            moveTrack,
            animTrack,
            scaleTrack]))
    elif trapName == 'rake':
        (trapPoint, trapHpr) = battle.getActorPosHpr(suit)
        trapPoint.setY(MovieUtil.SUIT_TRAP_RAKE_DISTANCE)
        throwDuration = 1.1
        throwingTrack = Track(createThrowIvals(thrownProp, trapPoint, duration = throwDuration, parent = suit))
        hprTrack = Track([
            LerpHprInterval(thrownProp, throwDuration, hpr = Point3(180, 90, -180))])
        scaleTrack = Track([
            LerpScaleInterval(thrownProp, 0.9, scale = Point3(0.7, 0.7, 0.7))])
        throwIvals.append(WaitInterval(0.2))
        throwIvals.append(MultiTrack([
            throwingTrack,
            hprTrack,
            scaleTrack]))
    else:
        notify.warning('__createThrownTrapMultiTrack() - Incorrect trap:                          %s thrown from toon' % trapName)
    
    def placeTrap(trapProp, suit, battle = battle, trapName = trapName):
        if not trapProp or trapProp.isEmpty():
            return None
        
        trapProp.wrtReparentTo(suit)
        if trapName == 'rake':
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_RAKE_DISTANCE, 0)
            trapProp.setHpr(Point3(0, 270, 0))
            trapProp.setScale(Point3(0.7, 0.7, 0.7))
            rakeOffset = MovieUtil.getSuitRakeOffset(suit)
            trapProp.setY(trapProp.getY() + rakeOffset)
        elif trapName == 'banana':
            trapProp.setHpr(0, 0, 0)
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_DISTANCE, -0.35)
            trapProp.pose(trapName, trapProp.getNumFrames(trapName) - 1)
        elif trapName == 'marbles':
            trapProp.setHpr(Point3(94, 0, 0))
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_MARBLES_DISTANCE, 0)
            trapProp.pose(trapName, trapProp.getNumFrames(trapName) - 1)
        elif trapName == 'tnt':
            trapProp.setHpr(0, 90, 0)
            trapProp.setPos(0, MovieUtil.SUIT_TRAP_TNT_DISTANCE, 0.4)
        else:
            notify.warning('placeTrap() - Incorrect trap: %s placed on a suit' % trapName)

    if explode == 1:
        print '**************should show explosion here when implemented'
        throwIvals.append(FunctionInterval(battle.removeTrap, extraArgs = [
            suit]))
    else:
        throwIvals.append(FunctionInterval(placeTrap, extraArgs = [
            trapProp,
            suit]))
        if trapName == 'tnt':
            tip = trapProp.find('**/joint-attachEmitter')
            sparks = BattleParticles.createParticleEffect(file = 'tnt')
            trapProp.sparksEffect = sparks
            throwIvals.append(FunctionInterval(BattleParticles.startParticleEffect, extraArgs = [
                sparks,
                tip,
                0]))
        
    throwIvals.append(FunctionInterval(MovieUtil.removeProps, extraArgs = [
        propList]))
    propTrack = Track(propIvals)
    if trapName == 'tnt':
        tip = thrownProp.find('**/joint-attachEmitter')
        sparks = BattleParticles.createParticleEffect(file = 'tnt')
        sparksIvals = Track([
            FunctionInterval(BattleParticles.startParticleEffect, extraArgs = [
                sparks,
                tip,
                0]),
            WaitInterval(throwDelay + throwDuration),
            FunctionInterval(BattleParticles.cleanupParticleEffect, extraArgs = [
                sparks])])
        throwTrack = MultiTrack([
            Track(throwIvals),
            sparksIvals])
    else:
        throwTrack = Track(throwIvals)
    toonTrack = Track([
        FunctionInterval(toon.headsUp, extraArgs = [
            battle,
            targetPos]),
        ActorInterval(toon, 'toss')])
    return MultiTrack([
        propTrack,
        throwTrack,
        toonTrack])


def __createPlacedTrapMultiTrack(trap, prop, propName, propPos = None, propHpr = None, explode = 0):
    toon = trap['toon']
    level = trap['level']
    battle = trap['battle']
    target = trap['target']
    suit = target['suit']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    targetPos = suitPos
    trapProp = prop
    trapPoint = Point3(0, MovieUtil.SUIT_TRAP_DISTANCE, 0)
    trapDelay = 2.5
    hands = toon.getLeftHands()
    if suit.battleTrap != NO_TRAP:
        notify.debug('trapSuit() - trap: %d destroyed existing trap: %d' % (level, suit.battleTrap))
        battle.removeTrap(suit)
    
    suit.battleTrapProp = trapProp
    suit.battleTrap = level
    trapIvals = []
    trapIvals.append(WaitInterval(trapDelay))
    trapIvals.append(FunctionInterval(trapProp.setScale, extraArgs = [
        Point3(0.1, 0.1, 0.1)]))
    trapIvals.append(FunctionInterval(trapProp.reparentTo, extraArgs = [
        suit]))
    trapIvals.append(FunctionInterval(trapProp.setPos, extraArgs = [
        trapPoint]))
    trapIvals.append(LerpScaleInterval(trapProp, 1.2, Point3(1.7, 1.7, 1.7)))
    if explode == 1:
        print '**************should show explosion here when implemented'
        trapTrack = Track([
            FunctionInterval(battle.removeTrap, extraArgs = [
                suit])])
    else:
        trapTrack = Track(trapIvals)
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [
        button,
        button2]
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
    toonTrack = Track(toonIvals)
    return MultiTrack([
        trapTrack,
        toonTrack])


def __trapBanana(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays banana peel in front of suit: %d' % (toon.getName(), suit.doId))
    bananas = trapProps
    return __createThrownTrapMultiTrack(trap, bananas, 'banana', anim = 1, explode = explode)


def __trapRake(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays rake in front of suit: %d' % (toon.getName(), suit.doId))
    rakes = trapProps
    return __createThrownTrapMultiTrack(trap, rakes, 'rake', anim = 1, explode = explode)


def __trapMarbles(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays marbles in front of suit: %d' % (toon.getName(), suit.doId))
    bothMarbles = trapProps
    pos = Point3(0, 0, 0)
    hpr = Point3(0, 0, 30)
    return __createThrownTrapMultiTrack(trap, bothMarbles, 'marbles', pos, hpr, anim = 1, explode = explode)


def __trapQuicksand(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays quicksand in front of suit: %d' % (toon.getName(), suit.doId))
    quicksand = trapProps[0]
    return __createPlacedTrapMultiTrack(trap, quicksand, 'quicksand', explode = explode)


def __trapTrapdoor(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays trapdoor in front of suit: %d' % (toon.getName(), suit.doId))
    trapdoor = trapProps[0]
    return __createPlacedTrapMultiTrack(trap, trapdoor, 'trapdoor', explode = explode)


def __trapTNT(trap, trapProps, explode):
    toon = trap['toon']
    suit = trap['target']['suit']
    notify.debug('toon: %s lays TNT in front of suit: %d' % (toon.getName(), suit.doId))
    tnts = trapProps
    return __createThrownTrapMultiTrack(trap, tnts, 'tnt', anim = 0, explode = explode)


def createThrowIvals(object, target, duration = 1.0, parent = render, gravity = -32.144):
    values = { }
    values['origin'] = None
    values['velocity'] = None
    
    def calcOriginAndVelocity(object = object, target = target, values = values, duration = duration, parent = parent, gravity = gravity):
        object.wrtReparentTo(parent)
        values['origin'] = object.getPos(parent)
        origin = object.getPos(parent)
        values['velocity'] = (target[2] - origin[2] - 0.5 * gravity * duration * duration) / duration

    
    def throwPos(t, object, duration, target, values = values, gravity = -32.144):
        if values['origin'] != None:
            origin = values['origin']
        else:
            origin = object.getPos()
        if values['velocity'] != None:
            velocity = values['velocity']
        else:
            velocity = 16
        x = origin[0] * (1 - t) + target[0] * t
        y = origin[1] * (1 - t) + target[1] * t
        time = t * duration
        z = origin[2] + velocity * time + 0.5 * gravity * time * time
        object.setPos(x, y, z)

    return [
        FunctionInterval(calcOriginAndVelocity),
        LerpFunctionInterval(throwPos, fromData = 0.0, toData = 1.0, duration = duration, extraArgs = [
            object,
            duration,
            target])]

