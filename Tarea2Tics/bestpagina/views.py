from django.shortcuts import render

# Create your views here.
def blank(request):
    return render(request,'blank.html')

def checkout(request):
    return render(request,'checkout.html')

def signup(request):
	return render(request,'signup.html')

def contact(request):
	return render(request,'contact.html')

def enviado(request):
	return render(request,'enviado.html')

