from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.
from .models import Obsview


class ExtractionView(generic.DetailView):
    model = Obsview
    template_name = 'outside/extraction.html'
