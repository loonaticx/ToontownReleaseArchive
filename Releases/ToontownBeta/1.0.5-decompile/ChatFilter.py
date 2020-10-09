# Source Generated with Decompyle++
# File: ChatFilter.pyo (Python 2.0)

import string
import whrandom

class ChatFilter:
    FilterList = ('fuck', 'shit', 'tits', 'cock', 'bastard', 'bitch', 'jerkoff', 'asshole', 'suck my dick', 'cunt', 'penis', 'vagina', 'piss', 'crap', 'breasts')
    ReplaceList = ('#$%*', '$%*@', '%&$@', '!@%#')
    
    def filter(self, message):
        if len(message) > 0:
            newMessage = message[:]
            for word in ChatFilter.FilterList:
                if string.find(string.lower(newMessage), word) >= 0:
                    newMessage = string.replace(newMessage, word, whrandom.choice(ChatFilter.ReplaceList))
                
            
            return newMessage
        else:
            return message

    
    def isValid(self, message):
        for word in ChatFilter.FilterList:
            if string.find(string.lower(message), word) >= 0:
                return 0
            
        
        return 1


