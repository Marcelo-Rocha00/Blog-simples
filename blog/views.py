from django.shortcuts import render
from .models import Postagem


def pagina_princioal(request):
    posts = Postagem.objects.all()
    
    return render(request, 'blog/redirecionamento.html', {'posts':posts})