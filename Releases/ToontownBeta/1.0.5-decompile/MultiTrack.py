# Source Generated with Decompyle++
# File: MultiTrack.pyo (Python 2.0)

from Interval import *
from Track import *

class MultiTrack(Interval):
    multiTrackNum = 1
    
    def __init__(self, trackList, name = None):
        self.tlist = trackList
        if name == None:
            name = 'MultiTrack-%d' % MultiTrack.multiTrackNum
            MultiTrack.multiTrackNum = MultiTrack.multiTrackNum + 1
        
        duration = self._MultiTrack__computeDuration()
        Interval.__init__(self, name, duration)
        for t in self.tlist:
            self.stopEventList = self.stopEventList + t.stopEventList
        

    
    def __getitem__(self, item):
        return self.tlist[item]

    
    def __computeDuration(self):
        duration = 0.0
        for t in self.tlist:
            dur = t.getDuration()
            if dur > duration:
                duration = dur
            
        
        return duration

    
    def updateFunc(self, t, event = IVAL_NONE):
        for track in self.tlist:
            if event == IVAL_INIT or event == IVAL_DONE:
                track.setT(t, event)
            elif t >= track.duration and self.prev_t < track.duration:
                track.setT(t, event)
            else:
                track.setT(t, event)
        

    
    def __repr__(self, indent = 0):
        str = Interval.__repr__(self, indent) + '\n'
        for t in self.tlist:
            str = str + t.__repr__(indent + 1)
        
        return str


