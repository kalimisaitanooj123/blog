from django.contrib import admin

# Register your models here.
from .models import *

from django.contrib import admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'name', 'content')
    list_filter = ("name",)
    search_fields = ['title', 'content']

admin.site.register(Blog, PostAdmin)

class Contact1(admin.ModelAdmin):
    admin.site.register(Contact)