from django.shortcuts import render,redirect
from blogs.models import Blog
from misc.models import About
from django.contrib import auth
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
def home(request):
    # categories = Category.objects.all()
    featured_post=Blog.objects.filter(is_featured=True,status='Published').order_by('updated_at')
    posts=Blog.objects.filter(is_featured=False,status='Published')
    about = About.objects.all()
    print(about)
    return render(request,'home.html',{'featured_post':featured_post,'posts':posts,'about':about})

def register(request):
    form = RegistrationForm()
    if(request.method=='POST'):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        return render(request,'register.html',{'form':form})

def login(request):
    if(request.method=='POST'):
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            print(user)
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    return render(request,'login.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('home')