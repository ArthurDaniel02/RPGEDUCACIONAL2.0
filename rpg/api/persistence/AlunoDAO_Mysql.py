from api.models import Aluno as AlunoModel
from django.db import connection
class AlunoDAOMysql:
    def salvar(self, a):
        model = AlunoModel(
            nome=a.getNome(), 
            cpf=a.getCpf(), 
            conta_id=a.getConta(), 
            moedas=a.getMoedas()
        )
        model.save()
        return True

    def alterar(self, a):
        m = AlunoModel.objects.get(id=a.getIdPessoa()) 
        from api.models import Item as ItemModel
        if a.getNome() is not None: m.nome = a.getNome()
        if a.getCpf() is not None: m.cpf = a.getCpf()
        if a.getConta() is not None: m.conta_id = a.getConta()
        if a.getMoedas() is not None: m.moedas = a.getMoedas()
        
        m.save()
        if hasattr(a, 'getItens') and a.getItens():
            for item_dominio in a.getItens():
                try:
                    item_bd = ItemModel.objects.get(id=item_dominio.getIdItem())
                    m.itens.add(item_bd) 
                except ItemModel.DoesNotExist:
                    continue
        return True

    def deletar(self, a):
        AlunoModel.objects.filter(id=a.getIdPessoa()).delete()
        return True

    def consultar(self):
        return list(AlunoModel.objects.all().values())

    def consultarbyId(self, a):
        try:
            return AlunoModel.objects.filter(id=a.getIdPessoa()).values().first()
        except:
            return None
        
    def consultarItens(self, a): 
        m = AlunoModel.objects.get(id=a.getIdPessoa())
   
        return list(m.itens.all().values())
    def consultar_usuario_a(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, pessoa_ptr_id, nome, classe, nivel, moedas FROM UsuarioA")
            colunas = [col[0] for col in cursor.description]
            return [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

    def consultar_turma(self):
        with connection.cursor() as cursor:
            cursor.execute('SELECT id, pessoa_ptr_id, Disciplina, nome, moedas FROM Turma')
            colunas = [col[0] for col in cursor.description]
            return [dict(zip(colunas, linha)) for linha in cursor.fetchall()]

    def obter_media_moedas(self, disciplina_id):
        with connection.cursor() as cursor:
            cursor.execute("SELECT media_moeda(%s)", [disciplina_id])
            resultado = cursor.fetchone()
            return float(resultado[0]) if resultado and resultado[0] is not None else 0.0
        