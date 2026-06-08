class Conta:
    def __init__(self):
        self._idConta = None
        self._email = None
        self._senhaHash = None
        self._tipoConta = None
        self._pessoa = None
    
    def add(self): return True
    def setIdConta(self, id): self._idConta = id
    def getIdConta(self): return self._idConta
    def setEmail(self, email): self._email = email
    def getEmail(self): return self._email
    def setSenhaHash(self, s): self._senhaHash = s
    def getSenhaHash(self): return self._senhaHash
    def setTipoConta(self, t): self._tipoConta = t
    def getTipoConta(self): return self._tipoConta
    def login(self, e, s): return True
    def logout(self): pass
    def recuperarSenha(self, e): pass
    def addPessoa(self, p): self._pessoa = p
    def getPessoa(self): return self._pessoa