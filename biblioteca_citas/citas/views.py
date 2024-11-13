from django.shortcuts import render, redirect, get_object_or_404
from .models import Cita, Fuente
from django.core.paginator import Paginator
# Create your views here.

# Vista Listar Citas
def listar_citas(request):
    citas = Cita.objects.select_related('citas').filter(citas=request.user)
    paginator = Paginator(citas, 5) #5 citas por pagina
    page_number = request.GET.get('page')
    page_onj = paginator.get_page(page_number)
    return render(request, 'listar_citas.html', {'page_onj': page_onj})

# Vista Creación de tarea
def crear_cita(request):
    if request.method == 'POST':
        texto = request.POST.get('texto') #Obtenemos el valor del formulario
        autor = request.POST.get('autor')
        fecha = request.POST.get('fecha')
        fuente = request.POST.get('fuente')

    #Creación de tarea en base de datos
        Cita.objects.create(texto=texto, autor=autor, fecha=fecha, fuente=fuente)
        return redirect('listar_citas') #Redirige a la lista de tareas después de crearla
    return render(request, 'agregarcita.html') #Mostrar el formulario en caso de GET
