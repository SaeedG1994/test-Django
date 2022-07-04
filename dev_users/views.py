from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Profile
from .form import CustomUserCreationForm

def profiles(request):
    profile = Profile.objects.all()
    context = {
        'profile':profile,

    }
    return render(request, 'Users/All-profiles.html', context)


def userProfile(request,pk):
    profile = Profile.objects.get(id=pk)
    top_skill = profile.skill_set.exclude(description__exact="")
    other_skill = profile.skill_set.filter(description="")
    context= {
        'profile':profile,
        'top_skill':top_skill,
        'other_skill':other_skill
    }
    return render(request,'Users/user-profile.html',context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'username or password is wrong')

    return render(request, 'Users/login-register-user.html')


def logoutUser(request):
    logout(request)
    messages.info(request,'You logout successfully')
    return redirect('profiles')


def registerUser(request):
    page ='register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request,'User account was created')
            login(request,user)
            return redirect('profiles')
        else:
            messages.error(request,'An Error User name or password its wrong ')

    context ={
        'page':page,
        'form':form
    }

    return render(request, 'Users/login-register-user.html',context)