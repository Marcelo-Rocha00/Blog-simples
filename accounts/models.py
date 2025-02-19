from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    data_cadastro = models.DateField(auto_now_add=True)
    telefone = models.CharField(max_length=15)
    
    USERNAME_FIELD = 'nome'
    
    def __str__(self):
        return self.nome