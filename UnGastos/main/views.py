from django.shortcuts import render
from .graphs.detailed_nature import DetailedNature


def home(request):
    dn = DetailedNature()
    dn.generate_graphic()

    return render(request, 'index.html')
