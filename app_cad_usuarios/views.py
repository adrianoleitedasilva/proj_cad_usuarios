from django.shortcuts import render
from .models import Usuario

def home(request):
   return render(request, 'usuarios/home.html')

def usuarios(request):
    # Salvando os dados da tela no BD
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.save()

    # Exibindo as informações do BD na nova tela
    # Convertendo as informações em um Dicionário
    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    # Retornando
    return render(request, 'usuarios/usuarios.html', usuarios)