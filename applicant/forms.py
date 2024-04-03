from django.forms import ModelForm
from .models import ApplicantPersonalFile
from django import forms

myDateInput = forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'})


class ApplicantForm(ModelForm):
    class Meta:
        model = ApplicantPersonalFile
        fields = '__all__'
        widgets = {'date_of_birth': myDateInput}