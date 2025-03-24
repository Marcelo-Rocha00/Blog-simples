from django import forms
from .models import Postagem, Categoria

class PostagemForm(forms.Modelform):
    novas_categorias = forms.CharField(
        max_length=200, required=False,
        help_text="Separe novas categorias com vírgula. "
    )
    
    class Meta:
        model = Postagem
        fields = '__all__'
        widgets = {
            'categorias': forms.CheckboxSelectMultiple(), 
        }
        
    def save(self, commit=True):
        postagem = super().save(commit=False)
        
        if commit:
            postagem.save()
            self.save_m2m() #necessário para ManyToManyField
            
            novas_categorias = self.cleaned_data.get("novas_categorias")
            if novas_categorias:
                nomes = [nome.strip() for nome in novas_categorias.split(",")]
                for nome in nomes:
                    categoria, _ = Categoria.objects.get_or_create(nome=nome)
                    postagem.categorias.add(categoria) #adiciona a postagem
        return postagem
            