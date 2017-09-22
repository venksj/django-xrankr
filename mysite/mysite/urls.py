"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
#################################################
#from mysite.views import hello
#from mysite.views import homepage
#from mysite.views import current_datetime
#from mysite.views import hours_ahead
#################################################
from search import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.homepage),
    #url(r'^hello/$', hello),
    #url(r'^gettime/$', current_datetime),
    #url(r'^gettime/plus/(\d{1,2})/$', hours_ahead),
    #url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    #url(r'^l/', include('login.urls')),
    url(r'^s/', include('search.urls')),
]
