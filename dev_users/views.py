from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Profile
from .form import CustomUserCreationForm, ProfileEditForm,SkillForm,MessageForm
from .utils import profileSearch,profilePaginator

def profiles(request):
    profiles,search_query= profileSearch(request)
    custom_range,profiles = profilePaginator(request,profiles,12)
    context = {
        'profiles': profiles,
        'search_query':search_query,
        'custom_range':custom_range,
    }
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
            messages.success(request,'login is successfully! 😎')
            return redirect(request.GET['next'] if 'next' in request.GET else 'user_account')
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
            return redirect('user_account')
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



@login_required(login_url="login_user")
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



@login_required(login_url="login_user")
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



@login_required(login_url="login_user")
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



@login_required(login_url="login_user")
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



@login_required(login_url="login_user")
def inbox(request):
    profile = request.user.profile
    messageRequest = profile.messages.all()
    unreadMessage = messageRequest.filter(is_read=False).count()
    context ={
        'messageRequest':messageRequest,
        'unreadMessage':unreadMessage,
    }
    return render(request,'Users/inbox.html',context)

@login_required(login_url="login_user")
def viewMessage(request,pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {
        'message':message,
        'profile':profile,

    }
    return render(request,'Users/view_Message.html',context)


def createMessage(request,pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient
            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request,'Your Message Successfully sent!')
            return redirect('user-profile',pk=recipient.id)

    context ={
        'form':form,
        'recipient':recipient,
    }
    return render(request,'Users/message_form.html',context)