from django.shortcuts import render
from .models import Mahsulotlar


def home(request):
    bus = Mahsulotlar.objects.filter(turi = 'avtobuslar')
    larg = Mahsulotlar.objects.filter(turi = 'yuk_mashinalari')
    specal = Mahsulotlar.objects.filter(turi = 'maxsus_mashinalari')
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
    bus = Mahsulotlar.objects.filter(turi = 'avtobuslar')
    larg = Mahsulotlar.objects.filter(turi = 'yuk_mashinalari')
    specal = Mahsulotlar.objects.filter(turi = 'maxsus_mashinalari')
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