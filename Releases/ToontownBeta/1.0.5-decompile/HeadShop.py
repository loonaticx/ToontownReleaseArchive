# Source Generated with Decompyle++
# File: HeadShop.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
import PandaObject
import OnscreenText
import AvatarDNA
import Avatar
import ScrollingLabel
import Button
import StateData
ANIMAL = 0
HEAD = 1
MUZZLE = 2
AnimalTypes = [
    'dog',
    'cat',
    'horse',
    'mouse',
    'rabbit',
    'fowl']
HeadTypes = [
    'long',
    'short']
MuzzleTypes = [
    'long',
    'short']

class HeadShop(PandaObject.PandaObject, StateData.StateData):
    
    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.soundEffect = None
        return None

    
    def enter(self, toon):
        if toon == None:
            return None
        
        if self.isLoaded == 0:
            self.load()
        
        base.disableMouse()
        camera.reparentTo(render)
        camera.setPos(0, 0, 0)
        camera.setHpr(0, 0, 0)
        if self.background:
            self.background.reparentTo(render)
            self.background.setPos(-5.0, 31.5, -9.75)
        
        toon.setPos(0.5, 18.0, -3.8)
        toon.setHpr(170.0, 0.0, 0.0)
        toon.loop('neutral')
        self.dna = toon.getStyle()
        self.animal = self.dna.getType()
        self.head = self.dna.getHeadSize()
        self.muzzle = self.dna.getMuzzleSize()
        if self.animalPicker:
            self.animalPicker.setItem(AnimalTypes.index(self.animal))
            self.animalPicker.setKeyFocus(1)
            self.animalPicker.manage()
        
        if self.headPicker:
            self.headPicker.setItem(HeadTypes.index(self.head))
            self.headPicker.manage()
        
        if self.muzzlePicker:
            self.muzzlePicker.setItem(MuzzleTypes.index(self.muzzle))
            self.muzzlePicker.manage()
            self.muzzleManaged = 1
        
        if self.doneButton:
            self.accept(self.doneButton.button.getBehaviorEvent(), self._HeadShop__handleForward)
            self.doneButton.manage()
        
        self.selection = ANIMAL
        self._HeadShop__customizeMenu()
        self.accept('up-up', self._HeadShop__handleUpArrow)
        self.accept('down-up', self._HeadShop__handleDownArrow)
        self.accept('Kisser', self._HeadShop__swapMuzzle, [
            toon])
        self.accept('Noggin', self._HeadShop__swapSkull, [
            toon])
        self.accept('Critter', self._HeadShop__swapAnimal, [
            toon])
        return None

    
    def exit(self):
        if self.isLoaded == 0:
            return None
        
        self.ignore('up-up')
        self.ignore('down-up')
        self.ignore('Kisser')
        self.ignore('Noggin')
        self.ignore('Critter')
        self.ignore(self.doneButton.button.getBehaviorEvent())
        self.animalPicker.setKeyFocus(0)
        self.animalPicker.unmanage()
        self.headPicker.setKeyFocus(0)
        self.headPicker.unmanage()
        self.muzzlePicker.setKeyFocus(0)
        self.muzzlePicker.unmanage()
        self.muzzleManaged = 0
        self.background.reparentTo(hidden)
        self.doneButton.unmanage()

    
    def load(self):
        if self.isLoaded == 1:
            return None
        
        self.background = loader.loadModelOnce('phase_3/models/gui/workshop-background')
        self.animalPicker = ScrollingLabel.ScrollingLabel('Critter', AnimalTypes)
        self.animalPicker.setPos(-0.55, 0.5)
        self.headPicker = ScrollingLabel.ScrollingLabel('Noggin', HeadTypes)
        self.headPicker.setPos(-0.55, 0.1)
        self.muzzlePicker = ScrollingLabel.ScrollingLabel('Kisser', MuzzleTypes)
        self.muzzlePicker.setPos(-0.55, -0.3)
        self.doneButton = Button.Button('HeadShopDone', 'Done', event = 'headshopDone')
        self.doneButton.setPos(0.8, -0.9)
        self.soundEffect = base.loadSfx('phase_3/audio/sfx/GUI_create_toon_bodyshop.mp3')
        self.isLoaded = 1
        return None

    
    def unload(self):
        if self.isLoaded == 0:
            return None
        
        self.exit()
        loader.unloadModel('phase_3/models/gui/workshop-background')
        self.animalPicker.cleanup()
        self.animalPicker = None
        self.headPicker.cleanup()
        self.headPicker = None
        self.muzzlePicker.cleanup()
        self.muzzlePicker = None
        self.doneButton.cleanup()
        self.doneButton = None
        self.modelsLoaded = 0
        if self.soundEffect:
            loader.unloadSound(self.soundEffect)
        
        self.isLoaded = 0
        return None

    
    def __handleDownArrow(self):
        self.selection = self.selection + 1
        if self.selection > MUZZLE:
            self.selection = ANIMAL
        
        self._HeadShop__updateMenus()

    
    def __handleUpArrow(self):
        self.selection = self.selection - 1
        if self.selection < ANIMAL:
            self.selection = MUZZLE
        
        self._HeadShop__updateMenus()

    
    def __updateMenus(self):
        if self.selection == ANIMAL:
            self.animalPicker.setKeyFocus(1)
            self.headPicker.setKeyFocus(0)
            self.muzzlePicker.setKeyFocus(0)
        elif self.selection == HEAD:
            self.animalPicker.setKeyFocus(0)
            self.headPicker.setKeyFocus(1)
            self.muzzlePicker.setKeyFocus(0)
        elif self.animal == 'mouse':
            self._HeadShop__handleUpArrow()
        else:
            self.animalPicker.setKeyFocus(0)
            self.headPicker.setKeyFocus(0)
            self.muzzlePicker.setKeyFocus(1)

    
    def __swapMuzzle(self, toon, choice):
        self.muzzle = MuzzleTypes[choice]
        self._HeadShop__swapHead(toon)

    
    def __swapSkull(self, toon, choice):
        self.head = HeadTypes[choice]
        self._HeadShop__swapHead(toon)

    
    def __swapAnimal(self, toon, choice):
        self.animal = AnimalTypes[choice]
        self._HeadShop__customizeMenu()
        self._HeadShop__swapHead(toon)

    
    def __swapHead(self, toon):
        base.playSfx(self.soundEffect)
        newHead = self.animal[0] + self.head[0] + self.muzzle[0]
        if newHead == 'mll':
            newHead = 'mls'
        
        if newHead == 'msl':
            newHead = 'mss'
        
        self.dna.head = newHead
        toon.swapToonHead(newHead)
        toon.loop('neutral', 0)
        toon.swapToonColor(self.dna)

    
    def __customizeMenu(self):
        if self.animal == 'rabbit':
            if not (self.muzzleManaged):
                self.muzzlePicker.manage()
                self.muzzleManaged = 1
            
            self.muzzlePicker.setTitle('Radar')
        elif self.animal == 'mouse':
            self.muzzlePicker.unmanage()
            self.muzzleManaged = 0
        elif not (self.muzzleManaged):
            self.muzzlePicker.manage()
            self.muzzleManaged = 1
        
        self.muzzlePicker.setTitle('Kisser')

    
    def __handleForward(self, item):
        if self.doneButton.button == item:
            messenger.send(self.doneEvent)
        


