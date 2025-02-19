from django.urls import path
from .views import login_View, logout_view, cadastro

urlpatterns = [
    path('login', login_View, name= 'login'),
    path('', cadastro, name='cadastro'),
    path('logout', logout_view, name='logout')
]
