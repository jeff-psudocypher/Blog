from django.contrib import admin
from .models import Category,Blog
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('blog_title',)}
    list_display = ('blog_title','category','blog_author','is_featured','status')
    search_fields = ('category__category_name','id','blog_title','status')
    list_editable = ('is_featured',)

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
