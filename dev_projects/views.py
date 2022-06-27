from django.shortcuts import render,redirect
from .models import Project, Tag
from django.http import  HttpResponse
from .form import ProjectForm


def projects(request):
    pro = Project.objects.all()
    context ={
        'projects':pro,
    }
    return render(request,'projects/projects.html',context)


def single_project(request,pk):
    single_pro = Project.objects.get(id=pk)
    tags = single_pro.tags.all()
    context = {
        'project':single_pro,
        'tags':tags
    }
    return render(request,'projects/single-projects.html',context)


def create_project(request):
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {
        'form':form
    }
    return render(request,'projects/create-project.html/',context)


def update_project(request,pk):
    project =Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method =='POST':
        form = ProjectForm(request.POST,instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context ={
        'form':form,
    }
    return render(request,'projects/create-project.html/',context)

def delete_project(request,pk):
    project =Project.objects.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context ={
        'object':project,
    }
    return render(request,'projects/delete-project.html',context)