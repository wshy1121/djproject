from django.contrib import admin
from .models import Article

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
    search_fields = ('title', 'content',)
    list_filter = ('title',)


admin.site.register(Article, ArticleAdmin)

