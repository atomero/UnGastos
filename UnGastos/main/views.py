from django.shortcuts import render
from .graphs.detailed_nature import DetailedNature
from .graphs.expenses_per_month import ExpensesMonth
from .graphs.resource_source import ResourceSource
from .graphs.total_vs_actual_indicator import TotalVsActual
from .graphs.creditors import CreditorsInfo


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


def indicators(request):
    ta = TotalVsActual()
    ta.generate_graphic()

    value = "1.36"

    return render(request, 'indicators.html', {'value': value})


def creditors(request):
    creditorsInfo = CreditorsInfo()
    creditorsInfo.generate_data()

    return render(request, 'creditors.html', {'creditors': creditorsInfo.creditors})
