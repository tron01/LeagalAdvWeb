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
    s = "select * from user u , login l where u.user_id = '"+str(u_id)+"' and u.user_id = l.user_id and l.type = 'user' "
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
    s = "select * from advocate where user_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
    return render(request,"view_adv.html",{"data":data})



def add_case(request):
    uid = request.session["uid"]
    print(uid)
    adv_id = request.GET.get("adv_id")
    print(adv_id)
    s = "select * from advocate where user_id = '"+str(adv_id)+"' "
    c.execute(s)
    conn.commit()
    data = c.fetchone()
    print(data)
    if 'register' in request.POST:
        case_title = request.POST.get("case_title")
        case_desc = request.POST.get("case_desc")
        # case_file = request.POST.get("case_file")

        myfile = request.FILES["case_file"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)

        s1 = "insert into case_request(`adv_id`,`user_id`,`case_title`,`case_desc`,`case_file`,`status`) values('"+str(adv_id)+"','"+str(uid)+"','"+str(case_title)+"','"+str(case_desc)+"','"+str(uploaded_file_url)+"','Applied')"
        c.execute(s1)
        conn.commit()   
        msg = "Case Registered Successfully"    
        # return HttpResponseRedirect("/login")
        return render(request,"add_case.html",{"msg":msg})

    return render(request,"add_case.html",{"data":data})

def case_status(request):
    uid = request.session["uid"]
    s = "select * from case_request c , user u, advocate a  where c.user_id = '"+str(uid)+"' and c.user_id = u.user_id and c.adv_id = a.user_id  order by c.case_id desc"

    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"case_status.html",{"data":data,"msgg":msgg})
    return render(request,"case_status.html",{"data":data})

def user_view_case_status(request):
    u_id = request.session["uid"]
    case_id = request.GET.get("case_id")
    adv_id = request.GET.get("adv_id")

    print(" inside user_view_case_status")

    s = "select * from case_request c , user u,advocate a  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"' and c.user_id = u.user_id and c.adv_id = a.user_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)
    
    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()

    s2 = "select * from documents where case_id = '"+str(case_id)+"' order by doc_id"
    print(s2)
    
    c.execute(s2)
    conn.commit()
    data2 = c.fetchall()


    s3 = "select * from rating  where case_id = '"+str(case_id)+"' and  adv_id = '"+str(adv_id)+"' "
    print(s3)
    
    c.execute(s3)
    conn.commit()
    data3 = c.fetchall()
    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"user_view_case_status.html",{"data":data,"msgg":msgg,"data1":data1,"data2":data2,"data3":data3})
    return render(request,"user_view_case_status.html",{"data":data,"data1":data1,"data2":data2,"data3":data3})

def add_rating(request):
    if 'rating' in request.POST:
        u_id = request.session["uid"]
        case_id = request.GET.get("case_id")
        adv_id = request.GET.get("adv_id")
        u_rating = request.POST.get("u_rating")
        rating_desc = request.POST.get("rating_desc")


        s = "select count(*) from rating where case_id = '"+str(case_id)+"' and adv_id = '"+str(adv_id)+"' and user_id = '"+str(u_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        cnt = c.fetchone()
        if cnt[0] == 0 :

            
            s1 = "insert into rating(`case_id`,`user_id`,`adv_id`,`rating`,`rate_desc`) values('"+str(case_id)+"','"+str(u_id)+"','"+str(adv_id)+"','"+str(u_rating)+"' ,'"+str(rating_desc)+"')"
            c.execute(s1)
            conn.commit()
            # msg = str(ipc_section)+" added Successfully"
            # return render(request,"add_rating.html")
            return HttpResponseRedirect("/user_view_case_status?case_id="+str(case_id)+"&adv_id="+str(adv_id))

        else:
            msg = " already done rating"
            # return render(request,"add_rating.html",{"msg":msg})
            return HttpResponseRedirect("/user_view_case_status?case_id="+str(case_id)+"&adv_id="+str(adv_id))

    return render(request,"add_rating.html")

def change_password(request):
    u_id = request.session["uid"]
    if 'change_pass' in request.POST:
        password = request.POST.get("new_pass")
        s = "update login set password = '"+str(password)+"' where user_id = '"+str(u_id)+"' and type= 'user' "
        c.execute(s)
        conn.commit()
        
        return HttpResponseRedirect("/user_profile/")
    return render(request,"user_password.html")