from django import forms
from django.forms import ModelForm
from .models import Estudiante, Docente

class EstudianteForm(Modelform):
    class Meta: "meta es la forma abstracta de cualquier objeto?"
       model = Estudiante
      fields = {'nombre','email'}
      widgets = {
          'nombre': forms.TextInput(attrs={'class':'form-control'})
          'email': forms.TextInput(attrs={'class':'form-control'})

 class DocenteForm(Modelform):
      class Meta: "meta es la forma abstracta de cualquier objeto?"
       model = Docente
       fields = {'nombre','email'}
       widgets = {
        'nombre': forms.TextInput(attrs={'class':'form-control'})
        'email': forms.TextInput(attrs={'class':'form-control'})

    class EjerciciosForm(ModelForm):
          dominio = forms.TextInput(attrs={'class':'form-control'})
          recorrido = forms.TextInput(attrs={'class':'form-control'})
          raices = forms.TextInput(attrs={'class':'form-control'})
          ejeDeSimetria = forms.TextInput(attrs={'class':'form-control'})
          interseccionConElEjeY = forms.TextInput(attrs={'class':'form-control'})
          vertice = forms.TextInput(attrs={'class':'form-control'})
          concavidad = forms.TextInput(attrs={'class':'form-control'})
          coeficientes = forms.TextInput(attrs={'class':'form-control'})
