from django.db import models

class AprendamosDeFuncionCuadratica(models.Model):
    ejercicios = models.BigIntegerField(primary_key=True)
    estudiante = models.CharField(max_length=120)
    docente = models.CharField(max_length=120)

    class Meta:
         abstract = True
   class Ejercicios(AprendamosDeFuncionCuadratica):
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

    class Estudiante(AprendamosDeFuncionCuadratica):
         nombre = models.CharField(max_length=120)
         email = models.EmailField()

    def __str__(self):
        return str(self.nombre) + " - " + self.email

    class Docente(AprendamosDeFuncionCuadratica):
        nombre = models.CharField(max_length=120)
        email = models.EmailField()

    def __str__(self):
        return str(self.nombre) + " - " + self.email