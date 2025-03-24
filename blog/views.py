from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Postagem, Categoria, Tag
from .forms import PostagemForm 

def pagina_princioal(request):
    posts = Postagem.objects.all()
    return render(request, 'blog/redirecionamento.html', {'posts':posts})


def criar_postagem(request):
    if request.method == "POST":
        autor_id = request.POST.get('autor')
        titulo = request.POST.get('titulo')
        conteudo = request.POST.get('conteudo')
        imagem = request.FILES.get('imagens')
        categoria_ids = request.POST.getlist('Categorias')
        tag_ids  = request.method.POST.getlist('tags')
        status_postagem = request.POST.get('status_postagem')
        if titulo:
            autor = User.objects.get(id=autor_id)
            postagem = Postagem.objects.create(
                autor = autor,
                titulo = titulo,
                conteudo = conteudo,
                imagem = imagem,
                status = status_postagem,
            )  
            # Adicionando categorias (ManyToMany)
            categorias = Categoria.objects.filter(id__in=categoria_ids)
            postagem.categorias.set(categorias)
            
            #adicionando tags (ManyToMany)
            tags = Tag.objects.filter(id__in=tag_ids)
            postagem.tags.set(tags)
            
            postagem.save()
            
            
            
            return redirect('home')
        # Caso contrário, só renderiza o formulário para criar a postagem
    autores = User.objects.all()
    categorias = Categoria.objects.all()
    tags = Tag.objects.all()
    
    return render(request, "blog/add_postagem.html", {
        'autores': autores,
        'categorias': categorias,
        'tags': tags
    })