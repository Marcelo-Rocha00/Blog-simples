from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer): #fazendo a conversão dos dados do usuário, para um arquivo json ou XML
    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'email', 'data_cadastro', 'telefone' ]