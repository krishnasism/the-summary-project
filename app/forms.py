# -*- coding: utf-8 -*-
from django import forms


class TopicForm(forms.Form):
   input = forms.CharField(max_length=100)


class UserTextForm(forms.Form):
   input = forms.CharField()
