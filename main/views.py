from django.shortcuts import render, get_object_or_404

from main.forms import AlunoForm
from .models import Aluno

def alunoView(request):
    alunos = Aluno.objects.all()
    return render(request, 'main/list.html', {'alunos':alunos})

def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk = id)
    return render(request, 'main/list.html', {'aluno':aluno})

def exemplo(request):

    if request.method == 'POST':
        name = request.POST.get('nome', None)
        email = request.POST.get('email', None)
        telefone = request.POST.get('telefone', None)

        print(name, email, telefone)
    return render(request, 'main/indexx.html')

def newAluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            return redirect('/')
    else:
        form = AlunoForm()
    return render(request, 'main/add_aluno.html', {'form':form})
