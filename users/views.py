from django.shortcuts import render,redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages

# Create your views here.
def index(request):
    context={}
    return render(request,'users/index.html',context)

def register(request):
    # let's check if the request is a POST
    # IF SO; let's validate the form usisng the is_valid function
    
    if request.method=='POST':
        form=NewUserForm(request.POST)
        if form.is_valid(): 
            user=form.save()
            login(request,user)
            messages.success(request,"Registered successfully")
            return redirect("users/index.html")
        messages.error(request,"failed to register try again")
        #say the request is NOT POST we return an empty form 
    form=NewUserForm()
            
    return render(request,'users/register.html',context={"register_form":form})
