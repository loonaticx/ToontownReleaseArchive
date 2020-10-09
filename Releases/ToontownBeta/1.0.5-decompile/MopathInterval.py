# Source Generated with Decompyle++
# File: MopathInterval.pyo (Python 2.0)

from Interval import *
import Mopath

class MopathInterval(Interval):
    mopathNum = 1
    notify = directNotify.newCategory('MopathInterval')
    
    def __init__(self, mopath, node, name = None):
        self.mopath = mopath
        self.node = node
        if name == None:
            name = 'Mopath-%d' % MopathInterval.mopathNum
            MopathInterval.mopathNum += 1
        
        duration = self.mopath.getMaxT()
        Interval.__init__(self, name, duration)

    
    def updateFunc(self, t, event = IVAL_NONE):
        self.mopath.goTo(self.node, t)
        self.notify.debug('updateFunc() - %s: t = %f' % (self.name, t))


