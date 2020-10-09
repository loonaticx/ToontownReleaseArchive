# Source Generated with Decompyle++
# File: ChatInputScheme.pyo (Python 2.0)


class ChatInputScheme:
    
    def __init__(self, chatMgr):
        self.chatMgr = chatMgr
        self.canChat = self.chatMgr.chatPermission()

    
    def delete(self):
        del self.chatMgr

    
    def show(self):
        pass

    
    def hide(self):
        pass


