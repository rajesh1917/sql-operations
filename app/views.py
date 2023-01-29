from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length

# Create your views here.

def display_topic(request):
    QST=Topic.objects.all()
    #QST=Topic.objects.filter(topic_name='Cricket')
    d={'Topic':QST}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    QSW=Webpage.objects.all()
    QSW=Webpage.objects.filter(topic_name='Cricket')
    
    QSW=Webpage.objects.all()[:5:]
    QSW=Webpage.objects.all().order_by('name')
    QSW=Webpage.objects.order_by('-name')
    QSW=Webpage.objects.filter(topic_name='Kabaddi').order_by('-name')
    
    QSW=Webpage.objects.all().order_by(Length('name'))
    
    QSW=Webpage.objects.all().order_by(Length('name').desc())

    #QSW=Webpage.objects.all()
    d={'Webpage':QSW}
    return render(request,'display_webpage.html',d)

def display_access(request):
    QSA=AccessRecord.objects.all().order_by('date')
    #QSA =AccessRecord.objects.all()
    d={'AccessRecord':QSA}
    return render(request,'display_access.html',d)