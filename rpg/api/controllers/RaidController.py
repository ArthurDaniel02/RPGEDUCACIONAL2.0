import json
from api.interfaces.controllers.IRaidController import IRaidController

class RaidControllerImpl(IRaidController):
    def __init__(self, raid_dao=None):
        self._raid_dao = raid_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._raid_dao.salvar(dados)
        return {"data": {"mensagem": "Raid criada com sucesso"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._raid_dao.alterar(dados)
        return {"data": {"mensagem": "Raid atualizada com sucesso"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._raid_dao.deletar(dados)
        return {"data": {"mensagem": "Raid deletada com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._raid_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        res = self._raid_dao.consultarbyId(dados)
        return {"data": res, "status": 200 if res else 404}