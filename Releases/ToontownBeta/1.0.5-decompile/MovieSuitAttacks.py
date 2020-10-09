# Source Generated with Decompyle++
# File: MovieSuitAttacks.pyo (Python 2.0)

from ToontownGlobals import *
from SuitBattleGlobals import *
from IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from AvatarDNA import *
from BattleBase import *
import MovieCamera
import DirectNotifyGlobal
import MovieUtil
import BattleParticles
import Toon
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSuitAttacks')

def __doDamage(toon, dmg, died):
    if dmg > 0:
        if died != 0:
            hp = 0
        else:
            hp = toon.hp - dmg
        if hp > 0 or died != 0:
            notify.debug('setting toon: %s hp: %d' % (toon.getName(), hp))
            toon.setHp(hp)
        else:
            notify.warning('__doDamage() - hp: %d' % hp)
    


def __showProp(prop, parent, pos, hpr = None, scale = None):
    prop.reparentTo(parent)
    prop.setPos(pos)
    if hpr:
        prop.setHpr(hpr)
    
    if scale:
        prop.setScale(scale)
    


def __animProp(prop, propName, propType = 'actor'):
    if 'actor' == propType:
        prop.play(propName)
    elif 'model' == propType:
        pass
    else:
        self.notify.error('No such propType as: %s' % propType)


def __hideProp(prop, propPool):
    prop.reparentTo(hidden)


def __suitFacePoint(suit, zOffset = 0):
    pnt = suit.getPos()
    pnt.setZ(pnt[2] + suit.shoulderHeight + 0.3 + zOffset)
    return Point3(pnt)


def __toonFacePoint(toon, zOffset = 0):
    pnt = toon.getPos()
    pnt.setZ(pnt[2] + toon.shoulderHeight + 0.3 + zOffset)
    return Point3(pnt)


def __toonTorsoPoint(toon, zOffset = 0):
    pnt = toon.getPos()
    pnt.setZ(pnt[2] + toon.shoulderHeight - 0.2)
    return Point3(pnt)


def __toonGroundPoint(attack, toon, zOffset = 0):
    pnt = toon.getPos()
    battle = attack['battle']
    pnt.setZ(battle.getZ() + zOffset)
    return Point3(pnt)


def __toonGroundMissPoint(attack, prop, toon, zOffset = 0):
    point = __toonMissPoint(prop, toon)
    battle = attack['battle']
    point.setZ(battle.getZ() + zOffset)
    return Point3(point)


def __toonMissPoint(prop, toon, yOffset = 0, parent = None):
    if parent:
        p = __toonFacePoint(toon) - prop.getPos(parent)
    else:
        p = __toonFacePoint(toon) - prop.getPos()
    v = Vec3(p)
    baseDistance = v.length()
    v.normalize()
    if parent:
        endPos = prop.getPos(parent) + v * (baseDistance + 5 + yOffset)
    else:
        endPos = prop.getPos() + v * (baseDistance + 5 + yOffset)
    return Point3(endPos)


def __throwBounceHitPoint(prop, toon):
    startPoint = prop.getPos()
    endPoint = __toonFacePoint(toon)
    return __throwBouncePoint(startPoint, endPoint)


def __throwBounceMissPoint(prop, toon):
    startPoint = prop.getPos()
    endPoint = __toonFacePoint(toon)
    return __throwBouncePoint(startPoint, endPoint)


def __throwBouncePoint(startPoint, endPoint):
    midPoint = startPoint + (endPoint - startPoint) / 2.0
    midPoint.setZ(0)
    return Point3(midPoint)


def doSuitAttack(attack):
    notify.debug('building suit attack in doSuitAttack: %s' % attack['name'])
    name = attack['id']
    if name == AUDIT:
        suitTrack = doAudit(attack)
    elif name == BOUNCE_CHECK:
        suitTrack = doBounceCheck(attack)
    elif name == BRAIN_STORM:
        suitTrack = doBrainStorm(attack)
    elif name == BUZZ_WORD:
        suitTrack = doBuzzWord(attack)
    elif name == CALCULATE:
        suitTrack = doCalculate(attack)
    elif name == CLIPON_TIE:
        suitTrack = doClipOnTie(attack)
    elif name == DEMOTION:
        suitTrack = doDemotion(attack)
    elif name == DOUBLE_TALK:
        suitTrack = doDoubleTalk(attack)
    elif name == EVICTION_NOTICE:
        suitTrack = doEvictionNotice(attack)
    elif name == FILIBUSTER:
        suitTrack = doFilibuster(attack)
    elif name == FILL_WITH_LEAD:
        suitTrack = doFillWithLead(attack)
    elif name == FINGER_WAG:
        suitTrack = doFingerWag(attack)
    elif name == FIRED:
        suitTrack = doFired(attack)
    elif name == FOUNTAIN_PEN:
        suitTrack = doFountainPen(attack)
    elif name == FREEZE_ASSETS:
        suitTrack = doFreezeAssets(attack)
    elif name == GLOWER_POWER:
        suitTrack = doGlowerPower(attack)
    elif name == HANG_UP:
        suitTrack = doHangUp(attack)
    elif name == HOT_AIR:
        suitTrack = doHotAir(attack)
    elif name == JARGON:
        suitTrack = doJargon(attack)
    elif name == LIQUIDATE:
        suitTrack = doLiquidate(attack)
    elif name == MUMBO_JUMBO:
        suitTrack = doMumboJumbo(attack)
    elif name == PICK_POCKET:
        suitTrack = doPickPocket(attack)
    elif name == POUND_KEY:
        suitTrack = doPoundKey(attack)
    elif name == RAZZLE_DAZZLE:
        suitTrack = doRazzleDazzle(attack)
    elif name == RED_TAPE:
        suitTrack = doRedTape(attack)
    elif name == ROLODEX:
        suitTrack = doRolodex(attack)
    elif name == RUBBER_STAMP:
        suitTrack = doRubberStamp(attack)
    elif name == RUB_OUT:
        suitTrack = doRubOut(attack)
    elif name == SCHMOOZE:
        suitTrack = doSchmooze(attack)
    elif name == SHAKE:
        suitTrack = doShake(attack)
    elif name == SHRED:
        suitTrack = doShred(attack)
    elif name == SYNERGY:
        suitTrack = doSynergy(attack)
    elif name == TABULATE:
        suitTrack = doTabulate(attack)
    elif name == TEE_OFF:
        suitTrack = doTeeOff(attack)
    elif name == WATERCOOLER:
        suitTrack = doWatercooler(attack)
    elif name == WITHDRAWAL:
        suitTrack = doWithdrawal(attack)
    elif name == WRITE_OFF:
        suitTrack = doWriteOff(attack)
    else:
        notify.warning('unknown attack: %d substituting Finger Wag' % name)
        suitTrack = doDefault(attack)
    camTrack = MovieCamera.chooseSuitShot(attack, suitTrack.getDuration())
    suit = attack['suit']
    neutralIval = FunctionInterval(suit.loop, extraArgs = [
        'neutral'])
    suitTrack = Track([
        suitTrack,
        neutralIval])
    battle = attack['battle']
    suit = attack['suit']
    suitPos = suit.getPos(battle)
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    if battle.isSuitLured(suit):
        resetTrack = getResetTrack(suit, battle)
        resetSuitTrack = Track([
            resetTrack,
            suitTrack])
        waitTrack = Track([
            WaitInterval(resetTrack.getDuration()),
            FunctionInterval(battle.unlureSuit, extraArgs = [
                suit])])
        resetCamTrack = Track([
            waitTrack,
            camTrack])
        return (resetSuitTrack, resetCamTrack)
    else:
        return (suitTrack, camTrack)


def getResetTrack(suit, battle):
    (resetPos, resetHpr) = battle.getActorPosHpr(suit)
    moveDist = Vec3(suit.getPos(battle) - resetPos).length()
    moveDuration = 0.5
    walkTrack = Track([
        FunctionInterval(suit.setHpr, extraArgs = [
            battle,
            resetHpr]),
        ActorInterval(suit, 'walk', startTime = 1, duration = moveDuration, endTime = 1e-005),
        FunctionInterval(suit.loop, extraArgs = [
            'neutral'])])
    moveTrack = Track([
        LerpPosInterval(suit, moveDuration, resetPos, other = battle)])
    return MultiTrack([
        walkTrack,
        moveTrack])


def __makeCancelledNodePath():
    tn = TextNode('CANCELLED')
    tn.setFont(getSuitFont())
    tn.setText('CANCELLED\nCANCELLED\nCANCELLED')
    tn.setAlign(TMALIGNCENTER)
    tntop = hidden.attachNewNode('CancelledTop')
    tnpath = tntop.attachNewNode(tn)
    tnpath.setPosHpr(0, 0, 0, 0, 0, 0)
    tnpath.setScale(1)
    tnpath.setColor(0.7, 0, 0, 1)
    tnpathback = tnpath.instanceTo(tntop)
    tnpathback.setPosHpr(0, 0, 0, 180, 0, 0)
    tnpath.setScale(1)
    return tntop


def __makeCheckmarkNodePath():
    tn = TextNode('CHECK')
    tn.setFont(getSuitFont())
    tn.setText('CHECK')
    tn.setAlign(TMALIGNCENTER)
    BattleParticles.loadParticles()
    texture = BattleParticles.getParticle('checkmark')
    print '**********texture=', texture
    tntop = hidden.attachNewNode('CheckmarkTop')
    tnpath = tntop.attachNewNode(tn)
    tnpath.setPosHpr(0, 0, 0, 0, 0, 0)
    tnpath.setScale(1)
    tnpath.setColor(0, 0, 0.7, 1)
    tnpathback = tnpath.instanceTo(tntop)
    tnpathback.setPosHpr(0, 0, 0, 180, 0, 0)
    tnpath.setScale(1)
    return tntop


def __checkPreFlight(prop, toon):
    prop.wrtReparentTo(render)
    endPoint = __toonFacePoint(toon)
    prop.lookAtPreserveScale(endPoint)
    prop.setP(prop, -90)
    return None


def doDefault(attack):
    notify.debug('building suit attack in doDefault')
    suitName = attack['suitName']
    if suitName == 'f':
        attack['name'] = 'PoundKey'
        attack['animName'] = 'phone'
        return doPoundKey(attack)
    elif suitName == 'p':
        attack['name'] = 'FountainPen'
        attack['animName'] = 'pen-squirt'
        return doFountainPen(attack)
    elif suitName == 'ym':
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'mm':
        attack['name'] = 'FingerWag'
        attack['animName'] = 'finger-wag'
        return doFingerWag(attack)
    elif suitName == 'cc':
        attack['name'] = 'PoundKey'
        attack['animName'] = 'phone'
        return doPoundKey(attack)
    elif suitName == 'tm':
        attack['name'] = 'ClipOnTie'
        attack['animName'] = 'throw-paper'
        return doClipOnTie(attack)
    elif suitName == 'nd':
        attack['name'] = 'PickPocket'
        attack['animName'] = 'pickpocket'
        return doPickPocket(attack)
    elif suitName == 'gh':
        attack['name'] = 'FountainPen'
        attack['animName'] = 'pen-squirt'
        return doFountainPen(attack)
    elif suitName == 'sc':
        attack['name'] = 'Watercooler'
        attack['animName'] = 'water-cooler'
        return doWatercooler(attack)
    elif suitName == 'pp':
        attack['name'] = 'BounceCheck'
        attack['animName'] = 'throw-paper'
        return doBounceCheck(attack)
    elif suitName == 'tw':
        attack['name'] = 'GlowerPower'
        attack['animName'] = 'glower'
        return doGlowerPower(attack)
    elif suitName == 'bc':
        attack['name'] = 'Audit'
        attack['animName'] = 'phone'
        return doAudit(attack)
    elif suitName == 'bf':
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'b':
        attack['name'] = 'EvictionNotice'
        attack['animName'] = 'throw-paper'
        return doEvictionNotice(attack)
    elif suitName == 'dt':
        attack['name'] = 'RubberStamp'
        attack['animName'] = 'rubber-stamp'
        return doRubberStamp(attack)
    elif suitName == 'ac':
        attack['name'] = 'RedTape'
        attack['animName'] = 'throw-object'
        return doRedTape(attack)
    else:
        self.notify.error('doDefault() - unsupported suit type: %s' % suitName)
    return None


