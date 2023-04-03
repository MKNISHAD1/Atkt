
from django.conf import settings
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,HttpResponse,HttpResponseRedirect,get_object_or_404, reverse
from django.contrib.auth import logout,authenticate,login
from django.contrib.auth.models import User
from Home.models import *
from Home.forms import *
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    return render(request,'index.html')
    
def about(request):
    return render(request,'about.html')

def reguser(request):
    all_data=Student.objects.all()
    print(all_data)
    # all_course=course.object.all()
    # print(all_course)
    if request.method=="POST":
        firstname=request.POST['first']
        middlename=request.POST['middle']
        lastname=request.POST['last']
        fathername=request.POST['father']
        uname=request.POST['usrname']
        pwd=request.POST['password']
        contact=request.POST['phone']
        sem=request.POST['Semester']
        cls=request.POST['Class']
        crs=request.POST['Course']
        prn=request.POST['prn']
        addr=request.POST['addr']
        rno=request.POST['rno']
        controlnum=request.POST['cno']
        rl=request.POST['role']
        mail=request.POST['email']
        gen=request.POST['gender']

        usr=User.objects.create_user(uname,mail,pwd)
        usr.first_name=firstname
        usr.last_name=lastname
        usr.email=mail
        if rl=="Stud":
            usr.is_active=True
        usr.save()

        cnodb=Control_No_ForRef(control_no=controlnum)
        cnodb.save()

        data= Student(user=usr,First_Name=firstname,Middle_Name=middlename,Last_Name=lastname,Father_Name=fathername,Phone_Number=contact,Email=mail,PRN=prn,Control_Number=controlnum,Semester=sem,Course=crs,Class=cls,Gender=gen, Roll_No=rno,Address=addr)
        data.save()

        if "pic" in request.FILES:
            img = request.FILES["pic"]
            data.Profile_Pic = img
            data.save()
        if "pdf" in request.FILES:
            feepdf = request.FILES["pdf"]
            data.Fee_pdf = feepdf
            data.save()   


# first parameter is that trugh which user get login



        # data=Students(PRN=prnno,Control_Number=contnum,Phone_Number=Contact,Semester=sem)
        # data.save()
        res="Dear {} Thanks for Sign Up".format(firstname)
        return render(request,"register.html",{"status":res,"STU":all_data})

    return render(request,'register.html',{"STU":all_data})

def loginuser(request):
    if request.method=="POST":
        unme=request.POST.get('username')
        pwd=request.POST.get('password')

        user=authenticate(username=unme,password=pwd)

        if user:
            login(request,user)
            if user.is_superuser:
                return HttpResponseRedirect("/admin")
            else:
                return HttpResponseRedirect("/Stud_Dash")
            # if user.is_active:
            #     # return render(request,"Student_Dashboard.html")
            #     return HttpResponseRedirect("/Stud_Dash")
        else:
            return render (request,"index.html",{"status":"Invalid Username or Passwowd !!"})

    return HttpResponse("called")

def data(request):
    return render(request,'Data.html')

def check_user(request):
    if request.method=="GET":
        un=request.GET.get('usr')
        check=User.objects.filter(username=un)
        # print(check,len(check))
        # return HttpResponse("/login")
        if len(check)==1:
            return HttpResponse("Exist")
        else:
            return HttpResponse("Not Exist")

def check_user1(request):
    if request.method=="GET":
        sp=request.GET.get('pass')
        check="Admin@mk007"
        # print(check,len(check))
        # return HttpResponse("/login")
        if check==sp:
            return HttpResponse("Right")
        else:
            return HttpResponse("Wrong")

