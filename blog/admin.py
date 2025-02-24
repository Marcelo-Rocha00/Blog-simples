from django.contrib import admin
from blog.models import Postagem,Comentario,Tag,Categoria

admin.site.register(Postagem)
admin.site.register(Comentario)
admin.site.register(Tag)
admin.site.register(Categoria)