from django.views.generic import TemplateView, RedirectView
from events.models import Schedule


class HomePageView(TemplateView):
    template_name = 'home.html'


class NewScheduleView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        new_schedule = Schedule.objects.create()
        return new_schedule.id


class ScheduleView(TemplateView):
    template_name = 'schedule.html'
