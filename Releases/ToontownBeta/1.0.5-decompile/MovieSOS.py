# Source Generated with Decompyle++
# File: MovieSOS.pyo (Python 2.0)

from IntervalGlobal import *
import MovieCamera
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('MovieSOS')

def doSOSs(calls):
    if len(calls) == 0:
        return (None, None)
    
    
    def callerFunc(toon, handle):
        toon.setChatAbsolute('%s HELP!' % handle.getName(), CFSpeech | CFTimeout)
        handle.d_setWhisper('%s needs help in battle!' % toon.getName())

    
    def calleeFunc(toon, handle):
        toon.setChatAbsolute('%s HELP!' % handle.getName(), CFSpeech | CFTimeout)

    
    def observerFunc(toon):
        toon.setChatAbsolute('HELP!', CFSpeech | CFTimeout)

    ivals = []
    for c in calls:
        toon = c['toon']
        targetType = c['targetType']
        handle = c['target']
        ivals.append(WaitInterval(0.5))
        if targetType == 'observer':
            ival = FunctionInterval(observerFunc, extraArgs = [
                toon])
        elif targetType == 'caller':
            ival = FunctionInterval(callerFunc, extraArgs = [
                toon,
                handle])
        elif targetType == 'callee':
            ival = FunctionInterval(calleeFunc, extraArgs = [
                toon,
                handle])
        else:
            notify.error('ivalid target type: %s' % targetType)
        ivals.append(ival)
        ivals.append(WaitInterval(2.0))
        notify.debug('toon: %s calls for help' % toon.getName())
    
    mtrack = Track(ivals)
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseSOSShot(toon, camDuration)
    return (mtrack, camTrack)

