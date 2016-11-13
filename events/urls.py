from django.conf.urls import url
from events.views import HomePageView, ScheduleView, NewScheduleView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^schedule/new', NewScheduleView.as_view(), name='new_schedule'),
    url(r'^schedule/(\d+)', ScheduleView.as_view(), name='view_schedule'),
]
