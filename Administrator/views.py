from django.shortcuts import render
from django.http import (HttpResponse,HttpResponseRedirect)
from django.shortcuts import render
import MySQLdb
import datetime
now = datetime.datetime.now()
from django.core.files.storage import FileSystemStorage


conn = MySQLdb.connect("localhost","root","","law")
c = conn.cursor()

 #-------------------------main-----------------------------------#
def index(request):
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    if 'admin_id'  in request.session:
        return HttpResponseRedirect("/admin_home/")
    return render(request,"index.html")


def login(request):
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    if 'admin_id'  in request.session:
        return HttpResponseRedirect("/admin_home/")
    if 'login' in request.POST:
        name = request.POST.get("name")
        password = request.POST.get("password")
        st="1"
        s1 = "select * from login where username = '"+str(name)+"' and password= '"+str(password)+"' and status='"+str(st)+"'"
        print(s1)
        print("inside login")
        c.execute(s1)
        log_count = c.fetchone()
        print(log_count)
        if not bool(log_count):
            msg = "User Does Not Exists"
            return render(request,"login.html",{"msg":msg})
            
        if log_count[3] == 'admin' :
            print("------------admin-----------")
            request.session["admin_id"] = log_count[0]
            
            return HttpResponseRedirect("/admin_home")
        
        if log_count[3] == 'advocate' :
            print("---------advocate----------")
            request.session["adv_id"] = log_count[0]

            return HttpResponseRedirect("/adv_home")

        elif log_count[3] == 'user' :
            print("------------user-----")
            request.session["uid"] = log_count[0]
            return HttpResponseRedirect("/user_home")
        
        # return render(request,"user_register.html")
    return render(request,"login.html")

def adv_register(request):
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    if 'admin_id'  in request.session:
        return HttpResponseRedirect("/admin_home/")
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


            s3 = "insert into login(`username`,`password`,`type`,`status`) values('"+str(email)+"','"+str(password)+"','advocate','0')"
            print(s3)
            c.execute(s3)
            conn.commit()

            c.execute("select last_insert_id()")
            last_U_id = c.fetchone()[0]
            print(last_U_id)

            s2 = "insert into advocate(`user_id`,`adv_img`,`adv_name`,`adv_enroll_no`,`adv_qual`,`adv_age`,`adv_gender`,`adv_email`,`adv_phone`,`adv_address`,`adv_category`) values('"+str(last_U_id)+"','"+str(uploaded_file_url)+"','"+str(name)+"','"+str(enr_id)+"','"+str(qual)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(address)+"','"+str(category)+"')"
            print(s2)
            c.execute(s2)
            conn.commit()
            
            msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
            msg = "Advocate Registered Successfully,Your Account will be activate soon..."
            return render(request,"adv_register.html",{"data":data,"msg":msg})
        else:
            msg = "Account Already Exists"
            return render(request,"adv_register.html",{"data":data,"msg":msg})
    return render(request,"adv_register.html",{"data":data})


def user_register(request):
    msg=""
    if 'adv_id'  in request.session:
        return HttpResponseRedirect("/adv_home/")
    if 'uid'  in request.session:
        return HttpResponseRedirect("/user_home/")
    if 'admin_id'  in request.session:
        return HttpResponseRedirect("/admin_home/")
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

            s3 = "insert into login(`username`,`password`,`type`,`status`) values('"+str(email)+"','"+str(password)+"','user','1')"
            print(s3)
            c.execute(s3)
            conn.commit()

            c.execute("select last_insert_id()")
            last_U_id = c.fetchone()[0]
            print(last_U_id)

            acc = ""
            cvv = ""
            s2 = "insert into user(`user_id`,`u_img`,`u_name`,`u_age`,`u_gender`,`u_email`,`u_phone`,`u_aadhar`,`u_address`,`u_account`,`u_cvv`) values('"+str(last_U_id)+"','"+str(uploaded_file_url)+"','"+str(name)+"','"+str(age)+"','"+str(gender)+"','"+str(email)+"','"+str(phone)+"','"+str(aadhar)+"','"+str(address)+"','"+str(acc)+"','"+str(cvv)+"')"
            print(s2)
            c.execute(s2)
            conn.commit()
           

            
            

            msgg = "Dear "+str(name)+" \nYour Registration is Succesffull.\n Your account wil be activate soon..."
            msg = "User Registered Successfully,Your Account will be activate soon... Try Login now"
            return render(request,"user_register.html",{"msg":msg})
    return render(request,"user_register.html",{"msg":msg})

