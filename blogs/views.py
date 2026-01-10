from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

# Create your views here.

def home(request): 
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published').order_by('updated_at')
    # Fetch about us
    try:
        about = About.objects.get()
    except:
        about = None
    context = { 
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
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


def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    '''
    if request.method == "POST":
        comment = request.POST.get("comment")
        Comment.objects.create(
            comment = comment,
            user = request.user,
            blog = single_blog
        )
    '''

    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST.get("comment")
        comment.save()
        return HttpResponseRedirect(request.path_info) # when redirect to same page use HttpResponseRedirect


    # Comments
    comments = Comment.objects.filter(blog=single_blog).order_by('-created_at')
    comment_count = comments.count()
    context = {
        'single_blog': single_blog,
        'comments': comments,
        'comment_count': comment_count
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword', '').strip()
    if not keyword:
        blogs = Blog.objects.none()
    else:
        blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    return render(request, 'search.html', {'blogs': blogs, 'keyword': keyword})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('home')

    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    auth.logout(request)
    return redirect('home')
