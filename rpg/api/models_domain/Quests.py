class Quests:
    def __init__(self):
        self._idQuest = None
        self._descricao = None
        self._disciplina = None
        self._alunos = []
    
    def add(self): return True
    def setIdQuest(self, id): self._idQuest = id
    def getIdQuest(self): return self._idQuest
    def setDescricao(self, d): self._descricao = d
    def getDescricao(self): return self._descricao
    def addDisciplina(self, d): self._disciplina = d
    def getDisciplina(self): return self._disciplina
    def addAluno(self, a): self._alunos.append(a)
    def getAlunos(self): return self._alunos