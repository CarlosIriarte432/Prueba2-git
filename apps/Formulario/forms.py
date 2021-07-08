from django import forms
from .models import Reservas

class ReservasForm(forms.ModelForm):
    class Meta:
        model = Reservas
        fields = ['nombre', 'rut', 'correo', 'transporte', 'hotel', 'tour', 'fecha']

        labels = {
            'nombre': 'Nombre',
            'rut': 'Rut',
            'correo': 'Email',
            'transporte': 'Vehiculo',
            'hotel': 'Hotel',
            'tour': 'Tour',
            'fecha': 'Fecha',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control'}),
            'transporte': forms.Select(choices="TRANSPORTE", attrs={'class':'form-control'}),
            'hotel': forms.Select(choices="HOTEL", attrs={'class':'form-control'}),
            'tour': forms.Select(choices="TOUR", attrs={'class':'form-control'}),
            'fecha': forms.TextInput(attrs={'class': 'form-control'}),
            
        
        
        }
