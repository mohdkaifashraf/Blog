from django.contrib import admin
from django.http import HttpRequest
from .models import Category, Blog, About, SocialLink, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':['title']}
    list_display = ['title', 'category' ,'author', 'is_featured', 'status']
    search_fields = ['id', 'title', 'category__category_name', 'status']
    list_editable = ['is_featured', 'category']


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request) -> bool:
        count = About.objects.all().count()

        if count == 0:
            return True
        else:
            return False

admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)
admin.site.register(Comment)