@login_required        
def Stud_dashboard(request):
    # context = {}
    # check = Student.objects.filter(user__id=request.user.id)
    # if len(check)>0:
    #     data = Student.objects.get(user__id=request.user.id)
    #     # datatest=Students.objects.get()//comment
    #     context["data"] = data
    #     # context["datatest"] = datatest//comment
    #     return render(request,"Student_Dashboard.html",context)
    # else:
    #     alldata=Student.objects.filter(user__id=request.user.id)
    #     # alldata=Teacher.objects.filter(user__id=request.user.id)//comment
    #     print(len(alldata))
    #     # data1 = testuser.objects.get(user__id=request.user.id)//commment
    #     context["alldata"]=alldata
    #     return render(request,"Student_Dashboard.html",context)
    context={}
    Tea=Teacher.objects.filter(user__id=request.user.id)
    if len(Tea)>0:
        data=Teacher.objects.get(user__id=request.user.id)
        context["data"]=data
        return render(request,"Student_Dashboard.html",context)
    else:
        data=Student.objects.get(user__id=request.user.id)
        context["data"]=data
        data1=ResultisOut_ForRef.objects.get()
        context["data1"]=data1
        return render(request,"Student_Dashboard.html",context)


def Tea_dashboard(request):    
    if request.method=="POST":
        firstname=request.POST["first"]
        lastname=request.POST["last"]
        uname=request.POST['usrname']
        pwd=request.POST['password']
        contact=request.POST['phone']
        gen=request.POST['gender']
        rl=request.POST['role']
        mail=request.POST['email']

        usr=User.objects.create_user(uname,mail,pwd)
        usr.first_name=firstname
        usr.last_name=lastname
        usr.email=mail
        if rl=="Tea":
            usr.is_staff=True
        usr.save()

        data= Teacher(user=usr,First_Name=firstname,Last_Name=lastname,Email=mail,Gender=gen,Phone_Number=contact)
        data.save()

        if "pic" in request.FILES:
            img = request.FILES["pic"]
            data.Profile_Pic = img
            data.save()
# first parameter is that trugh which user get login



        # data=Students(PRN=prnno,Control_Number=contnum,Phone_Number=Contact,Semester=sem)
        # data.save()
        res="Dear {} Thanks for Sign Up".format(firstname)
        return render(request,"Teacher_Dashboard.html",{"status":res})

    return render(request,'Teacher_Dashboard.html')
@login_required
def logoutuser(request):
    logout(request)
    return HttpResponseRedirect("/")

@login_required
def edit_profile(request):
    user=User.objects.get(id=request.user.id)
    if user.is_staff:
        context={}
        # ch= Teacher.objects.filter(user__id=request.id)
        # if len(ch)>0:
        data=Teacher.objects.get(user__id=request.user.id)
        context["data"]=data
        if request.method=="POST":
            fn=request.POST.get("fname")
            ln=request.POST.get("lname")
            em=request.POST.get("mail")
            gen=request.POST.get("gender")
            Contact=request.POST.get("phone")

            usr=User.objects.get(id=request.user.id)
            usr.first_name=fn
            usr.last_name=ln
            usr.email=em
            usr.save()

            data.Phone_Number=Contact
            data.Gender=gen
            data.First_Name=fn
            data.Last_Name=ln
            data.Email=em
            data.save()

            if "pic" in request.FILES:
                img = request.FILES["pic"]
                data.Profile_Pic = img
                data.save()
            context["status"]="Changes saved successfully"
        return render(request,"EditProfile.html",context)

    else:
        context={}
        ch = Student.objects.filter(user__id=request.user.id)
        if len(ch)>0:
            data = Student.objects.get(user__id=request.user.id)
            context["data"] = data
        if request.method=="POST":
        # print(request.POST)
            fn=request.POST.get("fname")
            mn=request.POST.get("mname")
            ln=request.POST.get("lname")
            fd=request.POST.get("fdname")
            em=request.POST.get("mail")
            gen=request.POST.get("gender")
            Contact=request.POST.get("phone")

            usr=User.objects.get(id=request.user.id)
            usr.first_name=fn
            usr.last_name=ln
            usr.email=em
            usr.save()

            data.Phone_Number=Contact
            data.Gender=gen
            data.First_Name=fn
            data.Middle_Name=mn
            data.Last_Name=ln
            data.Father_Name=fd
            data.Email=em
            data.save()

            if "pic" in request.FILES:
                img = request.FILES["pic"]
                data.Profile_Pic = img
                data.save()
            if "pdf" in request.FILES:
                feepdf = request.FILES["pdf"]
                data.Fee_pdf = feepdf
                data.save()

            context["status"]="Changes saved successfully"

        return render(request,"EditProfile.html",context)

           
@login_required
def change_pass(request):
    context={}
    ch = Student.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = Student.objects.get(user__id=request.user.id)
        context["data"] = data
    else:
        data = Teacher.objects.get(user__id=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            context["msz"] = "Password Changed Successfully!!!"
            context["col"] = "alert-success"
            user = User.objects.get(username=un)
            login(request,user)
        else:
            context["msz"] = "Incorrect Current Password"
            context["col"] = "alert-danger"

    return render(request,"Change_Pass.html",context)
@login_required
def test_check(request):
    context={}
    ch = Teacher.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = Teacher.objects.get(user__id=request.user.id)
        context["data"] = data
    else:
        data = Student_Result.objects.get(user__id=request.user.id)
        context["data"] = data             
    form=test_form()
    if request.method=="POST":
        form=test_form(request.POST)
        if form.is_valid():
            data=form.save()
            data.save()
            context["status"]="Added successfully"
    context["form"]=form
    return render(request,"test_check.html",context)

@login_required
def result(request):
    user=User.objects.get(id=request.user.id)
    if user.is_staff:
        context={}
        ch = Teacher.objects.filter(user__id=request.user.id)   
        if len(ch)>0:
            data = Teacher.objects.get(user__id=request.user.id)
            context["data"] = data
        return render(request,"Data.html",context)
    else:
        context={}
        rio=Student_Result.objects.filter(user__id=request.user.id)
        if rio==0:
                data1 = Student_Result.objects.get(user__id=request.user.id)
                context["data1"] = data1
                # data2=ResultisOut_ForRef.objects.get()
                # context["data2"]=data2
                data = Student.objects.get(user__id=request.user.id)
                context["data"] = data
                return render(request,"resultnotout.html",context)
        if len(rio)>0:
            data1 = Student_Result.objects.get(user__id=request.user.id)
            context["data1"] = data1
            # data2=ResultisOut_ForRef.objects.get()
            # context["data2"]=data2
            data = Student.objects.get(user__id=request.user.id)
            context["data"] = data
            return render(request,"Data.html",context)
        return render(request,"Data.html",context)
    

def forgotpass(request):
    context = {}
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return HttpResponseRedirect("/admin")
        else:
            return HttpResponseRedirect("/Stud_Dash")
        # context["status"] = "Password Changed Successfully!!!"

    return render(request,"forget_pass.html",context)

import random

def reset_password(request):
    un = request.GET["username"]
    try:
        user = get_object_or_404(User,username=un)
        otp = random.randint(1000,9999)
        msz = "Dear {} \n{} is your One Time Password (OTP) \nDo not share it with others \nThanks&Regards \nMyWebsite".format(user.username, otp)
        try:
            email = EmailMessage("Account Verification ",msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            print(user.email)
            return JsonResponse({"status":"error","email":user.email})
    except:
        return JsonResponse({"status":"failed"})

def feenotpaid(request):
    context={}
    # ch = Student.objects.filter(user__id=request.user.id)
    # if len(ch)>0:
    data = Student.objects.get(user__id=request.user.id)
    context["data"] = data
    # data1=ResultisOut_ForRef.objects.get()
    # context["data1"]=data1
    return render(request,"feenotpaaid.html",context)


def resultnotout(request):
    context={}
    rio=Student_Result.objects.filter(user__id=request.user.id)
    data = Student.objects.get(user__id=request.user.id)
    context["data"] = data
    if rio==0:
                data1 = Student_Result.objects.get(user__id=request.user.id)
                context["data1"] = data1
                data = Student.objects.get(user__id=request.user.id)
                context["data"] = data
                return render(request,"resultnotout.html",context)
    return render(request,"resultnotout.html",context)
