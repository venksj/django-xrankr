from django.conf.urls import url
from login import views


urlpatterns = [
    url(r'login/$', views.login),
    url(r'register/$', views.register),
    url(r'password/$', views.forgot_password),
]
