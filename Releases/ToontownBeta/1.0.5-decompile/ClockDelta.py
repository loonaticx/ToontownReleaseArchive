# Source Generated with Decompyle++
# File: ClockDelta.pyo (Python 2.0)

from PandaModules import *
import DirectNotifyGlobal
import math
notify = DirectNotifyGlobal.directNotify.newCategory('ClockDelta')
deltaSec = 0
deltaUsec = 0
cdelta = 0.0
globalClock = ClockObject.getGlobalClock()

try:
    wantTimestamps = base.config.GetBool('want-timestamps', 1)
except:
    wantTimestamps = simbase.config.GetBool('want-timestamps', 1)


def initClockDelta(sec, usec):
    global deltaSec, deltaUsec, cdelta
    notify.debug('init clock delta: %f %f' % (sec, usec))
    deltaSec = sec
    deltaUsec = usec
    cdelta = globalClock.getFrameTime()


def getServerTime():
    tv = TimeVal()
    getTimeOfDay(tv)
    return [
        tv.getSec(),
        tv.getUsec()]


def serverTime2frameTime(sec, usec):
    return float(sec) + float(usec) / 1000000.0


def serverTime2frameTimeDelta(sec, usec):
    if wantTimestamps:
        tsec = sec - deltaSec
        tusec = usec - deltaUsec
        if usec < 0:
            tsec = tsec - 1
            tusec = tusec + 1000000
        
        return serverTime2frameTime(tsec, tusec) + cdelta
    else:
        return globalClock.getFrameTime()


def localElapsedTime(sec, usec):
    server_t0 = serverTime2frameTimeDelta(sec, usec)
    client_t0 = globalClock.getFrameTime()
    notify.debug('-------------')
    notify.debug('real time: %f' % globalClock.getRealTime())
    notify.debug('server_t0: %f' % server_t0)
    notify.debug('client_t0: %f' % client_t0)
    dt = client_t0 - server_t0
    if dt >= 0.0:
        return dt
    else:
        notify.debug('negative clock delta: %f' % dt)
        return 0.0


def frameTime2serverTime(time):
    return (math.floor(time), (time - math.floor(time)) * 1000000.0)


def frameTime2serverTimeDelta(time):
    (tsec, tusec) = frameTime2serverTime(time - cdelta)
    sec = tsec + deltaSec
    usec = tusec + deltaUsec
    if usec >= 1000000:
        sec = sec + 1
        usec = usec - 1000000
    
    return (sec, usec)

