from api.models import Disciplina as DisciplinaModel

class DisciplinaDAOMysql:
    def salvar(self, d):
        model = DisciplinaModel(nome=d.getNome(), codigo="ABC")
        model.save()
        return True
    def alterar(self, d):
        m = DisciplinaModel.objects.get(id=d.getIdDisciplina())
        m.nome = d.getNome()
        m.save()
        return True
    def deletar(self, d):
        DisciplinaModel.objects.get(id=d.getIdDisciplina()).delete()
        return True
    def consultar(self):
        return list(DisciplinaModel.objects.all().values())
    def consultarbyId(self, d):
        return DisciplinaModel.objects.filter(id=d.getIdDisciplina()).values().first()