from django.shortcuts import render
from .models import Profile

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