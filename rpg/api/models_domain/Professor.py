class Professor:
    def __init__(self):
        self._idProfessor = None
        self._disciplinas = []
    
    def add(self): return True
    def setIdProfessor(self, id): self._idProfessor = id
    def getIdProfessor(self): return self._idProfessor
    def criarDisciplina(self, n, d): return None
    def criarQuest(self, d, m): return None
    def editarQuest(self, idQ): pass
    def criarRaid(self, n, hp): return None
    def addDisciplina(self, d): self._disciplinas.append(d)
    def getDisciplinas(self): return self._disciplinas