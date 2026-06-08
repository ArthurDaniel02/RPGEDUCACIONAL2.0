from api.models import Conta as ContaModel
from api.models_domain.Conta import Conta

class ContaDAOMysql:
    def salvar(self, conta_dom):
        model = ContaModel(login=conta_dom.getEmail(), senha=conta_dom.getSenhaHash(), email=conta_dom.getEmail())
        model.save()
        return True

    def alterar(self, conta_dom):
        model = ContaModel.objects.get(login=conta_dom.getEmail())
        model.senha = conta_dom.getSenhaHash()
        model.save()
        return True

    def deletar(self, conta_dom):
        ContaModel.objects.get(login=conta_dom.getEmail()).delete()
        return True

    def consultar(self):
        return list(ContaModel.objects.all().values())

    def consultarbyId(self, conta_dom):
        try:
            return ContaModel.objects.filter(id=conta_dom.getIdConta()).values().first()
        except: return None