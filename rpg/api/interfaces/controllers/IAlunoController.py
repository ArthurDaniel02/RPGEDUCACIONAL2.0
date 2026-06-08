from abc import ABC, abstractmethod

class IAlunoController(ABC):
    @abstractmethod
    def salvar(self, req, res):
        pass

    @abstractmethod
    def alterar(self, req, res):
        pass

    @abstractmethod
    def deletar(self, req, res):
        pass

    @abstractmethod
    def consultar(self, req, res):
        pass

    @abstractmethod
    def consultarbyId(self, req, res):
        pass

    @abstractmethod
    def comprarItem(self, req, res):
        pass