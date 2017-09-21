from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

import datetime
import MySQLdb



def hello(request):
    return HttpResponse("Hello World!!") 

#######################
def homepage(request):
    return render(request, 'login/index.html')
#######################


### First attempt - with function
#def current_datetime(request):
#    now = datetime.datetime.now()
#    html = "<html><body>It is now %s.</body></html>" % now        
#    return HttpResponse(html)


### Second Attempt - with template
#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = Template("<html><body>It is now {{ current_date }}.</body></html>")
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)


####### third attempt - by specifying templates in a different folder
#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render({'current_date': now})
#    return HttpResponse(html)


######## fourth attempt - use render function to make it easy
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})


#def hours_ahead(request, offset):
#    try:
#        offset = int(offset)
#    except ValueError:
#        raise Http404()
#    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#    html = "<html><body>In %s hour(s), it will be  %s.</body></html>" % (offset, dt)
#    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()

    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'next_time': dt, 'hour_offset': offset})


###### Dumb way to do database queries in views
def book_list(request):
    db = MySQLdb.connect(user='me', db='mydb',  passwd='secret', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT name FROM books ORDER BY name')
    names = [row[0] for row in cursor.fetchall()]
    db.close()
    return render(request, 'book_list.html', {'names': names})


#def homepage(request):
#    values = request.META   
#    html = []
#    for k in sorted(values):
#        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, values[k]))
#    return HttpResponse('<table>%s</table>' % '\n'.join(html))
