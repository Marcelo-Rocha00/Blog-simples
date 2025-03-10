from django.urls import path, include
from .views import pagina_princioal
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [
    path("teste/", pagina_princioal , name='Home')
    
] 


