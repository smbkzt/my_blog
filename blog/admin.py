from django.contrib import admin
from .models import BlogPost


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('post_article',)}


admin.site.register(BlogPost, CategoryAdmin)
