from django.shortcuts import render

from assignments.models import About

# Create your views here.
def about(request):
    about = About.objects.all()
    context = {
        'about': about,
    }

    return render(request, 'home.html', context)

def SocialLink(request):
    social_links = SocialLink.objects.all()
    context = {
        'social_links': social_links,
    }
    return render(request, 'home.html', context)