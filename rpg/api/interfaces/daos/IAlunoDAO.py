from abc import ABC, abstractmethod

class IAlunoDAO(ABC):
    @abstractmethod
    def salvar(self, obj) -> bool:
        pass

    @abstractmethod
    def alterar(self, obj) -> bool:
        pass

    @abstractmethod
    def deletar(self, obj) -> bool:
        pass

    @abstractmethod
    def consultar(self) -> list:
        pass

    @abstractmethod
    def consultarbyId(self, obj):
        pass
    @abstractmethod
    def consultar_usuario_a(self):
        pass

    @abstractmethod
    def consultar_turma(self):
        pass

    @abstractmethod
    def obter_media_moedas(self, disciplina_id):
        pass