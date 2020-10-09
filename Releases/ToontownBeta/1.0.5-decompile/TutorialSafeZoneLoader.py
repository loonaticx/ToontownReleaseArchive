# Source Generated with Decompyle++
# File: TutorialSafeZoneLoader.pyo (Python 2.0)

import TTSafeZoneLoader
import TutorialPlayground

class TutorialSafeZoneLoader(TTSafeZoneLoader.TTSafeZoneLoader):
    
    def __init__(self, hood, parentFSM, doneEvent):
        TTSafeZoneLoader.TTSafeZoneLoader.__init__(self, hood, parentFSM, doneEvent)
        self.playgroundClass = TutorialPlayground.TutorialPlayground


