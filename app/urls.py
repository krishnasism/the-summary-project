from django.urls import path
from . import views

urlpatterns=[
        path('',views.homePageView, name='home'),
        path('about/', views.AboutPageView.as_view(), name='about'),
        path('number/',views.hello,name='number'),
        path('summarizer/',views.summ,name='summarize'),
        ]   