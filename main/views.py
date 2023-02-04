from django.shortcuts import render, get_object_or_404
from .models import Aluno

def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos':alunos})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk = id)
    return render(request, 'main/list.html', {'aluno':aluno})
