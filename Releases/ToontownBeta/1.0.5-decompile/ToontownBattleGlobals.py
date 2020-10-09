# Source Generated with Decompyle++
# File: ToontownBattleGlobals.pyo (Python 2.0)

from ToontownGlobals import *
import math
BaseHp = 15
Tracks = [
    'toon-up',
    'trap',
    'lure',
    'sound',
    'throw',
    'squirt',
    'drop']
TrackColors = ((211 / 255.0, 148 / 255.0, 255 / 255.0), (249 / 255.0, 255 / 255.0, 93 / 255.0), (179 / 255.0, 190 / 255.0, 76 / 255.0), (93 / 255.0, 108 / 255.0, 239 / 255.0), (255 / 255.0, 145 / 255.0, 66 / 255.0), (255 / 255.0, 65 / 255.0, 199 / 255.0), (67 / 255.0, 243 / 255.0, 255 / 255.0))
TrackZones = [
    MinniesMelodyland,
    TheBrrrgh,
    TheBrrrgh,
    ToontownCentral,
    ToontownCentral,
    ToontownCentral,
    DonaldsDock]

try:
    wantAllProps = base.config.GetBool('want-all-props', 0)
except:
    wantAllProps = simbase.config.GetBool('want-all-props', 0)

if wantAllProps == 1:
    for i in range(len(TrackZones)):
        TrackZones[i] = ToontownCentral
    

HEAL_TRACK = 0
TRAP_TRACK = 1
LURE_TRACK = 2
SOUND_TRACK = 3
THROW_TRACK = 4
SQUIRT_TRACK = 5
DROP_TRACK = 6
MIN_TRACK_INDEX = 0
MAX_TRACK_INDEX = 6
MIN_LEVEL_INDEX = 0
MAX_LEVEL_INDEX = 5
Levels = [
    0,
    10,
    50,
    250,
    750,
    2000]