def getSuitTrack(attack, delay = 1e-006):
    suit = attack['suit']
    battle = attack['battle']
    tauntIndex = attack['taunt']
    target = attack['target']
    toon = target['toon']
    targetPos = toon.getPos(battle)
    taunt = getAttackTaunt(attack['name'], tauntIndex)
    trapStorage = { }
    trapStorage['trap'] = None
    ivals = [
        WaitInterval(delay),
        FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout])]
    
    def reparentTrap(suit = suit, battle = battle, trapStorage = trapStorage):
        trapProp = suit.battleTrapProp
        if trapProp != None:
            trapProp.wrtReparentTo(battle)
            trapStorage['trap'] = trapProp
        

    ivals.append(FunctionInterval(reparentTrap))
    ivals.append(FunctionInterval(suit.headsUp, extraArgs = [
        battle,
        targetPos]))
    ivals.append(ActorInterval(suit, attack['animName']))
    (origPos, origHpr) = battle.getActorPosHpr(suit)
    ivals.append(FunctionInterval(suit.setHpr, extraArgs = [
        battle,
        origHpr]))
    
    def returnTrapToSuit(suit = suit, trapStorage = trapStorage):
        trapProp = trapStorage['trap']
        if trapProp != None:
            trapProp.wrtReparentTo(suit)
            suit.battleTrapProp = trapProp
        

    ivals.append(FunctionInterval(returnTrapToSuit))
    ivals.append(FunctionInterval(suit.clearChat))
    return Track(ivals)


def getSuitAnimTrack(attack, delay = 0):
    suit = attack['suit']
    tauntIndex = attack['taunt']
    taunt = getAttackTaunt(attack['name'], tauntIndex)
    return Track([
        WaitInterval(delay),
        FunctionInterval(suit.setChatAbsolute, extraArgs = [
            taunt,
            CFSpeech | CFTimeout]),
        ActorInterval(attack['suit'], attack['animName']),
        FunctionInterval(suit.clearChat)])


def getPartTrack(particleEffect, startDelay, durationDelay, partExtraArgs):
    particleEffect = partExtraArgs[0]
    parent = partExtraArgs[1]
    if len(partExtraArgs) > 2:
        worldRelative = partExtraArgs[2]
    else:
        worldRelative = 1
    return Track([
        (startDelay, ParticleInterval(particleEffect, parent, worldRelative, duration = durationDelay))])


def getToonTrack(attack, damageDelay = 1e-006, damageAnimNames = None, dodgeDelay = 1e-006, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None, target = None):
    if not target:
        target = attack['target']
    
    toon = target['toon']
    battle = attack['battle']
    suit = attack['suit']
    targetPos = suit.getPos(battle)
    dmg = target['hp']
    ivals = []
    ivals.append(FunctionInterval(toon.headsUp, extraArgs = [
        battle,
        targetPos]))
    if dmg > 0:
        ivals.extend(getToonTakeDamageIntervals(toon, target['died'], dmg, damageDelay, damageAnimNames, splicedDamageAnims))
        return Track(ivals)
    else:
        toonAnims = []
        toonAnims.append(WaitInterval(dodgeDelay))
        if dodgeAnimNames:
            for d in dodgeAnimNames:
                if d == 'sidestep':
                    d = 'sidestep-left'
                
                toonAnims.append(ActorInterval(toon, d))
            
        else:
            toonAnims.extend(getSplicedAnims(splicedDodgeAnims, actor = toon))
        toonAnims.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
        ivals.extend(toonAnims)
        return Track(ivals)


def getToonTracks(attack, damageDelay = 1e-006, damageAnimNames = None, dodgeDelay = 1e-006, dodgeAnimNames = None, splicedDamageAnims = None, splicedDodgeAnims = None):
    toonTracks = []
    for t in attack['target']:
        toonTracks.append(getToonTrack(attack, damageDelay, damageAnimNames, dodgeDelay, dodgeAnimNames, splicedDamageAnims, splicedDodgeAnims, target = t))
    
    return toonTracks


def getPropTrack(prop, parent, posPoints, appearDelay, remainDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, scaleDownTime = 0.5, startScale = Point3(0.01), anim = 0, propName = 'none', animDuration = 0.0, animStartTime = 0.0, onlyIvals = 0):
    extraArgsForShowProp = [
        prop,
        parent]
    extraArgsForShowProp.extend(posPoints)
    if anim == 1:
        ivals = [
            WaitInterval(appearDelay),
            FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale),
            ActorInterval(prop, propName, duration = animDuration, startTime = animStartTime),
            WaitInterval(remainDelay),
            FunctionInterval(__hideProp, extraArgs = [
                prop,
                globalPropPool])]
    else:
        ivals = [
            WaitInterval(appearDelay),
            FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
            LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale),
            WaitInterval(remainDelay),
            LerpScaleInterval(prop, scaleDownTime, Point3(0, 0, 0)),
            FunctionInterval(__hideProp, extraArgs = [
                prop,
                globalPropPool])]
    if onlyIvals == 1:
        return ivals
    else:
        return Track(ivals)


def getPropAppearIntervals(prop, parent, posPoints, appearDelay, scaleUpPoint = Point3(1), scaleUpTime = 0.5, startScale = Point3(0.01), poseExtraArgs = []):
    showPropExtraArgs = [
        prop,
        parent]
    showPropExtraArgs.extend(posPoints)
    propIvals = [
        WaitInterval(appearDelay),
        FunctionInterval(__showProp, extraArgs = showPropExtraArgs)]
    if poseExtraArgs != []:
        propIvals.append(FunctionInterval(prop.pose, extraArgs = poseExtraArgs))
    
    propIvals.append(LerpScaleInterval(prop, scaleUpTime, scaleUpPoint, startScale = startScale))
    return propIvals


def getPropThrowIntervals(attack, prop, hitPoints = [], missPoints = [], hitDuration = 0.5, missDuration = 0.5, hitPointNames = 'none', missPointNames = 'none', lookAt = 'none', groundPointOffSet = 0):
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    
    def getLambdas(list, prop, toon):
        for i in range(len(list)):
            if list[i] == 'face':
                
                list[i] = lambda toon = toon: __toonFacePoint(toon)
            elif list[i] == 'miss':
                
                list[i] = lambda prop = prop, toon = toon: __toonMissPoint(prop, toon)
            elif list[i] == 'bounceHit':
                
                list[i] = lambda prop = prop, toon = toon: __throwBounceHitPoint(prop, toon)
            elif list[i] == 'bounceMiss':
                
                list[i] = lambda prop = prop, toon = toon: __throwBounceMissPoint(prop, toon)
            
        
        return list

    if hitPointNames != 'none':
        hitPoints = getLambdas(hitPointNames, prop, toon)
    
    if missPointNames != 'none':
        missPoints = getLambdas(missPointNames, prop, toon)
    
    propIvals = []
    propIvals.append(FunctionInterval(prop.wrtReparentTo, extraArgs = [
        render]))
    if lookAt != 'none':
        propIvals.append(FunctionInterval(prop.lookAt, extraArgs = lookAt))
    
    if dmg > 0:
        for i in range(len(hitPoints)):
            pos = hitPoints[i]
            propIvals.append(LerpPosInterval(prop, hitDuration, pos = pos))
        
    else:
        for i in range(len(missPoints)):
            pos = missPoints[i]
            propIvals.append(LerpPosInterval(prop, missDuration, pos = pos))
        
    propIvals.append(FunctionInterval(__hideProp, extraArgs = [
        prop,
        globalPropPool]))
    return propIvals


def getThrowIvals(object, target, duration = 1.0, parent = render, gravity = -32.144):
    values = { }
    
    def calcOriginAndVelocity(object = object, target = target, values = values, duration = duration, parent = parent, gravity = gravity):
        object.wrtReparentTo(parent)
        values['origin'] = object.getPos(parent)
        origin = object.getPos(parent)
        values['velocity'] = (target[2] - origin[2] - 0.5 * gravity * duration * duration) / duration

    return [
        FunctionInterval(calcOriginAndVelocity),
        LerpFunctionInterval(throwPos, fromData = 0.0, toData = 1.0, duration = duration, extraArgs = [
            object,
            duration,
            target,
            values,
            gravity])]


def throwPos(t, object, duration, target, values, gravity = -32.144):
    origin = values['origin']
    velocity = values['velocity']
    x = origin[0] * (1 - t) + target[0] * t
    y = origin[1] * (1 - t) + target[1] * t
    time = t * duration
    z = origin[2] + velocity * time + 0.5 * gravity * time * time
    object.setPos(x, y, z)


def getToonTakeDamageIntervals(toon, died, dmg, delay, damageAnimNames = None, splicedDamageAnims = None):
    toonIvals = []
    toonIvals.append(WaitInterval(delay))
    if damageAnimNames:
        toonIvals.append(FunctionInterval(__doDamage, extraArgs = [
            toon,
            dmg,
            died]))
        for d in damageAnimNames:
            toonIvals.append(ActorInterval(toon, d))
        
    else:
        splicedAnims = getSplicedAnims(splicedDamageAnims, actor = toon)
        firstAnim = splicedAnims[0]
        remainingAnims = splicedAnims[1:]
        toonIvals.append(firstAnim)
        toonIvals.append(FunctionInterval(__doDamage, extraArgs = [
            toon,
            dmg,
            died]))
        toonIvals.extend(remainingAnims)
    if died != 0:
        loseIval = ActorInterval(toon, 'lose')
        delay = loseIval.getDuration() * 0.8
        shrinkDur = loseIval.getDuration() * 0.2
        toonIvals.append(MultiTrack([
            Track([
                loseIval]),
            Track([
                (delay, LerpScaleInterval(toon, shrinkDur, Point3(0, 0, 0)))])]))
        toonIvals.append(FunctionInterval(toon.reparentTo, extraArgs = [
            hidden]))
        toonIvals.append(FunctionInterval(toon.setScale, extraArgs = [
            Point3(1, 1, 1)]))
    else:
        toonIvals.append(FunctionInterval(toon.loop, extraArgs = [
            'neutral']))
    return toonIvals


def getToonsDodgeTracks(attack, delay, dodgeAnimNames):
    target = attack['target']
    dmg = target['hp']
    toonDodgeTracks = []
    if dmg > 0:
        return []
    
    for t in target['leftToons']:
        toonAnimTrack = []
        for d in dodgeAnimNames:
            if d == 'sidestep':
                d = 'sidestep-left'
            
            toonAnimTrack.append((delay, ActorInterval(t, d)))
        
        toonAnimTrack.append(FunctionInterval(t.loop, extraArgs = [
            'neutral']))
        toonDodgeTracks.append(Track(toonAnimTrack))
    
    return toonDodgeTracks


