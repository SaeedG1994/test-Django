from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .form import CustomUserCreationForm, ProfileEditForm,SkillForm
from .utils import profileSearch

def profiles(request):
    profiles,search_query= profileSearch(request)
    context = {'profiles': profiles,'search_query':search_query}
    return render(request, 'Users/All-profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    top_skill = profile.skill_set.exclude(description__exact="")
    other_skill = profile.skill_set.filter(description="")
    context = {
        'profile': profile,
        'top_skill': top_skill,
        'other_skill': other_skill
    }
    return render(request, 'Users/user-profile.html', context)


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('profiles')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'username or password is wrong')

    return render(request, 'Users/login-register-user.html')


def logoutUser(request):
    logout(request)
    messages.info(request, 'You logout successfully')
    return redirect('profiles')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'User account was created')
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'An Error User name or password its wrong ')

    context = {
        'page': page,
        'form': form
    }

    return render(request, 'Users/login-register-user.html', context)


def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {
        'profile': profile,
        'skills': skills,
        'projects': projects
    }
    return render(request, 'Users/userAccount.html', context)

@login_required(login_url='login_user')
def editProfile(request):
    profile = request.user.profile
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'your profile has been updated')
            return redirect('user_account')
    context = {
        'form': form,

    }
    return render(request, 'Users/edit_ProfileForm.html', context)

@login_required(login_url='login_user')
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    if request.method == 'POST':
        form = SkillForm(request.POST)
        skill = form.save(commit=False)
        skill.owner = profile
        skill.save()
        messages.success(request,'Your Skill successfully added!---Thanks')
        return redirect('user_account')
    context = {
        'form':form
    }
    return render(request,'Users/skill-form.html',context)

@login_required(login_url='login_user')
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if request.method == 'POST':
        form =SkillForm(request.POST,instance=skill)
        form.save()
        messages.success(request,'Your Skill was Updated successfully!')
        return redirect('user_account')
    context = {
        'form':form
    }
    return render(request,'Users/skill-form.html',context)


def deleteSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == 'POST':
        skill.delete()
        messages.success(request,'Your Skill deleted Successfully!')
        return redirect('user_account')
    context ={
        'object':skill
    }
    return render(request,'Shared/delete-form.html',context)