from django.conf.urls import url
from events.views import HomePageView, ScheduleView


urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home_page'),
    url(r'^schedule/(\d+)', ScheduleView.as_view(), name='view_schedule'),
]
