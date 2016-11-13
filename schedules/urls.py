from django.conf.urls import url
from schedules.views import HomePageView, ScheduleView, NewScheduleView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^new', NewScheduleView.as_view(), name='new_schedule'),
    url(r'^(\d+)', ScheduleView.as_view(), name='view_schedule'),
]