def user_bank(request):
    
        # return render(request,"user_bank.html") 
    return render(request,"user_bank.html")
#-------------------------main end-----------------------------------#





#-------------------------admin-----------------------------------#

def admin_header_footer(request):
    
    return render(request,"admin_header_footer.html")

def admin_home(request):
    if 'admin_id' not in request.session:
        return HttpResponseRedirect("/login")
    
    s1 ="select COUNT(*) from user"
    s2 ="select COUNT(*)from advocate" 
    s3="" 
    print(s1)
    c.execute(s1)
   
    user_count = c.fetchone()[0]
    c.execute(s2)
    adv_count = c.fetchone()[0]
    print(user_count)
    print(adv_count)
    return render(request,"admin_home.html")

def admin_logout(request):
    if 'admin_id'  in request.session:
        request.session.pop('admin_id')
        return HttpResponseRedirect("/login")
    

#--------------------------------- Advocate_list manage- -----------------------------#
def advocate_list(request):
    s1 = "select * from advocate a , login l where l.status = '1' and l.type = 'advocate' and a.user_id = l.user_id "
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Advocates to show...."
        return render(request,"advocate_list.html",{"data":data,"msgg":msg})
    return render(request,"advocate_list.html",{"data":data})


def adv_request(request):

    s1 = "select * from advocate a , login l where  l.status =0 and l.type = 'advocate' and a.user_id = l.user_id"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)
    if not bool(data):
        msg = "No Requests to show...."
    
        return render(request,"adv_request.html",{"data":data,"msgg":msg})
    
    return render(request,"adv_request.html",{"data":data})


