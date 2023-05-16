from django.urls import path
from recipes.views import contato, teste, home

urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('teste/', teste)
]
