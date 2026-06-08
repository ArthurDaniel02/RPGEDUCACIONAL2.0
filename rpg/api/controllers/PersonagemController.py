import json
from api.interfaces.controllers.IPersonagemController import IPersonagemController

class PersonagemControllerImpl(IPersonagemController):
    def __init__(self, personagem_dao=None):
        self._personagem_dao = personagem_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._personagem_dao.salvar(dados)
        return {"data": {"mensagem": "Personagem criado com sucesso"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._personagem_dao.alterar(dados)
        return {"data": {"mensagem": "Personagem atualizado com sucesso"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._personagem_dao.deletar(dados)
        return {"data": {"mensagem": "Personagem deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._personagem_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        res = self._personagem_dao.consultarbyId(dados)
        return {"data": res, "status": 200 if res else 404}