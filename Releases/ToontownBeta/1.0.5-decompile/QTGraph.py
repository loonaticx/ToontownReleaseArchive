# Source Generated with Decompyle++
# File: QTGraph.pyo (Python 2.0)

from QTNode import *

def decodeQTMessage(msg):
    curNode = QTGraph['start']
    message = ''
    for index in msg:
        message = message + curNode.getPhrase(index)
        curNode = curNode[index]
        if curNode == None:
            break
        
    
    return message


def rebuildMenus():
    for key in QTGraph.keys():
        QTGraph[key].createMenu()
    


def QTSanityCheck():
    pass


def setupQTGraphConcise():
    QTGraphConcise = {
        'start': QTNode('start'),
        'letsgo': QTNode('letsgo'),
        'letsuse': QTNode('letsuse'),
        'ineed': QTNode('ineed'),
        'you': QTNode('you') }
    node = QTGraphConcise['start']
    node['Hi'] = QTSend
    node['Bye'] = QTSend
    node['Ok'] = QTSend
    node['Yes'] = QTSend
    node['No'] = QTSend
    node['Wow!'] = QTSend
    node['Huh?'] = QTSend
    node['Ouch!'] = QTSend
    node['Nice shot!'] = QTSend
    node['Thanks!'] = QTSend
    node['Sorry'] = QTSend
    node['Where should we go?'] = QTSend
    node["Let's go"] = QTGraphConcise['letsgo']
    node['Follow me'] = QTSend
    node['Hurry up!'] = QTSend
    node['Wait for me!'] = QTSend
    node["Let's use"] = QTGraphConcise['letsuse']
    node['I need'] = QTGraphConcise['ineed']
    node['You'] = QTGraphConcise['you']
    node = QTGraphConcise['letsgo']
    node[' on the trolley!'] = QTSend
    node[' back to the playground!'] = QTSend
    node[' fight the COGS!'] = QTSend
    node[' to Toontown Central!'] = QTSend
    node[" to Donald's Dock!"] = QTSend
    node[" to Minnie's Melodyland!"] = QTSend
    node[" to Daisy's Garden!"] = QTSend
    node[' to The Brrrgh!'] = QTSend
    node[" to Donald's Dreamland!"] = QTSend
    node = QTGraphConcise['letsuse']
    node[' trap!'] = QTSend
    node[' lure!'] = QTSend
    node[' sound!'] = QTSend
    node[' throw!'] = QTSend
    node[' squirt!'] = QTSend
    node[' drop!'] = QTSend
    node = QTGraphConcise['ineed']
    node[' more gags.'] = QTSend
    node[' a Toon-Up.'] = QTSend
    node[' to go.'] = QTSend
    node = QTGraphConcise['you']
    node[' are awesome!'] = QTSend
    node[' look nice.'] = QTSend
    node[' are a genius!'] = QTSend
    node[' stink!'] = QTSend
    node[' are too slow.'] = QTSend
    return QTGraphConcise


