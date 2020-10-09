# Source Generated with Decompyle++
# File: MickeyPaths.pyo (Python 2.0)

from Point3 import *
from Vec3 import *
import copy
__mickeyPaths = {
    'a': (Point3(110, -30, 1.759), ('b', 'd')),
    'b': (Point3(91, -29, -1.308), ('a', 'c', 'g', 'h')),
    'c': (Point3(111, -12, -1.308), ('b', 'd', 'h')),
    'd': (Point3(140, -28, -1.308), ('a', 'c', 'e', 'f', 'h')),
    'e': (Point3(185, -26, 6.192), ('d', 'l', 'u')),
    'f': (Point3(110, -65, -1.308), ('d', 'g', 'i')),
    'g': (Point3(75, -53, -1.308), ('b', 'f', 'j')),
    'h': (Point3(108, 11, -1.308), ('b', 'c', 'd', 'k')),
    'i': (Point3(116, -105, 6.192), ('f', 'r1', 's')),
    'j': (Point3(39, -54, 6.192), ('g', 'q', 'r')),
    'k': (Point3(97, 43, 6.192), ('h', 'n', 'o')),
    'l': (Point3(177, 5, 6.192), ('e', 'm')),
    'm': (Point3(160, 25.5, 6.192), ('l', 'n')),
    'n': (Point3(128, 44, 6.192), ('m', 'k')),
    'o': (Point3(66, 31.5, 6.192), ('k', 'p')),
    'p': (Point3(43, 10, 6.192), ('o', 'q')),
    'q': (Point3(35, -22, 6.192), ('p', 'j')),
    'r': (Point3(55, -83, 6.192), ('j', 'r1')),
    'r1': (Point3(79, -100, 6.192), ('r', 'i')),
    's': (Point3(144, -97.5, 6.192), ('i', 't')),
    't': (Point3(166, -80, 6.192), ('s', 'u')),
    'u': (Point3(181.5, -55.5, 6.192), ('t', 'e')) }
__pathWaypoints = (('a', 'b', [
    Point3(103, -30, 1.759),
    Point3(98, -30, -1.308)]), ('b', 'c', [
    Point3(98, -11, -1.308)]), ('a', 'd', [
    Point3(117, -30, 1.759),
    Point3(122, -30, -1.308)]), ('d', 'e', [
    Point3(166.5, -27, -1.308),
    Point3(180, -26, 6.174)]), ('f', 'g', [
    Point3(90, -63, -1.308)]), ('f', 'i', [
    Point3(112, -87, -1.308),
    Point3(114, -101, 6.191)]), ('g', 'j', [
    Point3(58, -51, -1.308),
    Point3(43, -53, 6.182)]), ('h', 'k', [
    Point3(99, 25, -1.308),
    Point3(93, 38, 6.174)]))
startNode = 'a'

def getNodePos(node):
    return __mickeyPaths[node][0]


def getAdjacentNodes(node):
    return __mickeyPaths[node][1]


def getWayPoints(fromNode, toNode):
    list = []
    if fromNode != toNode:
        for path in __pathWaypoints:
            if path[0] == fromNode and path[1] == toNode:
                for point in path[2]:
                    list.append(Point3(point))
                
                break
            elif path[0] == toNode and path[1] == fromNode:
                for point in path[2]:
                    list = [
                        Point3(point)] + list
                
                break
            
        
    
    return list


def getPointsFromTo(fromNode, toNode):
    startPoint = Point3(getNodePos(fromNode))
    endPoint = Point3(getNodePos(toNode))
    return [
        startPoint] + getWayPoints(fromNode, toNode) + [
        endPoint]


def getWalkDuration(fromNode, toNode, velocity):
    posPoints = getPointsFromTo(fromNode, toNode)
    duration = 0.0
    for pointIndex in range(len(posPoints) - 1):
        startPoint = posPoints[pointIndex]
        endPoint = posPoints[pointIndex + 1]
        distance = Vec3(endPoint - startPoint).length()
        duration += distance / velocity
    
    return duration

