from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from app.forms import TopicForm
# Create your views here.
from app.classes import controller
def homePageView(request):
    return render(request,'query.html')

class AboutPageView(TemplateView):
    template_name = 'about.html'


def hello(request):
    number=779
    text = "<h1>welcome to my app number %s!</h1>"% number
    return HttpResponse(text)

def summ(request):
    if request.method=="POST":
        Topic=TopicForm(request.POST)
    
    if Topic.is_valid():
        _topic=Topic.cleaned_data['topic']
    else:
        Topic=TopicForm()
        
    summary=controller.generateSummary(_topic)
    #text = "<h1>Summary: <br><br> %s!</h1>"% summ
    return render(request,'summary.html',{"summary":summary})
