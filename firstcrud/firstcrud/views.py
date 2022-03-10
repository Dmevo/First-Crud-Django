from django.http import HttpResponse
from django.shortcuts import render
from firstcrud import lista_pessoa
from firstcrud.models.pessoa import Pessoa

def form(request):
    if request.method == 'POST':
        nome = request.POST.get('nome', None)
        sobrenome = request.POST.get('sobrenome', None)
        idade = request.POST.get('idade', None)
        cidade = request.POST.get('cidade', None)
        id = len(lista_pessoa) + 1
        pessoa = Pessoa(id, nome, sobrenome, idade, cidade)
        lista_pessoa.append(pessoa)
        return render(request, "form.html", {"lista_pessoa":lista_pessoa})
    else:
        return render(request, "form.html", {"lista_pessoa":lista_pessoa})

def pessoas(request):
    return render(request, "pessoas.html", {"lista_pessoa":lista_pessoa})