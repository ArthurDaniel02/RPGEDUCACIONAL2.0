class Raid:
    def __init__(self):
        self._idRaid = None
        self._nomeBoss = None
    
    def add(self): return True
    def setIdRaid(self, id): self._idRaid = id
    def getIdRaid(self): return self._idRaid
    def setNomeBoss(self, n): self._nomeBoss = n
    def getNomeBoss(self): return self._nomeBoss