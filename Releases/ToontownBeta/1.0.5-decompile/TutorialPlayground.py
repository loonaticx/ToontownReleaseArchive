# Source Generated with Decompyle++
# File: TutorialPlayground.pyo (Python 2.0)

import TTPlayground

class TutorialPlayground(TTPlayground.TTPlayground):
    
    def handleEnterTunnel(self, requestStatus, collEntry):
        requestStatus['tutorial'] = 1
        self.fsm.request('TFA', [
            requestStatus])
        return None

    
    def enterTeleportIn(self, requestStatus):
        TTPlayground.TTPlayground.enterTeleportIn(self, requestStatus)
        messenger.send('toonEntersTutorial')
        return None


