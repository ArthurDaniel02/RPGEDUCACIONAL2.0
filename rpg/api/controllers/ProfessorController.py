import json
from api.interfaces.controllers.IProfessorController import IProfessorController

class ProfessorControllerImpl(IProfessorController):
    def __init__(self, professor_dao=None):
        self._professor_dao = professor_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._professor_dao.salvar(dados)
        return {"data": {"mensagem": "Professor cadastrado com sucesso"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._professor_dao.alterar(dados)
        return {"data": {"mensagem": "Professor atualizado com sucesso"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._professor_dao.deletar(dados)
        return {"data": {"mensagem": "Professor deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._professor_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        res = self._professor_dao.consultarbyId(dados)
        return {"data": res, "status": 200 if res else 404}