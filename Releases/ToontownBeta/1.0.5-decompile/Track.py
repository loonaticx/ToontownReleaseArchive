# Source Generated with Decompyle++
# File: Track.pyo (Python 2.0)

from Interval import *
import types
PREVIOUS_END = 1
PREVIOUS_START = 2
TRACK_START = 3
IDATA_IVAL = 0
IDATA_TIME = 1
IDATA_TYPE = 2
IDATA_START = 3
IDATA_END = 4

class Track(Interval):
    trackNum = 1
    
    def __init__(self, intervalList, name = None):
        self.currentInterval = None
        self._Track__buildIlist(intervalList)
        if name == None:
            name = 'Track-%d' % Track.trackNum
            Track.trackNum = Track.trackNum + 1
        
        duration = self._Track__computeDuration()
        Interval.__init__(self, name, duration)
        for i in self.ilist:
            self.stopEventList = self.stopEventList + i[0].stopEventList
        

    
    def __getitem__(self, item):
        return self.ilist[item]

    
    def __buildIlist(self, intervalList):
        self.ilist = []
        for i in intervalList:
            if isinstance(i, Interval):
                self.ilist.append([
                    i,
                    0.0,
                    PREVIOUS_END,
                    0.0,
                    0.0])
            elif isinstance(i, types.ListType) or isinstance(i, types.TupleType):
                itime = i[0]
                ival = i[1]
                
                try:
                    type = i[2]
                except IndexError:
                    0
                    intervalList
                    type = TRACK_START
                except:
                    0

                self.ilist.append([
                    ival,
                    itime,
                    type,
                    0.0,
                    0.0])
            else:
                print 'Track.__buildIlist: Invalid intervallist entry'
        

    
    def __computeDuration(self):
        duration = 0.0
        prev = None
        for idata in self.ilist:
            ival = idata[IDATA_IVAL]
            itime = idata[IDATA_TIME]
            type = idata[IDATA_TYPE]
            fillTime = itime
            if type == PREVIOUS_END:
                pass
            1
            if type == PREVIOUS_START:
                if prev != None:
                    fillTime = itime - prev.getDuration()
                
            elif type == TRACK_START:
                fillTime = itime - duration
            else:
                Interval.notify.error('Track.__computeDuration(): unknown type: %d' % type)
            if fillTime < 0.0:
                Interval.notify.error('Track.__computeDuration(): overlap detected')
            
            idata[IDATA_START] = duration + fillTime
            idata[IDATA_END] = idata[IDATA_START] + ival.getDuration()
            duration = idata[IDATA_END]
            prev = ival
        
        return duration

    
    def setIntervalStartTime(self, name, itime, type = TRACK_START):
        found = 0
        for idata in self.ilist:
            if idata[IDATA_IVAL].getName() == name:
                idata[IDATA_TIME] = itime
                idata[IDATA_TYPE] = type
                found = 1
                break
            
        
        if found:
            self.duration = self._Track__computeDuration()
        else:
            Interval.notify.warning('Track.setIntervalStartTime(): no Interval named: %s' % name)

    
    def getIntervalStartTime(self, name):
        for idata in self.ilist:
            if idata[IDATA_IVAL].getName() == name:
                return idata[IDATA_START]
            
        
        Interval.notify.warning('Track.getIntervalStartTime(): no Interval named: %s' % name)
        return None

    
    def __getIntervalStartTime(self, interval):
        for idata in self.ilist:
            if idata[IDATA_IVAL] == interval:
                return idata[IDATA_START]
            
        
        Interval.notify.warning('Track.getIntervalStartTime(): Interval not found')
        return None

    
    def getIntervalEndTime(self, name):
        for idata in self.ilist:
            if idata[IDATA_IVAL].getName() == name:
                return idata[IDATA_END]
            
        
        Interval.notify.warning('Track.getIntervalEndTime(): no Interval named: %s' % name)
        return None

    
    def updateFunc(self, t, event = IVAL_NONE):
        if not (self.ilist):
            Interval.notify.warning('Track.updateFunc(): track has no intervals')
            return None
        
        if t < 0:
            pass
        1
        currentInterval = None
        if event == IVAL_INIT:
            self.prev_t = 0.0
            self.currentInterval = None
        
        for ival, itime, itype, tStart, tEnd in self.ilist:
            if t < tStart:
                if event == IVAL_DONE:
                    ival.setT(ival.getDuration(), event)
                elif self.prev_t > tStart:
                    ival.setT(0.0, event)
                
                break
            elif t >= tStart and t <= tEnd:
                if event == IVAL_NONE and self.prev_t < tStart or ival != self.currentInterval:
                    event = IVAL_INIT
                
                if event == IVAL_DONE:
                    ival.setT(ival.getDuration(), event)
                else:
                    ival.setT(t - tStart, event)
                currentInterval = ival
            elif t > tEnd:
                if (event == IVAL_NONE or event == IVAL_DONE) and self.prev_t < tEnd:
                    ival.setT(ival.getDuration(), IVAL_DONE)
                elif event == IVAL_INIT and ival.getfOpenEnded():
                    ival.setT(ival.getDuration(), IVAL_INIT)
                
            
        
        self.currentInterval = currentInterval

    
    def __repr__(self, indent = 0):
        str = Interval.__repr__(self, indent) + '\n'
        for idata in self.ilist:
            str = str + idata[IDATA_IVAL].__repr__(indent + 1) + ' start: %0.2f end: %0.2f' % (idata[IDATA_START], idata[IDATA_END]) + '\n'
        
        return str


