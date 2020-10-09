# Source Generated with Decompyle++
# File: LocalToon.pyo (Python 2.0)

from PandaObject import *
import DistributedToon
import LocalAvatar
import ChatManager
import Toon
import ShtikerBook
import InventoryPage
import MapPage
import OptionsPage
import ShardPage
import QuestPage
import SuitPage
import BuildingPage
import LaffMeter

class LocalToon(DistributedToon.DistributedToon, LocalAvatar.LocalAvatar):
    
    def __init__(self, cr):
        
        try:
            self.LocalToon_initialized
        except:
            self.LocalToon_initialized = 1
            DistributedToon.DistributedToon.__init__(self, cr)
            LocalAvatar.LocalAvatar.__init__(self, cr)
            self.setNeverDisable(1)
            self.nametag.getNametag2d().setContents(Nametag.CSpeech)
            self.setPickable(0)
            Toon.loadDialog()
            self.isIt = 0

        return None

    
    def generate(self):
        self.book = ShtikerBook.ShtikerBook('bookDone')
        self.book.load()
        self.book.hideButton()
        self.optionsPage = OptionsPage.OptionsPage()
        self.optionsPage.load()
        self.book.addPage(self.optionsPage)
        self.shardPage = ShardPage.ShardPage()
        self.shardPage.load()
        self.book.addPage(self.shardPage)
        self.mapPage = MapPage.MapPage()
        self.mapPage.load()
        self.book.addPage(self.mapPage)
        self.invPage = InventoryPage.InventoryPage()
        self.invPage.load()
        self.book.addPage(self.invPage)
        self.book.setPage(self.mapPage)
        self.book.setPos(Vec3(0.0, 0.0, -0.04))
        self.laffMeter = LaffMeter.LaffMeter(self.style, self.hp, self.maxHp)
        self.laffMeter.setAvatar(self)
        self.laffMeter.setScale(0.075)
        self.laffMeter.setPos(-1.2, 0.0, -0.87)
        self.laffMeter.start()
        self.startBlink()
        self.startLookAround()
        self.nametag.manage(toonbase.marginManager)
        return None

    
    def disable(self):
        self.laffMeter.destroy()
        del self.laffMeter
        self.book.unload()
        del self.optionsPage
        del self.shardPage
        del self.mapPage
        del self.invPage
        del self.book
        self.nametag.unmanage(toonbase.marginManager)
        self.ignoreAll()
        DistributedToon.DistributedToon.disable(self)
        return None

    
    def disableBodyCollisions(self):
        pass

    
    def delete(self):
        
        try:
            self.LocalToon_deleted
        except:
            self.LocalToon_deleted = 1
            Toon.unloadDialog()
            DistributedToon.DistributedToon.delete(self)
            LocalAvatar.LocalAvatar.delete(self)

        return None

    
    def displayWhisper(self, chatString):
        LocalAvatar.LocalAvatar.displayWhisper(self, chatString)


