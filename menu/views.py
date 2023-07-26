from django.shortcuts import render
from menu.models import Menu

# Create your views here.

def menu_views(request):
    return render(request,'menu/paginas/menu.html')

def views_busca(request):

    imagens = Menu.objects.all()
    print(request)

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            imagens = imagens.filter(nome__icontains=nome)

    return render(request, 'menu/paginas/busca.html', context ={'imagens' : imagens})
