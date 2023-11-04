from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
# import simplejson as json
from django.core.files.storage import FileSystemStorage


conn = MySQLdb.connect("localhost","root","","law")
c = conn.cursor()

def adv_home(request):
    if 'adv_id' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"advocate_home.html")

def adv_logout(request):
    if 'adv_id'  in request.session:
        request.session.pop('adv_id')
        return HttpResponseRedirect("/login")