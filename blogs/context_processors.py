
from .models import Category, SocialLink

def get_categories(request):
    categories = Category.objects.all()

    return dict(categories = categories)

def socialink(request):
    social = SocialLink.objects.all()

    return dict(social = social)