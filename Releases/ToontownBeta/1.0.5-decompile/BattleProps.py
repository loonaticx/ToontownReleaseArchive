# Source Generated with Decompyle++
# File: BattleProps.pyo (Python 2.0)

from PandaModules import *
import Actor
import DirectNotifyGlobal
Props = (('feather', 'feather-mod', 'feather-chan'), ('lips', 'lips'), ('lipstick', 'lipstick'), ('hat', 'hat'), ('cane', 'cane'), ('cubes', 'cubes-mod', 'cubes-chan'), ('fishing-pole', 'fishing-pole-mod', 'fishing-pole-chan'), ('1dollar', '1dollar-bill-mod', '1dollar-bill-chan'), ('big-magnet', 'magnet'), ('hypno-goggles', 'hypnotize-mod', 'hypnotize-chan'), ('banana', 'banana-peel-mod', 'banana-peel-chan'), ('rake', 'rake-mod', 'rake-chan'), ('marbles', 'marbles-mod', 'marbles-chan'), ('tnt', 'tnt-mod', 'tnt-chan'), ('trapdoor', 'trapdoor'), ('quicksand', 'quicksand'), ('megaphone', 'megaphone'), ('creampie', 'tart'), ('fruitpie-slice', 'fruit-pie-slice'), ('creampie-slice', 'cream-pie-slice'), ('birthday-cake', 'birthday-cake-mod', 'birthday-cake-chan'), ('squirting-flower', 'squirting-flower'), ('glass', 'glass-mod', 'glass-chan'), ('water-gun', 'water-gun'), ('bottle', 'bottle'), ('firehose', 'firehose-mod', 'firehose-chan'), ('hydrant', 'hydrant'), ('button', 'button'), ('flowerpot', 'flowerpot-mod', 'flowerpot-chan'), ('sandbag', 'sandbag-mod', 'sandbag-chan'), ('anvil', 'anvil-mod', 'anvil-chan'), ('weight', 'weight-mod', 'weight-chan'), ('safe', 'safe-mod', 'safe-chan'), ('piano', 'piano-mod', 'piano-chan'), ('rake-react', 'rake-step-mod', 'rake-step-chan'), ('pad', 'pad'), ('propeller', 'propeller-mod', 'propeller-chan'), ('calculator', 'calculator-mod', 'calculator-chan'), ('rollodex', 'roll-o-dex'), ('rubber-stamp', 'rubber-stamp'), ('rubber-stamp-pad', 'rubber-stamp-pad-mod', 'rubber-stamp-pad-chan'), ('smile', 'smile-mod', 'smile-chan'), ('golf-club', 'golf-club'), ('golf-ball', 'golf-ball'), ('redtape', 'redtape'), ('redtape-tube', 'redtape-tube'), ('bounced-check', 'bounced-check'), ('calculator', 'calculator-mod', 'calculator-chan'), ('clip-on-tie', 'clip-on-tie-mod', 'clip-on-tie-chan'), ('pen', 'pen'), ('pencil', 'pencil'), ('phone', 'phone'), ('receiver', 'receiver'), ('sharpener', 'sharpener'), ('shredder', 'shredder'), ('shredder-paper', 'shredder-paper-mod', 'shredder-paper-chan'), ('watercooler', 'watercooler'), ('dagger', 'dagger'), ('card', 'card'), ('spray', 'spray'), ('splash', 'splash'), ('splat', 'splat-mod', 'splat-chan'))
CreampieColor = Vec4(250.0 / 255.0, 241.0 / 255.0, 24.0 / 255.0, 1.0)
FruitpieColor = Vec4(55.0 / 255.0, 40.0 / 255.0, 148.0 / 255.0, 1.0)
BirthdayCakeColor = Vec4(253.0 / 255.0, 119.0 / 255.0, 220.0 / 255.0, 1.0)
Splats = {
    'tart': (0.3, FruitpieColor),
    'fruitpie-slice': (0.5, FruitpieColor),
    'creampie-slice': (0.5, CreampieColor),
    'fruitpie': (0.7, FruitpieColor),
    'creampie': (0.7, CreampieColor),
    'birthday-cake': (0.9, BirthdayCakeColor) }
Variants = ('tart', 'fruitpie', 'splat-tart', 'splat-fruitpie-slice', 'splat-creampie-slice', 'splat-fruitpie', 'splat-creampie', 'splat-birthday-cake', 'splash-from-splat', 'clip-on-tie', 'lips', 'small-magnet', '5dollar', '10dollar')
PropFilePrefix = 'phase_5/models/props/'

