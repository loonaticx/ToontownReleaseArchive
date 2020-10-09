# Source Generated with Decompyle++
# File: FrustumD.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_FrustumD():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class FrustumD(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPSkjP2_o_()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPSkjPVXk5:
                libpanda._inPSkjPVXk5(self.this)
            

        
        def overloaded_makeOrtho2D_ptrFrustumd(self):
            returnValue = libpanda._inPSkjP_7T5(self.this)
            return returnValue

        
        def overloaded_makeOrtho2D_ptrFrustumd_double_double_double_double(self, l, r, t, b):
            returnValue = libpanda._inPSkjPIMrK(self.this, l, r, t, b)
            return returnValue

        
        def overloaded_makeOrtho_ptrFrustumd_double_double(self, fnear, ffar):
            returnValue = libpanda._inPSkjPh0j7(self.this, fnear, ffar)
            return returnValue

        
        def overloaded_makeOrtho_ptrFrustumd_double_double_double_double_double_double(self, fnear, ffar, l, r, t, b):
            returnValue = libpanda._inPSkjP6Ca4(self.this, fnear, ffar, l, r, t, b)
            return returnValue

        
        def makePerspectiveHfov(self, xfov, aspect, fnear, ffar):
            returnValue = libpanda._inPSkjPPLl6(self.this, xfov, aspect, fnear, ffar)
            return returnValue

        
        def makePerspectiveVfov(self, yfov, aspect, fnear, ffar):
            returnValue = libpanda._inPSkjPGN1m(self.this, yfov, aspect, fnear, ffar)
            return returnValue

        
        def makePerspective(self, xfov, yfov, fnear, ffar):
            returnValue = libpanda._inPSkjP0HgK(self.this, xfov, yfov, fnear, ffar)
            return returnValue

        
        def makeOrtho2D(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_makeOrtho2D_ptrFrustumd()
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_makeOrtho2D_ptrFrustumd_double_double_double_double(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 4 '

        
        def makeOrtho(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return self.overloaded_makeOrtho_ptrFrustumd_double_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 6:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    if isinstance(_args[5], types.FloatType) or isinstance(_args[5], types.IntType):
                                        return self.overloaded_makeOrtho_ptrFrustumd_double_double_double_double_double_double(_args[0], _args[1], _args[2], _args[3], _args[4], _args[5])
                                    else:
                                        raise TypeError, 'Invalid argument 5, expected one of: <types.FloatType> '
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 6 '


    globals()['FrustumD'] = FrustumD

