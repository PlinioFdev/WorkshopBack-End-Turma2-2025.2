from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo ao meu app1</h1>")