def setupQTGraphEnglish():
    QTGraphEnglish = {
        'start': QTNode('start'),
        'hi': QTNode('hi'),
        'no': QTNode('no'),
        'i': QTNode('i'),
        'you': QTNode('you'),
        'lets': QTNode('lets'),
        'what': QTNode('what'),
        'where': QTNode('where'),
        'thats': QTNode('thats'),
        'bye': QTNode('bye'),
        'iam': QTNode('iam'),
        'think': QTNode('think'),
        'want': QTNode('want'),
        'dont': QTNode('dont'),
        'like': QTNode('like'),
        'are': QTNode('are'),
        'look': QTNode('look'),
        'have': QTNode('have'),
        'need': QTNode('need'),
        'should': QTNode('should'),
        'get': QTNode('get'),
        'name': QTNode('name'),
        'nice': QTNode('nice'),
        'isa': QTNode('isa'),
        'whereis': QTNode('whereis'),
        'nickname': QTNode('nickname'),
        'lookingfor': QTNode('lookingfor'),
        'youre': QTNode('youre'),
        'this': QTNode('this'),
        'likethis': QTNode('likethis'),
        'that': QTNode('that'),
        'headto': QTNode('headto'),
        'play': QTNode('play'),
        'geta': QTNode('geta'),
        'great': QTNode('great'),
        'silly': QTNode('silly'),
        'cool': QTNode('cool'),
        'closest': QTNode('closest'),
        'find': QTNode('find'),
        'findquestion': QTNode('findquestion') }
    node = QTGraphEnglish['start']
    node['Thanks.'] = QTSend
    node['Hi'] = QTGraphEnglish['hi']
    node['Bye'] = QTGraphEnglish['bye']
    node['No'] = QTGraphEnglish['no']
    node['I'] = QTGraphEnglish['i']
    node['You'] = QTGraphEnglish['you']
    node["Let's"] = QTGraphEnglish['lets']
    node['What'] = QTGraphEnglish['what']
    node['Where'] = QTGraphEnglish['where']
    node["That's"] = QTGraphEnglish['thats']
    node = QTGraphEnglish['hi']
    node[', pal.'] = QTSend
    node[', stranger.'] = QTSend
    node[', want to talk?'] = QTSend
    node[", I'm"] = QTGraphEnglish['iam']
    node[", you're"] = QTGraphEnglish['youre']
    node = QTGraphEnglish['no']
    node[' way.'] = QTSend
    node[' prob.'] = QTSend
    node[' fun.'] = QTSend
    node[' time.'] = QTSend
    node[' can do.'] = QTSend
    node = QTGraphEnglish['i']
    node[' gotta go.'] = QTSend
    node[' think'] = QTGraphEnglish['think']
    node[' want'] = QTGraphEnglish['want']
    node[" don't"] = QTGraphEnglish['dont']
    node[' like'] = QTGraphEnglish['like']
    node[' am'] = QTGraphEnglish['iam']
    node = QTGraphEnglish['you']
    node[' are'] = QTGraphEnglish['are']
    node[' look'] = QTGraphEnglish['look']
    node[' have'] = QTGraphEnglish['have']
    node[' need'] = QTGraphEnglish['need']
    node[' should'] = QTGraphEnglish['should']
    node = QTGraphEnglish['lets']
    node[' talk.'] = QTSend
    node[' play a game.'] = QTSend
    node[' just hang out.'] = QTSend
    node[' make SUITs laff.'] = QTSend
    node[' head to'] = QTGraphEnglish['headto']
    node[' find'] = QTGraphEnglish['name']
    node = QTGraphEnglish['what']
    node[' did you say?'] = QTSend
    node["'s your name?"] = QTSend
    node["'s going on?"] = QTSend
    node[' are you?'] = QTSend
    node[' should we do?'] = QTSend
    node[' is that?'] = QTSend
    node[' do you mean?'] = QTSend
    node[' is a'] = QTGraphEnglish['isa']
    node = QTGraphEnglish['where']
    node[' am I?'] = QTSend
    node[' should we go?'] = QTSend
    node[' did you say?'] = QTSend
    node["'d you get"] = QTGraphEnglish['get']
    node["'d you find"] = QTGraphEnglish['findquestion']
    node[' is'] = QTGraphEnglish['whereis']
    node = QTGraphEnglish['thats']
    node[' not happening.'] = QTSend
    node[' a laff riot!'] = QTSend
    node[' okay.'] = QTSend
    node[' right.'] = QTSend
    node[' funny.'] = QTSend
    node[' what takes you to games.'] = QTSend
    node[' what heals you.'] = QTSend
    node[' what makes SUITS laff.'] = QTSend
    node[' the unfunny guys.'] = QTSend
    node[' a nice'] = QTGraphEnglish['nice']
    node = QTGraphEnglish['bye']
    node[", I'm leaving."] = QTSend
    node[' for now.'] = QTSend
    node[', guys.'] = QTSend
    node[', bye'] = QTGraphEnglish['nickname']
    node = QTGraphEnglish['iam']
    node[' just hanging out.'] = QTSend
    node[' lost.'] = QTSend
    node[' a cat.'] = QTSend
    node[' a dog.'] = QTSend
    node[' a duck.'] = QTSend
    node[' a mouse.'] = QTSend
    node[' a horse.'] = QTSend
    node[' okay.'] = QTSend
    node[' cool with that.'] = QTSend
    node[' outta here.'] = QTSend
    node[" lookin' for"] = QTGraphEnglish['lookingfor']
    node = QTGraphEnglish['think']
    node[" you're"] = QTGraphEnglish['youre']
    node[' this'] = QTGraphEnglish['this']
    node[' you should head to'] = QTGraphEnglish['headto']
    node = QTGraphEnglish['want']
    node[' more gags to use.'] = QTSend
    node[' to play a game.'] = QTSend
    node[' to get to'] = QTGraphEnglish['headto']
    node[' to get'] = QTGraphEnglish['geta']
    node[' to find'] = QTGraphEnglish['find']
    node = QTGraphEnglish['dont']
    node[' know.'] = QTSend
    node[' think so.'] = QTSend
    node[' want that.'] = QTSend
    node[' have time.'] = QTSend
    node[' play that.'] = QTSend
    node[' like'] = QTGraphEnglish['like']
    node = QTGraphEnglish['like']
    node[' you.'] = QTSend
    node[' this'] = QTGraphEnglish['likethis']
    node[' that'] = QTGraphEnglish['that']
    node[' to hang out at'] = QTGraphEnglish['headto']
    node = QTGraphEnglish['are']
    node[" lookin' bad."] = QTSend
    node[' low on points.'] = QTSend
    node[' too rude!'] = QTSend
    node[' krazy!'] = QTSend
    node[' cool.'] = QTSend
    node[' in'] = QTGraphEnglish['headto']
    node = QTGraphEnglish['look']
    node[' great'] = QTGraphEnglish['nickname']
    node[' alright'] = QTGraphEnglish['nickname']
    node[' goofy'] = QTGraphEnglish['nickname']
    node[' silly'] = QTGraphEnglish['nickname']
    node[' funny'] = QTGraphEnglish['nickname']
    node[' weird'] = QTGraphEnglish['nickname']
    node[" slammin'"] = QTGraphEnglish['nickname']
    node = QTGraphEnglish['have']
    node[' cool clothes.'] = QTSend
    node[" jammin' gags."] = QTSend
    node[' too much.'] = QTSend
    node[' really low points.'] = QTSend
    node[' no idea.'] = QTSend
    node[' to get outta here.'] = QTSend
    node[' a good time.'] = QTSend
    node = QTGraphEnglish['need']
    node[' some points.'] = QTSend
    node[' better skills.'] = QTSend
    node[' a joke.'] = QTSend
    node[' to lighten up.'] = QTSend
    node[' to play'] = QTGraphEnglish['play']
    node[' to get'] = QTGraphEnglish['geta']
    node = QTGraphEnglish['should']
    node[' get some points.'] = QTSend
    node[' get some new clothes.'] = QTSend
    node[' tell a joke.'] = QTSend
    node[' laugh a little.'] = QTSend
    node[' play'] = QTGraphEnglish['play']
    node[' head to'] = QTGraphEnglish['headto']
    node = QTGraphEnglish['get']
    node[' that great'] = QTGraphEnglish['great']
    node[' that silly'] = QTGraphEnglish['silly']
    node[' that cool'] = QTGraphEnglish['cool']
    node = QTGraphEnglish['name']
    node[' a trolley.'] = QTSend
    node[' Mickey.'] = QTSend
    node[' Minnie.'] = QTSend
    node[' Donald.'] = QTSend
    node[' Goofy.'] = QTSend
    node[' Pluto.'] = QTSend
    node[' Daisy.'] = QTSend
    node = QTGraphEnglish['nice']
    node[' outfit.'] = QTSend
    node[' trick you did.'] = QTSend
    node[' bag of gags.'] = QTSend
    node[' thing you said.'] = QTSend
    node = QTGraphEnglish['isa']
    node[' trolley?'] = QTSend
    node[' toon-up?'] = QTSend
    node[' gag?'] = QTSend
    node[' SUIT?'] = QTSend
    node[' good place to play?'] = QTSend
    node[' fun neighborhood?'] = QTSend
    node = QTGraphEnglish['whereis']
    node[' ToonTown Central?'] = QTSend
    node[" Donald's Boat?"] = QTSend
    node[' the Brrrgh?'] = QTSend
    node[' Melody Land?'] = QTSend
    node[" Goofy's Place?"] = QTSend
    node[' the Funny Farm?'] = QTSend
    node[" Daisy's Garden?"] = QTSend
    node[' the Construction Zone?'] = QTSend
    node[' Dreamland?'] = QTSend
    node[' the closest'] = QTGraphEnglish['closest']
    node = QTGraphEnglish['find']
    node[' a trolley.'] = QTSend
    node[' a shop.'] = QTSend
    node[' ToonTown Central.'] = QTSend
    node[" Donald's Dock."] = QTSend
    node[' Melody Land.'] = QTSend
    node[" Goofy's Place."] = QTSend
    node[' the Funny Farm.'] = QTSend
    node[' Dreamland.'] = QTSend
    node[' the Construction Zone.'] = QTSend
    node[' the Brrrgh.'] = QTSend
    node[" Minnie's Melody Land."] = QTSend
    node = QTGraphEnglish['findquestion']
    node[' a trolley?'] = QTSend
    node[' a shop?'] = QTSend
    node[' ToonTown Central?'] = QTSend
    node[" Donald's Dock?"] = QTSend
    node[' the Brrrgh?'] = QTSend
    node[' Melody Land?'] = QTSend
    node[" Goofy's Place?"] = QTSend
    node[' the Funny Farm?'] = QTSend
    node[" Daisy's Garden?"] = QTSend
    node[' Dreamland?'] = QTSend
    node[' the Construction Zone?'] = QTSend
    node = QTGraphEnglish['nickname']
    node[', small stuff.'] = QTSend
    node[', dufus.'] = QTSend
    node[', big guy'] = QTSend
    node[', airhead.'] = QTSend
    node[', scrub.'] = QTSend
    node[', bro.'] = QTSend
    node = QTGraphEnglish['lookingfor']
    node[' a trolley.'] = QTSend
    node[' the igloo.'] = QTSend
    node[' the dance place.'] = QTSend
    node[' the boat.'] = QTSend
    node[' the maze.'] = QTSend
    node[' my friends.'] = QTSend
    node[' someone to play'] = QTGraphEnglish['play']
    node[' someone with'] = QTGraphEnglish['geta']
    node = QTGraphEnglish['youre']
    node[' cool looking.'] = QTSend
    node[' so lost.'] = QTSend
    node[' short.'] = QTSend
    node[' way tall.'] = QTSend
    node[' right.'] = QTSend
    node[' wrong.'] = QTSend
    node[' okay.'] = QTSend
    node[" buggin'."] = QTSend
    node = QTGraphEnglish['likethis']
    node[' talk.'] = QTSend
    node[' outfit.'] = QTSend
    node[' game.'] = QTSend
    node[' place.'] = QTSend
    node[' joke.'] = QTSend
    node = QTGraphEnglish['this']
    node[' is cool.'] = QTSend
    node[' is weird.'] = QTSend
    node[' is fun.'] = QTSend
    node[" is kickin'."] = QTSend
    node[' is lame.'] = QTSend
    node = QTGraphEnglish['that']
    node[', too.'] = QTSend
    node[' idea.'] = QTSend
    node[' hat.'] = QTSend
    node[' joke.'] = QTSend
    node[' game we played.'] = QTSend
    node = QTGraphEnglish['headto']
    node[' ToonTown Central.'] = QTSend
    node[" Donald's Boat."] = QTSend
    node[' The Brrrgh.'] = QTSend
    node[' Melody Land.'] = QTSend
    node[" Daisy's Garden."] = QTSend
    node[" Goofy's Place."] = QTSend
    node[' the Funny Farm.'] = QTSend
    node[' Dreamland.'] = QTSend
    node[' the Construction Zone.'] = QTSend
    node[' trouble.'] = QTSend
    node = QTGraphEnglish['play']
    node[' a trolley game.'] = QTSend
    node[' in the water.'] = QTSend
    node[' around here.'] = QTSend
    node[' tag.'] = QTSend
    node[' with someone else.'] = QTSend
    node = QTGraphEnglish['geta']
    node[' a toon-up.'] = QTSend
    node[' a better gag to use.'] = QTSend
    node[' a few more points.'] = QTSend
    node[' a new outfit.'] = QTSend
    node[' a set of more gags'] = QTSend
    node = QTGraphEnglish['great']
    node[' set of gloves?'] = QTSend
    node[' pair of shoes?'] = QTSend
    node[' shirt?'] = QTSend
    node[' dress?'] = QTSend
    node[' pair of shorts?'] = QTSend
    node = QTGraphEnglish['silly']
    node[' outfit?'] = QTSend
    node[' gloves?'] = QTSend
    node[' shoes?'] = QTSend
    node[' shirt?'] = QTSend
    node[' dress?'] = QTSend
    node[' shorts?'] = QTSend
    node = QTGraphEnglish['cool']
    node[' gag?'] = QTSend
    node[' thing you used?'] = QTSend
    node[' stuff to wear?'] = QTSend
    node[' trick?'] = QTSend
    node = QTGraphEnglish['closest']
    node[' trolley?'] = QTSend
    node[' way out?'] = QTSend
    node[' SUIT?'] = QTSend
    node[' playground?'] = QTSend
    node[' shop?'] = QTSend
    return QTGraphEnglish