MaxSkill = 5000
MaxToonAcc = 95
StartingLevel = 0
CarryLimits = (((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((5, 0, 0, 0, 0, 0), (7, 3, 0, 0, 0, 0), (10, 7, 3, 0, 0, 0), (15, 10, 7, 3, 0, 0), (15, 15, 10, 5, 3, 0), (20, 15, 15, 10, 5, 2)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)), ((10, 0, 0, 0, 0, 0), (10, 5, 0, 0, 0, 0), (15, 10, 5, 0, 0, 0), (20, 15, 10, 5, 0, 0), (25, 20, 15, 10, 3, 0), (30, 25, 20, 15, 7, 3)))
MaxProps = ((15, 40), (30, 60), (75, 80))
AvProps = (('feather', 'bullhorn', 'lipstick', 'bamboocane', 'pixiedust', 'baton'), ('banana', 'rake', 'marbles', 'quicksand', 'trapdoor', 'tnt'), ('1dollar', 'smmagnet', '5dollar', 'bigmagnet', '10dollar', 'hypnogogs'), ('bikehorn', 'whistle', 'bugle', 'aoogah', 'elephant', 'foghorn'), ('cupcake', 'fruitpieslice', 'creampieslice', 'fruitpie', 'creampie', 'cake'), ('flower', 'waterglass', 'waterballoon', 'bottle', 'firehose', 'stormcloud'), ('flowerpot', 'sandbag', 'anvil', 'weight', 'safe', 'piano'))
AvPropsNew = (('feather', 'megaphone', 'lipstick', 'bamboo_cane', 'pixiedust', 'juggling_cubes'), ('bannana_peel', 'rake', 'marbles', 'quicksand_icon', 'trapdoor', 'tnt'), ('1dollarbill', 'small_magnet', '5dollarbill', 'big_magnet', '10dollarbill', 'hypno_goggles'), ('bikehorn', 'whistle', 'bugle', 'aoogah', 'elephant', 'fog_horn'), ('tart', 'fruit_pie_slice', 'cream_pie_slice', 'fruitpie', 'creampie', 'cake'), ('squirt_flower', 'glass_of_water', 'water_gun', 'seltzer_bottle', 'firehose', 'storm_cloud'), ('flower_pot', 'sandbag', 'anvil', 'weight', 'safe_box', 'piano'))
AvPropStrings = (('Feather', 'Megaphone', 'Lipstick', 'Bamboo Cane', 'Pixie Dust', 'Juggling Balls'), ('Banana Peel', 'Rake', 'Marbles', 'Quicksand', 'Trapdoor', 'TNT'), ('$1 bill', 'Small Magnet', '$5 bill', 'Big Magnet', '$10 bill', 'Hypno-goggles'), ('Bike Horn', 'Whistle', 'Bugle', 'Aoogah', 'Elephant', 'Foghorn'), ('Cupcake', 'Fruit Pie Slice', 'Cream Pie Slice', 'Fruit Pie', 'Cream Pie', 'Birthday Cake'), ('Squirting Flower', 'Glass of Water', 'Squirt Gun', 'Seltzer Bottle', 'Fire Hose', 'Storm Cloud'), ('Flower Pot', 'Sandbag', 'Anvil', 'Big Weight', 'Safe', 'Upright Piano'))
AvPropStringsPlural = (('Feathers', 'Megaphones', 'Lipsticks', 'Bamboo Canes', 'Pixie Dusts', 'Juggling Balls'), ('Banana Peels', 'Rakes', 'Marbles', 'Quicksands', 'Trapdoors', 'TNTs'), ('$1 bills', 'Small Magnets', '$5 bills', 'Big Magnets', '$10 bills', 'Hypno-goggles'), ('Bike Horns', 'Whistles', 'Bugles', 'Aoogahs', 'Elephants', 'Foghorns'), ('Cupcakes', 'Fruit Pie Slices', 'Cream Pie Slices', 'Fruit Pies', 'Cream Pies', 'Birthday Cakes'), ('Squirting Flowers', 'Glasses of Water', 'Squirt Guns', 'Seltzer Bottles', 'Fire Hoses', 'Storm Clouds'), ('Flower Pots', 'Sandbags', 'Anvils', 'Big Weights', 'Safes', 'Upright Pianos'))
AvPropAccuracy = ((70, 70, 70, 70, 70, 70), (0, 0, 0, 0, 0, 0), (50, 50, 60, 60, 70, 70), (95, 95, 95, 95, 95, 95), (75, 75, 75, 75, 75, 75), (95, 95, 95, 95, 95, 95), (50, 50, 50, 50, 50, 50))
AvTrackAccStrings = ('Medium', 'Perfect', 'Low', 'High', 'Medium', 'High', 'Low')
AvPropDamage = ((((8, 10), (Levels[0], Levels[1])), ((15, 18), (Levels[1], Levels[2])), ((25, 30), (Levels[2], Levels[3])), ((40, 45), (Levels[3], Levels[4])), ((60, 70), (Levels[4], Levels[5])), ((90, 120), (Levels[5], MaxSkill))), (((8, 9), (Levels[0], Levels[1])), ((15, 17), (Levels[1], Levels[2])), ((25, 28), (Levels[2], Levels[3])), ((38, 41), (Levels[3], Levels[4])), ((52, 55), (Levels[4], Levels[5])), ((60, 80), (Levels[5], MaxSkill))), (((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0)), ((0, 0), (0, 0))), (((3, 4), (Levels[0], Levels[1])), ((5, 7), (Levels[1], Levels[2])), ((9, 11), (Levels[2], Levels[3])), ((14, 16), (Levels[3], Levels[4])), ((19, 21), (Levels[4], Levels[5])), ((25, 30), (Levels[5], MaxSkill))), (((4, 6), (Levels[0], Levels[1])), ((8, 10), (Levels[1], Levels[2])), ((14, 17), (Levels[2], Levels[3])), ((24, 27), (Levels[3], Levels[4])), ((36, 40), (Levels[4], Levels[5])), ((48, 60), (Levels[5], MaxSkill))), (((3, 4), (Levels[0], Levels[1])), ((6, 8), (Levels[1], Levels[2])), ((10, 12), (Levels[2], Levels[3])), ((18, 21), (Levels[3], Levels[4])), ((27, 30), (Levels[4], Levels[5])), ((36, 50), (Levels[5], MaxSkill))), (((10, 10), (Levels[0], Levels[1])), ((18, 18), (Levels[1], Levels[2])), ((30, 30), (Levels[2], Levels[3])), ((45, 45), (Levels[3], Levels[4])), ((60, 60), (Levels[4], Levels[5])), ((85, 100), (Levels[5], MaxSkill))))
ATK_SINGLE_TARGET = 0
ATK_GROUP_TARGET = 1
AvPropTargetCat = ((ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET, ATK_SINGLE_TARGET, ATK_GROUP_TARGET), (ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET, ATK_SINGLE_TARGET), (ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET, ATK_GROUP_TARGET))
AvPropTarget = (0, 1, 0, 2, 1, 1, 1)

def getAvPropDamage(attackTrack, attackLevel, exp):
    minD = AvPropDamage[attackTrack][attackLevel][0][0]
    maxD = AvPropDamage[attackTrack][attackLevel][0][1]
    minE = AvPropDamage[attackTrack][attackLevel][1][0]
    maxE = AvPropDamage[attackTrack][attackLevel][1][1]
    expVal = min(exp, maxE)
    expPerHp = float((maxE - minE) + 1) / float((maxD - minD) + 1)
    return math.floor((expVal - minE) / expPerHp) + minD


def isGroup(track, level):
    if not track == SOUND_TRACK:
        if (track == HEAL_TRACK or track == LURE_TRACK) and level == 1 and level == 3 or level == 5:
            return 1
        else:
            return 0

