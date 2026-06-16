from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse

from .models import food
# Create your views here.
def item(request):
    return HttpResponse("Welcome")
def my_Intro(request):
    return HttpResponse('My name is Amar pandey, i am a python developer.')
def Food_List(request):
    Food_List=food.objects.all()
    return render(request,'food/foodlist.html',{'Food_List':Food_List})
def Food_details(request,dish):
    food_details= food.objects.get(dish=dish)
    return render(request,'food/detail.html',{'food_details':food_details})