from django.contrib import admin
from .models import BlogPost
from contact.models import Contact


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, CategoryAdmin)
admin.site.register(Contact)
