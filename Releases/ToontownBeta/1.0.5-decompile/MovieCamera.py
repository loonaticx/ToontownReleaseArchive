# Source Generated with Decompyle++
# File: MovieCamera.pyo (Python 2.0)

from PandaModules import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from ToontownBattleGlobals import *
from SuitBattleGlobals import *
import DirectNotifyGlobal
import whrandom
notify = DirectNotifyGlobal.directNotify.newCategory('MovieCamera')

def chooseHealShot(heals, attackDuration):
    openShot = chooseHealOpenShot(heals, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseHealCloseShot(heals, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseHealOpenShot(heals, attackDuration):
    numHeals = len(heals)
    av = None
    duration = 3.0
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseHealCloseShot(heals, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseTrapShot(traps, attackDuration):
    openShot = chooseTrapOpenShot(traps, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseTrapCloseShot(traps, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseTrapOpenShot(traps, attackDuration):
    numTraps = len(traps)
    av = None
    duration = 3.0
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseTrapCloseShot(traps, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseLureShot(lures, attackDuration):
    openShot = chooseLureOpenShot(lures, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseLureCloseShot(lures, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseLureOpenShot(lures, attackDuration):
    numLures = len(lures)
    av = None
    duration = 3.0
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseLureCloseShot(lures, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    shotChoices = [
        allGroupLowShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSoundShot(sounds, targets, attackDuration):
    openShot = chooseSoundOpenShot(sounds, targets, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseSoundCloseShot(sounds, targets, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseSoundOpenShot(sounds, targets, attackDuration):
    numSounds = len(sounds)
    av = None
    duration = 4.0
    if numSounds == 1:
        av = sounds[0]['toon']
        shotChoices = [
            avatarCloseUpThreeQuarterRightShot,
            avatarCloseUpThreeQuarterRightFollowShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSounds >= 2 and numSounds <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of sounds: %s' % numSounds)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSoundCloseShot(sounds, targets, openDuration, openName, attackDuration):
    numSuits = len(targets)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = targets[0]['suit']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseThrowShot(throws, suitThrowsDict, attackDuration):
    openShot = chooseThrowOpenShot(throws, suitThrowsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseThrowCloseShot(throws, suitThrowsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseThrowOpenShot(throws, suitThrowsDict, attackDuration):
    numThrows = len(throws)
    av = None
    duration = 3.0
    if numThrows == 1:
        av = throws[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numThrows >= 2 and numThrows <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of throws: %s' % numThrows)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseThrowCloseShot(throws, suitThrowsDict, openDuration, openName, attackDuration):
    numSuits = len(suitThrowsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitThrowsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSquirtShot(squirts, suitSquirtsDict, attackDuration):
    openShot = chooseSquirtOpenShot(squirts, suitSquirtsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseSquirtCloseShot(squirts, suitSquirtsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseSquirtOpenShot(squirts, suitSquirtsDict, attackDuration):
    numSquirts = len(squirts)
    av = None
    duration = 3.0
    if numSquirts == 1:
        av = squirts[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSquirts >= 2 and numSquirts <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of squirts: %s' % numSquirts)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSquirtCloseShot(squirts, suitSquirtsDict, openDuration, openName, attackDuration):
    numSuits = len(suitSquirtsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitSquirtsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseDropShot(drops, suitDropsDict, attackDuration):
    openShot = chooseDropOpenShot(drops, suitDropsDict, attackDuration)
    openDuration = openShot.getDuration()
    openName = openShot.getName()
    closeShot = chooseDropCloseShot(drops, suitDropsDict, openDuration, openName, attackDuration)
    track = Track([
        openShot,
        closeShot])
    return track


def chooseDropOpenShot(drops, suitDropsDict, attackDuration):
    numDrops = len(drops)
    av = None
    duration = 3.0
    if numDrops == 1:
        av = drops[0]['toon']
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterRightShot,
            avatarBehindShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numDrops >= 2 and numDrops <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of drops: %s' % numDrops)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseDropCloseShot(drops, suitDropsDict, openDuration, openName, attackDuration):
    numSuits = len(suitDropsDict)
    av = None
    duration = attackDuration - openDuration
    if numSuits == 1:
        av = toonbase.tcr.doId2do[suitDropsDict.keys()[0]]
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    elif numSuits >= 2 and numSuits <= 4:
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
    else:
        notify.error('Bad number of suits: %s' % numSuits)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseSuitShot(attack, attackDuration):
    groupStatus = attack['group']
    target = attack['target']
    if groupStatus == ATK_TGT_SINGLE:
        toon = target['toon']
    
    suit = attack['suit']
    name = attack['id']
    battle = attack['battle']
    camIvals = []
    
    def defaultCamera(suit = suit, attack = attack, attackDuration = attackDuration, openShotDuration = 3.5):
        shotChoices = [
            avatarCloseUpThrowShot,
            avatarCloseUpThreeQuarterLeftShot,
            allGroupLowShot,
            suitGroupLowLeftShot,
            avatarBehindHighShot]
        if openShotDuration > attackDuration:
            openShotDuration = attackDuration
        
        openShot = apply(whrandom.choice(shotChoices), [
            suit,
            openShotDuration])
        closeShot = chooseSuitCloseShot(attack, openShot.getDuration(), openShot.getName(), attackDuration)
        return Track([
            openShot,
            closeShot])

    if name == AUDIT:
        camIvals.append(defaultCamera())
    elif name == BOUNCE_CHECK:
        camIvals.append(defaultCamera())
    elif name == BRAIN_STORM:
        camIvals.append(defaultCamera(openShotDuration = 2.4))
    elif name == BUZZ_WORD:
        camIvals.append(defaultCamera(openShotDuration = 4.7))
    elif name == CALCULATE:
        camIvals.append(defaultCamera())
    elif name == CLIPON_TIE:
        camIvals.append(defaultCamera(openShotDuration = 3.3))
    elif name == DEMOTION:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == DOUBLE_TALK:
        camIvals.append(defaultCamera(openShotDuration = 3.9))
    elif name == EVICTION_NOTICE:
        camIvals.append(defaultCamera(openShotDuration = 3.2))
    elif name == FILIBUSTER:
        camIvals.append(defaultCamera(openShotDuration = 2.7))
    elif name == FILL_WITH_LEAD:
        camIvals.append(defaultCamera(openShotDuration = 3.2))
    elif name == FINGER_WAG:
        camIvals.append(defaultCamera(openShotDuration = 2.3))
    elif name == FIRED:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == FOUNTAIN_PEN:
        camIvals.append(defaultCamera(openShotDuration = 2.6))
    elif name == FREEZE_ASSETS:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == GLOWER_POWER:
        camIvals.append(defaultCamera(openShotDuration = 1.4))
    elif name == HANG_UP:
        camIvals.append(defaultCamera(openShotDuration = 5.1))
    elif name == HOT_AIR:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == JARGON:
        camIvals.append(defaultCamera())
    elif name == LIQUIDATE:
        camIvals.append(defaultCamera(openShotDuration = 2.5))
    elif name == MUMBO_JUMBO:
        camIvals.append(defaultCamera(openShotDuration = 2.8))
    elif name == PICK_POCKET:
        camIvals.append(defaultCamera(openShotDuration = 1.6))
    elif name == POUND_KEY:
        camIvals.append(defaultCamera(openShotDuration = 2.8))
    elif name == RAZZLE_DAZZLE:
        camIvals.append(defaultCamera(openShotDuration = 2.2))
    elif name == RED_TAPE:
        camIvals.append(defaultCamera())
    elif name == ROLODEX:
        camIvals.append(defaultCamera())
    elif name == RUBBER_STAMP:
        camIvals.append(defaultCamera(openShotDuration = 3.2))
    elif name == RUB_OUT:
        camIvals.append(defaultCamera(openShotDuration = 2.2))
    elif name == SCHMOOZE:
        camIvals.append(defaultCamera(openShotDuration = 2.8))
    elif name == SHAKE:
        shakeIntensity = 1.75
        camIvals.append(apply(suitCameraShakeShot, [
            suit,
            4.1,
            shakeIntensity]))
    elif name == SHRED:
        camIvals.append(defaultCamera(openShotDuration = 4.1))
    elif name == SYNERGY:
        camIvals.append(defaultCamera(openShotDuration = 1.7))
    elif name == TABULATE:
        camIvals.append(defaultCamera())
    elif name == TEE_OFF:
        camIvals.append(defaultCamera(openShotDuration = 4.5))
    elif name == WATERCOOLER:
        camIvals.append(defaultCamera())
    elif name == WITHDRAWAL:
        camIvals.append(defaultCamera(openShotDuration = 1.2))
    elif name == WRITE_OFF:
        camIvals.append(defaultCamera())
    else:
        notify.warning('unknown attack id in chooseSuitShot: %d using default cam' % name)
        camIvals.append(defaultCamera())
    camTrack = Track(camIvals)
    pbpText = attack['playByPlayText']
    pbpTrack = pbpText.getShowInterval(attack['name'], 3.5, suitText = 1)
    return MultiTrack([
        camTrack,
        pbpTrack])


def chooseSuitCloseShot(attack, openDuration, openName, attackDuration):
    av = None
    duration = attackDuration - openDuration
    if duration < 0:
        duration = 1e-006
    
    groupStatus = attack['group']
    diedTrack = None
    if groupStatus == ATK_TGT_SINGLE:
        av = attack['target']['toon']
        shotChoices = [
            avatarCloseUpThreeQuarterRightShot,
            suitGroupThreeQuarterLeftBehindShot]
        died = attack['target']['died']
        if died != 0:
            pbpText = attack['playByPlayText']
            diedText = av.getName() + ' was defeated!'
            diedTextList = [
                diedText]
            diedTrack = pbpText.getToonsDiedInterval(diedTextList, duration)
        
    elif groupStatus == ATK_TGT_GROUP:
        av = None
        shotChoices = [
            allGroupLowShot,
            suitGroupThreeQuarterLeftBehindShot]
        deadToons = []
        targetDicts = attack['target']
        for targetDict in targetDicts:
            died = targetDict['died']
            if died != 0:
                deadToons.append(targetDict['toon'])
            
        
        if len(deadToons) > 0:
            pbpText = attack['playByPlayText']
            diedTextList = []
            for toon in deadToons:
                pbpText = attack['playByPlayText']
                diedTextList.append(toon.getName() + ' was defeated!')
            
            diedTrack = pbpText.getToonsDiedInterval(diedTextList, duration)
        
    else:
        notify.error('Bad groupStatus: %s' % groupStatus)
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    if diedTrack == None:
        return track
    else:
        mtrack = MultiTrack([
            track,
            diedTrack])
        return mtrack


def makeShot(x, y, z, h, p, r, duration, other = None, name = 'madeShot'):
    if other:
        return heldRelativeShot(other, x, y, z, h, p, r, duration, name)
    else:
        return heldShot(x, y, z, h, p, r, duration, name)


def focusShot(x, y, z, duration, target, other = None, name = 'focusShot'):
    ivals = []
    if other:
        ivals.append(FunctionInterval(camera.setPos, extraArgs = [
            other,
            Point3(x, y, z)]))
    else:
        ivals.append(FunctionInterval(camera.setPos, extraArgs = [
            Point3(x, y, z)]))
    ivals.append(FunctionInterval(camera.lookAt, extraArgs = [
        target]))
    ivals.append(WaitInterval(duration))
    return Track(ivals)


def moveShot(x, y, z, h, p, r, duration, other = None, name = 'moveShot'):
    return motionShot(x, y, z, h, p, r, duration, other, name)


def focusMoveShot(x, y, z, duration, target, other = None, name = 'focusMoveShot'):
    camera.setPos(Point3(x, y, z))
    camera.lookAt(target)
    hpr = camera.getHpr()
    return motionShot(x, y, z, hpr[0], hpr[1], hpr[2], duration, other, name)


def chooseSOSShot(av, duration):
    shotChoices = [
        avatarCloseUpThreeQuarterRightShot,
        avatarBehindShot,
        avatarBehindHighShot,
        suitGroupThreeQuarterLeftBehindShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def chooseRewardShot(av, duration):
    shotChoices = [
        avatarCloseUpShot,
        avatarCloseUpThreeQuarterRightShot]
    track = apply(whrandom.choice(shotChoices), [
        av,
        duration])
    return track


def heldShot(x, y, z, h, p, r, duration, name = 'heldShot'):
    intervalList = []
    intervalList.append(FunctionInterval(camera.setPosHpr, extraArgs = [
        x,
        y,
        z,
        h,
        p,
        r]))
    intervalList.append(WaitInterval(duration))
    track = Track(intervalList, name)
    return track


def heldRelativeShot(other, x, y, z, h, p, r, duration, name = 'heldRelativeShot'):
    intervalList = []
    intervalList.append(FunctionInterval(camera.setPosHpr, extraArgs = [
        other,
        x,
        y,
        z,
        h,
        p,
        r]))
    intervalList.append(WaitInterval(duration))
    track = Track(intervalList, name)
    return track


def motionShot(x, y, z, h, p, r, duration, other = None, name = 'motionShot'):
    if other:
        posTrack = Track([
            LerpPosInterval(camera, duration, pos = Point3(x, y, z), other = other)])
        hprTrack = Track([
            LerpHprInterval(camera, duration, hpr = Point3(h, p, r), other = other)])
    else:
        posTrack = Track([
            LerpPosInterval(camera, duration, pos = Point3(x, y, z))])
        hprTrack = Track([
            LerpHprInterval(camera, duration, hpr = Point3(h, p, r))])
    return MultiTrack([
        posTrack,
        hprTrack])


def allGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 89, -30, 0, duration, 'allGroupShot')


def allGroupLowShot(avatar, duration):
    return heldShot(10, 0, 3, 89, 0, 0, duration, 'allGroupLowShot')


def toonGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 115, -30, 0, duration, 'toonGroupShot')


def suitGroupShot(avatar, duration):
    return heldShot(10, 0, 10, 65, -30, 0, duration, 'suitGroupShot')


def suitGroupLowLeftShot(avatar, duration):
    return heldShot(8.4, -3.85, 2.75, 36.3, 3.25, 0, duration, 'suitGroupLowLeftShot')


def suitGroupThreeQuarterLeftBehindShot(avatar, duration):
    return heldShot(9.37, 10.0, 5.56, 134.61, -2.7, 0, duration, 'suitGroupThreeQuarterLeftBehindShot')


def suitWakeUpShot(avatar, duration):
    return heldShot(10, -5, 10, 65, -30, 0, duration, 'suitWakeUpShot')


def suitCameraShakeShot(avatar, duration, shakeIntensity):
    intervalList = []
    shakeDelay = 0.3
    shakeDuration = 0.1
    shakeWaitInterval = 0.67
    numTimes = 4
    holdTime = duration - shakeDelay - (shakeDuration + shakeWaitInterval) * numTimes
    if holdTime <= 0:
        holdTime = 1e-005
    
    
    def shakeCameraIvals(intensity, duration = shakeDuration, numTimes = numTimes, waitInterval = shakeWaitInterval):
        ivals = []
        for i in range(0, numTimes):
            ivals.extend([
                WaitInterval(waitInterval),
                FunctionInterval(camera.setZ, extraArgs = [
                    camera.getZ() + intensity / 2]),
                WaitInterval(duration / 2),
                FunctionInterval(camera.setZ, extraArgs = [
                    camera.getZ() - intensity]),
                WaitInterval(duration / 2),
                FunctionInterval(camera.setZ, extraArgs = [
                    camera.getZ() + intensity / 2])])
        
        return ivals

    intervalList.append(FunctionInterval(camera.setPosHpr, extraArgs = [
        10,
        -5,
        10,
        65,
        -30,
        0]))
    intervalList.append(WaitInterval(shakeDelay))
    intervalList.extend(shakeCameraIvals(shakeIntensity))
    intervalList.append(WaitInterval(holdTime))
    return Track(intervalList, 'suitShakeCameraShot')


def avatarCloseUpShot(avatar, duration):
    return heldRelativeShot(avatar, 0, 8, avatar.getHeight() * 0.66, 179, 15, 0, duration, 'avatarCloseUpShot')


def avatarCloseUpThrowShot(avatar, duration):
    return heldRelativeShot(avatar, 0, 8, avatar.getHeight() * 0.66, 179, 3.6, 0, duration, 'avatarCloseUpThrowShot')


def avatarCloseUpThreeQuarterRightShot(avatar, duration):
    return heldRelativeShot(avatar, 5.2, 5.45, avatar.getHeight() * 0.66, 131.5, 3.6, 0, duration, 'avatarCloseUpThreeQuarterRightShot')


def avatarCloseUpThreeQuarterLeftShot(avatar, duration):
    return heldRelativeShot(avatar, -5.2, 5.45, avatar.getHeight() * 0.66, -131.5, 3.6, 0, duration, 'avatarCloseUpThreeQuarterLeftShot')


def avatarCloseUpThreeQuarterRightFollowShot(avatar, duration):
    intervalList = []
    intervalList.append(heldRelativeShot(avatar, 5.2, 5.45, avatar.getHeight() * 0.66, 131.5, 3.6, 0, duration * 0.65))
    intervalList.append(LerpHprInterval(node = camera, other = avatar, duration = duration * 0.2, hpr = Point3(110, 3.6, 0), blendType = 'easeInOut'))
    intervalList.append(WaitInterval(duration * 0.25))
    track = Track(intervalList, 'avatarCloseUpThreeQuarterRightFollowShot')
    return track


def avatarCloseUpZoomShot(avatar, duration):
    intervalList = []
    intervalList.append(LerpPosHprInterval(node = camera, other = avatar, duration = duration / 2, startPos = Point3(0, 10, avatar.getHeight()), startHpr = Point3(179, -10, 0), pos = Point3(0, 6, avatar.getHeight()), hpr = Point3(179, -10, 0), blendType = 'easeInOut'))
    intervalList.append(WaitInterval(duration / 2))
    track = Track(intervalList, 'avatarCloseUpZoomShot')
    return track


def avatarBehindShot(avatar, duration):
    return heldRelativeShot(avatar, 0, -7, avatar.getHeight(), 0, -12, 0, duration, 'avatarBehindShot')


def avatarBehindHighShot(avatar, duration):
    return heldRelativeShot(avatar, 0, -7, 5 + avatar.getHeight(), 0, -35, 0, duration, 'avatarBehindHighShot')


def avatarBehindThreeQuarterRightShot(avatar, duration):
    return heldRelativeShot(avatar, 7.67, -8.52, avatar.getHeight() * 0.66, 25, 7.5, 0, duration, 'avatarBehindThreeQuarterRightShot')


def avatarSideFollowThrow(suit, toon, duration, battle, throwDelay = 2.7, throwDuration = 1.2):
    if throwDelay + throwDuration > duration:
        throwDelay = duration / 2.0
        throwDuration = duration / 4.0
    
    watchDuration = duration - throwDelay - throwDuration
    suitHeadPoint = suit.getPos(battle)
    suitHeadPoint.setZ(suitHeadPoint.getZ() + suit.getHeight())
    toonHeadPoint = toon.getPos(battle)
    toonHeadPoint.setZ(toonHeadPoint.getZ() + toon.getHeight())
    return Track([
        focusShot(whrandom.randint(12, 14), whrandom.randint(-1, 1), suit.getHeight() - 2, throwDelay, suitHeadPoint),
        focusMoveShot(whrandom.randint(7, 8), whrandom.randint(-1, 1), suit.getHeight() - 2, throwDuration, toonHeadPoint),
        WaitInterval(watchDuration)])


def avatarSidePanThrow(suit, toon, duration, battle):
    throwDelay = duration * (1 / 5.0)
    throwDuration = duration * (3 / 5.0)
    return avatarSideFollowThrow(suit, toon, duration, battle, throwDelay, throwDuration)