def getSplicedAnims(anims, actor = None):
    ivals = []
    for nextAnim in anims:
        delay = 1e-006
        if len(nextAnim) >= 2:
            if nextAnim[1] > 0:
                delay = nextAnim[1]
            
        
        if len(nextAnim) <= 0:
            ivals.append(WaitInterval(delay))
        elif len(nextAnim) == 1:
            ivals.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 2:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(actor, nextAnim[0]))
        elif len(nextAnim) == 3:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2]))
        elif len(nextAnim) == 4:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(actor, nextAnim[0], startTime = nextAnim[2], duration = nextAnim[3]))
        elif len(nextAnim) == 5:
            ivals.append(WaitInterval(delay))
            ivals.append(ActorInterval(nextAnim[4], nextAnim[0], startTime = nextAnim[2], duration = nextAnim[3]))
        
    
    return ivals


def getSplicedLerpAnims(animName, origDuration, newDuration, startTime = 0, fps = 30):
    ivals = []
    addition = 0
    numIvals = origDuration * fps
    timeInterval = newDuration / numIvals
    animInterval = origDuration / numIvals
    for i in range(0, numIvals):
        ivals.append([
            animName,
            timeInterval,
            startTime + addition,
            animInterval])
        addition += animInterval
    
    return ivals


def doClipOnTie(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tie = globalPropPool.getProp('clip-on-tie')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        throwDelay = 2.17
        damageDelay = 3.3
        dodgeDelay = 3.1
    elif suitType == 'b':
        throwDelay = 2.17
        damageDelay = 3.3
        dodgeDelay = 3.1
    elif suitType == 'c':
        throwDelay = 1.45
        damageDelay = 2.61
        dodgeDelay = 2.34
    
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.66, 0.51, 0.28),
        Point3(-26.56, 68.2, -98.13)]
    tiePropIvals = getPropAppearIntervals(tie, suit.getRightHand(), posPoints, 0.5, Point3(1, 1, 1), scaleUpTime = 0.5, poseExtraArgs = [
        'clip-on-tie',
        0])
    if dmg > 0:
        tiePropIvals.append(ActorInterval(tie, 'clip-on-tie', duration = throwDelay, startTime = 1.1))
    else:
        tiePropIvals.append(WaitInterval(throwDelay))
    tiePropIvals.extend(getPropThrowIntervals(attack, tie, [
        __toonFacePoint(toon)], [
        __toonGroundPoint(attack, toon, 0.9)], hitDuration = 0.4, missDuration = 0.8))
    tiePropTrack = Track(tiePropIvals)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        tiePropTrack] + toonDodgeTracks)


def doPoundKey(attack):
    suit = attack['suit']
    phone = globalPropPool.getProp('phone')
    receiver = globalPropPool.getProp('receiver')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('PoundKey')
    BattleParticles.setEffectTexture(particleEffect, 'poundsign', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1, 1.55, [
        particleEffect,
        suit,
        0])
    phonePosPoints = [
        Point3(0.23, 0.17, -0.11),
        Point3(-6.05, -2.51, 177.58)]
    receiverPosPoints = [
        Point3(0.23, 0.17, -0.11),
        Point3(-6.05, -2.51, 177.58)]
    propTrack = Track([
        WaitInterval(0.3),
        FunctionInterval(__showProp, extraArgs = [
            phone,
            suit.getLeftHand(),
            phonePosPoints[0],
            phonePosPoints[1]]),
        FunctionInterval(__showProp, extraArgs = [
            receiver,
            suit.getLeftHand(),
            receiverPosPoints[0],
            receiverPosPoints[1]]),
        LerpScaleInterval(phone, 0.5, Point3(1, 1, 1), Point3(0, 0, 0)),
        WaitInterval(0.74),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            suit.getRightHand()]),
        LerpPosHprInterval(receiver, 0.0001, Point3(-0.45, 0.48, -0.62), Point3(-82.57, 71.11, -89.48)),
        WaitInterval(3.14),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            phone]),
        WaitInterval(0.62),
        LerpScaleInterval(phone, 0.5, Point3(0, 0, 0)),
        FunctionInterval(__hideProp, extraArgs = [
            receiver,
            globalPropPool]),
        FunctionInterval(__hideProp, extraArgs = [
            phone,
            globalPropPool])])
    toonTrack = getToonTrack(attack, 2.7, [
        'cringe'], 1.9, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 1.9, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        partTrack] + toonDodgeTracks)


def doShred(attack):
    suit = attack['suit']
    paper = globalPropPool.getProp('shredder-paper')
    shredder = globalPropPool.getProp('shredder')
    particleEffect = BattleParticles.createParticleEffect('Shred')
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 3.5, 1.9, [
        particleEffect,
        suit,
        0])
    paperPosPoints = [
        Point3(0.59, -0.31, 0.81),
        Point3(-79.51, -30.07, 177.45)]
    paperPropTrack = getPropTrack(paper, suit.getRightHand(), paperPosPoints, 2.4, 1e-005, scaleUpTime = 0.2, anim = 1, propName = 'shredder-paper', animDuration = 1.5, animStartTime = 2.8)
    shredderPosPoints = [
        Point3(0, -0.12, -0.34),
        Point3(-90.0, -48.44, -5.33)]
    shredderPropTrack = getPropTrack(shredder, suit.getLeftHand(), shredderPosPoints, 1, 3, scaleUpPoint = Point3(4.81, 4.81, 4.81))
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.1, [
        'conked'], suitTrack.getDuration() - 3.1, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, suitTrack.getDuration() - 3.1, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        paperPropTrack,
        shredderPropTrack,
        partTrack,
        toonTrack] + toonDodgeTracks)


