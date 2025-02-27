from django.urls import path, include
from .views import logado

app_name = 'blog'

urlpatterns = [
    path("teste/", logado , name='Home')
    
]
