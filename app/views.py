from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

from app.classes import controller

from app.forms import TopicForm, UserTextForm

from django.core.files.storage import FileSystemStorage
import os
import logging


def homePageView(request):
    return render(request, 'query.html')


def textSummaryPageView(request):
    return render(request, 'summarisetext.html')


def summ(request):
    CurrentForm = None
    text_summary = False
    if request.method == "POST":
        if "summaryText" in request.META['HTTP_REFERER']:
            CurrentForm = UserTextForm(request.POST)
            text_summary = True
        else:
            CurrentForm = TopicForm(request.POST)

    _input = ""
    if CurrentForm.is_valid():
        _input = CurrentForm.cleaned_data['input']
    else:
        CurrentForm = TopicForm()
    if _input and len(str(_input).strip()) != 0:
        summary = controller.generateSummary(_input, text_summary)
        return render(request, 'summary.html', {"summary": summary})
    else:
        return homePageView(request)


def imagePageView(request):
    # Unused
    return render(request, "imageupload.html")


def imageUpload(request):
    # Unused
    if request.method == 'POST' and request.FILES['myfile']:
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(
            BASE_DIR+'\\app\\static\\images\\'+myfile.name, myfile)
        summary = controller.generateImageSummary(myfile.name)

        return render(request, 'summary.html', {"summary": summary})

    return render(request, 'imageupload.html')
