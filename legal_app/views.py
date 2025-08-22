from django.shortcuts import render,redirect
from . models import Contact, FirmService,Feedback,User, LegalAdvisor
# Create your views here.
def home(request):
    feedback = Feedback.objects.all()
    data=[]
    for i in feedback:
        data.append(
            {
                "rating":i.rating,
                "remarks":i.remarks,
                "name":i.name,
                "profile_pic":User.objects.filter(email=i.email)[0].profile_pic
            }
        )
    feedback_dict={
           "feedback_key":data
    }


        

    return render(request,'legal_app/html/index.html',feedback_dict)
def about_us(request):
    return render(request, 'legal_app/html/about_us.html')


def contact_us(request):
   if request.method=="GET":
      return render(request, 'legal_app/html/contact_us.html')
   if request.method=="POST":
       name = request.POST["name"]
       email=request.POST["email"]
       phone = request.POST["phone"]
       query = request.POST["query"]
       print(name,email,phone,query)
       contact_obj = Contact(name=name,email=email,query=query,phone=phone)
       contact_obj.save()
       return redirect("home")

def  view_services(request):
    FirmService_list=FirmService.objects.all()#select * from firm service
    context={
               "service_key":FirmService_list

    }

    return render(request,'legal_app/html/view_services.html',context)


def our_advisors(request):
    LegalAdvisor_list=LegalAdvisor.objects.all()
    context={

        "legalAdvisor_key":LegalAdvisor_list
    }
    
    return render(request,'legal_app/html/our_advisors.html',context)

