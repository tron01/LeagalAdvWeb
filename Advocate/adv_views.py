from django.http import HttpResponseRedirect
from django.shortcuts import render


def adv_home(request):
    if 'adv_id' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"advocate_home.html")

def adv_logout(request):
    if 'adv_id'  in request.session:
        request.session.pop('adv_id')
        return HttpResponseRedirect("/login")