def setupQTGraphMiniEnglish():
    QTGraphMiniEnglish = {
        'start': QTNode('start'),
        'hi': QTNode('hi'),
        'bye': QTNode('bye'),
        'i': QTNode('i'),
        'you': QTNode('you'),
        'where': QTNode('where'),
        'thats': QTNode('thats'),
        'iam': QTNode('iam'),
        'like': QTNode('like'),
        'are': QTNode('are'),
        'look': QTNode('look'),
        'have': QTNode('have'),
        'whereis': QTNode('whereis'),
        'lookingfor': QTNode('lookingfor'),
        'headto': QTNode('headto') }
    node = QTGraphMiniEnglish['start']
    node['Hi'] = QTGraphMiniEnglish['hi']
    node['Thanks.'] = QTSend
    node['No.'] = QTSend
    node['Yes.'] = QTSend
    node['Bye'] = QTGraphMiniEnglish['bye']
    node['I'] = QTGraphMiniEnglish['i']
    node['You'] = QTGraphMiniEnglish['you']
    node['Where'] = QTGraphMiniEnglish['where']
    node["That's"] = QTGraphMiniEnglish['thats']
    node = QTGraphMiniEnglish['hi']
    node[", I'm"] = QTGraphMiniEnglish['iam']
    node[', want to talk?'] = QTSend
    node[', pal.'] = QTSend
    node = QTGraphMiniEnglish['bye']
    node['!!!'] = QTSend
    node[' for now.'] = QTSend
    node = QTGraphMiniEnglish['i']
    node[' am'] = QTGraphMiniEnglish['iam']
    node[' like'] = QTGraphMiniEnglish['like']
    node[' gotta go.'] = QTSend
    node = QTGraphMiniEnglish['you']
    node[' are'] = QTGraphMiniEnglish['are']
    node[' look'] = QTGraphMiniEnglish['look']
    node[' have'] = QTGraphMiniEnglish['have']
    node = QTGraphMiniEnglish['where']
    node['???'] = QTSend
    node[' are we?'] = QTSend
    node[' is'] = QTGraphMiniEnglish['whereis']
    node = QTGraphMiniEnglish['thats']
    node[' funny.'] = QTSend
    node[' what heals you.'] = QTSend
    node[' the bad guys.'] = QTSend
    node = QTGraphMiniEnglish['iam']
    node[' lost.'] = QTSend
    node[' looking for'] = QTGraphMiniEnglish['lookingfor']
    node[' a cat.'] = QTSend
    node[' a dog.'] = QTSend
    node[' a mouse.'] = QTSend
    node[' a horse.'] = QTSend
    node[' okay.'] = QTSend
    node = QTGraphMiniEnglish['like']
    node[' you.'] = QTSend
    node[' this game.'] = QTSend
    node = QTGraphMiniEnglish['are']
    node[' nuts.'] = QTSend
    node[' in'] = QTGraphMiniEnglish['headto']
    node = QTGraphMiniEnglish['look']
    node[' great.'] = QTSend
    node[' marvelous.'] = QTSend
    node[' funny.'] = QTSend
    node[' weird.'] = QTSend
    node = QTGraphMiniEnglish['have']
    node[' cool clothes.'] = QTSend
    node[' too much.'] = QTSend
    node = QTGraphMiniEnglish['whereis']
    node[' ToonTown Central?'] = QTSend
    node[" Donald's Boat?"] = QTSend
    node[' Melody Land?'] = QTSend
    node[" Goofy's Place?"] = QTSend
    node[' the Funny Farm?'] = QTSend
    node[' Dreamland?'] = QTSend
    node[' the Construction Zone?'] = QTSend
    node[' the Brrrgh?'] = QTSend
    node = QTGraphMiniEnglish['lookingfor']
    node[' the Igloo.'] = QTSend
    node[' a trolley.'] = QTSend
    node[' my pals.'] = QTSend
    node = QTGraphMiniEnglish['headto']
    node[' the Igloo.'] = QTSend
    node[' a trolley.'] = QTSend
    node[' ToonTown Central.'] = QTSend
    node[" Donald's Boat."] = QTSend
    node[' Melody Land.'] = QTSend
    node[" Goofy's Place."] = QTSend
    node[' the Funny Farm.'] = QTSend
    node[' Dreamland.'] = QTSend
    node[' the Construction Zone.'] = QTSend
    node[' the Brrrgh.'] = QTSend
    return QTGraphMiniEnglish


