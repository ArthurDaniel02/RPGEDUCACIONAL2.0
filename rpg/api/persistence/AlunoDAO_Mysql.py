from api.models import Aluno as AlunoModel

class AlunoDAOMysql:
    def salvar(self, a):
        model = AlunoModel(matricula=a.getIdAluno(), moedas=a.getMoedas())
        model.save()
        return True
    def alterar(self, a):
        m = AlunoModel.objects.get(id=a.getIdAluno())
        m.moedas = a.getMoedas()
        m.save()
        return True
    def deletar(self, a):
        AlunoModel.objects.get(id=a.getIdAluno()).delete()
        return True
    def consultar(self):
        return list(AlunoModel.objects.all().values())
    def consultarbyId(self, a):
        return AlunoModel.objects.filter(id=a.getIdAluno()).values().first()