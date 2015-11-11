from django.contrib import admin

# Register your models here.

from .models import ArticleAuthor, Articles, Category


class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "published_date", "hero_image_link", "blog_image_link")


class ArticleAuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "author_name")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

admin.site.register(Articles, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ArticleAuthor, ArticleAuthorAdmin)
