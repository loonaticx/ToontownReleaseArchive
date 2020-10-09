# Source Generated with Decompyle++
# File: RingTrack.pyo (Python 2.0)

import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('RingTrack')

def Eval(ringTrack, t):
    t = float(t)
    seqStart = 0.0
    for seq in ringTrack:
        duration = float(seq[0])
        seqEnd = seqStart + duration
        if t < seqEnd:
            seqT = (t - seqStart) / duration
            return __evalSeq(seq, seqT)
        else:
            seqStart = seqEnd
    
    if t == seqStart:
        notify.debug('time value at end of ring track: ' + str(t) + ' == ' + str(seqStart))
    else:
        notify.debug('time value beyond end of ring track: ' + str(t) + ' > ' + str(seqStart))
    lastSeq = ringTrack[len(ringTrack) - 1]
    return __evalSeq(lastSeq, 1.0)


def __evalSeq(seq, t):
    if seq[1] == None:
        return seq[2]
    elif callable(seq[1]):
        function = seq[1]
        arguments = []
        if len(seq) > 2:
            arguments = seq[2]
        
        return function(t, *arguments)
    else:
        return Eval(seq[1], t)


def ringLerp(t, a, b):
    invT = 1.0 - t
    return (float(a[0]) * invT + float(b[0]) * t, float(a[1]) * invT + float(b[1]) * t)

