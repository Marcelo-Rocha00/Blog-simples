
from django.urls import path, include
from .views import login_View, logout_view, SignUp
from . import views








urlpatterns = [
    path('login', login_View, name= 'login'),
    path('', SignUp.as_view(), name='cadastro'),
    path('logout', logout_view, name='logout'),
    
]