from django import forms
from django.contrib.admin import widgets

from .models import Interview


class InterviewForm(forms.ModelForm):
    title = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control form-control-lg','placeholder':'Заголовок'}))
    description = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Описание'}))
    complete = forms.CheckboxSelectMultiple()
    task_date = forms.SplitDateTimeField(required=False,widget=widgets.AdminSplitDateTime)


    class Meta:
        model = Interview
        fields = ['title', 'description', 'complete','task_date']


