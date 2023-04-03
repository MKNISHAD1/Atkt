from django import forms
from Home.models import *

class test_form(forms.ModelForm):
    class Meta:
        model =Student_Result
        # fields=["PRN","Name","Email"] // for selective option
        fields="__all__" #// for all field
        # exclude=["user"] # for removing that field 
        widget=forms.Select(attrs={'class':'narrow-select'})


