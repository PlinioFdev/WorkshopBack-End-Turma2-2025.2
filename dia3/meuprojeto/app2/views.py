from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Olá, este é o APP2!</h1>")
