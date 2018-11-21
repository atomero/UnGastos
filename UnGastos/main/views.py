from django.shortcuts import render
from .graphs.detailed_nature import DetailedNature
from .graphs.expenses_per_month import ExpensesMonth
from .graphs.resource_source import ResourceSource


def home(request):
    dn = DetailedNature()
    dn.generate_graphic()

    return render(request, 'index.html')


def expanse(request):
    em = ExpensesMonth()
    em.generate_graphic()

    return render(request, 'expanse.html')


def resource_source(request):
    rs = ResourceSource()
    rs.generate_graphic()

    return render(request, 'resource_source.html')
