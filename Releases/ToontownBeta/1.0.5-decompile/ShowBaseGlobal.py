# Source Generated with Decompyle++
# File: ShowBaseGlobal.pyo (Python 2.0)

from ShowBase import *
import __builtin__
__builtin__.base = ShowBase()
__builtin__.ostream = Notify.out()
__builtin__.directNotify = directNotify
directNotify.setDconfigLevels()

def inspect(anObject):
    import Inspector
    return Inspector.inspect(anObject)

__builtin__.inspect = inspect