def doFillWithLead(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pencil = globalPropPool.getProp('pencil')
    sharpener = globalPropPool.getProp('sharpener')
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSpray')
    headSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    torsoSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    legsSmotherEffect = BattleParticles.createParticleEffect(file = 'fillWithLeadSmother')
    BattleParticles.setEffectTexture(sprayEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(headSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(torsoSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(legsSmotherEffect, 'roll-o-dex', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, 2.5, 1.9, [
        sprayEffect,
        suit,
        0])
    pencilPosPoints = [
        Point3(-0.29, -0.33, -0.13),
        Point3(-158.75, 7.71, -168.69)]
    pencilPropTrack = getPropTrack(pencil, suit.getRightHand(), pencilPosPoints, 0.7, 3.2, scaleUpTime = 0.2)
    sharpenerPosPoints = [
        Point3(0.0, 0.0, -0.03),
        Point3(0.0, 0.0, 0.0)]
    sharpenerPropTrack = getPropTrack(sharpener, suit.getLeftHand(), sharpenerPosPoints, 1.3, 2.3, scaleUpPoint = Point3(1.0, 1.0, 1.0))
    damageAnims = []
    damageAnims.append([
        'conked',
        suitTrack.getDuration() - 1.5,
        1e-005,
        1.4])
    damageAnims.append([
        'conked',
        1e-005,
        0.7,
        0.7])
    damageAnims.append([
        'conked',
        1e-005,
        0.7,
        0.7])
    damageAnims.append([
        'conked',
        1e-005,
        1.4])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = suitTrack.getDuration() - 3.1, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, suitTrack.getDuration() - 3.1, [
        'sidestep'])
    animal = toon.style.getAnimal()
    bodyScale = Toon.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = Toon.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = Toon.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
    legsEffectHeight = legsHeight / 2
    effectX = headSmotherEffect.getX()
    effectY = headSmotherEffect.getY()
    headSmotherEffect.setPos(effectX, effectY - 1.5, headEffectHeight)
    torsoSmotherEffect.setPos(effectX, effectY - 1, torsoEffectHeight)
    legsSmotherEffect.setPos(effectX, effectY - 0.6, legsEffectHeight)
    partDelay = 3.5
    partIvalDelay = 0.7
    partDuration = 1.0
    headTrack = getPartTrack(headSmotherEffect, partDelay, partDuration, [
        headSmotherEffect,
        toon,
        0])
    torsoTrack = getPartTrack(torsoSmotherEffect, partDelay + partIvalDelay, partDuration, [
        torsoSmotherEffect,
        toon,
        0])
    legsTrack = getPartTrack(legsSmotherEffect, partDelay + partIvalDelay * 2, partDuration, [
        legsSmotherEffect,
        toon,
        0])
    
    def colorParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        colorIvals = []
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals.append(WaitInterval(partDelay + 0.2))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(colorParts(headParts))
        colorIvals.append(WaitInterval(partIvalDelay))
        colorIvals.extend(colorParts(torsoParts))
        colorIvals.append(WaitInterval(partIvalDelay))
        colorIvals.extend(colorParts(legsParts))
        colorIvals.append(WaitInterval(2.5))
        colorIvals.extend(resetParts(headParts))
        colorIvals.extend(resetParts(torsoParts))
        colorIvals.extend(resetParts(legsParts))
        colorTrack = Track(colorIvals)
        return MultiTrack([
            suitTrack,
            pencilPropTrack,
            sharpenerPropTrack,
            sprayTrack,
            headTrack,
            torsoTrack,
            legsTrack,
            colorTrack,
            toonTrack] + toonDodgeTracks)
    else:
        return MultiTrack([
            suitTrack,
            pencilPropTrack,
            sharpenerPropTrack,
            sprayTrack,
            toonTrack] + toonDodgeTracks)


def doFountainPen(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pen = globalPropPool.getProp('pen')
    
    def getPenTip(pen = pen):
        tip = pen.find('**/joint-toSpray')
        return tip.getPos(render)

    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    
    missPoint = lambda prop = pen, toon = toon: __toonMissPoint(prop, toon, 0, parent = render)
    hitSprayIvals = MovieUtil.getSprayIntervals(Point4(0, 0, 0, 0), getPenTip, hitPoint, 0.2, 0.2, 0.2, horizScale = 0.1, vertScale = 0.1)
    missSprayIvals = MovieUtil.getSprayIntervals(Point4(0, 0, 0, 0), getPenTip, missPoint, 0.2, 0.2, 0.2, horizScale = 0.1, vertScale = 0.1)
    suitTrack = getSuitTrack(attack)
    propIvals = [
        WaitInterval(0.01),
        FunctionInterval(__showProp, extraArgs = [
            pen,
            suit.getRightHand(),
            Point3(0, 0, 0)]),
        LerpScaleInterval(pen, 0.5, Point3(1.5, 1.5, 1.5)),
        WaitInterval(1.6)]
    if dmg > 0:
        propIvals += hitSprayIvals
    else:
        propIvals += missSprayIvals
    propIvals += [
        WaitInterval(0.01),
        LerpScaleInterval(pen, 0.5, Point3(0, 0, 0)),
        FunctionInterval(__hideProp, extraArgs = [
            pen,
            globalPropPool])]
    propTrack = Track(propIvals)
    splashTrack = []
    if dmg > 0:
        
        def prepSplash(splash, targetPoint):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(scale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setColor(0, 0, 0, 1)
        splash.setScale(0.15)
        splashIvals = [
            (2.2, FunctionInterval(prepSplash, extraArgs = [
                splash,
                __toonFacePoint(toon)])),
            ActorInterval(splash, 'splash-from-splat')]
        headParts = toon.getHeadParts()
        splashIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashIvals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        splashIvals.append(FunctionInterval(splash.reparentTo, extraArgs = [
            hidden]))
        splashIvals.append(WaitInterval(2.6))
        for partNum in range(0, headParts.getNumPaths()):
            nextPart = headParts.getPath(partNum)
            splashIvals.append(FunctionInterval(nextPart.clearColorScale))
        
        splashTrack.append(Track(splashIvals))
    
    toonTrack = getToonTrack(attack, 2.55, [
        'conked'], 0.2, [
        'duck'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack] + splashTrack)


def doRubOut(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    pad = globalPropPool.getProp('pad')
    pencil = globalPropPool.getProp('pencil')
    headEffect = BattleParticles.createParticleEffect(file = 'demotionUnFreeze')
    torsoEffect = BattleParticles.createParticleEffect(file = 'demotionUnFreeze')
    legsEffect = BattleParticles.createParticleEffect(file = 'demotionUnFreeze')
    suitTrack = getSuitTrack(attack)
    padPosPoints = [
        Point3(-0.66, 0.81, -0.06),
        Point3(-14.93, 2.29, 180.0)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.57)
    pencilPosPoints = [
        Point3(0.04, -0.38, -0.1),
        Point3(-172.25, 7.06, -63.73)]
    pencilPropTrack = getPropTrack(pencil, suit.getRightHand(), pencilPosPoints, 0.5, 2.57)
    toonTrack = getToonTrack(attack, 2.2, [
        'conked'], 2.0, [
        'jump'])
    hideIvals = []
    headParts = toon.getHeadParts()
    torsoParts = toon.getTorsoParts()
    legsParts = toon.getLegsParts()
    animal = toon.style.getAnimal()
    bodyScale = Toon.toonBodyScales[animal]
    headEffectHeight = __toonFacePoint(toon).getZ()
    legsHeight = Toon.legHeightDict[toon.style.legs] * bodyScale
    torsoEffectHeight = Toon.torsoHeightDict[toon.style.torso] * bodyScale / 2 + legsHeight
    legsEffectHeight = legsHeight / 2
    effectX = headEffect.getX()
    effectY = headEffect.getY()
    headEffect.setPos(effectX, effectY - 1.5, headEffectHeight)
    torsoEffect.setPos(effectX, effectY - 1, torsoEffectHeight)
    legsEffect.setPos(effectX, effectY - 0.6, legsEffectHeight)
    partDelay = 2.5
    headTrack = getPartTrack(headEffect, partDelay + 0, 0.5, [
        headEffect,
        toon,
        0])
    torsoTrack = getPartTrack(torsoEffect, partDelay + 1.1, 0.5, [
        torsoEffect,
        toon,
        0])
    legsTrack = getPartTrack(legsEffect, partDelay + 2.2, 0.5, [
        legsEffect,
        toon,
        0])
    
    def hideParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setTransparency, extraArgs = [
                1]))
            ivals.append(LerpFunctionInterval(nextPart.setAlphaScale, fromData = 1, toData = 0, duration = 0.2))
        
        return ivals

    
    def showParts(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
            ivals.append(FunctionInterval(nextPart.clearTransparency))
        
        return ivals

    if dmg > 0:
        hideIvals.append(WaitInterval(2.2))
        hideIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        hideIvals.extend(hideParts(headParts))
        hideIvals.append(WaitInterval(0.4))
        hideIvals.extend(hideParts(torsoParts))
        hideIvals.append(WaitInterval(0.4))
        hideIvals.extend(hideParts(legsParts))
        hideIvals.append(WaitInterval(1))
        hideIvals.extend(showParts(headParts))
        hideIvals.extend(showParts(torsoParts))
        hideIvals.extend(showParts(legsParts))
        hideTrack = Track(hideIvals)
        return MultiTrack([
            suitTrack,
            toonTrack,
            padPropTrack,
            pencilPropTrack,
            hideTrack,
            headTrack,
            torsoTrack,
            legsTrack])
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            padPropTrack,
            pencilPropTrack])


def doFingerWag(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('FingerWag')
    BattleParticles.setEffectTexture(particleEffect, 'blah', color = Vec4(0, 0, 0, 1))
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.3
        damageDelay = 2.7
        dodgeDelay = 1.7
    elif suitType == 'b':
        partDelay = 1.3
        damageDelay = 2.7
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 1.3
        damageDelay = 2.7
        dodgeDelay = 2.0
    
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay, 2, [
        particleEffect,
        suit,
        0])
    suitName = attack['suitName']
    if suitName == 'mm':
        particleEffect.setPos(0.167, 1.5, 2.731)
    elif suitName == 'tw':
        particleEffect.setPos(0.167, 1.8, 5)
        particleEffect.setHpr(90.0, -120, -0.019)
    elif suitName == 'pp':
        particleEffect.setPos(0.167, 1, 4.1)
    
    toonTrack = getToonTrack(attack, damageDelay, [
        'slip-backward'], dodgeDelay, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack] + toonDodgeTracks)


def doWriteOff(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    pad = globalPropPool.getProp('pad')
    pencil = globalPropPool.getProp('pencil')
    checkmark = __makeCheckmarkNodePath()
    suitTrack = getSuitTrack(attack)
    padPosPoints = [
        Point3(-0.25, 1.38, -0.08),
        Point3(19.83, 3.64, 171.12)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 0.5, 2.57, Point3(1.89, 1.89, 1.89))
    
    missPoint = lambda checkmark = checkmark, toon = toon: __toonMissPoint(checkmark, toon)
    pencilPosPoints = [
        Point3(-0.47, 1.08, 0.28),
        Point3(-21.8, -11.31, 176.19)]
    extraArgsForShowProp = [
        pencil,
        suit.getRightHand()]
    extraArgsForShowProp.extend(pencilPosPoints)
    pencilPropIvals = [
        WaitInterval(0.5),
        FunctionInterval(__showProp, extraArgs = extraArgsForShowProp),
        LerpScaleInterval(pencil, 0.5, Point3(1.5, 1.5, 1.5), startScale = Point3(0.01)),
        WaitInterval(2),
        FunctionInterval(checkmark.reparentTo, extraArgs = [
            render]),
        FunctionInterval(checkmark.setScale, extraArgs = [
            0.6]),
        FunctionInterval(checkmark.setPosHpr, extraArgs = [
            pencil,
            0,
            0,
            0,
            0,
            0,
            0]),
        FunctionInterval(checkmark.setP, extraArgs = [
            0]),
        FunctionInterval(checkmark.setR, extraArgs = [
            0])]
    pencilPropIvals.extend(getPropThrowIntervals(attack, checkmark, [
        __toonFacePoint(toon)], [
        missPoint]))
    pencilPropIvals.append(FunctionInterval(checkmark.removeNode))
    pencilPropIvals.append(WaitInterval(0.3))
    pencilPropIvals.append(LerpScaleInterval(pencil, 0.5, Point3(0, 0, 0)))
    pencilPropIvals.append(FunctionInterval(__hideProp, extraArgs = [
        pencil,
        globalPropPool]))
    pencilPropTrack = Track(pencilPropIvals)
    toonTrack = getToonTrack(attack, 3.4, [
        'slip-forward'], 2.4, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 2.4, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        padPropTrack,
        pencilPropTrack] + toonDodgeTracks)


def doRubberStamp(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    suitTrack = getSuitTrack(attack)
    stamp = globalPropPool.getProp('rubber-stamp')
    pad = globalPropPool.getProp('pad')
    cancelled = __makeCancelledNodePath()
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        padPosPoints = [
            Point3(-0.65, 0.83, -0.04),
            Point3(-6.58, -2.86, 165.07)]
        stampPosPoints = [
            Point3(-0.64, -0.17, -0.03),
            Point3(0, 0, 0)]
    elif suitType == 'c':
        padPosPoints = [
            Point3(0.19, -0.55, -0.21),
            Point3(-166.65, -3.61, -1.7)]
        stampPosPoints = [
            Point3(-0.64, -0.08, 0.11),
            Point3(0, 0, 0)]
    else:
        padPosPoints = [
            Point3(-0.65, 0.83, -0.04),
            Point3(-6.58, -2.86, 165.07)]
        stampPosPoints = [
            Point3(-0.64, -0.17, -0.03),
            Point3(0, 0, 0)]
    padPropTrack = getPropTrack(pad, suit.getLeftHand(), padPosPoints, 1e-006, 3.2)
    
    missPoint = lambda cancelled = cancelled, toon = toon: __toonMissPoint(cancelled, toon)
    propIvals = [
        FunctionInterval(__showProp, extraArgs = [
            stamp,
            suit.getRightHand(),
            stampPosPoints[0],
            stampPosPoints[1]]),
        LerpScaleInterval(stamp, 0.5, Point3(1, 1, 1)),
        WaitInterval(2.6),
        FunctionInterval(cancelled.reparentTo, extraArgs = [
            render]),
        FunctionInterval(cancelled.setScale, extraArgs = [
            0.6]),
        FunctionInterval(cancelled.setPosHpr, extraArgs = [
            stamp,
            0.81,
            -1.11,
            -0.16,
            0,
            0,
            270]),
        FunctionInterval(cancelled.setP, extraArgs = [
            0]),
        FunctionInterval(cancelled.setR, extraArgs = [
            0])]
    propIvals.extend(getPropThrowIntervals(attack, cancelled, [
        __toonFacePoint(toon)], [
        missPoint]))
    propIvals.append(FunctionInterval(cancelled.removeNode))
    propIvals.append(WaitInterval(0.3))
    propIvals.append(LerpScaleInterval(stamp, 0.5, Point3(0, 0, 0)))
    propIvals.append(FunctionInterval(__hideProp, extraArgs = [
        stamp,
        globalPropPool]))
    propTrack = Track(propIvals)
    toonTrack = getToonTrack(attack, 3.4, [
        'conked'], 1.9, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 1.9, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        padPropTrack] + toonDodgeTracks)


def doRazzleDazzle(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    hp = target['hp']
    hitSuit = hp > 0
    sign = globalPropPool.getProp('smile')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Smile')
    suitTrack = getSuitTrack(attack)
    signPosPoints = [
        Point3(0.0, -0.42, -0.04),
        Point3(171.09, 85.66, 14.78)]
    if hitSuit:
        
        hitPoint = lambda toon = toon: __toonFacePoint(toon)
    else:
        
        hitPoint = lambda sign = sign, toon = toon, suit = suit: __toonMissPoint(sign, toon, parent = suit.getRightHand())
    signPropIvals = [
        WaitInterval(0.5),
        FunctionInterval(__showProp, extraArgs = [
            sign,
            suit.getRightHand(),
            signPosPoints[0],
            signPosPoints[1]]),
        LerpScaleInterval(sign, 0.5, Point3(1.39, 1.39, 1.39)),
        WaitInterval(0.5),
        FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
            particleEffect]),
        FunctionInterval(BattleParticles.startParticleEffect, extraArgs = [
            particleEffect,
            sign,
            0]),
        FunctionInterval(particleEffect.wrtReparentTo, extraArgs = [
            render]),
        LerpPosInterval(particleEffect, 2.0, pos = hitPoint),
        FunctionInterval(BattleParticles.cleanupParticleEffect, extraArgs = [
            particleEffect]),
        FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
            particleEffect])]
    signPropTrack = Track(signPropIvals)
    signPropAnimInterval = [
        ActorInterval(sign, 'smile', duration = 4, startTime = 0)]
    signPropAnimTrack = Track(signPropAnimInterval)
    toonTrack = getToonTrack(attack, 2.6, [
        'cringe'], 1.9, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 1.9, [
        'sidestep'])
    multiTrack = MultiTrack([
        suitTrack,
        signPropTrack,
        signPropAnimTrack,
        toonTrack] + toonDodgeTracks)
    finalIvals = [
        multiTrack,
        FunctionInterval(__hideProp, extraArgs = [
            sign,
            globalPropPool])]
    finalTrack = Track(finalIvals)
    return finalTrack


