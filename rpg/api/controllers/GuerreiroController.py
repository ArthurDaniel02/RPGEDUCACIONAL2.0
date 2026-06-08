import json
from api.interfaces.controllers.IGuerreiroController import IGuerreiroController

class GuerreiroControllerImpl(IGuerreiroController):
    def __init__(self, guerreiro_dao=None):
        self.guerreiro_dao = guerreiro_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self.guerreiro_dao.salvar(dados)
        return {"data": {"mensagem": "Guerreiro criado"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self.guerreiro_dao.alterar(dados)
        return {"data": {"mensagem": "Guerreiro alterado"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self.guerreiro_dao.deletar(dados)
        return {"data": {"mensagem": "Guerreiro deletado"}, "status": 200}

    def consultar(self, request):
        return {"data": self.guerreiro_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        return {"data": self.guerreiro_dao.consultarbyId(dados), "status": 200}