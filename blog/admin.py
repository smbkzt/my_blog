from django.contrib import admin
from contact.models import Contact

from .models import BlogPost


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    # formfield_overrides = {
    #     models.TextField: {'widget': AdminDraceditorWidget},
    # }


admin.site.register(BlogPost, CategoryAdmin)
admin.site.register(Contact)
