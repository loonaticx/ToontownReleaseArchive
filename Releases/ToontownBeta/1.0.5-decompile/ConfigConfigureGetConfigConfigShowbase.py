# Source Generated with Decompyle++
# File: ConfigConfigureGetConfigConfigShowbase.pyo (Python 2.0)

import PandaStatic
import types
import libdirect
import libdirectDowncasts
import FFIExternalObject
classDefined = 0

def generateClass_ConfigConfigureGetConfigConfigShowbase():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class ConfigConfigureGetConfigConfigShowbase(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libdirectDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            raise RuntimeError, 'No C++ constructor defined for class: ' + self.__class__.__name__

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libdirect and libdirect._inPL4GTLJQT:
                libdirect._inPL4GTLJQT(self.this)
            

        
        def overloaded_GetBool_atomicstring_bool(sym, _def):
            returnValue = libdirect._inPL4GTh_h_(sym, _def)
            return returnValue

        overloaded_GetBool_atomicstring_bool = PandaStatic.PandaStatic(overloaded_GetBool_atomicstring_bool)
        
        def overloaded_GetBool_atomicstring(sym):
            returnValue = libdirect._inPL4GT_agQ(sym)
            return returnValue

        overloaded_GetBool_atomicstring = PandaStatic.PandaStatic(overloaded_GetBool_atomicstring)
        
        def overloaded_GetInt_atomicstring_int(sym, _def):
            returnValue = libdirect._inPL4GToDUV(sym, _def)
            return returnValue

        overloaded_GetInt_atomicstring_int = PandaStatic.PandaStatic(overloaded_GetInt_atomicstring_int)
        
        def overloaded_GetInt_atomicstring(sym):
            returnValue = libdirect._inPL4GTHRBW(sym)
            return returnValue

        overloaded_GetInt_atomicstring = PandaStatic.PandaStatic(overloaded_GetInt_atomicstring)
        
        def overloaded_GetFloat_atomicstring_float(sym, _def):
            returnValue = libdirect._inPL4GTFJ_T(sym, _def)
            return returnValue

        overloaded_GetFloat_atomicstring_float = PandaStatic.PandaStatic(overloaded_GetFloat_atomicstring_float)
        
        def overloaded_GetFloat_atomicstring(sym):
            returnValue = libdirect._inPL4GTDVWG(sym)
            return returnValue

        overloaded_GetFloat_atomicstring = PandaStatic.PandaStatic(overloaded_GetFloat_atomicstring)
        
        def overloaded_GetDouble_atomicstring_double(sym, _def):
            returnValue = libdirect._inPL4GT6bam(sym, _def)
            return returnValue

        overloaded_GetDouble_atomicstring_double = PandaStatic.PandaStatic(overloaded_GetDouble_atomicstring_double)
        
        def overloaded_GetDouble_atomicstring(sym):
            returnValue = libdirect._inPL4GT4pRv(sym)
            return returnValue

        overloaded_GetDouble_atomicstring = PandaStatic.PandaStatic(overloaded_GetDouble_atomicstring)
        
        def overloaded_GetString_atomicstring_atomicstring(sym, _def):
            returnValue = libdirect._inPL4GTbfEi(sym, _def)
            return returnValue

        overloaded_GetString_atomicstring_atomicstring = PandaStatic.PandaStatic(overloaded_GetString_atomicstring_atomicstring)
        
        def overloaded_GetString_atomicstring(sym):
            returnValue = libdirect._inPL4GT1UJ6(sym)
            return returnValue

        overloaded_GetString_atomicstring = PandaStatic.PandaStatic(overloaded_GetString_atomicstring)
        
        def GetString(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase.overloaded_GetString_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.StringType):
                        return ConfigConfigureGetConfigConfigShowbase.overloaded_GetString_atomicstring_atomicstring(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.StringType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        GetString = PandaStatic.PandaStatic(GetString)
        
        def GetBool(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase.overloaded_GetBool_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return ConfigConfigureGetConfigConfigShowbase.overloaded_GetBool_atomicstring_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        GetBool = PandaStatic.PandaStatic(GetBool)
        
        def GetFloat(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase.overloaded_GetFloat_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return ConfigConfigureGetConfigConfigShowbase.overloaded_GetFloat_atomicstring_float(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        GetFloat = PandaStatic.PandaStatic(GetFloat)
        
        def GetInt(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase.overloaded_GetInt_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.IntType):
                        return ConfigConfigureGetConfigConfigShowbase.overloaded_GetInt_atomicstring_int(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        GetInt = PandaStatic.PandaStatic(GetInt)
        
        def GetDouble(*_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], types.StringType):
                    return ConfigConfigureGetConfigConfigShowbase.overloaded_GetDouble_atomicstring(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            elif numArgs == 2:
                if isinstance(_args[0], types.StringType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        return ConfigConfigureGetConfigConfigShowbase.overloaded_GetDouble_atomicstring_double(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.StringType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 2 '

        GetDouble = PandaStatic.PandaStatic(GetDouble)

    globals()['ConfigConfigureGetConfigConfigShowbase'] = ConfigConfigureGetConfigConfigShowbase

