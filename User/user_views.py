from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
# import simplejson as json
from django.core.files.storage import FileSystemStorage

# Create your views here.

conn = MySQLdb.connect("localhost","root","","law")
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
    if 'uid' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"user_header_footer.html")


def user_about(request):
    return render(request,"user_about.html")

def user_profile(request):
    u_id = request.session["uid"]
    s = "select * from user u , login l where u.u_id = '"+str(u_id)+"' and u.u_id = l.user_id and l.type = 'user' "
    c.execute(s)
    data = c.fetchone()
    print(data)
    return render(request,"user_profile.html",{"data":data})

def user_ipc(request):
    s = "select * from ipc order by ipc_section"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_ipc.html",{"data":data})

def user_cat_list(request):
    s = "select * from category order by cat_id"
    # s = "SELECT *,BIN(ipc_section) AS binray_not_needed_column FROM ipc ORDER BY binray_not_needed_column ASC , ipc_section ASC"
    # s = "SELECT *  CAST(ipc_section as SIGNED) AS casted_column FROM ipc ORDER BY casted_column ASC , ipc_section ASC"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_cat_list.html",{"data":data})

def user_adv_list(request):
    s = "select * from category order by cat_name"
    print(s)
    c.execute(s)
    data =c.fetchall()
    print(data)

    if 'cat' in request.POST:
        category = request.POST.get("category")
        print(category)
        if category == 'All':
            s2 = "select * from advocate order by adv_category"
            print(s2)
            c.execute(s2)
            data2 =c.fetchall()
            print(data2)
            if not bool(data2):
                msg = "No Advocate List To show"
                return render(request,"user_adv_list.html",{"data":data,"data2":data2,"msg":msg})
            return render(request,"user_adv_list.html",{"data":data,"data2":data2})
        else:
            s1 = " select * from advocate where adv_category = '"+str(category)+"' "
            print(s1)
            c.execute(s1)
            data1 =c.fetchall()
            print(data1)
            if not bool(data1):
                msg = "No Advocate List To show"
                return render(request,"user_adv_list.html",{"data":data,"data2":data1,"msg":msg})
            return render(request,"user_adv_list.html",{"data":data,"data2":data1})
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"user_adv_list.html",{"data":data})

def view_adv(request):
    adv_id = request.GET.get("adv_id")
    print(adv_id)
    s = "select * from advocate where adv_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"view_adv.html",{"data":data})
