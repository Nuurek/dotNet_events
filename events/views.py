from django.views.generic import TemplateView
from django.shortcuts import redirect, render


class HomePageView(TemplateView):
    template_name = 'home.html'
