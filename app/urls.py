from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('summarizer/', views.summ, name='summarize'),
    path('imageupload/', views.imagePageView, name='imgPageView'),
    path('imgadd/', views.imageUpload, name='imgUpload'),
    path('summaryText/', views.textSummaryPageView, name='summaryTextView'),
]
