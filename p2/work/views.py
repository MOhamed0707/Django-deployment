from django.shortcuts import render
from work.forms import UserForm , UserInfoForm  # import modelforms
from django.urls import reverse   # have changed from django.core.urlresolvers to django.urls
from django.contrib.auth.decorators import login_required  # decorators uesifull in logged in and out
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse





# Create your views here.
def base(request):    #base page
    return render(request,'pages/base.html')

@login_required   #checked if user is active its mean that if there are some one logged in or not
def special(request):
    return HttpResponse("You Are Logged In ,Nice!!")   #if logged in goes to a page of special indicate successful logeed in



@login_required    #checked if user is active its mean that if there are some one logged in or not
def use_logout(request):
    logout(request)        # if logged in it do logging off
    return HttpResponseRedirect(reverse('base'))  #then back to base paage

def GD(request):
    
    return render(request,'pages/p2.html')

def register(request):
    registered=False
    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile= profile_form.save(commit = False)
            profile.user =user

            if 'user_profile_pic' in request.FILES:
                profile.user_profile_pic =request.FILES['user_profile_pic']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserInfoForm()
    return render(request,'pages/p3.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('base'))
            else:
                return HttpResponse("Account not Active")
        else:
            print("Someone tried to login and failed!!!")
            print("username:{} and password:{}.formate(username,password)")
            return HttpResponse("Invalid LogIn details supplied")
    else:
        return render(request,'pages/p4.html',{})
