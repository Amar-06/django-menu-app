from django import forms
from .models import food
# class addform(forms.ModelForm):
#     class Meta:
#         model=food 
#         fields=['dish','price','description','image']
# class updateform(forms.ModelForm):
#     class Meta:
#         model=food
#         fields=['dish','price','description','image']
class FoodForm(forms.ModelForm):

    class Meta:
        model = food

        fields = [
            'dish',
            'price',
            'description',
            'image'
        ]

        widgets = {

            'dish': forms.TextInput(
                attrs={'class': 'form-control'}
            ),

            'price': forms.NumberInput(
                attrs={'class': 'form-control'}
            ),

            'description': forms.Textarea(
                attrs={'class': 'form-control'}
            ),

            'image': forms.URLInput(
                attrs={'class': 'form-control'}
            ),
        }