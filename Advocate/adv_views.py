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



def adv_logout(request):
    if 'adv_id'  in request.session:
        request.session.pop('adv_id')
        return HttpResponseRedirect("/login")
    
def adv_header_footer(request):
    if 'adv_id' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"adv_header_footer.html")

def adv_home(request):
    if 'adv_id' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"adv_home.html")

def adv_ipc(request):
    if 'adv_id' not in request.session:
        return HttpResponseRedirect("/login")
    
    s = "select * from ipc order by ipc_section"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"adv_ipc.html",{"data":data})
