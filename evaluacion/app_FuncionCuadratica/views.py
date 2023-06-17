from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def homePageView(request):
    return HttpResponse("Esta es mi primera App! - Ambar, Antonia, Romina")