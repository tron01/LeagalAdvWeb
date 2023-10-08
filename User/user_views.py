from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
# import simplejson as json
from django.core.files.storage import FileSystemStorage

# Create your views here.

conn = MySQLdb.connect("localhost","root","","legal_advisor")
c = conn.cursor()


# Create your views here.
def user_home(request):
    if 'uid' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"user_home.html")

def user_logout(request):
    if 'uid' in request.session:
        request.session.pop('uid')
        return HttpResponseRedirect("/login")

def user_header_footer(request):
    if not bool(request.session["uid"]):
        return HttpResponseRedirect("/login")
    return render(request,"user_header_footer.html")