# Source Generated with Decompyle++
# File: DistributedSuitPlanner.pyo (Python 2.0)

from ShowBaseGlobal import *
import DistributedObject
import SuitPlannerBase
import ClockObject

class DistributedSuitPlanner(DistributedObject.DistributedObject, SuitPlannerBase.SuitPlannerBase):
    
    def __init__(self, cr):
        self.clock = ClockObject.ClockObject.getGlobalClock()
        DistributedObject.DistributedObject.__init__(self, cr)
        SuitPlannerBase.SuitPlannerBase.__init__(self)
        return None


