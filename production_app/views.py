from django.shortcuts import render
from .models import ProductionPerPhase
# Create your views here.

def production_list(request):
    productionperphase=ProductionPerPhase.objects.all()
    return render(request, 'ProductionPerPhase.html', {'productionperphase': productionperphase})