def doSynergy(attack):
    suit = attack['suit']
    particleEffect = BattleParticles.createParticleEffect('Synergy')
    waterfallEffect = BattleParticles.createParticleEffect('Waterfall')
    suitTrack = getSuitAnimTrack(attack)
    partTrack = getPartTrack(particleEffect, 1.0, 1.9, [
        particleEffect,
        suit,
        0])
    waterfallTrack = getPartTrack(waterfallEffect, 0.8, 1.9, [
        waterfallEffect,
        suit,
        0])
    damageAnims = [
        [
            'slip-forward',
            1.8]]
    dodgeAnims = []
    dodgeAnims.append([
        'jump',
        0.91,
        0,
        0.6])
    dodgeAnims.extend(getSplicedLerpAnims('jump', 0.31, 1.3, startTime = 0.6))
    dodgeAnims.append([
        'jump',
        0,
        0.91])
    toonTracks = getToonTracks(attack, splicedDamageAnims = damageAnims, splicedDodgeAnims = dodgeAnims)
    return MultiTrack([
        suitTrack,
        partTrack,
        waterfallTrack] + toonTracks)


def doTeeOff(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    club = globalPropPool.getProp('golf-club')
    ball = globalPropPool.getProp('golf-ball')
    suitTrack = getSuitTrack(attack)
    clubPosPoints = [
        Point3(0, 0, 0),
        Point3(48.3, 60.7, 20.0)]
    clubPropTrack = getPropTrack(club, suit.getLeftHand(), clubPosPoints, 0.5, 5.2, Point3(1.1, 1.1, 1.1))
    ballPosPoints = [
        Point3(2.1, 0, 0.1)]
    ballIvals = getPropAppearIntervals(ball, suit, ballPosPoints, 1.7, Point3(1.5, 1.5, 1.5))
    ballIvals.append(FunctionInterval(ball.wrtReparentTo, extraArgs = [
        render]))
    ballIvals.append(WaitInterval(2.15))
    
    missPoint = lambda ball = ball, toon = toon: __toonMissPoint(ball, toon)
    ballIvals.extend(getPropThrowIntervals(attack, ball, [
        __toonFacePoint(toon)], [
        missPoint]))
    ballPropTrack = Track(ballIvals)
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 2.25, [
        'conked'], suitTrack.getDuration() - 4.35, [
        'duck'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        clubPropTrack,
        ballPropTrack])


def doBrainStorm(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    BattleParticles.loadParticles()
    snowEffect = BattleParticles.createParticleEffect('BrainStorm')
    snowEffect2 = BattleParticles.createParticleEffect('BrainStorm')
    snowEffect3 = BattleParticles.createParticleEffect('BrainStorm')
    BattleParticles.setEffectTexture(snowEffect, 'brainstorm-box', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(snowEffect2, 'brainstorm-env', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(snowEffect3, 'brainstorm-track', color = Vec4(0, 0, 0, 1))
    cloud = MovieUtil.copyProp(toon.cloudActors[0])
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.3
    elif suitType == 'b':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.3
    elif suitType == 'c':
        partDelay = 1.2
        damageDelay = 4.5
        dodgeDelay = 3.3
    
    suitTrack = getSuitTrack(attack, delay = 0.9)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        Point3(180, 0, 0)]
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'cloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 1e-006, Point3(3, 3, 3), scaleUpTime = 0.7))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    pivals = []
    pivals.append(Track([
        ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.5)]))
    pivals.append(Track([
        (0.5, ParticleInterval(snowEffect2, cloud, worldRelative = 0, duration = 2.0))]))
    pivals.append(Track([
        (1.0, ParticleInterval(snowEffect3, cloud, worldRelative = 0, duration = 1.5))]))
    pivals.append(Track([
        ActorInterval(cloud, 'cloud', startTime = 3, duration = 0.5),
        ActorInterval(cloud, 'cloud', startTime = 2.5, duration = 0.5),
        ActorInterval(cloud, 'cloud', startTime = 1, duration = 1.5)]))
    cloudIvals.append(MultiTrack(pivals))
    cloudIvals.append(WaitInterval(0.4))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, Point3(1e-005, 1e-005, 1e-005)))
    cloudIvals.append(FunctionInterval(__hideProp, extraArgs = [
        cloud,
        globalPropPool]))
    cloudPropTrack = Track(cloudIvals)
    damageAnims = [
        [
            'cringe',
            damageDelay,
            0.4,
            0.8],
        [
            'duck',
            1e-006,
            1.6]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        cloudPropTrack] + toonDodgeTracks)


def doBuzzWord(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('BuzzWord')
    particleEffect2 = BattleParticles.createParticleEffect('BuzzWord')
    particleEffect3 = BattleParticles.createParticleEffect('BuzzWord')
    particleEffect4 = BattleParticles.createParticleEffect('BuzzWord')
    particleEffect5 = BattleParticles.createParticleEffect('BuzzWord')
    BattleParticles.setEffectTexture(particleEffect, 'buzzwords-crash', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'buzzwords-inc', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect3, 'buzzwords-main', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect4, 'buzzwords-over', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect5, 'buzzwords-syn', color = Vec4(0, 0, 0, 1))
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 4.0
        partDuration = 2.2
        damageDelay = 4.5
        dodgeDelay = 3.8
    elif suitType == 'b':
        partDelay = 1.3
        partDuration = 2
        damageDelay = 2.5
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 4.0
        partDuration = 2.2
        damageDelay = 4.5
        dodgeDelay = 3.8
    
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay, partDuration, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, partDelay, partDuration, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, partDelay, partDuration, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, partDelay, partDuration, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, partDelay, partDuration, [
        particleEffect5,
        suit,
        0])
    toonTrack = getToonTrack(attack, splicedDamageAnims = [
        [
            'cringe',
            damageDelay]], splicedDodgeAnims = [
        [
            'duck',
            dodgeDelay,
            1.4]])
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5])


def doDemotion(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    sprayEffect = BattleParticles.createParticleEffect('DemotionSpray')
    freezeEffect = BattleParticles.createParticleEffect('DemotionFreeze')
    unFreezeEffect = BattleParticles.createParticleEffect(file = 'demotionUnFreeze')
    facePoint = __toonFacePoint(toon)
    freezeEffect.setPos(0, 0, facePoint.getZ())
    unFreezeEffect.setPos(0, 0, facePoint.getZ())
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(sprayEffect, 0.7, 1.1, [
        sprayEffect,
        suit,
        0])
    partTrack2 = getPartTrack(freezeEffect, 1.4, 2.9, [
        freezeEffect,
        toon,
        0])
    partTrack3 = getPartTrack(unFreezeEffect, 6.65, 0.5, [
        unFreezeEffect,
        toon,
        0])
    dodgeAnims = [
        [
            'duck',
            1e-006,
            0.8]]
    damageAnims = []
    damageAnims.append([
        'cringe',
        1.0,
        0,
        0.5])
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.4, 0.5, startTime = 0.5))
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.3, 0.5, startTime = 0.9))
    damageAnims.extend(getSplicedLerpAnims('cringe', 0.3, 0.6, startTime = 1.2))
    damageAnims.append([
        'cringe',
        2.6,
        1.5])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, splicedDodgeAnims = dodgeAnims)
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            partTrack,
            partTrack2,
            partTrack3,
            toonTrack])
    else:
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack])


def doGlowerPower(attack):
    suit = attack['suit']
    leftKnives = []
    rightKnives = []
    for i in range(0, 3):
        leftKnives.append(globalPropPool.getProp('dagger'))
        rightKnives.append(globalPropPool.getProp('dagger'))
    
    suitTrack = getSuitTrack(attack)
    leftPosPoints = [
        Point3(1, 4.1, 4),
        Point3(0, 0, 0)]
    rightPosPoints = [
        Point3(-1, 4.1, 4),
        Point3(0, 0, 0)]
    leftKnifeTracks = []
    rightKnifeTracks = []
    for i in range(0, 3):
        knifeDelay = 0.11
        leftIvals = []
        leftIvals.append(WaitInterval(1.1))
        leftIvals.append(WaitInterval(i * knifeDelay))
        leftIvals.extend(getPropAppearIntervals(leftKnives[i], suit, leftPosPoints, 1e-006, Point3(0.4, 0.4, 0.4), scaleUpTime = 0.1))
        leftIvals.extend(getPropThrowIntervals(attack, leftKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.3, missDuration = 0.3))
        leftKnifeTracks.append(Track(leftIvals))
        rightIvals = []
        rightIvals.append(WaitInterval(1.1))
        rightIvals.append(WaitInterval(i * knifeDelay))
        rightIvals.extend(getPropAppearIntervals(rightKnives[i], suit, rightPosPoints, 1e-006, Point3(0.4, 0.4, 0.4), scaleUpTime = 0.1))
        rightIvals.extend(getPropThrowIntervals(attack, rightKnives[i], hitPointNames = [
            'face'], missPointNames = [
            'miss'], hitDuration = 0.3, missDuration = 0.3))
        rightKnifeTracks.append(Track(rightIvals))
    
    damageAnims = [
        [
            'slip-backward',
            1.6,
            0.35]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = 0.7, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 0.7, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack] + leftKnifeTracks + rightKnifeTracks + toonDodgeTracks)


def doRolodex(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    rollodex = globalPropPool.getProp('rollodex')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect(file = 'rollodexVortex')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'rollodexWaterfall')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'rollodexStream')
    BattleParticles.setEffectTexture(particleEffect, 'roll-o-dex')
    BattleParticles.setEffectTexture(particleEffect2, 'roll-o-dex')
    BattleParticles.setEffectTexture(particleEffect3, 'roll-o-dex')
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        propPosPoints = [
            Point3(-0.51, -0.03, -0.1),
            Point3(-87.75, -81.64, -100.52)]
        propScale = Point3(1.2, 1.2, 1.2)
        partDelay = 2.6
        part2Delay = 2.3
        part3Delay = 3.2
        partDuration = 1.6
        part2Duration = 1.9
        part3Duration = 1
        damageDelay = 3.8
        dodgeDelay = 2.5
    elif suitType == 'b':
        propPosPoints = [
            Point3(0.12, 0.24, 0.01),
            Point3(-99.05, -6.98, -178.98)]
        propScale = Point3(0.91, 0.91, 0.91)
        partDelay = 2.9
        part2Delay = 2.6
        part3Delay = 3.5
        partDuration = 1.6
        part2Duration = 1.9
        part3Duration = 1
        damageDelay = 4
        dodgeDelay = 2.5
    elif suitType == 'c':
        propPosPoints = [
            Point3(-0.51, -0.03, -0.1),
            Point3(-87.75, -81.64, -100.52)]
        propScale = Point3(1.2, 1.2, 1.2)
        partDelay = 2.3
        part2Delay = 2.3
        part3Delay = 3.2
        partDuration = 1.9
        part2Duration = 1.9
        part3Duration = 1
        damageDelay = 3.5
        dodgeDelay = 2.5
    
    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    partTrack = Track([
        (partDelay, FunctionInterval(battle.movie.needRestoreParticleEffect, extraArgs = [
            particleEffect])),
        FunctionInterval(BattleParticles.startParticleEffect, extraArgs = [
            particleEffect,
            suit,
            0]),
        FunctionInterval(particleEffect.wrtReparentTo, extraArgs = [
            render]),
        LerpPosInterval(particleEffect, partDuration, pos = hitPoint),
        FunctionInterval(BattleParticles.cleanupParticleEffect, extraArgs = [
            particleEffect]),
        FunctionInterval(battle.movie.clearRestoreParticleEffect, extraArgs = [
            particleEffect])])
    partTrack2 = getPartTrack(particleEffect2, part2Delay, part2Duration, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, part3Delay, part3Duration, [
        particleEffect3,
        suit,
        0])
    suitTrack = getSuitTrack(attack)
    propTrack = getPropTrack(rollodex, suit.getLeftHand(), propPosPoints, 1e-006, 4.7, scaleUpPoint = propScale, anim = 0, propName = 'rollodex', animDuration = 0, animStartTime = 0)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack,
        partTrack,
        partTrack2,
        partTrack3] + toonDodgeTracks)


