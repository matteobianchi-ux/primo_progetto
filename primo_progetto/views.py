from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "prima_app/homepage.html")

def welcome(request):
    return render(request, "welcome.html")

def lista(request):
    return render(request, "lista.html")

def chi_siamo(request):
    return render(request, "chi_siamo.html")

def variabili(request):
    context={ 'var1': '10', 'var2': 'ciao', 'var3': '123 hello world'}
    return render(request, "variabili.html", context)