import json
from api.interfaces.controllers.IContaController import IContaController

class ContaControllerImpl(IContaController):
    def __init__(self, conta_dao=None):
        self._conta_dao = conta_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._conta_dao.salvar(dados)
        return {"data": {"mensagem": "Conta criada"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._conta_dao.alterar(dados)
        return {"data": {"mensagem": "Conta atualizada"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._conta_dao.deletar(dados)
        return {"data": {"mensagem": "Conta deletada"}, "status": 200}

    def consultar(self, request):
        resultado = self._conta_dao.consultar()
     
        return {"data": resultado if resultado else [], "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        return {"data": self._conta_dao.consultarbyId(dados), "status": 200}

    def realizarLogin(self, request):
        dados = json.loads(request.body)
        return {"data": {"mensagem": "Login OK"}, "status": 200}

    def realizarLogout(self, request):
        return {"data": {"mensagem": "Logout OK"}, "status": 200}

    def recuperarSenha(self, request):
        return {"data": {"mensagem": "Email enviado"}, "status": 200}