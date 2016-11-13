from django.conf.urls import url, include
from django.contrib import admin
from schedules import urls as schedules_urls
from schedules import views as schedules_views


urlpatterns = [
    url(r'^$', schedules_views.HomePageView.as_view(), name='home_page'),
    url(r'^schedules/', include(schedules_urls)),
]
