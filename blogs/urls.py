from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
    path('blogs/<slug:slug>/', blogs, name='blogs'),
    path('blogs/search/', search, name='search'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]