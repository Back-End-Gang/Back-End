from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita, Fuente
from django.core.paginator import Paginator
# Create your views here.

def listar_citas(request):
    citas = Cita.objects.select_related('citas').filter(citas=request.user)
    paginator = Paginator(citas, 5) #5 citas por pagina
    page_number = request.GET.get('page')
    page_onj = paginator.get_page(page_number)
    return render(request, 'listar_citas.html', {'page_onj': page_onj})