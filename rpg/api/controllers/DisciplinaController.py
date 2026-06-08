import json
from api.interfaces.controllers.IDisciplinaController import IDisciplinaController

class DisciplinaControllerImpl(IDisciplinaController):
    def __init__(self, disciplina_dao=None):
        self._disciplina_dao = disciplina_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._disciplina_dao.salvar(dados)
        return {"data": {"mensagem": "Disciplina criada"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._disciplina_dao.alterar(dados)
        return {"data": {"mensagem": "Disciplina alterada"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._disciplina_dao.deletar(dados)
        return {"data": {"mensagem": "Disciplina deletada"}, "status": 200}

    def consultar(self, request):
        return {"data": self._disciplina_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        return {"data": self._disciplina_dao.consultarbyId(dados), "status": 200}

    def matricularAluno(self, request):
        dados = json.loads(request.body)
        return {"data": {"mensagem": "Matricula feita"}, "status": 200}