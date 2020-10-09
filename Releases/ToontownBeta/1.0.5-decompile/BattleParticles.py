# Source Generated with Decompyle++
# File: BattleParticles.pyo (Python 2.0)

from ParticleEffect import *
import os
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('BattleParticles')
ParticleNames = ('audit-div', 'audit-five', 'audit-four', 'audit-minus', 'audit-mult', 'audit-one', 'audit-plus', 'audit-six', 'audit-three', 'audit-two', 'blah', 'brainstorm-box', 'brainstorm-env', 'brainstorm-track', 'buzzwords-crash', 'buzzwords-inc', 'buzzwords-main', 'buzzwords-over', 'buzzwords-syn', 'doubletalk-double', 'doubletalk-dup', 'doubletalk-good', 'filibuster-cut', 'filibuster-fiscal', 'filibuster-impeach', 'filibuster-inc', 'jargon-brow', 'jargon-deep', 'jargon-hoop', 'jargon-ipo', 'legalese-hc', 'legalese-qpq', 'legalese-vd', 'mumbojumbo-boiler', 'mumbojumbo-creative', 'mumbojumbo-deben', 'mumbojumbo-high', 'mumbojumbo-iron', 'poundsign', 'schmooze-genius', 'schmooze-instant', 'schmooze-master', 'schmooze-viz', 'roll-o-dex', 'dagger', 'fire', 'snow', 'raindrop', 'gear', 'checkmark')
particleModel = None

def loadParticles():
    global particleModel
    if particleModel == None:
        particleModel = loader.loadModel('phase_5/models/props/suit-particles')
    


def unloadParticles():
    global particleModel
    if particleModel != None:
        particleModel.removeNode()
    
    del particleModel
    particleModel = None


def getParticle(name):
    if name in ParticleNames:
        particle = particleModel.find('**/' + str(name))
        return particle.instanceTo(hidden)
    else:
        notify.warning('getParticle() - no name: %s' % name)
        return None


def createParticleEffect(name = None, file = None, numParticles = None):
    if not name:
        effect = ParticleEffect()
        fileName = file + '.ptf'
        __loadParticleFile(effect, fileName)
        return effect
    
    if name == 'BigGearExplosion':
        return __makeBigGearExplosion(numParticles)
    elif name == 'BrainStorm':
        return __makeBrainStorm()
    elif name == 'BuzzWord':
        return __makeBuzzWord()
    elif name == 'Calculate':
        return __makeCalculate()
    elif name == 'DemotionFreeze':
        return __makeDemotionFreeze()
    elif name == 'DemotionSpray':
        return __makeDemotionSpray()
    elif name == 'DoubleTalkLeft':
        return __makeDoubleTalkLeft()
    elif name == 'DoubleTalkRight':
        return __makeDoubleTalkRight()
    elif name == 'FingerWag':
        return __makeFingerWag()
    elif name == 'FiredFlame':
        return __makeFiredFlame()
    elif name == 'FiredFlecks':
        return __makeFiredFlecks()
    elif name == 'FreezeAssets':
        return __makeFreezeAssets()
    elif name == 'GearExplosion':
        return __makeGearExplosion(numParticles)
    elif name == 'GlowerPower':
        return __makeGlowerPower()
    elif name == 'HotAir':
        return __makeHotAir()
    elif name == 'PoundKey':
        return __makePoundKey()
    elif name == 'Shred':
        return __makeShred()
    elif name == 'Smile':
        return __makeSmile()
    elif name == 'SpriteFiredFlecks':
        return __makeSpriteFiredFlecks()
    elif name == 'Synergy':
        return __makeSynergy()
    elif name == 'Waterfall':
        return __makeWaterfall()
    elif name == 'PoundKey':
        return __makePoundKey()
    elif name == 'RollODex_A':
        return __makeRollODex_A()
    elif name == 'RollODex_B':
        return __makeRollODex_B()
    elif name == 'Withdrawal':
        return __makeWithdrawal()
    else:
        notify.warning('createParticleEffect() - no name: %s' % name)
    return None


