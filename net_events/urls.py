from django.conf.urls import url, include
from django.contrib import admin
from events import urls as events_urls


urlpatterns = [
    url(r'^', include(events_urls)),
]
