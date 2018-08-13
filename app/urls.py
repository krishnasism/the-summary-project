from django.urls import path
from . import views

urlpatterns=[
        path('',views.homePageView, name='home'),
        path('summarizer/',views.summ,name='summarize'), 
        path('image/',views.imgsumm,name='imgsumm')
        ]   