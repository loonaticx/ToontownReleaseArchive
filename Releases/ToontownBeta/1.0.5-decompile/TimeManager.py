# Source Generated with Decompyle++
# File: TimeManager.pyo (Python 2.0)

from ShowBaseGlobal import *
from PandaObject import *
import DistributedObject
import DirectNotifyGlobal
import ClockDelta

class TimeManager(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('TimeManager')
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.setNeverDisable(1)
        return None

    
    def setServerTime(self, sec, usec):
        self.notify.debug('Setting server time to %s %s' % (sec, usec))
        ClockDelta.initClockDelta(sec, usec)
        return None


