# Source Generated with Decompyle++
# File: SuitBattleGlobals.pyo (Python 2.0)

from BattleBase import *
import whrandom
import DirectNotifyGlobal
notify = DirectNotifyGlobal.directNotify.newCategory('SuitBattleGlobals')

def pickFromFreqList(freqList):
    randNum = whrandom.randint(0, 99)
    count = 0
    index = 0
    level = None
    for f in freqList:
        count = count + f
        if randNum < count:
            level = index
            break
        
        index = index + 1
    
    return level


def getActualFromRelativeLevel(name, relLevel):
    data = SuitAttributes[name]
    if name == 'tbc' and name == 'bw' and name == 'mh' or name == 'rb':
        actualLevel = 11
    else:
        actualLevel = data['level'] + relLevel
    return actualLevel


def getSuitVitals(name, level = -1):
    data = SuitAttributes[name]
    if level == -1:
        level = pickFromFreqList(data['freq'])
    
    dict = { }
    dict['level'] = getActualFromRelativeLevel(name, level)
    if dict['level'] == 11:
        level = 0
    
    dict['hp'] = data['hp'][level]
    dict['def'] = data['def'][level]
    attacks = data['attacks']
    alist = []
    for a in attacks:
        adict = { }
        name = a[0]
        adict['name'] = name
        adict['animName'] = SuitAttacks[name][0]
        adict['hp'] = a[1][level]
        adict['acc'] = a[2][level]
        adict['freq'] = a[3][level]
        adict['group'] = SuitAttacks[name][1]
        alist.append(adict)
    
    dict['attacks'] = alist
    return dict


def pickSuitAttack(attacks, suitLevel):
    attackNum = None
    randNum = whrandom.randint(0, 99)
    notify.debug('pickSuitAttack: rolled %d' % randNum)
    count = 0
    index = 0
    total = 0
    for c in attacks:
        total = total + c[3][suitLevel]
    
    for c in attacks:
        count = count + c[3][suitLevel]
        if randNum < count:
            attackNum = index
            notify.debug('picking attack %d' % attackNum)
            break
        
        index = index + 1
    
    configAttackName = simbase.config.GetString('attack-type', 'random')
    if configAttackName == 'random':
        return attackNum
    else:
        i = 0
        for attack in attacks:
            if attack[0] == configAttackName:
                return i
            
            i += 1
        
        notify.warning('No such attack as %s:' % configAttackName)
        return attackNum


def getSuitAttack(suitName, suitLevel, attackNum = -1):
    attackChoices = SuitAttributes[suitName]['attacks']
    if attackNum == -1:
        notify.debug('getSuitAttack: picking attacking for %s' % suitName)
        attackNum = pickSuitAttack(attackChoices, suitLevel)
    
    attack = attackChoices[attackNum]
    adict = { }
    adict['suitName'] = suitName
    name = attack[0]
    adict['name'] = name
    adict['id'] = SuitAttacks.keys().index(name)
    adict['animName'] = SuitAttacks[name][0]
    adict['hp'] = attack[1][suitLevel]
    adict['acc'] = attack[2][suitLevel]
    adict['freq'] = attack[3][suitLevel]
    adict['group'] = SuitAttacks[name][1]
    return adict

