from django import forms
from django.core import validators
from app_two.models import My_Model

class My_New_Form(forms.ModelForm):
    class Meta:
        model = My_Model
        fields = "__all__"
