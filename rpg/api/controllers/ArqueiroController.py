import json
from api.interfaces.controllers.IArqueiroController import IArqueiroController

class ArqueiroControllerImpl(IArqueiroController):
    def __init__(self, arqueiro_dao=None):
        self._arqueiro_dao = arqueiro_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._arqueiro_dao.salvar(dados)
        return {"data": {"mensagem": "Arqueiro criado"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._arqueiro_dao.alterar(dados)
        return {"data": {"mensagem": "Arqueiro alterado"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._arqueiro_dao.deletar(dados)
        return {"data": {"mensagem": "Arqueiro deletado"}, "status": 200}

    def consultar(self, request):
        return {"data": self._arqueiro_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        return {"data": self._arqueiro_dao.consultarbyId(dados), "status": 200}