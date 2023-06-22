
from django.shortcuts import render
from app.models import *

def display_topics(request):
    topics=Topic.objects.filter()
    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=WebPage.objects.filter()
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    accessrecords=AccessRecords.objects.filter()
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)


