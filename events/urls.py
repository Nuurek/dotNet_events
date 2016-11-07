from django.conf.urls import url
from events.views import HomePageView


urlpatterns = [
    url(r'^$', HomePageView.as_view())
]
