from django.shortcuts import render
from .models import Mahsulotlar


def home(request):
    bus = Mahsulotlar.objects.filter(turi__translations__nomi='Avtobuslar')
    larg = Mahsulotlar.objects.filter(turi__translations__nomi='Yuk mashinalari')
    specal = Mahsulotlar.objects.filter(turi__translations__nomi='Maxsus mashinalari')
    all = Mahsulotlar.objects.all()
    context = {
        'bus': bus,
        'larg': larg,
        'specal': specal,
        'all': all
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def custom(request):
    bus = Mahsulotlar.objects.filter(turi__translations__nomi='Avtobuslar')
    larg = Mahsulotlar.objects.filter(turi__translations__nomi='Yuk mashinalari')
    specal = Mahsulotlar.objects.filter(turi__translations__nomi='Maxsus mashinalari')
    all = Mahsulotlar.objects.all()
    context = {
        'bus': bus,
        'larg': larg,
        'specal': specal,
        'all': all
    }
    return render(request, 'custom.html', context)


def part(request):
    return render(request, 'part.html')

def dmax(request):
    return render(request, 'max.html')