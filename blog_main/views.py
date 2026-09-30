
from django.shortcuts import render
from blogs.models import Category, Blog, About
def home(request):

    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured = True, status = 'published').order_by('updated_at')
    print(featured_post)
    posts = Blog.objects.filter(is_featured = False, status = 'published').order_by('updated_at')

    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'categories': categories,
        'featured_post':featured_post,
        'posts':posts,
        'about':about,
    }

    return render(request, 'home.html', context)