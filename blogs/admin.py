from django.contrib import admin
from .models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'status', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status')
    list_editable = ('is_featured',)

class aboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About, aboutAdmin)
admin.site.register(SocialLink)