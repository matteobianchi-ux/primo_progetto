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
    articolo=get_object_or_404(articolo, pk=pk)
    context={"articolo": articolo}
    return render (request, "articolo_detal.html", context)