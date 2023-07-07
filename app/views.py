from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

# Create your views here.
def insert_topic(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    return HttpResponse('topic data is inserted')
def insert_webpage(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter the name: ')
    u=input('enter the url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    return HttpResponse('webpage is created')
def insert_accessrecord(request):
    tn=input('enter topic name: ')
    TO=Topic.objects.get_or_create(topic_name=tn)[0]
    TO.save()
    n=input('enter the name: ')
    u=input('enter the url: ')
    WO=Webpage.objects.get_or_create(topic_name=TO,name=n,url=u)[0]
    WO.save()
    d=input('enter the date: ')
    a=input('enter the author: ')
    AR=AccessRecord.objects.get_or_create(name=WO,date=d,author=a)[0]
    AR.save()
    return HttpResponse('accessrecords are inserted')

