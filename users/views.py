from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registerform
# Create your views here.
def register(request):
    if(request.method=='POST'):
        form=registerform(request.POST)
        if(form.is_valid()):
            form.save()
            data=form.cleaned_data.get('username')
            messages.success(request,f"Welcome, registration succesfull {data}")
            return redirect('food:Food_List')
    else:
        form=registerform()
    return render(request,"users/register.html",{'form':form})