class PropPool:
    notify = DirectNotifyGlobal.directNotify.newCategory('PropPool')
    
    def __init__(self):
        self.props = { }
        self.propCache = []
        self.propStrings = { }
        self.propTypes = { }
        self.maxPoolSize = base.config.GetInt('prop-pool-size', 12)
        for p in Props:
            propName = p[0]
            modelName = p[1]
            if len(p) == 3:
                animName = p[2]
                propPath = PropFilePrefix + modelName
                animPath = PropFilePrefix + animName
                self.propTypes[propName] = 'actor'
                self.propStrings[propName] = (propPath, animPath)
            else:
                propPath = PropFilePrefix + modelName
                self.propTypes[propName] = 'model'
                self.propStrings[propName] = (propPath,)
        
        propName = 'tart'
        self.propStrings[propName] = (PropFilePrefix + 'tart',)
        self.propTypes[propName] = 'model'
        propName = 'fruitpie'
        self.propStrings[propName] = (PropFilePrefix + 'tart',)
        self.propTypes[propName] = 'model'
        splatAnimFileName = PropFilePrefix + 'splat-chan'
        for splat in Splats.keys():
            propName = 'splat-' + splat
            self.propStrings[propName] = (PropFilePrefix + 'splat-mod', splatAnimFileName)
            self.propTypes[propName] = 'actor'
        
        propName = 'splash-from-splat'
        self.propStrings[propName] = (PropFilePrefix + 'splat-mod', splatAnimFileName)
        self.propTypes[propName] = 'actor'
        propName = 'small-magnet'
        self.propStrings[propName] = (PropFilePrefix + 'magnet',)
        self.propTypes[propName] = 'model'
        propName = '5dollar'
        self.propStrings[propName] = (PropFilePrefix + '1dollar-bill-mod', PropFilePrefix + '1dollar-bill-chan')
        self.propTypes[propName] = 'actor'
        propName = '10dollar'
        self.propStrings[propName] = (PropFilePrefix + '1dollar-bill-mod', PropFilePrefix + '1dollar-bill-chan')
        self.propTypes[propName] = 'actor'

    
    def makeVariant(self, name):
        if name == 'tart':
            self.props[name].setScale(0.5)
        elif name == 'fruitpie':
            self.props[name].setScale(0.75)
        elif name[:6] == 'splat-':
            prop = self.props[name]
            scale = prop.getScale() * Splats[name[6:]][0]
            prop.setScale(scale)
            prop.setColor(Splats[name[6:]][1])
        elif name == 'splash-from-splat':
            self.props[name].setColor(Vec4(0.75, 0.75, 1.0, 1.0))
        elif name == 'clip-on-tie':
            tie = self.props[name]
            tie.getChild(0).setHpr(21.04, -19.65, -9.46)
        elif name == 'small-magnet':
            self.props[name].setScale(0.5)
        elif name == 'shredder-paper':
            paper = self.props[name]
            paper.setPosHpr(2.22, -0.95, 1.16, 0, -53.75, 123.69)
            paper.flattenMedium()
        elif name == 'lips':
            lips = self.props[name]
            lips.setPos(0, 0, -3.04)
            lips.flattenMedium()
        

    
    def unloadProps(self):
        for p in self.props.values():
            if type(p) != type(()):
                self.delProp(p)
            
        
        self.props = { }
        self.propCache = []

    
    def getProp(self, name):
        return self._PropPool__getPropCopy(name)

    
    def __getPropCopy(self, name):
        if self.propTypes[name] == 'actor':
            if not self.props.has_key(name):
                prop = Actor.Actor()
                prop.loadModel(self.propStrings[name][0])
                animDict = { }
                animDict[name] = self.propStrings[name][1]
                prop.loadAnims(animDict)
                prop.name = name
                self.storeProp(name, prop)
                if name in Variants:
                    self.makeVariant(name)
                
            
            return Actor.Actor(other = self.props[name])
        elif not self.props.has_key(name):
            prop = loader.loadModel(self.propStrings[name][0])
            prop.name = name
            self.storeProp(name, prop)
            if name in Variants:
                self.makeVariant(name)
            
        
        return self.props[name].copyTo(hidden)

    
    def storeProp(self, name, prop):
        self.props[name] = prop
        self.propCache.append(prop)
        if len(self.props) > self.maxPoolSize:
            oldest = self.propCache.pop(0)
            del self.props[oldest.name]
            self.delProp(oldest)
        
        self.notify.debug('props = %s' % self.props)
        self.notify.debug('propCache = %s' % self.propCache)

    
    def getPropType(self, name):
        return self.propTypes[name]

    
    def delProp(self, prop):
        if prop == None:
            self.notify.warning('tried to delete null prop!')
            return None
        
        if isinstance(prop, Actor.Actor):
            prop.cleanup()
        else:
            prop.removeNode()


globalPropPool = PropPool()
