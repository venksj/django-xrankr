from django.conf.urls import url
from search import views


urlpatterns = [
    url(r'search/$', views.autocomplete_view),
]
