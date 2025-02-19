from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput, max_length=128, required=True,label='Senha')
    confirmar_senha = forms.CharField(widget=forms.PasswordInput,max_length=128,required=True,label='Confirmar Senha')
    class Meta:
        model = Usuario
        fields = ['nome','email', 'telefone',]
        
        
        def clean(self):
            cleaned_data = super().clean()
            senha = cleaned_data.get('senha')
            confirmar_senha = cleaned_data.get('confirmar_senha')

            if senha != confirmar_senha:
                raise forms.ValidationError('As senhas não coincidem.')
            
            return cleaned_data
