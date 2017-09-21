from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from login.models import *


# Create your views here.


@csrf_protect
def register(request):
    error = False
    if request.method == 'POST':
        if 'name' in request.POST:
            u_name = request.POST['name']
            u_email = request.POST['email']
            u_password = request.POST['password']
            u_c_password = request.POST['password_confirm']
            if not u_name:
                error = True
                err_msg = "Username not provided"
            elif u_password != u_c_password:
                error = True
                err_msg = "Passwords didnot match"
            else: 
                # check if already present in the database
                try:
                    p = User.objects.get(email=u_email)
                except User.DoesNotExist:
                    #create the object and insert into the database
                    u1 = User.objects.create(username=u_name, 
                                             email=u_email, 
                                             password=u_password, 
                                             c_password=u_c_password)
                else:
                    error = True


                if error:
                    vdict = {'name': u_name, 'email': u_email, 'message': err_msg}
                    return render(request, 'login/register_fail.html', vdict)
                else: 
                    vdict = {'name': u_name, 'email': u_email}
                    return render(request, 'login/register_success.html', vdict)
    return render(request, 'login/register_form.html', {'error': error})


@csrf_protect
def login(request):
    error = False
    if request.method == 'POST':
        if 'email' in request.POST:
            u_email = request.POST['email']
            u_password = request.POST['password']
            if not u_email:
                error = True
                err_msg = "Email not provided"
            else: 
                # check if already present in the database
                try:
                    u1 = User.objects.get(email=u_email)
                    if u1.password != u_password:
                        error = True
                        err_msg = "Incorrect password provided"
                except User.DoesNotExist:
                    error = True
                    err_msg = "User doesn't exist"

                if error:
                    vdict = {'email': u_email, 'message': err_msg}
                    return render(request, 'login/login_fail.html', vdict)
                else: 
                    vdict = {'email': u_email}
                    return render(request, 'login/login_home.html', vdict)
    return render(request, 'login/login_form.html', {'error': error})


@csrf_protect
def forgot_password(request):
    error = False
    if request.method == 'POST':
        if 'email' in request.POST:
            u_email = request.POST['email']
            u_password = request.POST['password']
            u_c_password = request.POST['c_password']
            if not u_email:
                error = True
                err_msg = "Email not provided"
            elif u_password != u_c_password:
                error = True
                err_msg = "Passwords didnot match"
            else: 
                try:
                    u1 = User.objects.get(email=u_email)
                    User.objects.filter(id=u1.id).update(password=u_password, c_password=u_c_password)
                except User.DoesNotExist:
                    error = True
                    err_msg = "User doesn't exist"

                if error:
                    vdict = {'email': u_email, 'message': err_msg}
                    return render(request, 'login/forgot_password_fail.html', vdict)
                else: 
                    vdict = {'email': u_email, 'name': u1.username}
                    return render(request, 'login/forgot_password_success.html', vdict)
    return render(request, 'login/forgot_password_form.html', {'error': error})


