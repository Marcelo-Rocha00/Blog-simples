from django.db import models
from django.contrib.auth.models import User
from .utils import resize_image

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nome_categoria

class Tag(models.Model):
    nome = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.nome

class Postagem(models.Model):
    STATUS_CHOICE_POSTAGEM = (
        ("R"," Rascunho"),
        ("P"," Postado "))
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    conteudo = models.TextField()
    imagens = models.ImageField(blank=True, upload_to='imagens/')
    categorias = models.ManyToManyField(Categoria, related_name="postagens")
    tags = models.ManyToManyField(Tag, blank=True)
    status_postagem = models.CharField(max_length=1, choices=STATUS_CHOICE_POSTAGEM)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_publicação = models.DateTimeField(auto_now=True)
    
    
    def save(self, *args, **kwargs):
        if self.imagens:
            self.imagens = resize_image(self.imagens)  # Redimensiona a imagem antes de salvar
        super().save(*args, **kwargs)   
    
    def __str__(self):
        return self.titulo
    

class Comentario(models.Model):
    STATUS_CHOICE_COMENTARIO =(
        ("PE", "Pendente"),
        ("AP", "Aprovado"),
        ("RE", "Rejeitado")
    )
    
    post = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    status = models.CharField(max_length=2, choices=STATUS_CHOICE_COMENTARIO)
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.autor