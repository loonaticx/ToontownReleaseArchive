# Source Generated with Decompyle++
# File: WaitInterval.pyo (Python 2.0)

from PandaModules import *
from Interval import *

class WaitInterval(Interval):
    waitNum = 1
    
    def __init__(self, duration, name = None):
        if name == None:
            name = 'Wait-%d' % WaitInterval.waitNum
            WaitInterval.waitNum += 1
        
        Interval.__init__(self, name, duration)


