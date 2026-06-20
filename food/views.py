from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .forms import addform, updateform
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
def add_food(request):
    form = addform(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:Food_List')

    return render(request, 'food/foodadd.html', {'form': form})
def update_food(request,dish):
    item=food.objects.get(dish=dish)
    form=updateform(request.POST or None, instance=item)
    if(form.is_valid()):
        form.save()
        return redirect('food:Food_List')
    return render(request,'food/foodupdate.html',{'form':form, 'item':item})
def delete_food(request,dish):
    item=food.objects.get(dish=dish)
    if(request.method=='POST'):
        item.delete()
        return redirect('food:Food_List')
    return render(request,'food/fooddelete.html',{'item':item})