def doDoubleTalk(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('DoubleTalkLeft')
    particleEffect2 = BattleParticles.createParticleEffect('DoubleTalkRight')
    BattleParticles.setEffectTexture(particleEffect, 'doubletalk-double', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'doubletalk-good', color = Vec4(0, 0, 0, 1))
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 3.3
        damageDelay = 3.5
        dodgeDelay = 3.3
    elif suitType == 'b':
        partDelay = 3.3
        damageDelay = 3.5
        dodgeDelay = 3.3
    elif suitType == 'c':
        partDelay = 3.3
        damageDelay = 3.5
        dodgeDelay = 3.3
    
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay, 1.8, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, partDelay, 1.8, [
        particleEffect2,
        suit,
        0])
    damageAnims = [
        [
            'duck',
            damageDelay,
            0.4,
            1.05],
        [
            'cringe',
            1e-006,
            0.8]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, splicedDodgeAnims = [
        [
            'duck',
            dodgeDelay,
            1.4]])
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack,
        partTrack2])


def doFreezeAssets(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    snowEffect = BattleParticles.createParticleEffect('FreezeAssets')
    cloud = MovieUtil.copyProp(toon.cloudActors[0])
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.3
    elif suitType == 'b':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.3
    elif suitType == 'c':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.3
    
    suitTrack = getSuitTrack(attack, delay = 0.9)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        Point3(0, 0, 0)]
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'cloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 1e-006, Point3(3, 3, 3), scaleUpTime = 0.7))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    cloudIvals.append(ParticleInterval(snowEffect, cloud, worldRelative = 0, duration = 2.5))
    cloudIvals.append(WaitInterval(0.4))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, Point3(1e-005, 1e-005, 1e-005)))
    cloudIvals.append(FunctionInterval(__hideProp, extraArgs = [
        cloud,
        globalPropPool]))
    cloudPropTrack = Track(cloudIvals)
    damageAnims = [
        [
            'cringe',
            damageDelay,
            0.4,
            0.8],
        [
            'duck',
            1e-006,
            1.6]]
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        cloudPropTrack] + toonDodgeTracks)


def doHotAir(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect('HotAir')
    baseFlameEffect = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(sprayEffect, 'fire')
    BattleParticles.setEffectTexture(baseFlameEffect, 'fire')
    BattleParticles.setEffectTexture(flameEffect, 'fire')
    BattleParticles.setEffectTexture(flecksEffect, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    sprayDelay = 1.3
    flameDelay = 3.2
    flameDuration = 2.6
    flecksDelay = flameDelay + 0.8
    flecksDuration = flameDuration - 0.8
    damageDelay = 3.6
    dodgeDelay = 2.0
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, sprayDelay, 2.3, [
        sprayEffect,
        suit,
        0])
    baseFlameTrack = getPartTrack(baseFlameEffect, flameDelay, flameDuration, [
        baseFlameEffect,
        toon,
        0])
    flameTrack = getPartTrack(flameEffect, flameDelay, flameDuration, [
        flameEffect,
        toon,
        0])
    flecksTrack = getPartTrack(flecksEffect, flecksDelay, flecksDuration, [
        flecksEffect,
        toon,
        0])
    
    def changeColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals = []
        colorIvals.append(WaitInterval(4.0))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(changeColor(headParts))
        colorIvals.extend(changeColor(torsoParts))
        colorIvals.extend(changeColor(legsParts))
        colorIvals.append(WaitInterval(3.5))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorTrack = Track(colorIvals)
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        damageDelay,
        0.7,
        0.62])
    damageAnims.append([
        'slip-forward',
        1e-005,
        0.4,
        1.2])
    damageAnims.append([
        'slip-forward',
        1e-005,
        1.0])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            toonTrack,
            sprayTrack,
            baseFlameTrack,
            flameTrack,
            flecksTrack,
            colorTrack] + toonDodgeTracks)
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            sprayTrack] + toonDodgeTracks)


def doPickPocket(attack):
    suit = attack['suit']
    target = attack['target']
    dmg = target['hp']
    bill = globalPropPool.getProp('1dollar')
    suitTrack = getSuitTrack(attack)
    billPosPoints = [
        Point3(-0.01, 0.45, -0.25),
        Point3(-122.41, -21.32, -98.44)]
    billPropTrack = getPropTrack(bill, suit.getRightHand(), billPosPoints, 0.6, 0.55, scaleUpPoint = Point3(1.41, 1.41, 1.41))
    toonTrack = getToonTrack(attack, 0.6, [
        'cringe'], 0.01, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 0.01, [
        'sidestep'])
    multiTrackList = [
        suitTrack,
        toonTrack]
    if dmg > 0:
        multiTrackList.append(billPropTrack)
    
    return MultiTrack(multiTrackList + toonDodgeTracks)


def doFilibuster(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    sprayEffect = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect2 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect3 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    sprayEffect4 = BattleParticles.createParticleEffect(file = 'filibusterSpray')
    BattleParticles.setEffectTexture(sprayEffect, 'filibuster-cut', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(sprayEffect2, 'filibuster-fiscal', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(sprayEffect3, 'filibuster-impeach', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(sprayEffect4, 'filibuster-inc', color = Vec4(0, 0, 0, 1))
    partDelay = 1.3
    partDuration = 1.15
    damageDelay = 2.45
    dodgeDelay = 1.7
    suitTrack = getSuitTrack(attack)
    sprayTrack = getPartTrack(sprayEffect, partDelay, partDuration, [
        sprayEffect,
        suit,
        0])
    sprayTrack2 = getPartTrack(sprayEffect2, partDelay + 0.8, partDuration, [
        sprayEffect2,
        suit,
        0])
    sprayTrack3 = getPartTrack(sprayEffect3, partDelay + 1.6, partDuration, [
        sprayEffect3,
        suit,
        0])
    sprayTrack4 = getPartTrack(sprayEffect4, partDelay + 2.4, partDuration, [
        sprayEffect4,
        suit,
        0])
    damageAnims = []
    damageAnims.append([
        'cringe',
        damageDelay,
        0,
        1e-005])
    for i in range(0, 4):
        damageAnims.append([
            'cringe',
            1e-005,
            0.3,
            0.8])
    
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = dodgeDelay, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        sprayTrack,
        sprayTrack2,
        sprayTrack3,
        sprayTrack4] + toonDodgeTracks)


def doSchmooze(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    upperEffects = []
    lowerEffects = []
    textureNames = [
        'schmooze-genius',
        'schmooze-instant',
        'schmooze-master',
        'schmooze-viz']
    for i in range(0, 4):
        upperEffect = BattleParticles.createParticleEffect(file = 'schmoozeUpperSpray')
        lowerEffect = BattleParticles.createParticleEffect(file = 'schmoozeLowerSpray')
        BattleParticles.setEffectTexture(upperEffect, textureNames[i], color = Vec4(0, 0, 0, 1))
        BattleParticles.setEffectTexture(lowerEffect, textureNames[i], color = Vec4(0, 0, 0, 1))
        upperEffects.append(upperEffect)
        lowerEffects.append(lowerEffect)
    
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 1.3
        damageDelay = 1.8
        dodgeDelay = 1.1
    elif suitType == 'b':
        partDelay = 1.3
        damageDelay = 2.5
        dodgeDelay = 1.8
    elif suitType == 'c':
        partDelay = 1.3
        damageDelay = partDelay + 1.4
        dodgeDelay = 0.9
    
    suitTrack = getSuitTrack(attack)
    upperPartTracks = []
    lowerPartTracks = []
    for i in range(0, 4):
        upperPartTracks.append(getPartTrack(upperEffects[i], partDelay + i * 0.65, 0.8, [
            upperEffects[i],
            suit,
            0]))
        lowerPartTracks.append(getPartTrack(lowerEffects[i], partDelay + i * 0.65 + 0.7, 1.0, [
            lowerEffects[i],
            suit,
            0]))
    
    damageAnims = []
    damageAnims.append([
        'conked',
        damageDelay,
        0,
        1e-005])
    for i in range(0, 3):
        damageAnims.append([
            'conked',
            1e-005,
            0.3,
            0.71])
    
    damageAnims.append([
        'conked',
        1e-005,
        0.3])
    dodgeAnims = []
    dodgeAnims.append([
        'duck',
        dodgeDelay,
        0.2,
        2.7])
    dodgeAnims.append([
        'duck',
        1e-005,
        1.22,
        1.28])
    dodgeAnims.append([
        'duck',
        1e-005,
        3.16])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, splicedDodgeAnims = dodgeAnims)
    return MultiTrack([
        suitTrack,
        toonTrack] + upperPartTracks + lowerPartTracks)


def doShake(attack):
    suit = attack['suit']
    suitTrack = getSuitAnimTrack(attack)
    toonTracks = getToonTracks(attack, 1.5, [
        'slip-forward'], 1.3, [
        'jump'])
    return MultiTrack([
        suitTrack] + toonTracks)


def doHangUp(attack):
    suit = attack['suit']
    phone = globalPropPool.getProp('phone')
    receiver = globalPropPool.getProp('receiver')
    suitTrack = getSuitTrack(attack)
    phonePosPoints = [
        Point3(0.23, 0.17, -0.11),
        Point3(-6.05, -2.51, 177.58)]
    receiverPosPoints = [
        Point3(0.23, 0.17, -0.11),
        Point3(-6.05, -2.51, 177.58)]
    propTrack = Track([
        WaitInterval(0.3),
        FunctionInterval(__showProp, extraArgs = [
            phone,
            suit.getLeftHand(),
            phonePosPoints[0],
            phonePosPoints[1]]),
        FunctionInterval(__showProp, extraArgs = [
            receiver,
            suit.getLeftHand(),
            receiverPosPoints[0],
            receiverPosPoints[1]]),
        LerpScaleInterval(phone, 0.5, Point3(1, 1, 1), Point3(0, 0, 0)),
        WaitInterval(0.74),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            suit.getRightHand()]),
        LerpPosHprInterval(receiver, 0.0001, Point3(-0.53, 0.21, -0.54), Point3(-100.66, -43.3, 8.15)),
        WaitInterval(3.07),
        FunctionInterval(receiver.wrtReparentTo, extraArgs = [
            phone]),
        WaitInterval(0.69),
        LerpScaleInterval(phone, 0.5, Point3(0, 0, 0)),
        FunctionInterval(__hideProp, extraArgs = [
            receiver,
            globalPropPool]),
        FunctionInterval(__hideProp, extraArgs = [
            phone,
            globalPropPool])])
    toonTrack = getToonTrack(attack, 5.5, [
        'slip-backward'], 4.7, [
        'jump'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


def doRedTape(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    tape = globalPropPool.getProp('redtape')
    tubes = []
    for i in range(0, 3):
        tubes.append(globalPropPool.getProp('redtape-tube'))
    
    suitTrack = getSuitTrack(attack)
    tapePosPoints = [
        Point3(0.24, 0.09, -0.38),
        Point3(-77.47, 74.05, 15.52)]
    tapeScaleUpPoint = Point3(0.9, 0.9, 0.24)
    tapeIvals = getPropAppearIntervals(tape, suit.getRightHand(), tapePosPoints, 0.8, tapeScaleUpPoint, scaleUpTime = 0.5)
    tapeIvals.append(WaitInterval(1.73))
    
    hitPoint = lambda toon = toon: __toonTorsoPoint(toon)
    tapeIvals.extend(getPropThrowIntervals(attack, tape, [
        hitPoint], [
        __toonGroundPoint(attack, toon, 0.7)]))
    propTrack = Track(tapeIvals)
    hips = toon.getHipsParts()
    animal = toon.style.getAnimal()
    scale = Toon.toonBodyScales[animal]
    legs = toon.style.legs
    torso = toon.style.torso
    torso = torso[0]
    animal = animal[0]
    tubeHeight = -0.8
    if torso == 's':
        scaleUpPoint = Point3(scale * 2.03, scale * 2.03, scale * 0.7975)
    elif torso == 'm':
        scaleUpPoint = Point3(scale * 2.03, scale * 2.03, scale * 0.7975)
    elif torso == 'l':
        scaleUpPoint = Point3(scale * 2.03, scale * 2.03, scale * 1.11)
    
    if animal == 'h' or animal == 'd':
        tubeHeight = -0.87
        scaleUpPoint = Point3(scale * 1.69, scale * 1.69, scale * 0.67)
    
    tubePosPoints = [
        Point3(0, 0, tubeHeight),
        Point3(0, 0, 0)]
    tubeTracks = []
    for partNum in range(0, hips.getNumPaths()):
        nextPart = hips.getPath(partNum)
        tubeTracks.append(FunctionInterval(battle.movie.needRestoreHips))
        tubeTracks.append(getPropTrack(tubes[partNum], nextPart, tubePosPoints, 3.25, 3.17, scaleUpPoint = scaleUpPoint))
    
    toonTrack = getToonTrack(attack, 3.4, [
        'struggle'], 2.8, [
        'jump'])
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            toonTrack,
            propTrack] + tubeTracks)
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            propTrack])


