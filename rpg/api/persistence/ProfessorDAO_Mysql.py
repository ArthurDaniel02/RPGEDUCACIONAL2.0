from api.models import Professor as ProfessorModel

class ProfessorDAOMysql:
    def salvar(self, p):
        model = ProfessorModel(titulacao="Mestre")
        model.save()
        return True
    def alterar(self, p):
        m = ProfessorModel.objects.get(id=p.getIdProfessor())
        m.save()
        return True
    def deletar(self, p):
        ProfessorModel.objects.get(id=p.getIdProfessor()).delete()
        return True
    def consultar(self):
        return list(ProfessorModel.objects.all().values())
    def consultarbyId(self, p):
        return ProfessorModel.objects.filter(id=p.getIdProfessor()).values().first()