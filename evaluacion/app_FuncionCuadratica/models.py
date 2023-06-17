from django.db import models

class Ejercicios(models.Model):
      dominio = models.BooleanField(primary_key =True)
      recorrido = models.BooleanField()
      raices = models.BooleanField()
      ejeDeSimetria = models.BooleanField()
      interseccionConElEjeY = models.BooleanField()
      vertice = models.BooleanField()
      concavidad = models.BooleanField()
      coeficientes = models.BooleanField()

def __str__(self):
    return self.Ejercicios

class Estudiante(models.Model):
      nombre = models.CharField(max_length=120)
      email = models.EmailField()

def __str__(self):
    return str(self.nombre) + " - " + self.email

class Docente(models.Model):
      nombre = models.CharField(max_length=120)
      email = models.EmailField()

      def __str__(self):
            return str(self.nombre) + " - " + self.email