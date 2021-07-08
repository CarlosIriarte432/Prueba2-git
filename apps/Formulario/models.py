from django.db import models

# Create your models here.

HOTEL = (
    ('Hotel', 'Hotel'),
    ('Airbnb', 'AirBnB'),
)

TRANSPORTE = (
    ('Transporte_Compartido', 'Transporte_Compartido'),
    ('Alquiler_de_Vehiculos', 'Alquiler_de_Vehiculos'),
)

TOUR = (
    ('Tour_a_Punta Cana', 'Tour_a_Punta Cana'),
    ('Tour_a_Macchu Picchu', 'Tour_a_Macchu Picchu'),
    ('Tour_a_Paris', 'Tour_a_Paris'),
    ('Tour_a_Londres', 'Tour_a_Londres'),
    ('Tour_a_Cancun', 'Tour_a_Cancun'),
    ('Tour_a_Isla de Pascua', 'Tour_a_Isla de Pascua'),
)


class Reservas (models.Model):
    nombre = models.CharField(max_length=30)
    rut = models.CharField(max_length=20)
    correo = models.EmailField(max_length=70,blank=True, null= True, unique= True)   
    transporte = models.CharField(max_length=50, choices=TRANSPORTE)     
    hotel = models.CharField(max_length=50, choices=HOTEL)
    tour = models.CharField(max_length=50, choices=TOUR)
    fecha = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre


