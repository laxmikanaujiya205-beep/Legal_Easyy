from django.shortcuts import render,redirect
from .models import User, Feedback, Contact, LegalAdvisor
from django.contrib import messages

def user_logout(request):
   request.session.flush()
   messages.success(request,"Successfully logged out!!")
   return redirect("user_login")

def user_home(request):
    # fetching email from session to identify the user
    if request.method=="GET":
       user_email=request.session["web_key"]
       User_Obj=User.objects.get(email=user_email)#it will return a single object
    #sending data from view to html(template) page
    #create a dictionary and bind the data with a key 
    #send that dict with render function

       user_dict={
        "user_key":User_Obj
        }

       return render(request,"legal_app/user/user_home.html",user_dict)
# Create your views here.
def user_login(request):
    if request.method=="GET":
        return render(request,'legal_app/user/user_login.html')
    if request.method=="POST":
        user_email=request.POST["email"]
        user_password=request.POST["password"]
        ## select * from user where email.userEmail and 
        user_list=User.objects.filter(email=user_email,password=user_password)   
        if len(user_list)>0:
            request.session["web_key"]=user_email #binding email in a session to track user for multiple request
            return redirect("user_home")

        else:
            messages.error(request,"Invalid Credentials") 
            return redirect("user_login")


def user_feedback(request):
    if request.method=="GET":
     return render(request, 'legal_app/user/user_feedback.html')
    if request.method=="POST":
     user_name=request.POST["name"]
     user_email=request.session["web_key"]
     user_rating=request.POST["rating"]
     user_remarks=request.POST["message"]

    feedback_obj=Feedback(name=user_name,email=user_email,rating=user_rating,remarks=user_remarks )
    feedback_obj.save()
    messages.success(request,"...Thankyou for your Feedback...")
    return redirect("user_feedback")


def user_registration(request):
    if request.method=="GET":
       return render(request, 'legal_app/user/user_registration.html')
    if request.method=="POST":
       name = request.POST["name"]
       email=request.POST["email"]
       password = request.POST["password"]
       phone = request.POST["phone"]
       profile_pic = request.FILES["profile_pic"]
       print(name,email,password,phone,profile_pic)
       user_obj = User(name=name,email=email,password=password,phone=phone,profile_pic=profile_pic)
       user_obj.save()
       return redirect("user_login")


def user_advisors(request):
    LegalAdvisor_list=LegalAdvisor.objects.all()
    context={

        "legalAdvisor_key":LegalAdvisor_list
    }
    
    return render(request,'legal_app/user/user_advisors.html',context)

def upload_document(request):
   
    return render(request,'legal_app/user/upload_document.html')


def user_edit_profile(request):
   
    if request.method=="GET":
             user_email=request.session["web_key"]
             User_Obj=User.objects.get(email=user_email)
             user_dict={
                "user_key":User_Obj
                }
             return render(request,'legal_app/user/user_edit_profile.html',user_dict)
    


    if request.method=="POST":
             user_name=request.POST["name"]
             user_phone=request.POST["phone"]
             user_pic=request.FILES.get("pic")
             user_email=request.session["web_key"]
             User_Obj=User.objects.get(email=user_email)
             if user_pic is not None:
                 User_Obj.profile_pic=user_pic
             User_Obj.name=user_name
             User_Obj.phone=user_phone
             User_Obj.save()
             messages.success(request,"Profile updated Succesfully👍") 
             return redirect("user_home")   