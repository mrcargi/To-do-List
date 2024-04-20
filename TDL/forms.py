from django import forms
from . import models
from django.forms import ModelForm


class TaskForm(ModelForm):
    
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class':'form-control','rows':3})
    )

    class Meta:
        model = models.Task
        fields = ['title','description','deadline']
        widgets = {
            'deadline': forms.DateInput(attrs={'type': 'date'}),
            'user':forms.HiddenInput()
            }
        
