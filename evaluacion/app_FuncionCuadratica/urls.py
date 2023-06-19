from django.urls import path
from . import views
from .views import AboutPageView, EstudiantePageView, HomePageView, AddEstudiantePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about", AboutPageView.as_view(), name="about"),
    path("estudiante", EstudiantePageView.as_view(), name="estudiante"),
    path("IngresarEstudiante", AddEstudiantePageView.as_view(), name='ingresar-estudiante'),
    path("IngresarDocente", AddEstudiantePageView.as_view(), name='ingresar-docentente'),
]