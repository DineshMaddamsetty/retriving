
from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

def display_topics(request):
    topics=Topic.objects.all()
    topics=Topic.objects.filter(topic_name='Cricket')
    #topics=Topic.objects.get(topic_name='Cricket')



    d={'topics':topics}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    webpages=WebPage.objects.all()
    webpages=WebPage.objects.filter(name='Gowtham')
    #webpages=WebPage.objects.get(name='Gowtham')
    webpages=WebPage.objects.exclude(name='Gowtham')
    # arange topic name based on ascii values
    webpages=WebPage.objects.all().order_by('topic_name')
    webpages=WebPage.objects.all().order_by('-topic_name')
    webpages=WebPage.objects.all().order_by('-topic_name')
    webpages=WebPage.objects.all().order_by(Length('topic_name'))
    webpages=WebPage.objects.all().order_by(Length('topic_name').desc())
    #slicing
    webpages=WebPage.objects.all()[::-1]
    #slicing
    webpages=WebPage.objects.all()[1::]
    #slicing
    webpages=webpage.objects.all()[:2:-1]
    #webpages=WebPage.objects.all()[::-1]
    d={'webpages':webpages}
    return render(request,'display_webpages.html',d)

def display_accessrecords(request):
    accessrecords=AccessRecords.objects.filter()
    d={'accessrecords':accessrecords}
    return render(request,'display_accessrecords.html',d)


