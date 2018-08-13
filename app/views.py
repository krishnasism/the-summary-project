from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from app.classes import controller

from app.forms import TopicForm

from django.core.files.storage import FileSystemStorage
import os



def homePageView(request):
    return render(request,'query.html')

def summ(request):
    if request.method=="POST":
        Topic=TopicForm(request.POST)
    
    if Topic.is_valid():
        _topic=Topic.cleaned_data['topic']
    else:
        Topic=TopicForm()
        
    summary=controller.generateSummary(_topic)
    return render(request,'summary.html',{"summary":summary})

def imagePageView(request):
    return render(request,"imageupload.html")

def imageUpload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(BASE_DIR+'\\app\\static\\images\\'+myfile.name, myfile)
        #uploaded_file_url = fs.url(filename)
        summary = controller.generateImageSummary(myfile.name)
        
        return render(request,'summary.html',{"summary":summary})
        #text = "Image Uploaded<br><br>"+imageSumm1
        #return HttpResponse(text)
    
    return render(request, 'imageupload.html')