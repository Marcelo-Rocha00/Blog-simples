from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login , logout
from django.contrib import messages
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User
from django.views import  View
from django.urls import reverse_lazy
from blog.urls import logado
# Create your views here.


class SignUp(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/cadastro.html', {'form': form})
        
    def post(self, request):
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            print("Formulário válido, salvando usuário...")
            user = form.save()
            messages.success(request, 'Registro realizado com sucesso!', extra_tags='cadastro')
            return redirect(reverse_lazy('login'))
        else:
            print("Erros no formulário:", form.errors)  # <-- Mostra os erros no terminal
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}", extra_tags='cadastro')

        return render(request, 'accounts/cadastro.html', {'form': form})


def login_View(request):
    if request.method == 'POST':
        username = request.POST['username']
        print("nome:",username)
        password = request.POST['password']
        print("senha:",password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            
            login(request, user)
            
            return redirect('blog:Home')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts/login.html', {'nome':user})
    
    else:
        return render(request, 'accounts/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')