def setupQTGraphMiniFrench():
    QTGraphMiniFrench = {
        'start': QTNode('start'),
        'hi': QTNode('hi'),
        'bye': QTNode('bye'),
        'i': QTNode('i'),
        'you': QTNode('you'),
        'where': QTNode('where'),
        'thats': QTNode('thats'),
        'iam': QTNode('iam'),
        'like': QTNode('like'),
        'are': QTNode('are'),
        'look': QTNode('look'),
        'have': QTNode('have'),
        'whereis': QTNode('whereis'),
        'lookingfor': QTNode('lookingfor'),
        'headto': QTNode('headto') }
    node = QTGraphMiniFrench['start']
    node['Salut'] = QTGraphMiniFrench['hi']
    node['Merci.'] = QTSend
    node['Non.'] = QTSend
    node['Oui.'] = QTSend
    node['Au revoir'] = QTGraphMiniFrench['bye']
    node['Je'] = QTGraphMiniFrench['i']
    node['Vous'] = QTGraphMiniFrench['you']
    node['Ou'] = QTGraphMiniFrench['where']
    node["C'est"] = QTGraphMiniFrench['thats']
    node = QTGraphMiniFrench['hi']
    node[', je suis'] = QTGraphMiniFrench['iam']
    node[', voulez-vous parler?'] = QTSend
    node[', ami.'] = QTSend
    node = QTGraphMiniFrench['bye']
    node['!!!'] = QTSend
    node[' pour maintenant.'] = QTSend
    node = QTGraphMiniFrench['i']
    node[' suis'] = QTGraphMiniFrench['iam']
    node[' aime'] = QTGraphMiniFrench['like']
    node[' dois aller.'] = QTSend
    node = QTGraphMiniFrench['you']
    node[' etes'] = QTGraphMiniFrench['are']
    node[' semblez'] = QTGraphMiniFrench['look']
    node[' avez'] = QTGraphMiniFrench['have']
    node = QTGraphMiniFrench['where']
    node['???'] = QTSend
    node[' sommes-nous?'] = QTSend
    node[' est'] = QTGraphMiniFrench['whereis']
    node = QTGraphMiniFrench['thats']
    node[' drole.'] = QTSend
    node[' ce qui vous guerit.'] = QTSend
    node[' les mauvais types.'] = QTSend
    node = QTGraphMiniFrench['iam']
    node[' perdu.'] = QTSend
    node[' recherche'] = QTGraphMiniFrench['lookingfor']
    node[' un chat.'] = QTSend
    node[' un chien.'] = QTSend
    node[' une souris.'] = QTSend
    node[' un cheval.'] = QTSend
    node[' bien.'] = QTSend
    node = QTGraphMiniFrench['like']
    node[' tu.'] = QTSend
    node[' ce jeu.'] = QTSend
    node = QTGraphMiniFrench['are']
    node[' fou.'] = QTSend
    node[' dans'] = QTGraphMiniFrench['headto']
    node = QTGraphMiniFrench['look']
    node[' bon.'] = QTSend
    node[' merveilleux.'] = QTSend
    node[' drole.'] = QTSend
    node[' etrange.'] = QTSend
    node = QTGraphMiniFrench['have']
    node[' les vetements gentils.'] = QTSend
    node[' trop.'] = QTSend
    node = QTGraphMiniFrench['whereis']
    node[' le ToonTown Central?'] = QTSend
    node[" le Donald's Boat?"] = QTSend
    node[' le Melody Land?'] = QTSend
    node[" le Goofy's Place?"] = QTSend
    node[' le Funny Farm?'] = QTSend
    node[' le Dreamland?'] = QTSend
    node[' le Construction Zone?'] = QTSend
    node[' le Brrrgh?'] = QTSend
    node = QTGraphMiniFrench['lookingfor']
    node[" l'Igloo."] = QTSend
    node[' un chariot.'] = QTSend
    node[' mes amis.'] = QTSend
    node = QTGraphMiniFrench['headto']
    node[" l'Igloo."] = QTSend
    node[' un chariot.'] = QTSend
    node[' le ToonTown Central.'] = QTSend
    node[" le Donald's Boat."] = QTSend
    node[' le Melody Land.'] = QTSend
    node[" le Goofy's Place."] = QTSend
    node[' le Funny Farm.'] = QTSend
    node[' le Dreamland.'] = QTSend
    node[' le Construction Zone.'] = QTSend
    node[' le Brrrgh.'] = QTSend
    return QTGraphMiniFrench

lang = base.config.GetString('quicktalker-language', 'concise')
if lang == 'concise':
    QTGraph = setupQTGraphConcise()
elif lang == 'english':
    QTGraph = setupQTGraphEnglish()
elif lang == 'minienglish':
    QTGraph = setupQTGraphMiniEnglish()
elif lang == 'minifrench':
    QTGraph = setupQTGraphMiniFrench()

QTSanityCheck()
if base.config.GetBool('want-quicktalker', 1):
    rebuildMenus()

