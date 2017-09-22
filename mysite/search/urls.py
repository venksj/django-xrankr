from django.conf.urls import url
from search import views


urlpatterns = [
    #url(r'search/$', views.autocomplete_view),
    url(r'^autocomplete/', views.autocomplete_view, name='autocomplete-view'),
    url(r'^course', views.course_detail, name='course-detail'),
    url(r'^search', views.search_query, name='search-query'),
    #url(r'^$', HomePageView.as_view(), name='index-view'),
]
