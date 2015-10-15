from django.contrib import admin
from books.models import Publisher, Author, Book  
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date')
    list_filter = ('publisher', 'publication_date')
    ordering = ('-publication_date',)
    search_fields = ('title',)

admin.site.register(Publisher)  
admin.site.register(Author)  
admin.site.register(Book, BookAdmin) 

