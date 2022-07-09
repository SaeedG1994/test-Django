from django.shortcuts import render,redirect
from django.contrib.auth.decorators import  login_required
from .models import Project, Tag
from .form import ProjectForm
from django.contrib import messages
from .utils import projectSearch,paginatorProject


def projects(request):
    projects,search_query= projectSearch(request)
    custom_range,projects = paginatorProject(request,projects,6)
    context ={'projects':projects,'search_query':search_query,'custom_range':custom_range}
    return render(request,'projects/projects.html',context)


def single_project(request,pk):
    single_pro = Project.objects.get(id=pk)
    tags = single_pro.tags.all()
    context = {
        'project':single_pro,
        'tags':tags
    }
    return render(request,'projects/single-projects.html',context)

@login_required(login_url="login_user")
def create_project(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            form.save()
            messages.success(request,'Your Project Successfully Created!')
            return redirect('user_account')
    context = {
        'form':form
    }
    return render(request,'projects/create-project.html/',context)

@login_required(login_url="login_user")
def update_project(request,pk):
    profile = request.user.profile
    project =profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Project Successfully Updated!')
            return redirect('user_account')
    context ={
        'form':form,
    }
    return render(request,'projects/create-project.html/',context)

@login_required(login_url="login_user")
def delete_project(request,pk):
    profile = request.user.profile
    project =profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        messages.success(request,'Your Project Successfully Deleted!')
        return redirect('user_account')
    context ={
        'object':project,
    }
    return render(request, 'Shared/delete-form.html', context)