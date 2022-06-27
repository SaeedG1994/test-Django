from django.shortcuts import render


def profiles(request):
    return render(request, 'Users/profiles.html')