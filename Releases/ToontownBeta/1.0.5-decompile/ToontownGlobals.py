# Source Generated with Decompyle++
# File: ToontownGlobals.pyo (Python 2.0)

from PandaModules import *
WallBitmask = BitMask32.bit(0)
FloorBitmask = BitMask32.bit(1)
CameraBitmask = BitMask32.bit(2)
DefaultCameraFov = 52.0
MakeAToonCameraFov = 35.0
DefaultCameraFar = 400.0
MaxFriends = 50
ToonFont = None
InterfaceFont = None
SignFont = None
SuitFont = None

def getToonFont():
    global ToonFont
    if ToonFont == None:
        ToonFont = loader.loadFont('phase_3/models/fonts/ImpressBT')
    
    return ToonFont


def getInterfaceFont():
    global InterfaceFont
    if InterfaceFont == None:
        InterfaceFont = loader.loadFont('phase_3/models/fonts/ImpressBT')
    
    return InterfaceFont


def getSignFont():
    global SignFont
    if SignFont == None:
        SignFont = loader.loadFont('phase_3/models/fonts/MickeyFont')
    
    return SignFont


def getSuitFont():
    global SuitFont
    if SuitFont == None:
        SuitFont = loader.loadFont('phase_4/models/fonts/vtRemingtonPortable')
    
    return SuitFont


def getAspectRatio():
    return 4.0 / 3.0

QuietZone = 1
UberZone = 2
DonaldsDock = 1000
ToontownCentral = 2000
TheBrrrgh = 3000
MinniesMelodyland = 4000
DaisyGardens = 5000
ConstructionZone = 6000
FunnyFarm = 7000
GoofyStadium = 8000
DonaldsDreamland = 9000
BossbotHQ = 10000
SellbotHQ = 11000
CashbotHQ = 12000
LawbotHQ = 13000
Tutorial = 20000
Hoods = [
    DonaldsDock,
    ToontownCentral,
    TheBrrrgh,
    MinniesMelodyland,
    DaisyGardens,
    DonaldsDreamland]
RaceGameId = 1
CannonGameId = 2
TagGameId = 3
PatternGameId = 4
RingGameId = 5
MinigameIDs = [
    RaceGameId,
    CannonGameId,
    TagGameId,
    PatternGameId]
SinglePlayerMinigameIDs = [
    RaceGameId,
    CannonGameId,
    PatternGameId]
NetworkLatency = 1.0
devServerIP = '206.18.93.16'
prodServerIP = 'toontown.starwave.com'
debugServerIP = '206.18.93.31'
ThinkPosHotkey = 'f1-up'
PlaceMarkerHotkey = 'f2-up'
FriendsListHotkey = 'f7-up'
StickerBookHotkey = 'f8-up'
OptionsPageHotkey = 'escape-up'
ScreenshotHotkey = 'f9-up'
phaseMap = {
    Tutorial: 4,
    ToontownCentral: 4,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8 }
streetPhaseMap = {
    ToontownCentral: 5,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8 }
dnaMap = {
    Tutorial: 'toontown_central',
    ToontownCentral: 'toontown_central',
    DonaldsDock: 'donalds_dock',
    MinniesMelodyland: 'minnies_melody_land',
    GoofyStadium: 'not done yet',
    TheBrrrgh: 'the_burrrgh',
    DaisyGardens: 'daisys_garden',
    FunnyFarm: 'not done yet',
    DonaldsDreamland: 'donalds_dreamland',
    ConstructionZone: 'not done yet' }
safeZoneCountMap = {
    Tutorial: 6,
    ToontownCentral: 6,
    DonaldsDock: 10,
    MinniesMelodyland: 5,
    GoofyStadium: 500,
    TheBrrrgh: 8,
    DaisyGardens: 9,
    FunnyFarm: 500,
    DonaldsDreamland: 5,
    ConstructionZone: 500 }
townCountMap = {
    ToontownCentral: 37,
    DonaldsDock: 40,
    MinniesMelodyland: 40,
    GoofyStadium: 40,
    TheBrrrgh: 40,
    DaisyGardens: 40,
    FunnyFarm: 40,
    DonaldsDreamland: 40,
    ConstructionZone: 40 }
hoodCountMap = {
    Tutorial: 2,
    ToontownCentral: 2,
    DonaldsDock: 2,
    MinniesMelodyland: 2,
    GoofyStadium: 2,
    TheBrrrgh: 2,
    DaisyGardens: 2,
    FunnyFarm: 2,
    DonaldsDreamland: 2,
    ConstructionZone: 2 }
StarHPLevels = [
    15,
    25,
    30,
    35,
    45,
    55,
    70,
    85]
ToonForwardSpeed = 16.0
ToonReverseSpeed = 8.0
ToonRotateSpeed = 80.0
ToonForwardSlowSpeed = 3.0
ToonReverseSlowSpeed = 1.0
ToonRotateSlowSpeed = 25.0
MickeySpeed = 5.0
