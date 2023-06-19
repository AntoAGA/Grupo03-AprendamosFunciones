from django.contrib.messages.views import SuccessMessageMixin
from django.core.checks import messages
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView

from .forms import EstudianteForm
from .models import Estudiante


class HomePageView(TemplateView):
    # def homePageView(request):
    template_name = "home.html"
    # return HttpResponse("Hola, Mundo!")


class AboutPageView(TemplateView):
    # def homePageView(request):
    template_name = "about.html"


class EstudiantePageView(ListView):
    model = Estudiante
    template_name = "estudiante.html"
    context_object_name = 'data'


class AddEstudiantePageView(SuccessMessageMixin, CreateView):
    form_class = EstudianteForm
    template_name = 'IngresarEstudiante.html'
    success_message = 'Estudiante Ingresado'
    error_message = "Error en ingresar estudiante"
    success_url = reverse_lazy("ingresar-estudiante")

    def get_success_url(self):
        return reverse('ingresar-estudiante')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)