def doBounceCheck(attack):
    suit = attack['suit']
    target = attack['target']
    battle = attack['battle']
    toon = target['toon']
    hp = target['hp']
    hitSuit = hp > 0
    check = globalPropPool.getProp('bounced-check')
    checkPosPoints = [
        Point3(0, 0, 0),
        Point3(-176, 89, 11)]
    
    def getThrowEndPoint(suit = suit, toon = toon, battle = battle, whichBounce = 'none'):
        pnt = toon.getPos(battle)
        if whichBounce == 'one':
            pnt.setY(pnt[1] + 8)
            pnt.setZ(battle.getZ())
        elif whichBounce == 'two':
            pnt.setY(pnt[1] + 5)
            pnt.setZ(battle.getZ())
        elif whichBounce == 'threeHit':
            pnt.setZ(pnt[2] + toon.shoulderHeight + 0.3)
        elif whichBounce == 'threeMiss':
            pnt.setZ(battle.getZ())
        elif whichBounce == 'four':
            pnt.setY(pnt[1] - 5)
            pnt.setZ(battle.getZ())
        
        return Point3(pnt)

    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        throwDelay = 2.5
        dodgeDelay = 4.3
        damageDelay = 5.1
    elif suitType == 'b':
        throwDelay = 1.8
        dodgeDelay = 3.6
        damageDelay = 4.4
    elif suitType == 'c':
        throwDelay = 1.8
        dodgeDelay = 3.6
        damageDelay = 4.4
    
    suitTrack = getSuitTrack(attack)
    checkIvals = getPropAppearIntervals(check, suit.getRightHand(), checkPosPoints, 1e-005, Point3(8.5, 8.5, 8.5), startScale = Point3(1, 1, 1))
    checkIvals.append(WaitInterval(throwDelay))
    checkIvals.append(FunctionInterval(__checkPreFlight, extraArgs = [
        check,
        toon]))
    checkIvals.extend(getThrowIvals(check, getThrowEndPoint(whichBounce = 'one'), duration = 0.5, parent = battle))
    checkIvals.extend(getThrowIvals(check, getThrowEndPoint(whichBounce = 'two'), duration = 1, parent = battle))
    if hitSuit:
        checkIvals.extend(getThrowIvals(check, getThrowEndPoint(whichBounce = 'threeHit'), duration = 0.8, parent = battle))
    else:
        checkIvals.extend(getThrowIvals(check, getThrowEndPoint(whichBounce = 'threeMiss'), duration = 0.9, parent = battle))
        checkIvals.extend(getThrowIvals(check, getThrowEndPoint(whichBounce = 'four'), duration = 0.9, parent = battle))
    checkIvals.append(FunctionInterval(__hideProp, extraArgs = [
        check,
        globalPropPool]))
    checkPropTrack = Track(checkIvals)
    toonTrack = getToonTrack(attack, damageDelay, [
        'conked'], dodgeDelay, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        checkPropTrack,
        toonTrack] + toonDodgeTracks)


def doWatercooler(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    watercooler = globalPropPool.getProp('watercooler')
    
    def getCoolerSpout(watercooler = watercooler):
        spout = watercooler.find('**/joint-toSpray')
        return spout.getPos(render)

    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    
    missPoint = lambda prop = watercooler, toon = toon: __toonMissPoint(prop, toon, 0, parent = render)
    hitSprayIvals = MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getCoolerSpout, hitPoint, 0.2, 0.2, 0.2, horizScale = 0.3, vertScale = 0.3)
    missSprayIvals = MovieUtil.getSprayIntervals(Point4(0.75, 0.75, 1.0, 0.8), getCoolerSpout, missPoint, 0.2, 0.2, 0.2, horizScale = 0.3, vertScale = 0.3)
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(0.48, 0.11, -0.92),
        Point3(37.03, -10.62, -79.21)]
    propIvals = [
        WaitInterval(1.01),
        FunctionInterval(__showProp, extraArgs = [
            watercooler,
            suit.getLeftHand(),
            posPoints[0],
            posPoints[1]]),
        LerpScaleInterval(watercooler, 0.5, Point3(1.15, 1.15, 1.15)),
        WaitInterval(1.6)]
    if dmg > 0:
        propIvals += hitSprayIvals
    else:
        propIvals += missSprayIvals
    propIvals += [
        WaitInterval(0.01),
        LerpScaleInterval(watercooler, 0.5, Point3(0, 0, 0)),
        FunctionInterval(__hideProp, extraArgs = [
            watercooler,
            globalPropPool])]
    propTrack = Track(propIvals)
    splashTrack = []
    if dmg > 0:
        
        def prepSplash(splash, targetPoint):
            splash.reparentTo(render)
            splash.setPos(targetPoint)
            scale = splash.getScale()
            splash.setBillboardPointWorld()
            splash.setScale(scale)

        splash = globalPropPool.getProp('splash-from-splat')
        splash.setColor(0.75, 0.75, 1, 0.8)
        splash.setScale(0.3)
        splashIvals = [
            (3.2, FunctionInterval(prepSplash, extraArgs = [
                splash,
                __toonFacePoint(toon)])),
            ActorInterval(splash, 'splash-from-splat'),
            FunctionInterval(splash.reparentTo, extraArgs = [
                hidden])]
        splashTrack.append(Track(splashIvals))
    
    toonTrack = getToonTrack(attack, suitTrack.getDuration() - 1.5, [
        'cringe'], 2.4, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, suitTrack.getDuration() - 1.5, [
        'sidestep'])
    multiTrackList = [
        suitTrack,
        toonTrack,
        propTrack]
    multiTrackList += splashTrack
    multiTrackList += toonDodgeTracks
    return MultiTrack(multiTrackList)


def doFired(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    baseFlameEffect = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameEffect = BattleParticles.createParticleEffect('FiredFlame')
    flecksEffect = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(baseFlameEffect, 'fire')
    BattleParticles.setEffectTexture(flameEffect, 'fire')
    BattleParticles.setEffectTexture(flecksEffect, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    baseFlameSmall = BattleParticles.createParticleEffect(file = 'firedBaseFlame')
    flameSmall = BattleParticles.createParticleEffect('FiredFlame')
    flecksSmall = BattleParticles.createParticleEffect('SpriteFiredFlecks')
    BattleParticles.setEffectTexture(baseFlameSmall, 'fire')
    BattleParticles.setEffectTexture(flameSmall, 'fire')
    BattleParticles.setEffectTexture(flecksSmall, 'roll-o-dex', color = Vec4(200, 200, 200, 1))
    baseFlameSmall.setScale(0.7)
    flameSmall.setScale(0.7)
    flecksSmall.setScale(0.7)
    suitTrack = getSuitTrack(attack)
    baseFlameTrack = getPartTrack(baseFlameEffect, 1.0, 1.9, [
        baseFlameEffect,
        toon,
        0])
    flameTrack = getPartTrack(flameEffect, 1.0, 1.9, [
        flameEffect,
        toon,
        0])
    flecksTrack = getPartTrack(flecksEffect, 1.8, 1.1, [
        flecksEffect,
        toon,
        0])
    baseFlameSmallTrack = getPartTrack(baseFlameSmall, 1.0, 1.9, [
        baseFlameSmall,
        toon,
        0])
    flameSmallTrack = getPartTrack(flameSmall, 1.0, 1.9, [
        flameSmall,
        toon,
        0])
    flecksSmallTrack = getPartTrack(flecksSmall, 1.8, 1.1, [
        flecksSmall,
        toon,
        0])
    
    def changeColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return ivals

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        headParts = toon.getHeadParts()
        torsoParts = toon.getTorsoParts()
        legsParts = toon.getLegsParts()
        colorIvals = []
        colorIvals.append(WaitInterval(2.0))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.extend(changeColor(headParts))
        colorIvals.extend(changeColor(torsoParts))
        colorIvals.extend(changeColor(legsParts))
        colorIvals.append(WaitInterval(3.5))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorTrack = Track(colorIvals)
    
    damageAnims = []
    damageAnims.append([
        'cringe',
        1.5,
        0.7,
        0.62])
    damageAnims.append([
        'slip-forward',
        1e-005,
        0.4,
        1.2])
    damageAnims.extend(getSplicedLerpAnims('slip-forward', 0.31, 0.8, startTime = 1.2))
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, dodgeDelay = 0.3, dodgeAnimNames = [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 0.3, [
        'sidestep'])
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            baseFlameTrack,
            flameTrack,
            flecksTrack,
            toonTrack,
            colorTrack] + toonDodgeTracks)
    else:
        return MultiTrack([
            suitTrack,
            baseFlameSmallTrack,
            flameSmallTrack,
            flecksSmallTrack,
            toonTrack] + toonDodgeTracks)


def doAudit(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-one', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-two', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-three', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-four', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-mult', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1, 1.9, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.3, 2.1, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.4, 2.2, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.3, [
        particleEffect5,
        suit,
        0])
    calcPosPoints = [
        Point3(0.35, 0.52, 0.03),
        Point3(2.03, -6.34, 6.01)]
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 1e-006, 1.87, scaleUpPoint = Point3(1.0, 1.37, 1.31), anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.4)
    toonTrack = getToonTrack(attack, 3.2, [
        'conked'], 0.9, [
        'duck'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5])


