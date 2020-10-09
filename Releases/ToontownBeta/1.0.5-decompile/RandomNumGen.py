# Source Generated with Decompyle++
# File: RandomNumGen.pyo (Python 2.0)

import DirectNotifyGlobal
import whrandom

def generateSeed():
    
    def randint():
        return whrandom.randint(1, 256)

    x = randint()
    y = x
    z = x
    while y == x:
        y = randint()
    while z == x or z == y:
        z = randint()
    RandomNumGen.notify.debug('setting random seed to: ' + str(x) + ',' + str(y) + ',' + str(z))
    return [
        x,
        y,
        z]


class RandomNumGen:
    notify = DirectNotifyGlobal.directNotify.newCategory('RandomNumGen')
    
    def __init__(self, seed):
        self.notify.debug('seed: ' + str(seed))
        x = seed[0]
        y = seed[1]
        z = seed[2]
        g = whrandom.whrandom()
        g.seed(x, y, z)
        self._RandomNumGen__generator = g

    
    def choice(self, seq):
        return self._RandomNumGen__generator.choice(seq)

    
    def randint(self, a, b):
        return self._RandomNumGen__generator.randint(a, b)

    
    def random(self):
        return self._RandomNumGen__generator.random()


