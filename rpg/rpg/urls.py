from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
def api_root(request):
    return JsonResponse({"message": "Bem-vindo à API RPG!", "rotas": "/api/conta/, /api/aluno/, etc."})
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/', include('api.urls')),
]