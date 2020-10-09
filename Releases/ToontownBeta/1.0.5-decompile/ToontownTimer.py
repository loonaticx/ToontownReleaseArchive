# Source Generated with Decompyle++
# File: ToontownTimer.pyo (Python 2.0)

from ShowBaseGlobal import *
from ToontownGlobals import *
from DirectGui import *
import OnscreenText
import Task

class ToontownTimer(DirectFrame):
    
    def __init__(self):
        DirectFrame.__init__(self, relief = None, scale = 0.45, image = loader.loadModel('phase_4/models/gui/clock_gui'), text = '0', text_fg = (0, 0, 0, 1), text_font = getInterfaceFont(), text_pos = (-0.01, -0.15), text_scale = 0.35)
        self.initialiseoptions(ToontownTimer)
        self.countdownTask = None
        return None

    
    def posInTopRightCorner(self):
        self.setPos(1.16, 0, 0.83)
        return None

    
    def setTime(self, time):
        if time < 0:
            time = 0
        
        if time > 999:
            time = 999
        
        timeStr = str(time)
        timeStrLen = len(timeStr)
        self['text'] = timeStr
        if time <= 5:
            self['text_fg'] = Vec4(1, 0, 0, 1)
        else:
            self['text_fg'] = Vec4(0, 0, 0, 1)
        if len(timeStr) == 1:
            self['text_scale'] = 0.34
            self['text_pos'] = (-0.015, -0.145)
        elif len(timeStr) == 2:
            self['text_scale'] = 0.27
            self['text_pos'] = (-0.015, -0.12)
        elif len(timeStr) == 3:
            self['text_scale'] = 0.2
            self['text_pos'] = (-0.01, -0.1)
        
        return None

    
    def _timerTask(self, task):
        countdownTime = int(task.duration - task.time)
        if not (self['text_text'] == str(countdownTime)):
            self.setTime(countdownTime)
        
        if task.time >= task.duration:
            if task.callback:
                task.callback()
            
            return Task.done
        else:
            return Task.cont

    
    def countdown(self, duration, callback = None):
        self.countdownTask = Task.Task(self._timerTask)
        self.countdownTask.duration = duration
        self.countdownTask.callback = callback
        taskMgr.removeTasksNamed('timerTask')
        return taskMgr.spawnTaskNamed(self.countdownTask, 'timerTask')

    
    def stop(self):
        if self.countdownTask:
            taskMgr.removeTask(self.countdownTask)
        

    
    def reset(self):
        self.stop()
        self.setTime(0)

    
    def destroy(self):
        self.reset()
        DirectFrame.destroy(self)
        return None

    
    def cleanup(self):
        self.destroy()
        self.notify.warning('Call destroy, not cleanup')
        return None


