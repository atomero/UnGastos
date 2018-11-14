from django.shortcuts import render
from .graphs.detailed_nature import DetailedNature
from .graphs.expenses_per_month import ExpensesMonth


def home(request):
    dn = DetailedNature()
    dn.generate_graphic()

    # em = ExpensesMonth()
    # em.generate_graphic()

    return render(request, 'index.html')

def expanse(request):
    em = ExpensesMonth()
    em.generate_graphic()
    
    return render(request, 'expanse.html')