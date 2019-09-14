from django.shortcuts import render

# Create your views here.
def productos(request):
    return render(request, 'productos.html')

def agregar(request):
    return render(request, 'agregar.html')

def signup(request):
	return render(request,'signup.html')

def contact(request):
	return render(request,'contact.html')

def enviado(request):
	return render(request,'enviado.html')

def ficha(request):
	return render(request,'ficha.html')

