# Source Generated with Decompyle++
# File: PatternPad.pyo (Python 2.0)

from ShowBaseGlobal import *
from DirectGui import *

class PatternPad(DirectFrame):
    ButtonNames = ('upButton', 'rightButton', 'downButton', 'leftButton')
    DI = 0.5
    LI = 1.0
    RI = 0.6
    ButtonDarkColors = ((DI, 0, 0, 1), (0, 0, DI, 1), (DI, DI, 0, 1), (0, DI, 0, 1))
    ButtonLightColors = ((LI, 0, 0, 1), (0, 0, LI, 1), (LI, LI, 0, 1), (0, LI, 0, 1))
    ButtonRolloverColors = ((RI, 0, 0, 1), (0, 0, RI, 1), (RI, RI, 0, 1), (0, RI, 0, 1))
    
    def __init__(self, parent = guiTop, **kw):
        self._PatternPad__pressHandlers = ((lambda db, self = self: self._PatternPad__pressButton(0)), (lambda db, self = self: self._PatternPad__pressButton(1)), (lambda db, self = self: self._PatternPad__pressButton(2)), (lambda db, self = self: self._PatternPad__pressButton(3)))
        self._PatternPad__releaseHandlers = ((lambda db, self = self: self._PatternPad__releaseButton(0)), (lambda db, self = self: self._PatternPad__releaseButton(1)), (lambda db, self = self: self._PatternPad__releaseButton(2)), (lambda db, self = self: self._PatternPad__releaseButton(3)))
        self._PatternPad__enterHandlers = ((lambda db, self = self: self._PatternPad__enterButton(0)), (lambda db, self = self: self._PatternPad__enterButton(1)), (lambda db, self = self: self._PatternPad__enterButton(2)), (lambda db, self = self: self._PatternPad__enterButton(3)))
        self._PatternPad__exitHandlers = ((lambda db, self = self: self._PatternPad__exitButton(0)), (lambda db, self = self: self._PatternPad__exitButton(1)), (lambda db, self = self: self._PatternPad__exitButton(2)), (lambda db, self = self: self._PatternPad__exitButton(3)))
        BP = 0.25
        BBW = 0.02
        BFS = 0.12
        FS = 0.4
        FCI = 0.1
        optiondefs = (('callbacks', None, self.setCallbacks), ('pressHandlers', self._PatternPad__pressHandlers, self.setPressHandlers), ('releaseHandlers', self._PatternPad__releaseHandlers, self.setReleaseHandlers), ('enterHandlers', self._PatternPad__enterHandlers, self.setEnterHandlers), ('exitHandlers', self._PatternPad__exitHandlers, self.setExitHandlers), ('frameSize', (-FS, FS, -FS, FS), None), ('frameColor', (FCI, FCI, FCI, 1), None), ('buttons_frameSize', (-BFS, BFS, -BFS, BFS), None), ('buttons_borderWidth', (BBW, BBW), None), ('buttons_relief', RAISED, None), ('buttons_clickSound', None, None), ('buttons_rolloverSound', None, None), ('upButton_pos', (0, 0, BP), None), ('downButton_pos', (0, 0, -BP), None), ('leftButton_pos', (-BP, 0, 0), None), ('rightButton_pos', (BP, 0, 0), None))
        self.defineoptions(kw, optiondefs, dynamicGroups = ('buttons',))
        DirectFrame.__init__(self, parent)
        for i in range(0, len(self.ButtonNames)):
            self.createcomponent(self.ButtonNames[i], (), 'buttons', DirectButton, (), parent = self, frameColor = self.ButtonDarkColors[i])
        
        self.initialiseoptions(PatternPad)
        self.setPressCallback(None)
        self.setReleaseCallback(None)
        self.setEnterCallback(None)
        self.setExitCallback(None)

    
    def destroy(self):
        for name in self.ButtonNames:
            self.destroycomponent(name)
        
        DirectFrame.destroy(self)

    
    def __getButtons(self):
        buttons = []
        for name in self.ButtonNames:
            buttons.append(self.component(name))
        
        return buttons

    
    def disable(self):
        buttons = self._PatternPad__getButtons()
        for button in buttons:
            button['state'] = DISABLED
        

    
    def enable(self):
        buttons = self._PatternPad__getButtons()
        for button in buttons:
            button['state'] = NORMAL
        

    
    def setPressCallback(self, callback):
        self._PatternPad__clientPressCallback = callback

    
    def setReleaseCallback(self, callback):
        self._PatternPad__clientReleaseCallback = callback

    
    def setEnterCallback(self, callback):
        self._PatternPad__clientEnterCallback = callback

    
    def setExitCallback(self, callback):
        self._PatternPad__clientExitCallback = callback

    
    def setCallbacks(self):
        buttons = self._PatternPad__getButtons()
        if self['callbacks'] == None:
            for button in buttons:
                button['command'] = None
            
        else:
            for i in range(0, len(buttons)):
                buttons[i]['command'] = self['callbacks'][i]
            

    
    def __bindButtonHandlers(self, event, handlerTypeName):
        buttons = self._PatternPad__getButtons()
        if self[handlerTypeName] == None:
            for button in buttons:
                button.unbind(event)
            
        else:
            for i in range(0, len(buttons)):
                buttons[i].bind(event, self[handlerTypeName][i])
            

    
    def setPressHandlers(self):
        self._PatternPad__bindButtonHandlers(B1PRESS, 'pressHandlers')

    
    def setReleaseHandlers(self):
        self._PatternPad__bindButtonHandlers(B1RELEASE, 'releaseHandlers')

    
    def setEnterHandlers(self):
        self._PatternPad__bindButtonHandlers(ENTER, 'enterHandlers')

    
    def setExitHandlers(self):
        self._PatternPad__bindButtonHandlers(EXIT, 'exitHandlers')

    
    def __pressButton(self, index):
        self._PatternPad__lightenButton(index)
        if self._PatternPad__clientPressCallback != None:
            self._PatternPad__clientPressCallback(index)
        

    
    def __releaseButton(self, index):
        self._PatternPad__darkenButton(index)
        if self._PatternPad__clientReleaseCallback != None:
            self._PatternPad__clientReleaseCallback(index)
        

    
    def __enterButton(self, index):
        if self._PatternPad__clientEnterCallback != None:
            self._PatternPad__clientEnterCallback(index)
        

    
    def __exitButton(self, index):
        if self._PatternPad__clientExitCallback != None:
            self._PatternPad__clientExitCallback(index)
        

    
    def __lightenButton(self, index):
        buttons = self._PatternPad__getButtons()
        buttons[index]['frameColor'] = self.ButtonLightColors[index]

    
    def __darkenButton(self, index):
        buttons = self._PatternPad__getButtons()
        buttons[index]['frameColor'] = self.ButtonDarkColors[index]

    
    def simButtonPress(self, index):
        self._PatternPad__lightenButton(index)

    
    def simButtonRelease(self, index):
        self._PatternPad__darkenButton(index)


