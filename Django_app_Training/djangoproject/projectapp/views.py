from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def greet(request):
    return HttpResponse("Welcome To Django Framework")

def beranda(request):
    return render(request, 'beranda.html')

def tentang(request):
    return render(request, 'about.html')

def gallery(request):
    return render(request, 'gallery.html')