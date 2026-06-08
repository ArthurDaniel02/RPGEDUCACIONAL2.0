from api.models import Pessoa as PessoaModel
from api.models_domain.Pessoa import Pessoa

class PessoaDAOMysql:
    def salvar(self, p):
        model = PessoaModel(nome=p.getNome(), cpf="000") # Exemplo
        model.save()
        return True
    def alterar(self, p):
        m = PessoaModel.objects.get(id=p.getIdPessoa())
        m.nome = p.getNome()
        m.save()
        return True
    def deletar(self, p):
        PessoaModel.objects.get(id=p.getIdPessoa()).delete()
        return True
    def consultar(self):
        return list(PessoaModel.objects.all().values())
    def consultarbyId(self, p):
        return PessoaModel.objects.filter(id=p.getIdPessoa()).values().first()