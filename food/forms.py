from django import forms
from .models import food
class addform(forms.ModelForm):
    class Meta:
        model=food 
        fields=['dish','price','description','image']
class updateform(forms.ModelForm):
    class Meta:
        model=food
        fields=['dish','price','description','image']