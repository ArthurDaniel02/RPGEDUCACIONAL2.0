from api.models import Personagem as PersonagemModel

class PersonagemDAOMysql:
    def salvar(self, p):
        model = PersonagemModel(nome=p.getNome(), classe="Guerreiro")
        model.save()
        return True
    def alterar(self, p):
        m = PersonagemModel.objects.get(id=p.getIdPersonagem())
        m.nome = p.getNome()
        m.save()
        return True
    def deletar(self, p):
        PersonagemModel.objects.get(id=p.getIdPersonagem()).delete()
        return True
    def consultar(self):
        return list(PersonagemModel.objects.all().values())
    def consultarbyId(self, p):
        return PersonagemModel.objects.filter(id=p.getIdPersonagem()).values().first()