from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import registerform
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if(request.method=='POST'):
        form=registerform(request.POST)
        if(form.is_valid()):
            form.save()
            data=form.cleaned_data.get('username')
            messages.success(request,f"Welcome, registration succesfull {data}")
            return redirect('login')
    else:
        form=registerform()
    return render(request,"users/register.html",{'form':form})
def logout_user(request):
    logout(request)
    return render(request,'users/Logout.html')
@login_required
def profilepage(request):
    return render(request,'users/profile.html')
