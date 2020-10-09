# Source Generated with Decompyle++
# File: LineSegs.pyo (Python 2.0)

import PandaStatic
import types
import libpanda
import libpandaDowncasts
import FFIExternalObject
import VBase4
import VBase3
import Point3
import GeomNode
classDefined = 0

def generateClass_LineSegs():
    global classDefined
    if classDefined:
        return None
    
    classDefined = 1
    
    class LineSegs(FFIExternalObject.FFIExternalObject):
        __CModuleDowncasts__ = [
            libpandaDowncasts]
        
        def __init__(self, *_args):
            FFIExternalObject.FFIExternalObject.__init__(self)
            if len(_args) == 1 and _args[0] == None:
                return None
            
            apply(self.constructor, _args)

        
        def constructor(self):
            self.this = libpanda._inPXs2xPnQY()
            self.userManagesMemory = 1

        
        def __del__(self):
            if self.userManagesMemory and self.this != 0:
                self.destructor()
            

        
        def destructor(self):
            if libpanda and libpanda._inPXs2xXduo:
                libpanda._inPXs2xXduo(self.this)
            

        
        def reset(self):
            returnValue = libpanda._inPXs2xZEnq(self.this)
            return returnValue

        
        def overloaded_setColor_ptrLineSegs_float_float_float_float(self, r, g, b, a):
            returnValue = libpanda._inPXs2xhg3B(self.this, r, g, b, a)
            return returnValue

        
        def overloaded_setColor_ptrLineSegs_float_float_float(self, r, g, b):
            returnValue = libpanda._inPXs2xBos9(self.this, r, g, b)
            return returnValue

        
        def overloaded_setColor_ptrLineSegs_ptrConstLVecBase4f(self, color):
            returnValue = libpanda._inPXs2xt93d(self.this, color.this)
            return returnValue

        
        def setThickness(self, thick):
            returnValue = libpanda._inPXs2xCOp7(self.this, thick)
            return returnValue

        
        def overloaded_moveTo_ptrLineSegs_float_float_float(self, x, y, z):
            returnValue = libpanda._inPXs2xklxC(self.this, x, y, z)
            return returnValue

        
        def overloaded_moveTo_ptrLineSegs_ptrConstLVecBase3f(self, v):
            returnValue = libpanda._inPXs2x1KI1(self.this, v.this)
            return returnValue

        
        def overloaded_drawTo_ptrLineSegs_float_float_float(self, x, y, z):
            returnValue = libpanda._inPXs2x1CHg(self.this, x, y, z)
            return returnValue

        
        def overloaded_drawTo_ptrLineSegs_ptrConstLVecBase3f(self, v):
            returnValue = libpanda._inPXs2xjPeS(self.this, v.this)
            return returnValue

        
        def getCurrentPosition(self):
            returnValue = libpanda._inPXs2xA8l_(self.this)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            return returnObject

        
        def isEmpty(self):
            returnValue = libpanda._inPXs2x641p(self.this)
            return returnValue

        
        def overloaded_create_ptrLineSegs_bool(self, frameAccurate):
            returnValue = libpanda._inPXs2x8r3i(self.this, frameAccurate)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_create_ptrLineSegs(self):
            returnValue = libpanda._inPXs2xmSE_(self.this)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_create_ptrLineSegs_ptrGeomNode_bool(self, previous, frameAccurate):
            returnValue = libpanda._inPXs2xSfoc(self.this, previous.this, frameAccurate)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def overloaded_create_ptrLineSegs_ptrGeomNode(self, previous):
            returnValue = libpanda._inPXs2x40ma(self.this, previous.this)
            returnObject = GeomNode.GeomNode(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject.setPointer()

        
        def getNumVertices(self):
            returnValue = libpanda._inPXs2xEMkT(self.this)
            return returnValue

        
        def getVertex(self, vertex):
            returnValue = libpanda._inPXs2xzQZQ(self.this, vertex)
            returnObject = Point3.Point3(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setVertex_ptrLineSegs_int_ptrConstLPoint3f(self, vertex, vert):
            returnValue = libpanda._inPXs2xFzV4(self.this, vertex, vert.this)
            return returnValue

        
        def overloaded_setVertex_ptrLineSegs_int_float_float_float(self, vertex, x, y, z):
            returnValue = libpanda._inPXs2xqOXV(self.this, vertex, x, y, z)
            return returnValue

        
        def getVertexColor(self, vertex):
            returnValue = libpanda._inPXs2xzcje(self.this, vertex)
            returnObject = VBase4.VBase4(None)
            returnObject.this = returnValue
            if returnObject.this == 0:
                return None
            
            returnObject.userManagesMemory = 1
            return returnObject

        
        def overloaded_setVertexColor_ptrLineSegs_int_ptrConstLVecBase4f(self, vertex, color):
            returnValue = libpanda._inPXs2xszOI(self.this, vertex, color.this)
            return returnValue

        
        def overloaded_setVertexColor_ptrLineSegs_int_float_float_float_float(self, vertex, r, g, b, a):
            returnValue = libpanda._inPXs2xIYYd(self.this, vertex, r, g, b, a)
            return returnValue

        
        def overloaded_setVertexColor_ptrLineSegs_int_float_float_float(self, vertex, r, g, b):
            returnValue = libpanda._inPXs2x_Jzm(self.this, vertex, r, g, b)
            return returnValue

        
        def setVertex(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], Point3.Point3):
                        return self.overloaded_setVertex_ptrLineSegs_int_ptrConstLPoint3f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <Point3.Point3> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setVertex_ptrLineSegs_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 '

        
        def setVertexColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 2:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], VBase4.VBase4):
                        return self.overloaded_setVertexColor_ptrLineSegs_int_ptrConstLVecBase4f(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <VBase4.VBase4> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setVertexColor_ptrLineSegs_int_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            elif numArgs == 5:
                if isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                if isinstance(_args[4], types.FloatType) or isinstance(_args[4], types.IntType):
                                    return self.overloaded_setVertexColor_ptrLineSegs_int_float_float_float_float(_args[0], _args[1], _args[2], _args[3], _args[4])
                                else:
                                    raise TypeError, 'Invalid argument 4, expected one of: <types.FloatType> '
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 2 4 5 '

        
        def setColor(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase4.VBase4):
                    return self.overloaded_setColor_ptrLineSegs_ptrConstLVecBase4f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase4.VBase4> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_setColor_ptrLineSegs_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            elif numArgs == 4:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            if isinstance(_args[3], types.FloatType) or isinstance(_args[3], types.IntType):
                                return self.overloaded_setColor_ptrLineSegs_float_float_float_float(_args[0], _args[1], _args[2], _args[3])
                            else:
                                raise TypeError, 'Invalid argument 3, expected one of: <types.FloatType> '
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 4 '

        
        def drawTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_drawTo_ptrLineSegs_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_drawTo_ptrLineSegs_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '

        
        def create(self, *_args):
            numArgs = len(_args)
            if numArgs == 0:
                return self.overloaded_create_ptrLineSegs()
            elif numArgs == 1:
                if isinstance(_args[0], types.IntType):
                    return self.overloaded_create_ptrLineSegs_bool(_args[0])
                elif isinstance(_args[0], GeomNode.GeomNode):
                    return self.overloaded_create_ptrLineSegs_ptrGeomNode(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.IntType> <GeomNode.GeomNode> '
            elif numArgs == 2:
                if isinstance(_args[0], GeomNode.GeomNode):
                    if isinstance(_args[1], types.IntType):
                        return self.overloaded_create_ptrLineSegs_ptrGeomNode_bool(_args[0], _args[1])
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.IntType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <GeomNode.GeomNode> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 0 1 2 '

        
        def moveTo(self, *_args):
            numArgs = len(_args)
            if numArgs == 1:
                if isinstance(_args[0], VBase3.VBase3):
                    return self.overloaded_moveTo_ptrLineSegs_ptrConstLVecBase3f(_args[0])
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <VBase3.VBase3> '
            elif numArgs == 3:
                if isinstance(_args[0], types.FloatType) or isinstance(_args[0], types.IntType):
                    if isinstance(_args[1], types.FloatType) or isinstance(_args[1], types.IntType):
                        if isinstance(_args[2], types.FloatType) or isinstance(_args[2], types.IntType):
                            return self.overloaded_moveTo_ptrLineSegs_float_float_float(_args[0], _args[1], _args[2])
                        else:
                            raise TypeError, 'Invalid argument 2, expected one of: <types.FloatType> '
                    else:
                        raise TypeError, 'Invalid argument 1, expected one of: <types.FloatType> '
                else:
                    raise TypeError, 'Invalid argument 0, expected one of: <types.FloatType> '
            else:
                raise TypeError, 'Invalid number of arguments: ' + `numArgs` + ', expected one of: 1 3 '


    globals()['LineSegs'] = LineSegs

