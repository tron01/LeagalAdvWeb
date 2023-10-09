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

#main home page
def index(request):
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    if 'admin_id'  in request.session:
        return HttpResponseRedirect("/admin_home/")
    return render(request,"index.html")


def login(request):
    if 'login' in request.POST:
        name = request.POST.get("name")
        password = request.POST.get("password")
        st="1"
        s1 = "select * from login where username = '"+str(name)+"' and password= '"+str(password)+"' and status='"+str(st)+"'"
        print(s1)
        c.execute(s1)
        log_count = c.fetchone()
        print(log_count)

        if not bool(log_count):
            msg = "User Does Not Exists"
            return render(request,"login.html",{"msg":msg})
            
        if log_count[4] == 'admin' :
            print("------------admin-----------")
            request.session["admin_id"] = log_count[1]
            print( log_count[1])
            return HttpResponseRedirect("/admin_home")
        
        if log_count[4] == 'advocate' :
            print("---------advocate----------")
            request.session["adv_id"] = log_count[1]

            return HttpResponseRedirect("/adv_home")

        elif log_count[4] == 'user' :
            print("------------user-----")
            request.session["uid"] = log_count[1]
            return HttpResponseRedirect("/user_home")
        
        # return render(request,"user_register.html")
    return render(request,"login.html")

def adv_register(request):
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    print("-----------------------inside advocate register-------------------------")
    s = "select * from category"
    c.execute(s)
    conn.commit()
    data = c.fetchall()
    if 'submit' in request.POST:
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        enr_id = request.POST.get("enr_id")
        qual = request.POST.get("qual")
        category = request.POST.get("category")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        password = request.POST.get("password")

        s1 = "select count(*) from advocate where adv_email = '"+str(email)+"' or adv_enroll_no= '"+str(enr_id)+"' or adv_phone = '"+str(phone)+"'"
        print(s1)
        c.execute(s1)
        reg_count = c.fetchone()

        if reg_count[0] == 0 :
            s2 = "insert into advocate(`adv_img`,`adv_name`,`adv_enroll_no`,`adv_qual`,`adv_age`,`adv_gender`,`adv_email`,`adv_phone`,`adv_address`,`adv_category`) values('"+str(uploaded_file_url)+"','"+str(name)+"','"+str(enr_id)+"','"+str(qual)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(address)+"','"+str(category)+"')"
            print(s2)
            c.execute(s2)
            conn.commit()
            s3 = "insert into login(`user_id`,`username`,`password`,`type`,`status`) values((select max(adv_id) from advocate),'"+str(email)+"','"+str(password)+"','advocate','0')"
            print(s3)
            c.execute(s3)
            conn.commit()
            msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
            msg = "Advocate Registered Successfully,Your Account will be activate soon..."
            return render(request,"adv_register.html",{"data":data,"msg":msg})
        else:
            msg = "Account Already Exists"
            return render(request,"adv_register.html",{"data":data,"msg":msg})
    return render(request,"adv_register.html",{"data":data})


def user_register(request):
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    print("-----------------------inside User register-------------------------")
    if 'submit' in request.POST:
        myfile = request.FILES["img"]
        fs = FileSystemStorage()        
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        aadhar = request.POST.get("aadhar")
        address = request.POST.get("address")
        password = request.POST.get("password")

        s1 = "select count(*) from user where u_email = '"+str(email)+"' or u_phone= '"+str(phone)+"' or u_aadhar='"+str(aadhar)+"'"
        print(s1)
        c.execute(s1)
        reg_count = c.fetchone()

        if reg_count[0] != 0 :
            msg = "Account Already Exists"
            return render(request,"user_register.html",{"msg":msg})

        else:
            """
            """
            acc = ""
            cvv = ""
            s2 = "insert into user(`u_img`,`u_name`,`u_age`,`u_gender`,`u_email`,`u_phone`,`u_aadhar`,`u_address`,`u_account`,`u_cvv`) values('"+str(uploaded_file_url)+"','"+str(name)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(aadhar)+"','"+str(address)+"','"+str(acc)+"','"+str(cvv)+"')"
            print(s2)
            c.execute(s2)
            conn.commit()
            s3 = "insert into login(`user_id`,`username`,`password`,`type`,`status`) values((select max(u_id) from user),'"+str(email)+"','"+str(password)+"','user','1')"
            print(s3)
            c.execute(s3)
            conn.commit()
            msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
            msg = "User Registered Successfully,Your Account will be activate soon... Try Login now"
            return render(request,"user_register.html",{"msg":msg})
    return render(request,"user_register.html",{"msg":msg})

def user_bank(request):
    
        # return render(request,"user_bank.html") 
    return render(request,"user_bank.html")

def admin_home(request):
    if 'admin_id' not in request.session:
        return HttpResponseRedirect("/login")
    return render(request,"admin_home.html")
def admin_logout(request):
    if 'admin_id'  in request.session:
        request.session.pop('admin_id')
        return HttpResponseRedirect("/login")