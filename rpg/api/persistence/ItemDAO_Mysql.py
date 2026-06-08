from api.models import Item as ItemModel

class ItemDAOMysql:
    def salvar(self, i):
        model = ItemModel(nome=i.getNomeItem(), preco=i.getPrecoMoedas())
        model.save()
        return True
    def alterar(self, i):
        m = ItemModel.objects.get(id=i.getIdItem())
        m.nome = i.getNomeItem()
        m.save()
        return True
    def deletar(self, i):
        ItemModel.objects.get(id=i.getIdItem()).delete()
        return True
    def consultar(self):
        return list(ItemModel.objects.all().values())
    def consultarbyId(self, i):
        return ItemModel.objects.filter(id=i.getIdItem()).values().first()