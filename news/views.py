from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse

from .models import Articolo, Giornalista

# Create your views here.

#def home(request):
#   return HttpResponse("<h1>Homepage news!</h1>")

#def home(request):
#    a=""
#    g=""
#    for art in Articolo.objects.all():
#        a+=(art.titolo+"<br>")

#    for gio in Giornalista.objects.all():
#        g+=(gio.nome+"<br>")

#    response="Articoli:<br>"+a+"<br>Giornalisti:<br>"+g
#    print(response)

#    return HttpResponse("<h1>"+response+"</1>")

#La principale differenza sta nel fatto che la prima crea una serie di stringhe concatenate mentre la seconda crea delle liste


#def home(request):
#    a=[]
#    g=[]
#    for art in Articolo.objects.all():
#        a.append(art.titolo)

#    for gio in Giornalista.objects.all():
#        g.append(gio.nome)

#    response=str(a)+"<br>"+str(g)
#    print(response)

#    return HttpResponse("<h1>"+response+"</1>")

def home(request):
    articoli=Articolo.objects.all()
    giornalisti=Giornalista.objects.all()
    context={"articoli": articoli, "giornalisti": giornalisti}
    print(context)
    return render(request, "news/homepage.html", context)

#La principale differenza sta nel fatto che il secondo crea delle liste, mentre il terzo utilizza il context

def ArticoloDetailView(request, pk):
    #articolo=Articolo.objects.get(pk=pk)
    articolo = get_object_or_404(Articolo, pk=pk)
    context={"articolo": articolo}
    return render (request, "news/articolo.html", context)

def listaArticoli(request, pk):
    articoli=Articolo.objects.filter(giornalista_id=pk)
    context={
        'articoli':articoli,
    }
    return render(request, 'news/lista_articoli.html', context)

from django.shortcuts import render, get_object_or_404
from .models import Articolo, Giornalista

def listaArticoli(request, pk=None):
    # Controlliamo se è stato passato l'ID del giornalista nell'URL
    if pk is None:
        # Se pk è None, recuperiamo tutti gli articoli presenti nel database
        articoli=Articolo.objects.all()
        titolo_pagina="Tutti gli articoli"
    else:
        # Se pk è stato passato, filtriamo gli articoli selezionando solo quelli
        # in cui il campo 'giornalista' corrisponde alla primary key ricevuta.
        giornalista=get_object_or_404(Giornalista, pk=pk)
        articoli=Articolo.objects.filter(giornalista=giornalista)
        titolo_pagina="Articoli di un giornalista"

    # Dizionario 'context' da passare al template HTML
    context={
        'articoli':articoli,
        'titolo_pagina':titolo_pagina,
    }
    return render(request, 'news/lista_articoli.html', context)