from django.shortcuts import render
from django.http import HttpResponse
from multiprocessing import context
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from first_app import models

# Create your views here.
# functionbase views:
# def index(request):
#     return render(request, 'template', context={})


# classbase view:
# class IndexView(TemplateView):
#     template_name = 'first_app/index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['sample_text_1'] = 'SamPle Text 1'
#         context['sample_text_2'] = 'SamPle Text 2'
#         return context

class IndexView(ListView):
    context_object_name = 'musician_list'
    model = models.Musician
    template_name = 'first_app/index.html'


class MusicianDetail(DetailView):
    context_object_name = 'musician'
    model = models.Musician
    template_name = 'first_app/musician_details.html'


class AddMusician(CreateView):
    fields = ('first_name', 'last_name', 'instrument')
    model = models.Musician     # it will create form for us
    template_name = 'first_app/musician_form.html'
