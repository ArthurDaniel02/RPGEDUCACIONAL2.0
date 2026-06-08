import json
from api.interfaces.controllers.IAlunoController import IAlunoController

class AlunoControllerImpl(IAlunoController):
    def __init__(self, aluno_dao=None, item_dao=None):
        self._aluno_dao = aluno_dao
        self._item_dao = item_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        sucesso = self._aluno_dao.salvar(dados)
        return {"data": {"mensagem": "Aluno cadastrado"}, "status": 201 if sucesso else 400}

    def alterar(self, request):
        dados = json.loads(request.body)
        sucesso = self._aluno_dao.alterar(dados)
        return {"data": {"mensagem": "Aluno atualizado"}, "status": 200 if sucesso else 400}

    def deletar(self, request):
        dados = json.loads(request.body)
        sucesso = self._aluno_dao.deletar(dados)
        return {"data": {"mensagem": "Aluno deletado"}, "status": 200 if sucesso else 400}

    def consultar(self, request):
        return {"data": self._aluno_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        res = self._aluno_dao.consultarbyId(dados)
        return {"data": res, "status": 200 if res else 404}

    def comprarItem(self, request):
        dados = json.loads(request.body)
        aluno = self._aluno_dao.consultarbyId({"id": dados.get("aluno_id")})
        item = self._item_dao.consultarbyId({"id": dados.get("item_id")})
        if aluno and item and aluno.get("moedas") >= item.get("preco"):
            return {"data": {"mensagem": "Compra realizada"}, "status": 200}
        return {"data": {"erro": "Saldo insuficiente"}, "status": 400}