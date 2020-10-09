# Source Generated with Decompyle++
# File: DownloadWatcher.pyo (Python 2.0)

import DirectObject
import OnscreenText
from PandaModules import *
import Task

class DownloadWatcher(DirectObject.DirectObject):
    
    def __init__(self):
        self.text = OnscreenText.OnscreenText(text = 'Download initializing...', pos = (-1.06, -0.96), fg = (1, 1, 1, 0.5), scale = 0.05, align = TMALIGNLEFT, mayChange = 1)
        self.accept('launcherPercentPhaseComplete', self.update)

    
    def update(self, phase, percent, reqByteRate, actualByteRate):
        self.text.setText('Download %d: %d%%' % (phase, percent))

    
    def cleanup(self):
        self.text.cleanup()
        self.ignoreAll()


