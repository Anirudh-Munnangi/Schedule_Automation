from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse
from . import models
import os,sys
# Performing import of script settings
current_path=os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_path)
try:
    from settings import script_settings as ss
except ImportError:
    print("Cannot Import Settings Module")
# Create your views here.

def sign_up(request):
    if request.method == 'POST':
        print(request.POST.get("uname"))
        print(request.POST.get("email"))
        print(request.POST.get("pwd"))
        user=User.objects.create_user(request.POST.get("uname"),request.POST.get("email"),request.POST.get("pwd"))
        # Update fields and then save again
        user.first_name = request.POST.get("fname")
        user.last_name = request.POST.get("lname")
        user.save()
    else:
        return(render(request,"form_automation/sign_up.html",{}))

def user_view_redirect(request):
    if (request.user).groups.filter(name="Services").exists():
        user_value=(User.objects.get(username=request.user))
        users_request_objects=models.RequestDetails.objects.filter(request_ownername=str(user_value))
        return(render(request,'form_automation/service_index.html',{'requests':users_request_objects}))
    else:
        if request.method =="POST":
            number=request.POST.get("pno")
            email=request.POST.get("email_val")
            category=request.POST.get("category")
            date_time=request.POST.get("atime")
            name=request.POST.get("proname")
            owner=ss.dict_of_services[request.POST.get("category")]
            instance_of_RequestDetails=models.RequestDetails()
            instance_of_RequestDetails.create_request(number,email,category,date_time,name,owner)
            #return(HttpResponse("Thank you for submitting a schedule request. \n\nYou shall be replied by text to your phone number when your request is approved."))
            return(HttpResponse("<p>Thank you for submitting a schedule request. \n\nYou shall be replied by text to your phone number when your request is approved.</p><a href=''>Click to submit another</a>"))
        else:
            return(render(request,"form_automation/user_index.html",{}))
