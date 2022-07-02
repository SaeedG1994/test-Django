from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
            print('user name does not exist')
        user = authenticate(request,username=username,password=password)
        if request is not None:
            login(request,user)
            return redirect('profiles')
        else:
            print('username or password is wrong')

    return render(request,'Users/login-user.html')


def logoutUser(request):
    logout(request)
    return redirect('profiles')