SuitAttributes = {
    'f': {
        'name': 'Flunky',
        'pluralname': 'Flunkies',
        'caste': 'Corporate',
        'level': 0,
        'hp': (6, 12, 20, 30, 42),
        'def': (2, 5, 10, 12, 15),
        'freq': (50, 30, 10, 5, 5),
        'acc': (35, 40, 45, 50, 55),
        'attacks': (('PoundKey', (2, 2, 3, 4, 6), (75, 75, 80, 80, 90), (30, 35, 40, 45, 50)), ('Shred', (3, 4, 5, 6, 7), (50, 55, 60, 65, 70), (10, 15, 20, 25, 30)), ('ClipOnTie', (1, 1, 2, 2, 3), (75, 80, 85, 90, 95), (60, 50, 40, 30, 20)), ('CarbonCopy', (0, 0, 0, 0, 0), (75, 75, 75, 75, 75), (0, 0, 0, 0, 0))) },
    'p': {
        'name': 'Pencil Pusher',
        'pluralname': 'Pencil Pushers',
        'caste': 'Corporate',
        'level': 1,
        'hp': (12, 20, 30, 42, 56),
        'def': (5, 10, 15, 20, 25),
        'freq': (50, 30, 10, 5, 5),
        'acc': (45, 50, 55, 60, 65),
        'attacks': (('FountainPen', (2, 3, 4, 6, 9), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('RubOut', (4, 5, 6, 8, 12), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('FingerWag', (1, 2, 2, 3, 4), (75, 75, 75, 75, 75), (35, 30, 25, 20, 15)), ('WriteOff', (4, 6, 8, 10, 12), (75, 75, 75, 75, 75), (5, 10, 15, 20, 25)), ('FillWithLead', (3, 4, 5, 6, 7), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20))) },
    'ym': {
        'name': 'Yes Man',
        'pluralname': 'Yes Men',
        'caste': 'Corporate',
        'level': 2,
        'hp': (20, 30, 42, 56, 72),
        'def': (10, 15, 20, 25, 30),
        'freq': (50, 30, 10, 5, 5),
        'acc': (65, 70, 75, 80, 85),
        'attacks': (('RubberStamp', (2, 2, 3, 3, 4), (75, 75, 75, 75, 75), (35, 35, 35, 35, 35)), ('RazzleDazzle', (1, 1, 1, 1, 1), (50, 50, 50, 50, 50), (25, 20, 15, 10, 5)), ('Synergy', (4, 5, 6, 7, 8), (50, 60, 70, 80, 90), (5, 10, 15, 20, 25)), ('TeeOff', (3, 3, 4, 4, 5), (50, 60, 70, 80, 90), (35, 35, 35, 35, 35)), ('Ditto', (0, 0, 0, 0, 0), (75, 75, 75, 75, 75), (0, 0, 0, 0, 0))) },
    'mm': {
        'name': 'Micromanager',
        'pluralname': 'Micromanagers',
        'caste': 'Corporate',
        'level': 3,
        'hp': (30, 42, 56, 72, 90),
        'def': (15, 20, 25, 30, 35),
        'freq': (50, 30, 10, 5, 5),
        'acc': (70, 75, 80, 82, 85),
        'attacks': (('Demotion', (6, 8, 12, 15, 18), (50, 60, 70, 80, 90), (30, 30, 30, 30, 30)), ('FingerWag', (4, 6, 9, 12, 15), (50, 60, 70, 80, 90), (10, 10, 10, 10, 10)), ('FountainPen', (3, 4, 6, 8, 10), (50, 60, 70, 80, 90), (15, 15, 15, 15, 15)), ('BrainStorm', (4, 6, 9, 12, 15), (5, 5, 5, 5, 5), (25, 25, 25, 25, 25)), ('BuzzWord', (4, 6, 9, 12, 15), (50, 60, 70, 80, 90), (20, 20, 20, 20, 20))) },
    'cc': {
        'name': 'Cold Caller',
        'pluralname': 'Cold Callers',
        'caste': 'Sales',
        'level': 0,
        'hp': (6, 12, 20, 30, 42),
        'def': (2, 5, 10, 12, 15),
        'freq': (50, 30, 10, 5, 5),
        'acc': (35, 40, 45, 50, 55),
        'attacks': (('FreezeAssets', (1, 1, 1, 1, 1), (95, 95, 95, 95, 95), (5, 10, 15, 20, 25)), ('PoundKey', (2, 2, 3, 4, 5), (75, 80, 85, 90, 95), (25, 25, 25, 25, 25)), ('DoubleTalk', (2, 3, 4, 6, 8), (50, 55, 60, 65, 70), (25, 25, 25, 25, 25)), ('HotAir', (3, 4, 6, 8, 10), (50, 50, 50, 50, 50), (45, 40, 35, 30, 25))) },
    'tm': {
        'name': 'Telemarketer',
        'pluralname': 'Telemarketers',
        'caste': 'Sales',
        'level': 1,
        'hp': (12, 20, 30, 42, 56),
        'def': (5, 10, 15, 20, 25),
        'freq': (50, 30, 10, 5, 5),
        'acc': (45, 50, 55, 60, 65),
        'attacks': (('ClipOnTie', (2, 2, 3, 3, 4), (75, 75, 75, 75, 75), (15, 15, 15, 15, 15)), ('PickPocket', (1, 1, 1, 1, 1), (75, 75, 75, 75, 75), (15, 15, 15, 15, 15)), ('Rolodex', (4, 6, 7, 9, 12), (50, 50, 50, 50, 50), (30, 30, 30, 30, 30)), ('DoubleTalk', (4, 6, 7, 9, 12), (75, 80, 85, 90, 95), (40, 40, 40, 40, 40))) },
    'nd': {
        'name': 'Namedropper',
        'pluralname': 'Namedroppers',
        'caste': 'Sales',
        'level': 2,
        'hp': (20, 30, 42, 56, 72),
        'def': (10, 15, 20, 25, 30),
        'freq': (50, 30, 10, 5, 5),
        'acc': (65, 70, 75, 80, 85),
        'attacks': (('RazzleDazzle', (4, 5, 6, 9, 12), (75, 80, 85, 90, 95), (30, 30, 30, 30, 30)), ('Rolodex', (5, 6, 7, 10, 14), (95, 95, 95, 95, 95), (40, 40, 40, 40, 40)), ('Synergy', (3, 4, 6, 9, 12), (50, 50, 50, 50, 50), (15, 15, 15, 15, 15)), ('PickPocket', (2, 2, 2, 2, 2), (95, 95, 95, 95, 95), (15, 15, 15, 15, 15))) },
    'gh': {
        'name': 'Gladhander',
        'pluralname': 'Gladhanders',
        'caste': 'Sales',
        'level': 3,
        'hp': (30, 42, 56, 72, 90),
        'def': (15, 20, 25, 30, 35),
        'freq': (50, 30, 10, 5, 5),
        'acc': (70, 75, 80, 82, 85),
        'attacks': (('RubberStamp', (4, 3, 3, 2, 1), (90, 70, 50, 30, 10), (40, 30, 20, 10, 5)), ('FountainPen', (3, 3, 2, 1, 1), (70, 60, 50, 40, 30), (40, 30, 20, 10, 5)), ('Filibuster', (4, 6, 9, 12, 15), (30, 40, 50, 60, 70), (10, 20, 30, 40, 45)), ('Schmooze', (5, 7, 11, 15, 20), (55, 65, 75, 85, 95), (10, 20, 30, 40, 45))) },
    'sc': {
        'name': 'Short Change',
        'pluralname': 'Short Changes',
        'caste': 'Money',
        'level': 0,
        'hp': (6, 12, 20, 30, 42),
        'def': (2, 5, 10, 12, 15),
        'freq': (50, 30, 10, 5, 5),
        'acc': (35, 40, 45, 50, 55),
        'attacks': (('Watercooler', (2, 2, 3, 4, 6), (50, 50, 50, 50, 50), (20, 20, 20, 20, 20)), ('BounceCheck', (3, 5, 7, 9, 11), (75, 80, 85, 90, 95), (10, 10, 10, 10, 10)), ('ClipOnTie', (1, 1, 2, 2, 3), (50, 50, 50, 50, 50), (20, 20, 20, 20, 20)), ('PickPocket', (2, 2, 3, 4, 6), (95, 95, 95, 95, 95), (50, 50, 50, 50, 50))) },
    'pp': {
        'name': 'Penny Pincher',
        'pluralname': 'Penny Pinchers',
        'caste': 'Money',
        'level': 1,
        'hp': (12, 20, 30, 42, 56),
        'def': (5, 10, 15, 20, 25),
        'freq': (50, 30, 10, 5, 5),
        'acc': (45, 50, 55, 60, 65),
        'attacks': (('BounceCheck', (4, 5, 6, 8, 12), (75, 75, 75, 75, 75), (45, 45, 45, 45, 45)), ('FreezeAssets', (2, 3, 4, 6, 9), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('FingerWag', (1, 2, 3, 4, 6), (50, 50, 50, 50, 50), (35, 35, 35, 35, 35)), ('PennyPinch', (0, 0, 0, 0, 0), (75, 75, 75, 75, 75), (0, 0, 0, 0, 0))) },
    'tw': {
        'name': 'Tightwad',
        'pluralname': 'Tightwads',
        'caste': 'Money',
        'level': 2,
        'hp': (20, 30, 42, 56, 72),
        'def': (10, 15, 20, 25, 30),
        'freq': (50, 30, 10, 5, 5),
        'acc': (65, 70, 75, 80, 85),
        'attacks': (('Fired', (3, 4, 5, 5, 6), (75, 75, 75, 75, 75), (75, 5, 5, 5, 5)), ('GlowerPower', (3, 4, 6, 9, 12), (95, 95, 95, 95, 95), (10, 15, 20, 25, 30)), ('FingerWag', (3, 3, 4, 4, 5), (75, 75, 75, 75, 75), (5, 70, 5, 5, 5)), ('FreezeAssets', (3, 4, 6, 9, 12), (75, 75, 75, 75, 75), (5, 5, 65, 5, 30)), ('BounceCheck', (5, 6, 9, 13, 18), (75, 75, 75, 75, 75), (5, 5, 5, 60, 30))) },
    'bc': {
        'name': 'Bean Counter',
        'pluralname': 'Bean Counters',
        'caste': 'Money',
        'level': 3,
        'hp': (30, 42, 56, 72, 90),
        'def': (15, 20, 25, 30, 35),
        'freq': (50, 30, 10, 5, 5),
        'acc': (70, 75, 80, 82, 85),
        'attacks': (('Audit', (4, 6, 9, 12, 15), (95, 95, 95, 95, 95), (20, 20, 20, 20, 20)), ('Calculate', (4, 6, 9, 12, 15), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)), ('Tabulate', (4, 6, 9, 12, 15), (75, 75, 75, 75, 75), (25, 25, 25, 25, 25)), ('WriteOff', (4, 6, 9, 12, 15), (95, 95, 95, 95, 95), (30, 30, 30, 30, 30))) },
    'bf': {
        'name': 'Bottom Feeder',
        'pluralname': 'Bottom Feeders',
        'caste': 'Legal',
        'level': 0,
        'hp': (6, 12, 20, 30, 42),
        'def': (2, 5, 10, 12, 15),
        'freq': (50, 30, 10, 5, 5),
        'acc': (35, 40, 45, 50, 55),
        'attacks': (('RubberStamp', (2, 3, 4, 5, 6), (75, 80, 85, 90, 95), (20, 20, 20, 20, 20)), ('Shred', (2, 4, 6, 8, 10), (50, 55, 60, 65, 70), (20, 20, 20, 20, 20)), ('Watercooler', (3, 4, 5, 6, 7), (95, 95, 95, 95, 95), (10, 10, 10, 10, 10)), ('PickPocket', (1, 1, 2, 2, 3), (25, 30, 35, 40, 45), (50, 50, 50, 50, 50))) },
    'b': {
        'name': 'Bloodsucker',
        'pluralname': 'Bloodsuckers',
        'caste': 'Legal',
        'level': 1,
        'hp': (12, 20, 30, 42, 56),
        'def': (5, 10, 15, 20, 25),
        'freq': (50, 30, 10, 5, 5),
        'acc': (45, 50, 55, 60, 65),
        'attacks': (('EvictionNotice', (1, 2, 3, 3, 4), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('RedTape', (2, 3, 4, 6, 9), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('Withdrawal', (6, 8, 10, 12, 14), (95, 95, 95, 95, 95), (10, 10, 10, 10, 10)), ('Liquidate', (2, 3, 4, 6, 9), (50, 60, 70, 80, 90), (50, 50, 50, 50, 50))) },
    'dt': {
        'name': 'Double Talker',
        'pluralname': 'Double Talkers',
        'caste': 'Legal',
        'level': 2,
        'hp': (20, 30, 42, 56, 72),
        'def': (10, 15, 20, 25, 30),
        'freq': (50, 30, 10, 5, 5),
        'acc': (65, 70, 75, 80, 85),
        'attacks': (('RubberStamp', (1, 1, 1, 1, 1), (50, 60, 70, 80, 90), (5, 5, 5, 5, 5)), ('BounceCheck', (1, 1, 1, 1, 1), (50, 60, 70, 80, 90), (5, 5, 5, 5, 5)), ('BuzzWord', (1, 2, 3, 5, 6), (50, 60, 70, 80, 90), (20, 20, 20, 20, 20)), ('DoubleTalk', (6, 6, 9, 13, 18), (50, 60, 70, 80, 90), (25, 25, 25, 25, 25)), ('Jargon', (3, 4, 6, 9, 12), (50, 60, 70, 80, 90), (25, 25, 25, 25, 25)), ('MumboJumbo', (3, 4, 6, 9, 12), (50, 60, 70, 80, 90), (20, 20, 20, 20, 20))) },
    'ac': {
        'name': 'Ambulance Chaser',
        'pluralname': 'Ambulance Chasers',
        'caste': 'Legal',
        'level': 3,
        'hp': (30, 42, 56, 72, 90),
        'def': (15, 20, 25, 30, 35),
        'freq': (50, 30, 10, 5, 5),
        'acc': (65, 70, 75, 80, 85),
        'attacks': (('Shake', (4, 6, 9, 12, 15), (75, 75, 75, 75, 75), (15, 15, 15, 15, 15)), ('RedTape', (6, 8, 12, 15, 19), (75, 75, 75, 75, 75), (30, 30, 30, 30, 30)), ('Rolodex', (3, 4, 5, 6, 7), (75, 75, 75, 75, 75), (20, 20, 20, 20, 20)), ('HangUp', (2, 3, 4, 5, 6), (75, 75, 75, 75, 75), (35, 35, 35, 35, 35))) } }
ATK_TGT_UNKNOWN = 1
ATK_TGT_SINGLE = 2
ATK_TGT_GROUP = 3
SuitAttacks = {
    'Audit': ('phone', ATK_TGT_SINGLE),
    'BounceCheck': ('throw-paper', ATK_TGT_SINGLE),
    'BrainStorm': ('effort', ATK_TGT_SINGLE),
    'BuzzWord': ('speak', ATK_TGT_SINGLE),
    'Calculate': ('phone', ATK_TGT_SINGLE),
    'ClipOnTie': ('throw-paper', ATK_TGT_SINGLE),
    'Demotion': ('magic1', ATK_TGT_SINGLE),
    'DoubleTalk': ('speak', ATK_TGT_SINGLE),
    'EvictionNotice': ('throw-paper', ATK_TGT_SINGLE),
    'Filibuster': ('speak', ATK_TGT_SINGLE),
    'FillWithLead': ('pencil-sharpener', ATK_TGT_SINGLE),
    'FingerWag': ('finger-wag', ATK_TGT_SINGLE),
    'Fired': ('magic2', ATK_TGT_SINGLE),
    'FountainPen': ('pen-squirt', ATK_TGT_SINGLE),
    'FreezeAssets': ('glower', ATK_TGT_SINGLE),
    'GlowerPower': ('glower', ATK_TGT_SINGLE),
    'HangUp': ('phone', ATK_TGT_SINGLE),
    'HotAir': ('speak', ATK_TGT_SINGLE),
    'Jargon': ('speak', ATK_TGT_SINGLE),
    'Liquidate': ('magic1', ATK_TGT_SINGLE),
    'MumboJumbo': ('speak', ATK_TGT_SINGLE),
    'PickPocket': ('pickpocket', ATK_TGT_SINGLE),
    'PoundKey': ('phone', ATK_TGT_SINGLE),
    'RazzleDazzle': ('smile', ATK_TGT_SINGLE),
    'RedTape': ('throw-object', ATK_TGT_SINGLE),
    'Rolodex': ('roll-o-dex', ATK_TGT_SINGLE),
    'RubberStamp': ('rubber-stamp', ATK_TGT_SINGLE),
    'RubOut': ('hold-eraser', ATK_TGT_SINGLE),
    'Schmooze': ('speak', ATK_TGT_SINGLE),
    'Shake': ('stomp', ATK_TGT_GROUP),
    'Shred': ('shredder', ATK_TGT_SINGLE),
    'Synergy': ('magic3', ATK_TGT_GROUP),
    'Tabulate': ('phone', ATK_TGT_SINGLE),
    'TeeOff': ('golf-club-swing', ATK_TGT_SINGLE),
    'Watercooler': ('watercooler', ATK_TGT_SINGLE),
    'Withdrawal': ('magic1', ATK_TGT_SINGLE),
    'WriteOff': ('hold-pencil', ATK_TGT_SINGLE) }
AUDIT = SuitAttacks.keys().index('Audit')
BOUNCE_CHECK = SuitAttacks.keys().index('BounceCheck')
BRAIN_STORM = SuitAttacks.keys().index('BrainStorm')
BUZZ_WORD = SuitAttacks.keys().index('BuzzWord')
CALCULATE = SuitAttacks.keys().index('Calculate')
CLIPON_TIE = SuitAttacks.keys().index('ClipOnTie')
DEMOTION = SuitAttacks.keys().index('Demotion')
DOUBLE_TALK = SuitAttacks.keys().index('DoubleTalk')
EVICTION_NOTICE = SuitAttacks.keys().index('EvictionNotice')
FILIBUSTER = SuitAttacks.keys().index('Filibuster')
FILL_WITH_LEAD = SuitAttacks.keys().index('FillWithLead')
FINGER_WAG = SuitAttacks.keys().index('FingerWag')
FIRED = SuitAttacks.keys().index('Fired')
FOUNTAIN_PEN = SuitAttacks.keys().index('FountainPen')
FREEZE_ASSETS = SuitAttacks.keys().index('FreezeAssets')
GLOWER_POWER = SuitAttacks.keys().index('GlowerPower')
HANG_UP = SuitAttacks.keys().index('HangUp')
HOT_AIR = SuitAttacks.keys().index('HotAir')
JARGON = SuitAttacks.keys().index('Jargon')
LIQUIDATE = SuitAttacks.keys().index('Liquidate')
MUMBO_JUMBO = SuitAttacks.keys().index('MumboJumbo')
PICK_POCKET = SuitAttacks.keys().index('PickPocket')
POUND_KEY = SuitAttacks.keys().index('PoundKey')
RAZZLE_DAZZLE = SuitAttacks.keys().index('RazzleDazzle')
RED_TAPE = SuitAttacks.keys().index('RedTape')
ROLODEX = SuitAttacks.keys().index('Rolodex')
RUBBER_STAMP = SuitAttacks.keys().index('RubberStamp')
RUB_OUT = SuitAttacks.keys().index('RubOut')
SCHMOOZE = SuitAttacks.keys().index('Schmooze')
SHAKE = SuitAttacks.keys().index('Shake')
SHRED = SuitAttacks.keys().index('Shred')
SYNERGY = SuitAttacks.keys().index('Synergy')
TABULATE = SuitAttacks.keys().index('Tabulate')
TEE_OFF = SuitAttacks.keys().index('TeeOff')
WATERCOOLER = SuitAttacks.keys().index('Watercooler')
WITHDRAWAL = SuitAttacks.keys().index('Withdrawal')
WRITE_OFF = SuitAttacks.keys().index('WriteOff')

def getFaceoffTaunt(suitName):
    if SuitFaceoffTaunts.has_key(suitName):
        taunts = SuitFaceoffTaunts[suitName]
    else:
        taunts = [
            'I am tauntless.',
            'I am 100% taunt-free',
            'I have nary a taunt.',
            'Please write taunts for me.']
    return whrandom.choice(taunts)

SuitFaceoffTaunts = {
    'f': [
        "I'm gonna tell the boss about you!",
        "I may be just a flunky - But I'm real spunky.",
        "I'm using you to step up the corporate ladder.",
        "You're not going to like the way I work.",
        'The boss is counting on me to stop you.',
        "You're going to look good on my resume.",
        "You'll have to go through me first.",
        "Let's see how you rate my job performance.",
        'I excel at Toon disposal.',
        "You're never going to meet my boss.",
        "I'm sending you back to the Playground."],
    'p': [
        "I'm gonna rub you out!",
        "Hey, you can't push me around.",
        "I'm No.2!",
        "I'm going to scratch you out.",
        "I'll have to make my point more clear.",
        'Let me get right to the point.',
        "Let's hurry, I bore easily.",
        'I hate it when things get dull.',
        'So you want to push your luck?',
        'Did you pencil me in?',
        'Careful, I may leave a mark.'],
    'ym': [
        "I'm positive you're not going to like this.",
        "I don't know the meaning of no.",
        'Want to meet?  I say yes, anytime.',
        'You need some positive enforcement.',
        "I'm going to make a positive impression.",
        "I haven't been wrong yet.",
        "Yes, I'm ready for you.",
        'Are you positive you want to do this?',
        "I'll be sure to end this on a positive note.",
        "I'm confirming our meeting time.",
        "I won't take no for an answer."],
    'mm': [
        "I'm going to get into your business!",
        'Sometimes big hurts come in small packages.',
        'No job is too small for me.',
        "I want the job done right, so I'll do it myself.",
        'You need someone to manage your assets.',
        'Oh good, a project.',
        "Well, you've managed to find me.",
        'I think you need some managing.',
        "I'll take care of you in no time.",
        "I'm watching every move you make.",
        'Are you sure you want to do this?',
        "We're going to do this my way.",
        "I'm going to be breathing down your neck.",
        'I can be very intimidating.'],
    'cc': [
        'Surprised to hear from me?',
        'You rang?',
        'Are you ready to accept my charges?',
        'This caller always collects.',
        "I'm one smooth operator.",
        "Hold the phone -- I'm here.",
        'Have you been waiting for my call?',
        "I was hoping you'd answer my call.",
        "I'm going to cause a ringing sensation.",
        'I always make my calls direct.',
        'Boy, did you get your wires crossed.',
        'This call is going to cost you.',
        "You've got big trouble on the line."],
    'tm': [
        'I plan on making this inconvenient for you.',
        'Can I interest you in an insurance plan?',
        'You should have missed my call.',
        "You won't be able to get rid of me now.",
        'This a bad time?  Good.',
        'I was planning on running into you.',
        'I will be reversing the charges for this call.',
        'I have some costly items for you today.',
        'Too bad for you - I make house calls.',
        "I'm prepared to close this deal quickly.",
        "I'm going to use up a lot of your resources."],
    'nd': [
        'In my opinion, your name is mud.',
        "I hope you don't mind if I drop your name.",
        "Haven't we met before?",
        "Let's hurry, I'm having lunch with 'Mr. Hollywood.'",
        "Have I mentioned I know 'The Mingler?'",
        "You'll never forget me.",
        'I know all the right people to bring you down.',
        "I think I'll just drop in.",
        "I'm in the mood to drop some Toons.",
        "You name it, I've dropped it."],
    'gh': [
        'Put it there, Toon.',
        "Let's shake on it.",
        "I'm going to enjoy this.",
        "You'll notice I have a very firm grip.",
        "Let's seal the deal.",
        "Let's get right to the business at hand.",
        "Off handedly I'd say, you're in trouble.",
        "You'll find I'm a handful.",
        'I can be quite handy.',
        "I'm a very hands-on kinda guy.",
        'Would you like some hand-me-downs?',
        'Let me show you some of my handiwork.',
        'I think the handwriting is on the wall.'],
    'sc': [
        'I will make short work of you',
        "You're about to have money trouble.",
        "You're about to be overcharged.",
        'This will be a short-term assignment.',
        "I'll be done with you in short order.",
        "You'll soon experience a shortfall.",
        "Let's make this a short stop.",
        "I think you've come up short.",
        'I have a short temper for Toons.',
        "I'll be with you shortly.",
        "You're about to be shorted."],
    'pp': [
        'This is going to sting a little.',
        "I'm going to give you a pinch for luck.",
        "You don't want to press your luck with me.",
        "I'm going to put a crimp in your smile.",
        'Perfect, I have an opening for you.',
        'Let me add my two cents.',
        "I've been asked to pinch-hit.",
        "I'll prove you're not dreaming.",
        'Heads you lose, tails I win.',
        'A Penny for your gags.'],
    'tw': [
        'Things are about to get very tight.',
        "That's Mr. Tightwad to you.",
        "I'm going to cut off your funding.",
        'Is this the best deal you can offer?',
        "Let's get going - time is money.",
        "You'll find I'm very tightfisted.",
        "You're in a tight spot.",
        'Prepare to walk a tight rope.',
        'I hope you can afford this.',
        "I'm going to make this a tight squeeze.",
        "I'm going to make a big dent in your budget."],
    'bc': [
        'I enjoy subtracting Toons.',
        'You can count on me to make you pay.',
        'Bean there, done that.',
        'I can hurt you where it counts.',
        'I make every bean count.',
        'Your expense report is overdue.',
        'Time for an audit.',
        "Let's step into my office.",
        'Where have you bean?',
        "I've bean waiting for you.",
        "I'm going to bean you."],
    'bf': [
        "Looks like you've hit rock bottom.",
        "I'm ready to feast.",
        "I'm a sucker for Toons.",
        'Oh goody, lunch time.',
        'Perfect timing, I need a quick bite.',
        "I'd like some feedback on my performance.",
        "Let's talk about the bottom line.",
        "You'll find my talents are bottomless.",
        'Good, I need a little pick-me-up.',
        "I'd love to have you for lunch."],
    'b': [
        'Do you have a donation for me?',
        "I'm going to make you a sore loser.",
        "I'm going to leave you high and dry.",
        'I\'m "A" "Positive" I\'m going to win.',
        '"O" don\'t be so "Negative".',
        "I'm surprised you found me, I'm very mobile.",
        "I'm going to need to do a quick count on you.",
        "You're soon going to need a cookie and some juice.",
        "When I'm through you'll need to lie down.",
        'This will only hurt for a second.',
        "I'm going to make you dizzy.",
        "Good timing, I'm a pint low."],
    'dt': [
        "I'm gonna give you double the trouble.",
        'See if you can stop my double cross.',
        'I serve a mean double-DECKER.',
        "It's time to do some double-dealing.",
        'I plan to do some double DIPPING.',
        "You're not going to like my double play.",
        'You may want to double think this.',
        'Get ready for a double TAKE.',
        'You may want to double up against me.',
        'Doubles anyone??'],
    'ac': [
        "I'm going to chase you out of town!",
        'Do you hear a siren?',
        "I'm going to enjoy this.",
        'I love the thrill of the chase.',
        'Let me give you the run down.',
        'Do you have insurance?',
        'I hope you brought a stretcher with you.',
        'I doubt you can keep up with me.',
        "It's all uphill from here.",
        "You're going to need some urgent care soon.",
        'This is no laughing matter.',
        "I'm going to give you the business."] }

def getAttackTauntIndexFromIndex(suit, attackIndex):
    adict = getSuitAttack(suit.getStyleName(), suit.getLevel(), attackIndex)
    return getAttackTauntIndex(adict['name'])


def getAttackTauntIndex(attackName):
    if SuitAttackTaunts.has_key(attackName):
        taunts = SuitAttackTaunts[attackName]
        return whrandom.randint(0, len(taunts) - 1)
    else:
        return 0


def getAttackTaunt(attackName, index = None):
    if SuitAttackTaunts.has_key(attackName):
        taunts = SuitAttackTaunts[attackName]
    else:
        taunts = [
            'Take that!',
            'Take a memo on this!']
    if index != None:
        return taunts[index]
    else:
        return whrandom.choice(taunts)

SuitAttackTaunts = {
    'Audit': [
        "I believe your books don't balance.",
        "Looks like you're in the red.",
        'Let me help you with your books.',
        'Your debit column is much too high.',
        "Let's check your assets.",
        'This will put you in debt.',
        "Let's take a close look at what you owe.",
        'This should drain your account.',
        'Time for you to account for your expenses.',
        "I've found an error in your books."],
    'BounceCheck': [
        "Ah, too bad, you're funless.",
        'You have a payment due.',
        'I believe this check is yours.',
        'You owed me for this.',
        "I'm collecting on this debt.",
        "This check isn't going to be tender.",
        "You're going to be charged for this.",
        'Check this out.',
        'This is going to cost you.',
        "I'd like to cash this in.",
        "I'm just going to kick this back to you.",
        'This is one sour note.',
        "I'm deducting a service charge."],
    'Calculate': [
        'These numbers do add up!',
        'Did you count on this?',
        "Add it up, you're going down.",
        'Let me help you add this up.',
        'Did you register all your expenses?',
        "I'm fast with a calculator.",
        "Here's the grand total.",
        'Wow, your bill is adding up.',
        'A good calculator is a necessity.',
        'Cogs: 1 Toons: 0'],
    'ClipOnTie': [
        'Better dress for our meeting.',
        "You can't go OUT without your tie.",
        'The best dressed Cogs wear them.',
        'Try this on for size.',
        'You should dress for success.',
        'No tie, no service.',
        'Do you need help putting this on?',
        'Nothing says powerful like a good tie.',
        "Let's see if this fits.",
        'This is going to choke you up.',
        "You'll want to dress up before you go OUT.",
        "I think I'll tie you up."],
    'Demotion': [
        "You're moving down the corporate ladder.",
        "I'm sending you back to the Mail Room.",
        'Time to turn in your nameplate.',
        "You're going down, clown.",
        "Looks like you're stuck.",
        "You're going nowhere fast.",
        "You're in a dead end position.",
        "You won't be moving anytime soon.",
        "You're not going anywhere.",
        'This will go on your permanent record.'],
    'EvictionNotice': [
        "It's moving time.",
        'Pack your bags, Toon.',
        'Time to make some new living arrangements.',
        'Consider yourself served.',
        "You're behind on your lease.",
        'This will be extremely unsettling.',
        "You're about to be uprooted.",
        "I'm going to send you packing.",
        "You're out of place.",
        'Prepare to be relocated.',
        "You're in a hostel position."],
    'FingerWag': [
        'I have told you a thousand times.',
        'Now see here Toon.',
        "Don't make me laugh.",
        "Don't make me come over there.",
        "I'm tired of repeating myself.",
        "I believe we've been over this.",
        'You have no respect for us Cogs.',
        "I think it's time you pay attention.",
        'Blah, Blah, Blah, Blah, Blah.',
        "Don't make me stop this meeting.",
        'Am I going to have to separate you?',
        "We've been through this before."],
    'Fired': [
        'I hope you brought some marshmallows.',
        "It's going to get rather warm around here.",
        'This should take the chill out of the air.',
        "I hope you're cold blooded.",
        'Hot, hot and hotter.',
        "You're outta here.",
        'How does "well-done" sound?',
        'Can you say ouch?',
        'Hope you wore sunscreen.',
        'Do you feel a little toasty?',
        "You're going down in flames.",
        "You'll go out in a blaze.",
        "You're a flash in the pan.",
        'I think I have a bit of a flare about me.',
        "I just sparkle, don't I?",
        'Oh look, a crispy critter.',
        "You shouldn't run around half baked."],
    'FountainPen': [
        'This is going to leave a stain.',
        "Let's ink this deal.",
        "You've got a big spot on your feats.",
        'Be prepared for some permanent damage.',
        "You're going to need a good dry cleaner.",
        'You should change.',
        'This fountain pen has such a nice font.',
        "Here, I'll use my pen.",
        'Can you read my writing?',
        'I call this the plume of doom.',
        "There's a blot on your performance.",
        "Don't you hate when this happens?"],
    'FreezeAssets': [
        'Your assets are mine.',
        'Do you feel a draft?',
        "Hope you don't have plans.",
        'This should keep you on ice.',
        "There's a chill in the air.",
        'Winter is coming early this year.',
        'Are you feeling a little blue?',
        'Let me crystallize my plan.',
        "You're going to take this hard.",
        'This should cause freezer burn.',
        'I hope you like cold cuts.',
        "I'm very cold blooded."],
    'GlowerPower': [
        'You looking at me?',
        "I'm told I have very piercing eyes.",
        'I like to stay on the cutting edge.',
        "Jeepers, Creepers, don't you love my peepers?",
        "Here's looking at you kid.",
        "How's this for expressive eyes?",
        'My eyes are my strongest feature.',
        'The eyes have it.',
        'Peeka-boo, I see you.',
        'Look into my eyes...',
        'Shall we take a peek at your future?'],
    'HangUp': [
        "You've been disconnected.",
        'Good bye!',
        "It's time I end our connection.",
        "...and don't call back!",
        'Click!',
        'This conversation is over.',
        "I'm severing this link.",
        'I think you have a few hang ups.',
        "It appears you've got a weak link.",
        'Your time is up.',
        'I hope you receive this loud and clear.',
        'You got the wrong number.'],
    'PickPocket': [
        'Let me check your valuables.',
        "Hey, what's that over there?",
        'Like taking candy from a baby.',
        'What a steal.',
        "I'll hold this for you.",
        'Watch my hands at all times.',
        'The hand is quicker than the eye.',
        "There's nothing up my sleeve.",
        'The management is not responsible for lost items.',
        "Finder's keepers.",
        "You'll never see it coming.",
        'One for me, none for you.',
        "Don't mind if I do.",
        "You won't be needing this..."],
    'PoundKey': [
        'Time to return some calls.',
        "I'd like to make a collect call.",
        "Ring-a-ling - it's for you!",
        "I've been wanting to drop a pound or two.",
        'I have a lot of clout.',
        'This may cause a slight pounding sensation.',
        "I'll just punch in this number.",
        'Let me call up a little surprise.',
        "I'll ring you up.",
        "O.K. Toon, it's the pound for you."],
    'RazzleDazzle': [
        'Read my lips.',
        'How about these choppers?',
        "Aren't I charming?",
        "I'm going to wow you.",
        'My dentist does excellent work.',
        "Blinding aren't they?",
        "Hard to believe these aren't real.",
        "Shocking, aren't they?",
        "I'm going to cap this off.",
        'I floss after every meal.',
        'Say Cheese!'],
    'RedTape': [
        'This should wrap things up.',
        "I'm going to tie you up for awhile.",
        "You're on a roll.",
        'See if you can cut through this.',
        'This will get sticky.',
        "Hope you're claustrophobic",
        "I'll make sure you stick around.",
        'Let me keep you busy.',
        'Just try to unravel this.',
        'I want this meeting to stick with you.'],
    'Rolodex': [
        "Your card's in here somewhere.",
        "Here's the number for a pest exterminator.",
        'I want to give you my card.',
        "I've got your number right here.",
        "I've got you covered from a-z.",
        "You'll flip over this.",
        'Take this for a spin.',
        'Watch out for paper cuts.',
        "I'll let my fingers do the knocking.",
        'Is this how I can contact you?',
        'I want to make sure we stay in touch.'],
    'RubberStamp': [
        'I always make a good impression.',
        "It's important to apply firm and even pressure.",
        'A perfect imprint every time.',
        'I want to stamp you out.',
        'You must be RETURNED TO SENDER.',
        "You've been CANCELLED.",
        'You have a PRIORITY delivery.',
        "I'll make sure you RECEIVED my message.",
        "You're not going anywhere - you have POSTAGE DUE.",
        "I'll need a response ASAP."],
    'RubOut': [
        'And now for my disappearing act.',
        "I sense I've lost you somewhere.",
        'I decided to leave you out.',
        'I always rub out all obstacles.',
        "I'll just erase this error.",
        'I can make any nuisance disappear.',
        'I like things neat and tidy.',
        'Please try and stay animated.',
        "Now I see you...  now I don't.",
        'This will cause some fading.',
        "I'm going to eliminate the problem.",
        'Let me take care of your problem areas.'],
    'Shake': [
        "You're right on the epicenter.",
        "You're standing on a fault line.",
        "It's going to be a bumpy ride.",
        'I think of this as a natural disaster.',
        "It's a disaster of seismic proportions.",
        "This one's off the Richter scale.",
        'Time to duck and cover.',
        'You seem disturbed.',
        'Ready for a jolt?',
        'This will shake you up.',
        'I suggest a good escape plan.'],
    'Shred': [
        'I need to get rid of some hazardous waste.',
        "I'm increasing my throughput.",
        "I think I'll dispose of you right now.",
        'This will get rid of the evidence.',
        "There's no way to prove it now.",
        'See if you can put this back together.',
        'That tears it.',
        "I'm going to rip that idea to shreds.",
        "We don't want this to fall into the wrong hands.",
        'Easy come, easy go.',
        "Isn't this your last shred of hope?"],
    'Synergy': [
        "I'm taking this to committee.",
        "Your project's been cancelled.",
        "Your budget's been cut.",
        "We're restructuring your division.",
        'I put it to a vote, and you lose.',
        'I just received the final approval.',
        'A good team can get rid of any problem.',
        "I'll get back to you on this.",
        "Let's get right to business.",
        'Consider this a Synergy crisis.'],
    'Tabulate': [
        "This doesn't add up.",
        'By my count, you lose.',
        "You're racking up quite a tab.",
        "I'll have you totaled in a moment.",
        'Are you ready for these numbers?',
        'Your bill is now due and payable.',
        'Time for the reckoning.',
        'I like to put things in order.',
        'And the tally is...',
        'These numbers should prove to be quite powerful.'],
    'TeeOff': [
        "You're not up to par.",
        'Fore!',
        "I'm getting teed off.",
        "Caddie, I'll need my driver!",
        'Just try and avoid this a hazard.',
        'Swing!',
        'This is a sure hole in one.',
        "You're in my fairway.",
        'Notice my grip.',
        'Watch the birdie!',
        'Keep your eye on the ball!',
        'Mind if I play through?'],
    'Watercooler': [
        'This ought to cool you off',
        "Isn't this refreshing?",
        'I deliver.',
        'Straight from the tap - into your lap.',
        "What's the matter, it's just spring water.",
        "Don't worry, it's purified.",
        'Ah, another satisfied customer.',
        "It's time for your daily delivery.",
        "Hope your colors don't run.",
        'Care for a drink?',
        'It all comes out in the wash.',
        "The drink's on you."],
    'Withdrawal': [
        "I believe you're overdrawn.",
        'I hope your balance is high enough for this.',
        'Take that, with interest.',
        'Your balance is dropping.',
        "You're going to need to make a deposit soon.",
        "You've suffered an economic collapse.",
        "I think you're in a slump.",
        'Your finances have taken a decline.',
        'I foresee a definite downturn.',
        "It's a reversal of fortune."],
    'WriteOff': [
        'Let me increase your losses.',
        "Let's make the best of a bad deal.",
        'Time to balance the books.',
        "This won't look good on your books.",
        "I'm looking for some dividends.",
        'You must account for your losses.',
        'You can forget about a bonus.',
        "I'll shuffle your accounts around.",
        "You're about to suffer some losses.",
        'This is going to hurt your bottom line.'],
    'Brainstorm': [
        'I forecast rain.',
        'Hope you packed your umbrella.',
        'I want to enlighten you.How about a few rain DROPS?',
        'Not so sunny now, are you Toon?',
        'Ready for a down pour?',
        "I'm going to take you by storm.",
        'I call this a lightening attack.I love to be a wet blanket.'],
    'Buzz Word': [
        'Pardon me if I drone on.',
        'Have you heard the latest?',
        'Can you catch on to this?',
        'See if you can hum this Toon.',
        'Let me put in a good word for you.I\'ll "B" perfectly clear.You should "B" more careful.See if you can dodge this swarm.',
        "Careful, you're about to get stung.",
        'Looks like you have a bad case of hives.'],
    'Filibuster': [
        "Shall I fill 'er up?",
        'This is going to take awhile.',
        'I could do this all day.',
        "I don't even need to take a breath.",
        'I keep going and going and going.',
        'I never get tired of this one.',
        'I can talk a blue streak.',
        'Mind if I bend your ear?',
        "I think I'll shoot the breeze.",
        'I can always get a word in edgewise.'],
    'Hot Air': [
        "We're having a heated discussion.",
        "You're experiencing a heat wave.",
        "I've reached my boiling point.",
        'This should cause some wind burn.',
        'I hate to grill you, but...',
        "Always remember, where's there's smoke, there's fire.",
        "You're looking a little burned out.",
        'Another meeting up in smoke,',
        "Guess it's time to add fuel to the fire.",
        'Let me kindle a working relationship.',
        'I have some glowing remarks for you.',
        'Air Raid!!!'],
    'Jargon': [
        'What nonsense.',
        'See if you can make sense of this.',
        'I hope you get this loud and clear.',
        "Looks like I'm going to have to raise my voice.",
        'I insist on having my say.',
        "I'm very outspoken.",
        'Time to talk to you down.',
        'I must pontificate on this subject.',
        'See, words can hurt you.',
        'Did you catch my meaning?',
        'Words, words, words, words, words.'],
    'Liquidate': [
        'I like to keep things fluid.',
        'Are you having some cash flow problems?',
        "I'll have to purge your assets.",
        'Time for you to go with the flow.',
        "Remember it's slippery when wet.",
        'Your numbers are running.',
        'You seem to be slipping.',
        "It's all crashing down on you.",
        "I think you're diluted.",
        "You're all washed up."],
    'Mumbo Jumbo': [
        "Let me make this perfectly clear.It's as simple as this.",
        "This is how we're going to do this.",
        'Let me supersize this for you.',
        'You might call this techobabble.',
        'Here are my five-dollar words.',
        'Boy, this is a mouth full.',
        'Some call me bombastic.',
        'Let me just interject this.',
        'I believe these are the right words.'],
    'Schmooze': [
        "You'll never see this coming",
        'This will look good on you.',
        "You've earned this.",
        "I don't mean to gush.",
        'Flattery will get me everywhere.',
        "I'm going to pile it on now.",
        'Time to lay it on thick.',
        "I'm going to get on your good side.",
        'That deserves a good slap on the back.',
        "I'm going to ring your praises.",
        'I hate to knock you off your pedestal, but...'] }
