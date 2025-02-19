from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login as auth_login, logout
from django.contrib import messages
from .forms import UsuarioForm
# Create your views here.

def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        
        if form.is_valid():
            # Aqui o form já é válido, então podemos criar e salvar o cliente
            cliente = form.save(commit=False)  # Não salva imediatamente, ainda podemos manipular
            cliente.set_password(form.cleaned_data['senha'])  # Define a senha criptografada
            cliente.save()  # Agora sim, salva o cliente no banco de dados
            
            return redirect('login')  # Redireciona para uma página de listagem de clientes
            # Cria a conta associada ao cliente
        
        else:
            print('Formulário inválido:', form.errors)  # Exibe erros para debug

    else:
        form = UsuarioForm()  # Cria um formulário vazio para GET

    return render(request, 'accounts/cadastro.html', {'form': form})

def login_View(request):
    if request.method == 'POST':
        usuario = request.POST['nome']
        password = request.POST['password']
        print(usuario)
        user = authenticate(request, usuario=usuario, password=password)
        if user is not None:
            
            auth_login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts/login.html', {'nome':user})
    
    else:
        return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')