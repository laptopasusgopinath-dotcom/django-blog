from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category'),
    path('blogs/<slug:slug>/', blogs, name='blogs'),
    path('search/', search, name='search'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('comment/delete/<int:id>/', delete_comment, name='delete_comment'),
]