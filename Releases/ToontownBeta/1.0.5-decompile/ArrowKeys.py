# Source Generated with Decompyle++
# File: ArrowKeys.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *

class ArrowKeys(PandaObject):
    UP_KEY = 'up'
    DOWN_KEY = 'down'
    LEFT_KEY = 'left'
    RIGHT_KEY = 'right'
    UP_INDEX = 0
    DOWN_INDEX = 1
    LEFT_INDEX = 2
    RIGHT_INDEX = 3
    NULL_HANDLERS = (None, None, None, None)
    
    def __init__(self):
        self._ArrowKeys__upPressed = 0
        self._ArrowKeys__downPressed = 0
        self._ArrowKeys__leftPressed = 0
        self._ArrowKeys__rightPressed = 0
        self.setPressHandlers(self.NULL_HANDLERS)
        self.setReleaseHandlers(self.NULL_HANDLERS)
        self.accept(self.UP_KEY, self._ArrowKeys__upKeyPressed)
        self.accept(self.DOWN_KEY, self._ArrowKeys__downKeyPressed)
        self.accept(self.LEFT_KEY, self._ArrowKeys__leftKeyPressed)
        self.accept(self.RIGHT_KEY, self._ArrowKeys__rightKeyPressed)

    
    def destroy(self):
        events = [
            self.UP_KEY,
            self.DOWN_KEY,
            self.LEFT_KEY,
            self.RIGHT_KEY]
        for event in events:
            self.ignore(event)
            self.ignore(event + '-up')
        

    
    def upPressed(self):
        return self._ArrowKeys__upPressed

    
    def downPressed(self):
        return self._ArrowKeys__downPressed

    
    def leftPressed(self):
        return self._ArrowKeys__leftPressed

    
    def rightPressed(self):
        return self._ArrowKeys__rightPressed

    
    def setPressHandlers(self, handlers):
        self._ArrowKeys__checkCallbacks(handlers)
        self._ArrowKeys__pressHandlers = handlers

    
    def setReleaseHandlers(self, handlers):
        self._ArrowKeys__checkCallbacks(handlers)
        self._ArrowKeys__releaseHandlers = handlers

    
    def clearPressHandlers(self):
        self.setPressHandlers(self.NULL_HANDLERS)

    
    def clearReleaseHandlers(self):
        self.setReleaseHandlers(self.NULL_HANDLERS)

    
    def __checkCallbacks(self, callbacks):
        for callback in callbacks:
            pass
        

    
    def __doCallback(self, callback):
        if callback:
            callback()
        

    
    def __upKeyPressed(self):
        self.ignore(self.UP_KEY)
        self.accept(self.UP_KEY + '-up', self._ArrowKeys__upKeyReleased)
        self._ArrowKeys__upPressed = 1
        self._ArrowKeys__doCallback(self._ArrowKeys__pressHandlers[self.UP_INDEX])

    
    def __downKeyPressed(self):
        self.ignore(self.DOWN_KEY)
        self.accept(self.DOWN_KEY + '-up', self._ArrowKeys__downKeyReleased)
        self._ArrowKeys__downPressed = 1
        self._ArrowKeys__doCallback(self._ArrowKeys__pressHandlers[self.DOWN_INDEX])

    
    def __leftKeyPressed(self):
        self.ignore(self.LEFT_KEY)
        self.accept(self.LEFT_KEY + '-up', self._ArrowKeys__leftKeyReleased)
        self._ArrowKeys__leftPressed = 1
        self._ArrowKeys__doCallback(self._ArrowKeys__pressHandlers[self.LEFT_INDEX])

    
    def __rightKeyPressed(self):
        self.ignore(self.RIGHT_KEY)
        self.accept(self.RIGHT_KEY + '-up', self._ArrowKeys__rightKeyReleased)
        self._ArrowKeys__rightPressed = 1
        self._ArrowKeys__doCallback(self._ArrowKeys__pressHandlers[self.RIGHT_INDEX])

    
    def __upKeyReleased(self):
        self.ignore(self.UP_KEY + '-up')
        self.accept(self.UP_KEY, self._ArrowKeys__upKeyPressed)
        self._ArrowKeys__upPressed = 0
        self._ArrowKeys__doCallback(self._ArrowKeys__releaseHandlers[self.UP_INDEX])

    
    def __downKeyReleased(self):
        self.ignore(self.DOWN_KEY + '-up')
        self.accept(self.DOWN_KEY, self._ArrowKeys__downKeyPressed)
        self._ArrowKeys__downPressed = 0
        self._ArrowKeys__doCallback(self._ArrowKeys__releaseHandlers[self.DOWN_INDEX])

    
    def __leftKeyReleased(self):
        self.ignore(self.LEFT_KEY + '-up')
        self.accept(self.LEFT_KEY, self._ArrowKeys__leftKeyPressed)
        self._ArrowKeys__leftPressed = 0
        self._ArrowKeys__doCallback(self._ArrowKeys__releaseHandlers[self.LEFT_INDEX])

    
    def __rightKeyReleased(self):
        self.ignore(self.RIGHT_KEY + '-up')
        self.accept(self.RIGHT_KEY, self._ArrowKeys__rightKeyPressed)
        self._ArrowKeys__rightPressed = 0
        self._ArrowKeys__doCallback(self._ArrowKeys__releaseHandlers[self.RIGHT_INDEX])


