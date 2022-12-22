from django import forms
from .models import Tracker_model

class Add_expense_form(forms.ModelForm):
    class Meta:
        model=Tracker_model
        fields = '__all__'
        widgets={'Date':forms.DateInput(attrs={'type':'date'})}