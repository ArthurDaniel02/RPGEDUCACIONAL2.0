from abc import ABC, abstractmethod

class IArqueiroController(ABC):
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