def startParticleEffect(effect, parent, worldRelative = 1):
    notify.debug('startParticleEffect() - name: %s' % effect.getName())
    particles = effect.getParticlesNamed('particles-1')
    if worldRelative == 1:
        particles.setRenderParent(render.node())
    
    effect.enable()
    effect.reparentTo(parent)


def cleanupParticleEffect(effect):
    notify.debug('cleanupParticleEffect() - %s' % effect.getName())
    effect.disable()
    effect.reparentTo(hidden)
    particles = effect.getParticlesNamed('particles-1')
    particles.setRenderParent(particles.node)
    effect.cleanup()


def aimEffect(effect, origin, target, parent = None):
    if parent:
        effect.reparentTo(parent)
    
    effect.setPos(origin)
    heading = math.atan((target[0] - origin[0]) / (target[1] - origin[1]))
    pitch = math.atan((target[2] - origin[2]) / (target[1] - origin[1]))
    conversion = math.pi * 180
    effect.setHpr(heading * conversion, pitch * conversion, 0)
    return effect


def setEffectTexture(effect, name, color = None):
    particles = effect.getParticlesNamed('particles-1')
    np = getParticle(name)
    if color:
        particles.renderer.setColor(color)
    
    particles.renderer.setFromNode(np)


def __loadParticleFile(effect, name):
    if launcher and not launcher.isDummy():
        pfile = os.path.join(launcher.getInstallDir(), 'phase_4/etc/' + name)
    else:
        pfile = 'phase_4/etc/' + name
    if not os.path.exists(pfile):
        pfile = os.path.expandvars('$TOONTOWN/src/battle/' + name)
        if not os.path.exists(pfile):
            notify.warning('__loadParticleFile() - no path: %s' % pfile)
            return None
        
    
    notify.debug('Loading particle file: %s' % pfile)
    effect.loadConfig(Filename(pfile))


def __makeSynergy():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'synergy.ptf')
    return effect


def __makeWithdrawal():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'withdrawal.ptf')
    return effect


def __makeSmile():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'smile.ptf')
    return effect


def __makeCalculate():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'calculate.ptf')
    return effect


def __makeFingerWag():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'fingerwag.ptf')
    return effect


def __makeShred():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'shred.ptf')
    return effect


def __makeWaterfall():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'waterfall.ptf')
    return effect


def __makePoundKey():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'poundkey.ptf')
    return effect


def __makeRollODex_A():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'rollodex_A.ptf')
    return effect


def __makeRollODex_B():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'rollodex_B.ptf')
    return effect


def __makeDemotionSpray():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'demotionSpray.ptf')
    return effect


def __makeDemotionFreeze():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'demotionFreeze.ptf')
    return effect


def __makeFiredFlame():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'firedFlame.ptf')
    return effect


def __makeFiredFlecks():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'firedFlecks.ptf')
    return effect


def __makeGlowerPower():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'glowerPowerKnives.ptf')
    return effect


def __makeBuzzWord():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'buzzWord.ptf')
    return effect


def __makeDoubleTalkLeft():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'doubleTalkLeft.ptf')
    return effect


def __makeDoubleTalkRight():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'doubleTalkRight.ptf')
    return effect


def __makeHotAir():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'hotAirSpray.ptf')
    return effect


def __makeFreezeAssets():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'freezeAssets.ptf')
    return effect


def __makeBrainStorm():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'brainStorm.ptf')
    return effect


def __makeSpriteFiredFlecks():
    effect = ParticleEffect()
    __loadParticleFile(effect, 'spriteFiredFlecks.ptf')
    return effect


def __makeGearExplosion(numParticles = None):
    effect = ParticleEffect()
    __loadParticleFile(effect, 'gearExplosion.ptf')
    if numParticles:
        particles = effect.getParticlesNamed('particles-1')
        particles.setPoolSize(numParticles)
    
    return effect


def __makeBigGearExplosion(numParticles = None):
    effect = ParticleEffect()
    __loadParticleFile(effect, 'gearExplosionBig.ptf')
    if numParticles:
        particles = effect.getParticlesNamed('particles-1')
        particles.setPoolSize(numParticles)
    
    return effect

