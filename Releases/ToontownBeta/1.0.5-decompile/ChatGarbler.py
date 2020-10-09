# Source Generated with Decompyle++
# File: ChatGarbler.pyo (Python 2.0)

import string
import whrandom

class ChatGarbler:
    animalSounds = {
        'dog': [
            'woof',
            'arf'],
        'cat': [
            'meow'],
        'mouse': [
            'squeak'],
        'horse': [
            'neigh',
            'brrr'],
        'rabbit': [
            'eek',
            'eep'],
        'fowl': [
            'quack',
            'quackity'],
        'default': [
            'blah'] }
    
    def garble(self, toon, message):
        newMessage = ''
        animalType = toon.getStyle().getType()
        if ChatGarbler.animalSounds.has_key(animalType):
            wordlist = ChatGarbler.animalSounds[animalType]
        else:
            wordlist = ChatGarbler.animalSounds['default']
        numWords = whrandom.randint(1, 7)
        for i in range(1, numWords + 1):
            wordIndex = whrandom.randint(0, len(wordlist) - 1)
            newMessage = newMessage + wordlist[wordIndex]
            if i < numWords:
                newMessage = newMessage + ' '
            
        
        return newMessage


