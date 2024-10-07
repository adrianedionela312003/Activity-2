from django.shortcuts import render
from django.views.generic import TemplateView

class homepageview(TemplateView):
    template_name = 'app/home.html'

class contactpageview(TemplateView):
    template_name = 'app/contact.html'
class aboutpageview(TemplateView):
    template_name = 'app/about.html'


