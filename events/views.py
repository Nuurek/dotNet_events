from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ScheduleView(TemplateView):
    template_name = 'schedule.html'
