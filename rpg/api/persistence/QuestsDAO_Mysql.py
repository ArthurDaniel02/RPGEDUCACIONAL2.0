from api.models import Quests as QuestsModel

class QuestsDAOMysql:
    def salvar(self, q):
        model = QuestsModel(titulo=q.getDescricao(), resposta_correta="A")
        model.save()
        return True
    def alterar(self, q):
        m = QuestsModel.objects.get(id=q.getIdQuest())
        m.descricao = q.getDescricao()
        m.save()
        return True
    def deletar(self, q):
        QuestsModel.objects.get(id=q.getIdQuest()).delete()
        return True
    def consultar(self):
        return list(QuestsModel.objects.all().values())
    def consultarbyId(self, q):
        return QuestsModel.objects.filter(id=q.getIdQuest()).values().first()