def action_adv(request):
    reg_id = request.GET.get("reg_id")
    st = request.GET.get("st")
    print("inside action_adv")
    if st == 'Approve' :
        print("Approve")

        s = "update login set status = '1' where user_id = "+(reg_id)+" and type = 'advocate'"
        print(s)
        c.execute(s)
        conn.commit()
       
        return HttpResponseRedirect("/adv_request")
    
    if st == 'Reject' :
        print("Reject")

        s = "delete from login  where user_id = "+(reg_id)+" and type = 'advocate'"
        print(s)
        c.execute(s)
        conn.commit()
        s = "delete from advocate  where user_id = '"+str(reg_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/adv_request")
    
    return HttpResponseRedirect("/adv_request")

def adv_remove(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside adv_remove")
    
    s = "delete from login where user_id = "+(reg_id)+" and type='advocate'"
    print(s)
    c.execute(s)
    conn.commit()
    s1 = "delete from advocate  where user_id = '"+str(reg_id)+"'"
    print(s1)
    c.execute(s1)
    conn.commit()
    
    return HttpResponseRedirect("/advocate_list")



def advocate_status(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside adv_status")
    
    s = "update login set status = '0' where user_id = "+(reg_id)+" and type = 'advocate'"
    print(s)
    c.execute(s)
    conn.commit()
    return HttpResponseRedirect("/advocate_list")
#--------------------------------- Advocate_list manage End---------------------------#
#--------------------------------- user List manage------------------------------------#
def user_list(request):
    print("inside user_list")
    s1 = "select * from user u , login l where l.status = '1' and l.type = 'user' and l.user_id = u.user_id"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)

    if not bool(data):
        msg = "No Users to show...."
        return render(request,"user_list.html",{"data":data,"msgg":msg})
    return render(request,"user_list.html",{"data":data})

def user_status(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside user_status")
    
    s = "update login set status = '0' where user_id = "+(reg_id)+" and type = 'user'"
    print(s)
    c.execute(s)
    conn.commit()
    return HttpResponseRedirect("/user_list")

def user_request(request):
    s1 = "select * from user u , login l where u.user_id = l.user_id and l.status = '0' and l.type = 'user'"
    print(s1)
    c.execute(s1)
    data = c.fetchall()
    print(data)
    if not bool(data):
        msg = "No Requests to show...."
        return render(request,"user_request.html",{"data":data,"msgg":msg})
    
    return render(request,"user_request.html",{"data":data})

def action_user(request):
    reg_id = request.GET.get("reg_id")
    st = request.GET.get("st")
    print("inside action_adv")
    if st == 'Approve' :
        print("Approve")

        s = "update login set status = '1' where user_id = "+(reg_id)+" and type = 'user'"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/user_request")
    
    if st == 'Reject' :
        print("Reject")

        s = "delete from login  where user_id = "+(reg_id)+" and type = 'user'"
        print(s)
        c.execute(s)
        conn.commit()
        s = "delete from user  where user_id = '"+str(reg_id)+"'"
        print(s)
        c.execute(s)
        conn.commit()
        return HttpResponseRedirect("/user_request")
    
    return HttpResponseRedirect("/user_request")

def user_remove(request):
    reg_id = request.GET.get("reg_id")
    
    print("inside action_adv")
    
    s = "delete from login where user_id = '"+str(reg_id)+"' and type='user'"
    print(s)
    c.execute(s)
    conn.commit()
    s1 = "delete from user  where u_id = '"+str(reg_id)+"'"
    print(s1)
    c.execute(s1)
    conn.commit()
    return HttpResponseRedirect("/user_list")
#--------------------------------- user List manage End----------------#

def case_category(request):
    ss = "select * from category"
    c.execute(ss)
    data1 = c.fetchall()
    if 'cat' in request.POST:
        category = request.POST.get("category")
        cat_description = request.POST.get("cat_description")
        s = "select count(*) from category where cat_name = '"+str(category)+"'"
        c.execute(s)
        data = c.fetchone()

        if data[0] == 0 :
            s1 = "insert into category(`cat_name`,`cat_description`) values('"+str(category)+"','"+str(cat_description)+"')"
            c.execute(s1)
            conn.commit()
            msg = str(category)+" added Successfully"
            return render(request,"case_category.html",{"msg":msg,"data1":data1})
        else:
            msg = str(category)+" already exists"
            return render(request,"case_category.html",{"msg":msg,"data1":data1})
    return render(request,"case_category.html",{"data1":data1})

def cat_remove(request):
    cat_id = request.GET.get("cat_id")
    
    print("inside cat_remove")
    
    s = "delete from category where cat_id = '"+str(cat_id)+"'"
    print(s)
    c.execute(s)
    conn.commit()
    
    return HttpResponseRedirect("/case_category")


def edit_cat(request):
    cat_id = request.GET.get("cat_id")
    print("inside edit_cat")
    s = "select * from category where cat_id = "+(cat_id)+""
    print(s)
    c.execute(s)
    data = c.fetchone()
    print(data)
    
    if 'cat_sub' in request.POST:
        category = request.POST.get("category")
        cat_description = request.POST.get("cat_description")
        s1 = "update category set cat_name ='"+str(category)+"', cat_description ='"+str(cat_description)+"' where cat_id = "+(cat_id)+""
        print(s1)
        data1 =c.execute(s1)
        conn.commit()
        return HttpResponseRedirect("/case_category")
    return render(request,"update_case_cat.html",{"data":data})


def ipc_section(request):
    ss = "select * from ipc"
    c.execute(ss)
    data1 = c.fetchall()
    if 'ipc' in request.POST:
        ipc_section = request.POST.get("ipc_section")
        ipc_description = request.POST.get("ipc_description")
        s = "select count(*) from ipc where ipc_section = '"+str(ipc_section)+"'"
        c.execute(s)
        data = c.fetchone()

        if data[0] == 0 :
            s1 = "insert into ipc(`ipc_section`,`ipc_description`) values('"+str(ipc_section)+"','"+str(ipc_description)+"')"
            c.execute(s1)
            conn.commit()
            msg = str(ipc_section)+" added Successfully"
            return render(request,"ipc_section.html",{"data1":data1,"msg":msg})
        else:
            msg = str(ipc_section)+" already exists"
            return render(request,"ipc_section.html",{"msg":msg,"data1":data1})
    return render(request,"ipc_section.html",{"data1":data1})

def ipc_remove(request):
    ipc_id = request.GET.get("ipc_id")
    
    print("inside ipc_remove")
    
    s = "delete from ipc where ipc_id = '"+str(ipc_id)+"'"
    print(s)
    c.execute(s)
    conn.commit()
    
    return HttpResponseRedirect("/ipc_section")

def edit_ipc(request):
    ipc_id = request.GET.get("ipc_id")
    print("inside edit_ipc")
    s = "select * from ipc where ipc_id = "+(ipc_id)+""
    print(s)
    c.execute(s)
    data = c.fetchone()
    print(data)
    
    if 'ipc_update' in request.POST:
        ipc_section = request.POST.get("ipc_section")
        ipc_description = request.POST.get("ipc_description")
        s1 = "update ipc set ipc_section ='"+str(ipc_section)+"', ipc_description ='"+str(ipc_description)+"' where ipc_id = "+(ipc_id)+""
        print(s1)
        data1 =c.execute(s1)
        conn.commit()
        return HttpResponseRedirect("/ipc_section")
    return render(request,"update_ipc.html",{"data":data})

def user_case(request):
    
    print("inside user_case")
    s = "select * from case_request"
    print(s)
    c.execute(s)
    data = c.fetchall()
    print(data)
    return render(request,"case_list.html",{"data":data})


def view_case_list(request):
    u_id = request.GET.get("u_id")
    case_id = request.GET.get("case_id")
    adv_id = request.GET.get("adv_id")
    
    print("inside view_case_list")
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
    print(data1)

    s2 = "select * from documents where case_id = '"+str(case_id)+"' and u_id ='"+str(u_id)+"' order by doc_id"
    print(s2)
    c.execute(s2)
    conn.commit()
    data2 = c.fetchall()
    print(data2)

    s4 = "select * from documents where case_id = '"+str(case_id)+"'  and adv_id ='"+str(adv_id)+"'  order by doc_id"
    print(s4)
    c.execute(s4)
    conn.commit()
    data4 = c.fetchall()
    print(data4)


    s3 = "select * from rating  where case_id = '"+str(case_id)+"' and  adv_id = '"+str(adv_id)+"' "
    print(s3)
    c.execute(s3)
    conn.commit()
    data3 = c.fetchall()
    
    print(data)
    if not bool(data):
        msgg = "No case Applications"
        return render(request,"view_case_list.html",{"data":data,"msgg":msgg,"data1":data1,"data2":data2,"data3":data3,"data4":data4})
    
    return render(request,"view_case_list.html",{"data":data,"data1":data1,"data2":data2,"data3":data3,"data4":data4})

def view_feedback(request):
    print("inside feedback")

    if 'submit' in request.POST:
        print("inside submit")
        user_type = request.POST.get("user_type")
        print(user_type)
        if user_type == 'user' :
            s = "select * from feedback f,user u where f.type='user'"
            print(s)
            c.execute(s)
            data_feed = c.fetchall()
            print(data_feed)
            if not bool(data_feed):
                msg = "No Users to show...."

                return render(request,"view_feedback.html",{"msgg":msg})
            else:
                return render(request,"view_feedback.html",{"data_feed":data_feed,"user":user_type})

        if user_type == 'advocate' :
            s = "select * from feedback f,advocate a where f.type='advocate'"
            print(s)
            c.execute(s)
            data_feed = c.fetchall()
            print(data_feed)
            if not bool(data_feed):
                msg = "No Users to show...."

                return render(request,"view_feedback.html",{"msgg":msg})
            else:
                return render(request,"view_feedback.html",{"data_feed":data_feed,"user":user_type})
    return render(request,"view_feedback.html")


def approve_pay(request):
    pay_id = request.GET.get("pay_id")
    print("inside approve_pay")
    value="Approved";
    s = "update payment set Approval ='"+str(value)+"' where pay_id = "+(pay_id)+""
    print(s)
    c.execute(s)
    data = c.fetchone()
    print(data)
    return HttpResponseRedirect("/user_case")
   
def reject_pay(request):
    pay_id = request.GET.get("pay_id")
    print("inside reject_pay")
    value="Rejected";
    s = "update payment set Approval ='"+str(value)+"' where pay_id = "+(pay_id)+""
    print(s)
    c.execute(s)
    data = c.fetchone()
    print(data)
    return HttpResponseRedirect("/user_case")
    
#-------------------------admin end-----------------------------------#