# Source Generated with Decompyle++
# File: MovieToonVictory.pyo (Python 2.0)

from IntervalGlobal import *
from RewardPanel import *
import MovieCamera
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('MovieToonVictory')

def __findToonReward(rewards, toon):
    for r in rewards:
        if r['toon'] == toon:
            return r
        
    
    return None


def doToonVictory(localToonActive, toons, rewardDicts, rpanel):
    tracks = []
    if localToonActive == 1:
        tracks.append(FunctionInterval(rpanel.show))
    
    camTracks = []
    endTracks = []
    for t in toons:
        rdict = __findToonReward(rewardDicts, t)
        expTrack = rpanel.getExpTrack(t, rdict['exp'], rdict['inv'])
        if expTrack:
            tracks.insert(1, FunctionInterval(t.loop, extraArgs = [
                'victory']))
            tracks.append(expTrack)
            endTracks.append(FunctionInterval(t.loop, extraArgs = [
                'neutral']))
            camDuration = expTrack.getDuration()
            camExpTrack = MovieCamera.chooseRewardShot(t, camDuration)
            camTracks.append(MovieCamera.chooseRewardShot(t, camDuration))
        
    
    if localToonActive == 1:
        tracks.append(FunctionInterval(rpanel.hide))
    
    tracks = tracks + endTracks
    mtrack = Track(tracks)
    camTrack = Track(camTracks)
    return (mtrack, camTrack)