def doCalculate(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-one', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-plus', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-mult', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-three', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-div', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1, 1.9, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.3, 2.1, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.4, 2.2, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.3, [
        particleEffect5,
        suit,
        0])
    calcPosPoints = [
        Point3(0.35, 0.52, 0.03),
        Point3(2.03, -6.34, 6.01)]
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 1e-006, 1.87, scaleUpPoint = Point3(1.0, 1.37, 1.31), anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.4)
    toonTrack = getToonTrack(attack, 3.2, [
        'conked'], 1.8, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 1.8, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5] + toonDodgeTracks)


def doTabulate(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    calculator = globalPropPool.getProp('calculator')
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect, 'audit-plus', color = Vec4(0, 0, 0, 1))
    particleEffect2 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect2, 'audit-minus', color = Vec4(0, 0, 0, 1))
    particleEffect3 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect3, 'audit-mult', color = Vec4(0, 0, 0, 1))
    particleEffect4 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect4, 'audit-div', color = Vec4(0, 0, 0, 1))
    particleEffect5 = BattleParticles.createParticleEffect('Calculate')
    BattleParticles.setEffectTexture(particleEffect5, 'audit-one', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.1, 1.9, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.2, 2.0, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 2.3, 2.1, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, 2.4, 2.2, [
        particleEffect4,
        suit,
        0])
    partTrack5 = getPartTrack(particleEffect5, 2.5, 2.3, [
        particleEffect5,
        suit,
        0])
    calcPosPoints = [
        Point3(0.35, 0.52, 0.03),
        Point3(2.03, -6.34, 6.01)]
    calcPropTrack = getPropTrack(calculator, suit.getLeftHand(), calcPosPoints, 1e-006, 1.87, scaleUpPoint = Point3(1.0, 1.37, 1.31), anim = 1, propName = 'calculator', animStartTime = 0.5, animDuration = 3.4)
    toonTrack = getToonTrack(attack, 3.2, [
        'conked'], 1.8, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 1.8, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        calcPropTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4,
        partTrack5] + toonDodgeTracks)


def doLiquidate(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    BattleParticles.loadParticles()
    rainEffect = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect2 = BattleParticles.createParticleEffect(file = 'liquidate')
    rainEffect3 = BattleParticles.createParticleEffect(file = 'liquidate')
    cloud = MovieUtil.copyProp(toon.cloudActors[0])
    suitType = getSuitBodyType(attack['suitName'])
    if suitType == 'a':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.45
    elif suitType == 'b':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.45
    elif suitType == 'c':
        partDelay = 0.2
        damageDelay = 3.5
        dodgeDelay = 2.45
    
    suitTrack = getSuitTrack(attack, delay = 0.9)
    initialCloudHeight = suit.height + 3
    cloudPosPoints = [
        Point3(0, 3, initialCloudHeight),
        Point3(180, 0, 0)]
    cloudIvals = []
    cloudIvals.append(FunctionInterval(cloud.pose, extraArgs = [
        'cloud',
        0]))
    cloudIvals.extend(getPropAppearIntervals(cloud, suit, cloudPosPoints, 1e-006, Point3(3, 3, 3), scaleUpTime = 0.7))
    cloudIvals.append(FunctionInterval(cloud.wrtReparentTo, extraArgs = [
        render]))
    targetPoint = __toonFacePoint(toon)
    targetPoint.setZ(targetPoint[2] + 3)
    cloudIvals.append(WaitInterval(1.1))
    cloudIvals.append(LerpPosInterval(cloud, 1, pos = targetPoint))
    cloudIvals.append(WaitInterval(partDelay))
    pivals = []
    pivals.append(Track([
        ParticleInterval(rainEffect, cloud, worldRelative = 0, duration = 2.4)]))
    pivals.append(Track([
        (0.1, ParticleInterval(rainEffect2, cloud, worldRelative = 0, duration = 2.3))]))
    pivals.append(Track([
        (0.1, ParticleInterval(rainEffect3, cloud, worldRelative = 0, duration = 2.3))]))
    pivals.append(Track([
        ActorInterval(cloud, 'cloud', startTime = 3, duration = 0.1),
        ActorInterval(cloud, 'cloud', startTime = 1, duration = 2.3)]))
    cloudIvals.append(MultiTrack(pivals))
    cloudIvals.append(WaitInterval(0.4))
    cloudIvals.append(LerpScaleInterval(cloud, 0.5, Point3(1e-005, 1e-005, 1e-005)))
    cloudIvals.append(FunctionInterval(__hideProp, extraArgs = [
        cloud,
        globalPropPool]))
    cloudPropTrack = Track(cloudIvals)
    damageAnims = [
        [
            'cringe',
            damageDelay,
            0.4,
            0.8],
        [
            'duck',
            1e-006,
            1.6,
            1.7]]
    damageAnims = [
        [
            'cringe',
            damageDelay,
            0.4]]
    toonTrack = getToonTrack(attack, damageDelay, [
        'cringe'], dodgeDelay, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, dodgeDelay, [
        'sidestep'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        cloudPropTrack] + toonDodgeTracks)


def doEvictionNotice(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    paper = globalPropPool.getProp('shredder-paper')
    suitTrack = getSuitTrack(attack)
    posPoints = [
        Point3(-0.04, 0.15, -1.38),
        Point3(6.34, -14.62, -18.02)]
    paperIvals = getPropAppearIntervals(paper, suit.getRightHand(), posPoints, 0.8, Point3(1, 1, 1), scaleUpTime = 0.5)
    paperIvals.append(WaitInterval(1.73))
    
    hitPoint = lambda toon = toon: __toonFacePoint(toon)
    paperIvals.extend(getPropThrowIntervals(attack, paper, [
        hitPoint], [
        __toonGroundPoint(attack, toon, 0.7)]))
    propTrack = Track(paperIvals)
    toonTrack = getToonTrack(attack, 3.4, [
        'conked'], 2.8, [
        'jump'])
    return MultiTrack([
        suitTrack,
        toonTrack,
        propTrack])


def doWithdrawal(attack):
    suit = attack['suit']
    battle = attack['battle']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    particleEffect = BattleParticles.createParticleEffect('Withdrawal')
    suitTrack = getSuitAnimTrack(attack)
    partTrack = getPartTrack(particleEffect, 1e-005, suitTrack.getDuration() + 1.2, [
        particleEffect,
        suit,
        0])
    toonTrack = getToonTrack(attack, 1.2, [
        'cringe'], 0.2, splicedDodgeAnims = [
        [
            'duck',
            1e-005,
            0.8]])
    headParts = toon.getHeadParts()
    torsoParts = toon.getTorsoParts()
    legsParts = toon.getLegsParts()
    
    def changeColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.setColorScale, extraArgs = [
                Vec4(0, 0, 0, 1)]))
        
        return Track(ivals)

    
    def resetColor(parts):
        ivals = []
        for partNum in range(0, parts.getNumPaths()):
            nextPart = parts.getPath(partNum)
            ivals.append(FunctionInterval(nextPart.clearColorScale))
        
        return ivals

    if dmg > 0:
        colorIvals = []
        colorIvals.append(WaitInterval(1.6))
        colorIvals.append(FunctionInterval(battle.movie.needRestoreColor))
        colorIvals.append(MultiTrack([
            changeColor(headParts),
            changeColor(torsoParts),
            changeColor(legsParts)]))
        colorIvals.append(WaitInterval(2.9))
        colorIvals.extend(resetColor(headParts))
        colorIvals.extend(resetColor(torsoParts))
        colorIvals.extend(resetColor(legsParts))
        colorTrack = Track(colorIvals)
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack,
            colorTrack])
    else:
        return MultiTrack([
            suitTrack,
            partTrack,
            toonTrack])


def doJargon(attack):
    suit = attack['suit']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    particleEffect4 = BattleParticles.createParticleEffect(file = 'jargonSpray')
    BattleParticles.setEffectTexture(particleEffect, 'jargon-brow', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'jargon-deep', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect3, 'jargon-hoop', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect4, 'jargon-ipo', color = Vec4(0, 0, 0, 1))
    damageDelay = 2.2
    dodgeDelay = 1.5
    partDelay = 1.1
    partInterval = 1.2
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, partDelay + partInterval * 0, 2, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, partDelay + partInterval * 1, 2, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, partDelay + partInterval * 2, 2, [
        particleEffect3,
        suit,
        0])
    partTrack4 = getPartTrack(particleEffect4, partDelay + partInterval * 3, 2, [
        particleEffect4,
        suit,
        0])
    damageAnims = []
    damageAnims.append([
        'conked',
        damageDelay,
        0,
        0.4])
    damageAnims.append([
        'conked',
        0.0001,
        2.7,
        0.85])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.09])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.09])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.66])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.09])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.09])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.86])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.14])
    damageAnims.append([
        'conked',
        0.0001,
        0.4,
        0.14])
    damageAnims.append([
        'conked',
        0.0001,
        0.4])
    dodgeAnims = []
    dodgeAnims.append([
        'duck',
        dodgeDelay,
        1.2])
    dodgeAnims.append([
        'duck',
        0.0001,
        1.3])
    toonTrack = getToonTrack(attack, splicedDamageAnims = damageAnims, splicedDodgeAnims = dodgeAnims)
    return MultiTrack([
        suitTrack,
        toonTrack,
        partTrack,
        partTrack2,
        partTrack3,
        partTrack4])


def doMumboJumbo(attack):
    suit = attack['suit']
    target = attack['target']
    toon = target['toon']
    dmg = target['hp']
    BattleParticles.loadParticles()
    particleEffect = BattleParticles.createParticleEffect(file = 'mumbojumboSpray')
    particleEffect2 = BattleParticles.createParticleEffect(file = 'mumbojumboSpray')
    particleEffect3 = BattleParticles.createParticleEffect(file = 'mumbojumboSmother')
    particleEffect4 = BattleParticles.createParticleEffect(file = 'mumbojumboSmother')
    particleEffect5 = BattleParticles.createParticleEffect(file = 'mumbojumboSmother')
    BattleParticles.setEffectTexture(particleEffect, 'mumbojumbo-boiler', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect2, 'mumbojumbo-creative', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect3, 'mumbojumbo-deben', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect4, 'mumbojumbo-high', color = Vec4(0, 0, 0, 1))
    BattleParticles.setEffectTexture(particleEffect5, 'mumbojumbo-iron', color = Vec4(0, 0, 0, 1))
    suitTrack = getSuitTrack(attack)
    partTrack = getPartTrack(particleEffect, 2.5, 2, [
        particleEffect,
        suit,
        0])
    partTrack2 = getPartTrack(particleEffect2, 2.5, 2, [
        particleEffect2,
        suit,
        0])
    partTrack3 = getPartTrack(particleEffect3, 3.3, 1.7, [
        particleEffect3,
        toon,
        0])
    partTrack4 = getPartTrack(particleEffect4, 3.3, 1.7, [
        particleEffect4,
        toon,
        0])
    partTrack5 = getPartTrack(particleEffect5, 3.3, 1.7, [
        particleEffect5,
        toon,
        0])
    toonTrack = getToonTrack(attack, 3.2, [
        'cringe'], 2.2, [
        'sidestep'])
    toonDodgeTracks = getToonsDodgeTracks(attack, 2.2, [
        'sidestep'])
    if dmg > 0:
        return MultiTrack([
            suitTrack,
            toonTrack,
            partTrack,
            partTrack2,
            partTrack3,
            partTrack4,
            partTrack5] + toonDodgeTracks)
    else:
        return MultiTrack([
            suitTrack,
            toonTrack,
            partTrack,
            partTrack2] + toonDodgeTracks)

