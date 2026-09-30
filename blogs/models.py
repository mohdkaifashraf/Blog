from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        
        return self.category_name


    class Meta:
        verbose_name_plural = 'category'

STATUS_CHOICES = (
    ("draft","draft"),
    ("published","published")
)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=150, auto_created=True, unique=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    featured_image = models.ImageField(upload_to='uploads/%y/%m/%d', height_field=None, width_field=None, max_length=None)
    is_featured = models.BooleanField(default=True)
    short_description = models.CharField(max_length=200, null = True)
    blog_body = models.TextField(max_length=2000)
    status = models.CharField(choices = STATUS_CHOICES, max_length=50)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)   


    def __str__(self) -> str:
        return self.title
