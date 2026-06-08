import json
from api.interfaces.controllers.IQuestsController import IQuestsController

class QuestsControllerImpl(IQuestsController):
    def __init__(self, quests_dao=None):
        self._quests_dao = quests_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._quests_dao.salvar(dados)
        return {"data": {"mensagem": "Quest criada"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._quests_dao.alterar(dados)
        return {"data": {"mensagem": "Quest alterada"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._quests_dao.deletar(dados)
        return {"data": {"mensagem": "Quest deletada"}, "status": 200}

    def consultar(self, request):
        return {"data": self._quests_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        return {"data": self._quests_dao.consultarbyId(dados), "status": 200}

    def responderQuest(self, request):
        dados = json.loads(request.body)
        return {"data": {"mensagem": "Respondida"}, "status": 200}