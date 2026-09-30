from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Blog, Category

def post_by_category(request, category_id):
    posts = Blog.objects.filter(status = 'published', category_id = category_id)
    
    #  use try except when you want to redirect some other place
    try:
        category =  Category.objects.get(pk=category_id)

    except:

        return redirect('home')

    # use get_object_or_404 if you want to show 404 error
    # category =  get_object_or_404(Category, pk=category_id)

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'post_by_category.html', context)
