from django.shortcuts import render,redirect,get_object_or_404
from blogs.models import Category,Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    return render(request,'dashboard/dashboard.html',{'category_count':category_count,'blogs_count':blogs_count})


def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if(request.method=='POST'):
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('categories')
    form = CategoryForm()
    return render(request,'dashboard/add_category.html',{'form':form})

def edit_category(request,pk):

    category = get_object_or_404(Category, pk=pk)
    if(request.method=='POST'):
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form = CategoryForm(instance=category)
    return render(request,'dashboard/edit_category.html',{'form':form,'category':category})

def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')