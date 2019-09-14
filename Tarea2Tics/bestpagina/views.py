from django.shortcuts import render

# Create your views here.
def blank(request):
    return render(request,'blank.html')

def checkout(request):
    return render(request,'checkout.html')