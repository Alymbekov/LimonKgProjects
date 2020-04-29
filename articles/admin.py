from django.contrib import admin

from .models import Article, Comment, Category, ArticleViews

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Category)

@admin.register(ArticleViews)
class ArticleViews(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    list_display_links = ('__str__', )
    search_fields = ('__str__', )




