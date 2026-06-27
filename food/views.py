from django.shortcuts import render, redirect, get_object_or_404

from .models import food
from .forms import FoodForm

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# ---------------- LIST VIEW ----------------

class FoodList_classview(ListView):

    model = food

    template_name = 'food/foodlist.html'

    context_object_name = 'food_list'


# ---------------- DETAIL VIEW ----------------

class FoodDetail_classview(DetailView):

    model = food

    template_name = 'food/detail.html'

    context_object_name = 'food_details'


# ---------------- ADD FOOD ----------------

def add_food(request):

    form = FoodForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:Food_List')

    return render(
        request,
        'food/foodadd.html',
        {'form': form}
    )
#class based 
class FoodCreateView(CreateView):
    model = food

    fields = ['dish', 'price',
              'description', 'image']

    template_name = 'food/foodadd.html'

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)


# ---------------- UPDATE FOOD ----------------

def update_food(request, pk):

    item = get_object_or_404(food, pk=pk)

    form = FoodForm(
        request.POST or None,
        instance=item
    )

    if form.is_valid():
        form.save()
        return redirect('food:Food_List')

    return render(
        request,
        'food/foodupdate.html',
        {
            'form': form,
            'item': item
        }
    )


# ---------------- DELETE FOOD ----------------

def delete_food(request, pk):

    item = get_object_or_404(food, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('food:Food_List')

    return render(
        request,
        'food/fooddelete.html',
        {'item': item}
    )
'''
def item(request):
    return HttpResponse("Welcome")
def my_Intro(request):
    return HttpResponse('My name is Amar pandey, i am a python developer.')


def Food_List(request):
    Food_List=food.objects.all()
    return render(request,'food/foodlist.html',{'Food_List':Food_List})
class FoodList_classview(ListView):
    model=food
    template_name="food/foodlist.html"
    context_object_name='food_list'


def Food_details(request,dish):
    food_details= food.objects.get(dish=dish)
    return render(request,'food/detail.html',{'food_details':food_details})

class FoodDetail_classview(DetailView):
    model=food
    template_name="food/detail.html"
    context_object_name='food_details'
    slug_field = 'dish'
    slug_url_kwarg = 'dish'

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
'''