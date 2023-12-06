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



def rej_com_case(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.user_id  and c.user_id = u.user_id and c.status = 'Completed'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    print(data)

    s1 = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.user_id  and c.user_id = u.user_id and c.status = 'Rejected'  order by c.case_id desc"

    # s = "select * from case_request c , user u  where c.user_id = '"+str(uid)+"' and c.user_id = u.u_id  order by c.case_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()
    print(data1)



    if not bool(data):
        msgg = "No case Applications"
    if not bool(data1):
        msgg2 = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"rej_com_case.html",{"data":data,"msgg":msgg,"data1":data1,"msgg2":msgg2})

    
    return render(request,"rej_com_case.html",{"data":data,"data1":data1})



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


def status(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    st = request.GET.get("st")

    if st == 'Approved':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Accepted"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_request")


def adv_case_status(request):
    adv_id = request.session["adv_id"]
    print(adv_id)
    s = "select * from case_request c , advocate a, user u where c.adv_id = '"+str(adv_id)+"' and c.adv_id = a.user_id  and c.user_id = u.user_id and c.status != 'Applied' and c.status != 'Rejected' and c.status != 'Completed'   order by c.case_id desc"

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
        return render(request,"adv_case_status.html",{"data":data,"msgg":msgg})
    return render(request,"adv_case_status.html",{"data":data})


def view_case_status(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")

    s = "select * from case_request c , user u  where c.case_id = '"+str(case_id)+"' and  c.user_id = '"+str(u_id)+"' and c.user_id = u.user_id  order by c.case_id desc"
    print(s)
    c.execute(s)
    conn.commit()
    data = c.fetchall()

    s1 = "select * from payment where case_id= '"+str(case_id)+"' order by pay_id desc"
    print(s1)
    c.execute(s1)
    conn.commit()
    data1 = c.fetchall()
    
    s2 = "select * from documents where case_id = '"+str(case_id)+"' and  u_id = '"+str(u_id)+"' order by doc_id"
    print(s2)
    
    c.execute(s2)
    conn.commit()
    data2 = c.fetchall()

    s3 = "select * from documents where case_id = '"+str(case_id)+"' and  adv_id = '"+str(adv_id)+"' order by doc_id"
    print(s3)
    
    c.execute(s3)
    conn.commit()
    data3 = c.fetchall()

    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
    # if 'login' in request.POST:
        # return HttpResponseRedirect("/login")
        return render(request,"view_case_status.html",{"data":data,"msgg":msgg,"data1":data1,"data2":data2,"data3":data3})
        
    return render(request,"view_case_status.html",{"data":data,"data1":data1,"data2":data2,"data3":data3})

def case_ipc(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")

    if 'ipc' in request.POST:
        ipc_description = request.POST.get("ipc_description")
        s = "update case_request set ipc_sections= '"+str(ipc_description)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        
        
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))
    return render(request,"case_ipc.html")


def add_fee(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")
    tdate = now.date()
    if 'fee' in request.POST:
        amount = request.POST.get("amount")
        s = "insert into payment(`user_id`,`adv_id`,`case_id`,`posted_date`,`amount`,`status`) values('"+str(u_id)+"', '"+str(adv_id)+"', '"+str(case_id)+"','"+str(tdate)+"','"+str(amount)+"','Not Paid')"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))
    return render(request,"add_fee.html")


def add_doc(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    # st = request.GET.get("st")
    tdate = now.date()
    if 'doc' in request.POST:
        file_name = request.POST.get("file_name")
        # file_doc = request.POST.get("file_doc")
        myfile = request.FILES["file_doc"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        ss = "select count(*) from documents where document = '"+str(uploaded_file_url)+"'"
        c.execute(ss)
        doc_count = c.fetchone()
        if doc_count[0] == 0: 
            s = "insert into documents(`case_id`,`adv_id`,`doc_name`,`document`,`posted_date`) values('"+str(case_id)+"','"+str(adv_id)+"','"+str(file_name)+"','"+str(uploaded_file_url)+"',  '"+str(tdate)+"')"
            print(s)
            c.execute(s)
            conn.commit()
            return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))
        else:
            msg = "file Already Exists"
        return render(request,"add_doc.html",{"msg":msg})
    return render(request,"add_doc.html")
        # return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))

        
def status1(request):
    adv_id = request.session["adv_id"]
    case_id = request.GET.get("case_id")
    u_id = request.GET.get("u_id")
    st = request.GET.get("st")

    # if st == 'Approved':
    #     s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
    #     print(s)
    #     c.execute(s)
    #     conn.commit()
    #     msg = "Mark as Accepted"
    #     # return render(request,"adv_case_request.html",{"msg":msg})
    #     return HttpResponseRedirect("/adv_case_request")


    if st == 'Rejected':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Rejected"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_status")

    if st == 'Completed':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Completed"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/adv_case_status")


    if st == 'Proceeding':
        s = "update case_request set status= '"+str(st)+"' where case_id='"+str(case_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        msg = "Mark as Proceeding"
        # return render(request,"adv_case_request.html",{"msg":msg})
        return HttpResponseRedirect("/view_case_status?case_id="+str(case_id)+"&u_id="+str(u_id))

    # data = c.fetchall()
    # print(data)
    # if not bool(data):
    #     msgg = "No case Applications"
    # # if 'login' in request.POST:
    #     # return HttpResponseRedirect("/login")
    # return HttpResponseRedirect("/view_case_request?case_id=case_id&u_id=u_id")
    return render(request,"adv_case_status.html")

def adv_feedback(request):
    adv_id = request.session["adv_id"]
    tdate = now.date()

    if 'submit' in request.POST:
        subject = request.POST.get("subject")
        feedback_desc = request.POST.get("feedback_desc")
        s = "insert into feedback(`u_id`,`feed_subject`,`feed_description`,`type`,`posted_date`) values('"+str(adv_id)+"','"+str(subject)+"','"+str(feedback_desc)+"','advocate','"+str(tdate)+"')"
        c.execute(s)
        conn.commit()
        msg = "Feedback Send Successfully"
    # if request.POST:
    #     return HttpResponseRedirect("/payment5/")
        return render(request,"adv_feedback.html",{"msg":msg})
    return render(request,"adv_feedback.html")

