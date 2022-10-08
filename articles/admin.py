from django.contrib import admin
from articles.models import Article
from articles.models import ArticleNER


class ArticleAdmin(admin.ModelAdmin):
    pass

class ArticleNERAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleNER, ArticleNERAdmin)
