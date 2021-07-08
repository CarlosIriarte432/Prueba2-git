from django.urls import path, include
from apps.Formulario import views
from .views import ReservasList, ReservasCreate, ReservasUpdate, ReservasDelete
from rest_framework.urlpatterns import format_suffix_patterns
from apps.Formulario import views

urlpatterns = [
    path('listar_reserva/', ReservasList.as_view(), name="reservas_list"),
    path('agregar_reserva/', ReservasCreate.as_view(), name="reservas_form"),
    path('editar_reserva/<int:pk>', ReservasUpdate.as_view(), name="reservas_update"),
    path('borrar_reserva/<int:pk>', ReservasDelete.as_view(), name="reservas_borrar"),

]

urlpatterns += [
    path('api/', views.API_objects.as_view()),
    path('api/<int:pk>/', views.API_objects_details.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
