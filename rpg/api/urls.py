from django.urls import path
from . import views

urlpatterns = [
    path('conta/', views.conta_list),
    path('conta/<int:pk>/', views.conta_detail),
    path('conta/login/', views.conta_login),
    path('pessoa/', views.pessoa_list),
    path('aluno/', views.aluno_list),
    path('aluno/comprar/', views.aluno_comprar),
    path('professor/', views.professor_list),
    path('personagem/', views.personagem_list),
    path('disciplina/', views.disciplina_list),
    path('disciplina/matricular/', views.disciplina_matricular),
    path('quests/', views.quests_list),
    path('quests/responder/', views.quests_responder),
    path('item/', views.item_list),
]