from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.db.models import Q
from .models import Blog, Category, Comment
from django.db.models import Q

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


def blogs(request, slug):

    single_blog = get_object_or_404(Blog, slug=slug, status = 'published')

    if request.method=='POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()

        return redirect('blogs', slug=single_blog.slug)

    # comments
    comments = Comment.objects.filter(blog =single_blog)
    comment_count= comments.count()

    context={
        'single_blog': single_blog,
        'comments':comments,
        'comment_count':comment_count
    }

    return render(request, 'blogs.html', context)

def search(request):

    keyword  = request.GET.get('keyword')
    blogs = Blog.objects.filter(
    Q(title__icontains=keyword) |
    Q(short_description__icontains=keyword) |
    Q(blog_body__icontains=keyword),
    status='published'
)
    print(blogs)

    context = {
        'blogs':blogs,
        'keyword':keyword
    }
    return render(request, 'search.html', context)
