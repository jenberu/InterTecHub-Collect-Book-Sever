from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    
       model=Book
       list_display= ['id', 'title', 'author', 'isbn', 'published_year','is_favorite']
       


admin.site.register(Book,BookAdmin)        