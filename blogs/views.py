from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request): 
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    context = { 
        'featured_posts': featured_posts,
        'posts': posts,
    }
    return render(request, 'home.html', context)

def posts_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    posts = Blog.objects.filter(status='Published', category=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html', context)
