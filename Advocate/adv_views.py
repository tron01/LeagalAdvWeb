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

def advocate_profile(request):
    adv_id = request.session["adv_id"]

    s = "select * from advocate a , login l where a.user_id = '"+str(adv_id)+"' and a.user_id = l.user_id and l.type = 'advocate' "
    c.execute(s)
    data = c.fetchone()
    print(data)
    return render(request,"advocate_profile.html",{"data":data})

def adv_change_password(request):
    adv_id = request.session["adv_id"]
    if 'change_pass' in request.POST:
        password = request.POST.get("new_pass")
        s = "update login set password = '"+str(password)+"' where user_id = '"+str(adv_id)+"' and type = 'advocate' "
        c.execute(s)
        conn.commit()
        
        return HttpResponseRedirect("/advocate_profile/")
    return render(request,"adv_change_password.html")


def adv_case_request(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.user_id  and c.user_id = u.user_id and c.status = 'Applied'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"adv_case_request.html",{"data":data,"msgg":msgg})
    return render(request,"adv_case_request.html",{"data":data})

def view_case_request(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")

    s = "select * from case_request c , user u  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"'"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()

    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()

    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"view_case_request.html",{"data":data,"msgg":msgg,"data1":data1})
    return render(request,"view_case_request.html",{"data":data,"data1":data1})

