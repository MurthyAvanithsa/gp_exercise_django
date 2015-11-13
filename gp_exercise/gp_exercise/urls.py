"""gp_exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from blog.views.articles_view import ArticlesView
from blog.views.article_details_view import ArticleDetailsView
from blog.views.search_view import SearchView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
    url(r'^homepage/$', ArticlesView.as_view(), name="article"),

    url(r'^article/(?P<article_id>[0-9]+)/$', ArticleDetailsView.as_view(), name="article-details"),
    url(r'^search/', SearchView.as_view(), name="article-search"),
]
