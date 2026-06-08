import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .config import inject

@csrf_exempt
def conta_list(request):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    
    if request.method == 'POST': 
        res = ctrl.salvar(request)
    else: 
        res = ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def conta_detail(request, pk):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    
    if request.method == 'PUT': res = ctrl.alterar(request)
    elif request.method == 'DELETE': res = ctrl.deletar(request)
    else: res = ctrl.consultarbyId(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def conta_login(request):
    dao = inject('IContaDAO')
    ctrl = inject('IContaController', dao_instance=dao)
    res = ctrl.realizarLogin(request)
    return JsonResponse(res['data'], status=res['status'])

@csrf_exempt
def pessoa_list(request):
    dao = inject('IPessoaDAO')
    ctrl = inject('IPessoaController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def aluno_list(request):
    dao = inject('IAlunoDAO')
    ctrl = inject('IAlunoController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def aluno_comprar(request):
    dao_a = inject('IAlunoDAO')
    dao_i = inject('IItemDAO')
    ctrl = inject('IAlunoController', dao_instance=dao_a)
    ctrl._item_dao = dao_i # Injeção extra para o item_dao
    res = ctrl.comprarItem(request)
    return JsonResponse(res['data'], status=res['status'])

@csrf_exempt
def professor_list(request):
    dao = inject('IProfessorDAO')
    ctrl = inject('IProfessorController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def personagem_list(request):
    dao = inject('IPersonagemDAO')
    ctrl = inject('IPersonagemController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def disciplina_list(request):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def disciplina_matricular(request):
    dao = inject('IDisciplinaDAO')
    ctrl = inject('IDisciplinaController', dao_instance=dao)
    res = ctrl.matricularAluno(request)
    return JsonResponse(res['data'], status=res['status'])

@csrf_exempt
def quests_list(request):
    dao = inject('IQuestsDAO')
    ctrl = inject('IQuestsController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)

@csrf_exempt
def quests_responder(request):
    dao = inject('IQuestsDAO')
    ctrl = inject('IQuestsController', dao_instance=dao)
    res = ctrl.responderQuest(request)
    return JsonResponse(res['data'], status=res['status'])

@csrf_exempt
def item_list(request):
    dao = inject('IItemDAO')
    ctrl = inject('IItemController', dao_instance=dao)
    res = ctrl.salvar(request) if request.method == 'POST' else ctrl.consultar(request)
    return JsonResponse(res['data'], status=res['status'], safe=False)