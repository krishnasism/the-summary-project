#-*- coding: utf-8 -*-
from django import forms

class TopicForm(forms.Form):
   topic = forms.CharField(max_length = 100)

