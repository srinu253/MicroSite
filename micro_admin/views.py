from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf
from django.template import RequestContext
from django.contrib.auth.hashers import check_password
import json
from microsite.settings import BASE_DIR

from micro_admin.models import USER_ROLES, User
from micro_admin.forms import ChangePasswordForm, UserForm


#@csrf_protect
def index(request):
    if request.user.is_authenticated():
        return render_to_response('admin/index.html')
    if request.method=="POST":
        user = authenticate(username=request.POST.get('email'), password=request.POST.get('password'))
        if user is not None:
            if user.is_active:
                login(request, user)
                data = {'error':False}
            else:
                data = {'error':True,'message':"The password is valid, but the account has been disabled!"}
        else:
            data = {'error':True,'message':"The username and password were incorrect."}
        return HttpResponse(json.dumps(data))
    else:
        data = {}
        data.update(csrf(request))
        return render_to_response('admin/login.html',data,context_instance=RequestContext(request))


def out(request):
    if not request.user.is_authenticated():
        return HttpResponse('')

    logout(request)
    return HttpResponseRedirect('/portal/')


@login_required
def change_password(request):
    if request.method == 'POST':
        validate_changepassword = ChangePasswordForm(request.POST)
        if validate_changepassword.is_valid():
            user = request.user
            if not check_password(request.POST['oldpassword'],user.password):
                return HttpResponse(json.dumps({'error':True,'response':{'oldpassword':'Invalid old password'}}))
            if request.POST['newpassword'] != request.POST['retypepassword']:
                return HttpResponse(json.dumps({'error':True,'response':{'newpassword':'New password and ConformPasswords did not match'}}))
            user.set_password(request.POST['newpassword'])
            user.save()
            return HttpResponse(json.dumps({'error':False,'response':'Password changed successfully'}))
        else:
            return HttpResponse(json.dumps({'error':True,'response':validate_changepassword.errors}))
    return render_to_response('admin/useraccount/change-password.html')


@login_required
def contacts(request):
    return HttpResponse('no design available')


@login_required
def jobs(request):
    return HttpResponse('no design available')
