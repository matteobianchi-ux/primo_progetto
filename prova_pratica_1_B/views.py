from django.shortcuts import render
import random

# Create your views here.

def pari(request):
    return render(request, "prova_pratica_1_b/pari.html")

def massimo(request):
    context={ 'var1': random.randint(1,20), 'var2': random.randint(1,20), 'var3': random.randint(1,20)}
    return render(request, "prova_pratica_1_B/massimo.html", context)

def studenti(request):
    context={ 'studente1:' 'True', 'studente1:' 'False', 'studente1:' 'True' }
    return render(request, "prova_pratica_1_B/studenti.html")

def index(request):
    voti=[]
    for i in range(30):
        voti.append(random.randint(1,20))
    context={voti}
    return render(request, "prova_pratica_1_B/index.html", context)