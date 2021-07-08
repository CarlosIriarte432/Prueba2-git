from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

    # las importaciones para la API 
    
from rest_framework import generics
from .serializers import ReservasSerializer
from .models import Reservas
from .forms import ReservasForm
# Create your views here.

class ReservasList (ListView):
    model = Reservas
    template_name = 'Formulario/listar_reserva.html'

class ReservasCreate (CreateView):
    model = Reservas
    form_class = ReservasForm
    template_name = 'Formulario/agregar_reserva.html'
    success_url = reverse_lazy('reservas_list')
    
class ReservasUpdate(UpdateView):
    model = Reservas
    form_class = ReservasForm
    template_name = 'Formulario/editar_reserva.html'
    success_url = reverse_lazy('reservas_list')
    
class ReservasDelete(DeleteView):
    model = Reservas
    template_name = 'Formulario/borrar_reserva.html'
    success_url = reverse_lazy('reservas_list')
    

class API_objects(generics.ListCreateAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    
class API_objects_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reservas.objects.all()
    serializer_class = ReservasSerializer
    
def agregar_cliente(request):
    if request.method == "POST":
        form = ReservasForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/formulario")
    else:
        form = ReservasForm()
        return render(request, "Registro/formulario.html", {'form': form})    
