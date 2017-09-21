from django.shortcuts import render

# Create your views here.
import json

try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

#from urllib import urlencode
from copy import deepcopy 

from django.http import HttpResponse
from django.conf import settings
from django.shortcuts import render
from django.views.generic.base import TemplateView 

from search.models import CourseProvider, Course

# Create your views here.
#client = settings.ES_CLIENT


def autocomplete_view(request):
    query = request.GET.get('term', '')
    resp = client.suggest(
        index='django',
        body={
            'name_complete': {
                "text": query,
                "completion": {
                    "field": 'name_complete',
                }
            }
        }
    )
    options = resp['name_complete'][0]['options']
    data = json.dumps(
        [{'id': i['payload']['pk'], 'value': i['text']} for i in options]
    )
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

