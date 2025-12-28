from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', posts_by_category, name='posts_by_category')
]