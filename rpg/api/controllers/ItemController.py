import json
from api.interfaces.controllers.IItemController import IItemController

class ItemControllerImpl(IItemController):
    def __init__(self, item_dao=None):
        self._item_dao = item_dao

    def salvar(self, request):
        dados = json.loads(request.body)
        self._item_dao.salvar(dados)
        return {"data": {"mensagem": "Item criado com sucesso"}, "status": 201}

    def alterar(self, request):
        dados = json.loads(request.body)
        self._item_dao.alterar(dados)
        return {"data": {"mensagem": "Item atualizado com sucesso"}, "status": 200}

    def deletar(self, request):
        dados = json.loads(request.body)
        self._item_dao.deletar(dados)
        return {"data": {"mensagem": "Item deletado com sucesso"}, "status": 200}

    def consultar(self, request):
        return {"data": self._item_dao.consultar(), "status": 200}

    def consultarbyId(self, request):
        dados = json.loads(request.body)
        res = self._item_dao.consultarbyId(dados)
        return {"data": res, "status": 200 if res else 404}