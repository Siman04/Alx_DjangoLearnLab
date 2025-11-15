from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author') 
    ordering = ('-publication_year',) 

class CustomUserAdmin(UserAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
