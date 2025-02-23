from django.urls import path, include
from .views import login_View, logout_view, cadastro, UsuarioViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'usuario', UsuarioViewset )





urlpatterns = [
    path('login', login_View, name= 'login'),
    path('', cadastro, name='cadastro'),
    path('logout', logout_view, name='logout'),
    path('api/', include(router.urls)),
    
]
