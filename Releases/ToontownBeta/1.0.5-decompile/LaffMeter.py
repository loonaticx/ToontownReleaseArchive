# Source Generated with Decompyle++
# File: LaffMeter.pyo (Python 2.0)

from ShowBaseGlobal import *
import DistributedAvatar
import ToontownGlobals
from DirectGui import *

class LaffMeter(DirectFrame):
    deathColor = Vec4(0.58039216, 0.80392157, 0.34117647, 1.0)
    
    def __init__(self, avdna, hp, maxHp):
        DirectFrame.__init__(self, relief = None)
        self.initialiseoptions(LaffMeter)
        self.style = avdna
        self.av = None
        self.hp = hp
        self.maxHp = maxHp
        if self.style.type == 't':
            self.isToon = 1
        else:
            self.isToon = 0
        self.load()

    
    def load(self):
        self.pallet = loader.loadModelOnce('phase_3/models/gui/laff_o_meter')
        if self.isToon:
            hType = self.style.getType()
            if hType == 'dog':
                headModel = self.pallet.find('**/doghead')
            elif hType == 'cat':
                headModel = self.pallet.find('**/cathead')
            elif hType == 'mouse':
                headModel = self.pallet.find('**/mousehead')
            elif hType == 'horse':
                headModel = self.pallet.find('**/horsehead')
            elif hType == 'rabbit':
                headModel = self.pallet.find('**/bunnyhead')
            elif hType == 'fowl':
                headModel = self.pallet.find('**/duckhead')
            else:
                raise StandardError('unknown toon species: ', hType)
            self.color = self.style.getHeadColor()
            self['image'] = headModel
            self['image_color'] = self.color
            self.setScale(0.1)
            self.frown = DirectFrame(parent = self, relief = None, image = self.pallet.find('**/frown'))
            self.smile = DirectFrame(parent = self, relief = None, image = self.pallet.find('**/smile'))
            self.eyes = DirectFrame(parent = self, relief = None, image = self.pallet.find('**/eyes'))
            self.openSmile = DirectFrame(parent = self, relief = None, image = self.pallet.find('**/open_smile'))
            self.tooth1 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_1'))
            self.tooth2 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_2'))
            self.tooth3 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_3'))
            self.tooth4 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_4'))
            self.tooth5 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_5'))
            self.tooth6 = DirectFrame(parent = self.openSmile, relief = None, image = self.pallet.find('**/tooth_6'))
            self.maxLabel = DirectLabel(parent = self.eyes, relief = None, pos = (0.442, 0, 0.051), text = '120', text_scale = 0.4, text_font = ToontownGlobals.getInterfaceFont())
            self.hpLabel = DirectLabel(parent = self.eyes, relief = None, pos = (-0.398, 0, 0.051), text = '120', text_scale = 0.4, text_font = ToontownGlobals.getInterfaceFont())
            self.teeth = [
                self.tooth6,
                self.tooth5,
                self.tooth4,
                self.tooth3,
                self.tooth2,
                self.tooth1]
            self.fractions = [
                0.0,
                0.166666,
                0.333333,
                0.5,
                0.666666,
                0.833333]
        

    
    def destroy(self):
        if self.av:
            self.ignore(self.av.uniqueName('hpChange'))
        
        del self.style
        del self.av
        del self.hp
        del self.maxHp
        self.pallet.removeNode()
        del self.pallet
        if self.isToon:
            del self.frown
            del self.smile
            del self.openSmile
            del self.tooth1
            del self.tooth2
            del self.tooth3
            del self.tooth4
            del self.tooth5
            del self.tooth6
            del self.teeth
            del self.fractions
            del self.maxLabel
            del self.hpLabel
        
        DirectFrame.destroy(self)

    
    def adjustTeeth(self):
        if self.isToon:
            for i in range(len(self.teeth)):
                if self.hp > self.maxHp * self.fractions[i]:
                    self.teeth[i].show()
                else:
                    self.teeth[i].hide()
            
        

    
    def adjustText(self):
        if self.isToon:
            self.maxLabel['text'] = str(self.maxHp)
            self.hpLabel['text'] = str(self.hp)
        

    
    def adjustFace(self, hp, maxHp):
        if self.isToon:
            self.frown.hide()
            self.smile.hide()
            self.openSmile.hide()
            self.eyes.hide()
            for tooth in self.teeth:
                tooth.hide()
            
            self.hp = hp
            self.maxHp = maxHp
            if self.hp < 1:
                self.frown.show()
                self['image_color'] = self.deathColor
            elif self.hp >= self.maxHp:
                self.smile.show()
                self.eyes.show()
                self['image_color'] = self.color
                self.adjustText()
            else:
                self.openSmile.show()
                self.eyes.show()
                self.maxLabel.show()
                self.hpLabel.show()
                self['image_color'] = self.color
                self.adjustTeeth()
                self.adjustText()
        

    
    def start(self):
        if self.av:
            self.hp = self.av.hp
            self.maxHp = self.av.maxHp
        
        if self.isToon:
            self.show()
            self.adjustFace(self.hp, self.maxHp)
            if self.av:
                self.accept(self.av.uniqueName('hpChange'), self.adjustFace)
            
        

    
    def stop(self):
        if self.isToon:
            self.hide()
            if self.av:
                self.ignore(self.av.uniqueName('hpChange'))
            
        

    
    def setAvatar(self, av):
        if self.av:
            self.ignore(self.av.uniqueName('hpChange'))
        
        self.av = av


