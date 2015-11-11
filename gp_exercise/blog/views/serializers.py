__author__ = 'murthy'
from rest_framework.serializers import ModelSerializer
from blog.models import Articles, ArticleAuthor, Category
from rest_framework import serializers

class AuthorSerializer(ModelSerializer):
    """
    A serializer for ``Author``.
    """
    class Meta(object):
        model = ArticleAuthor


class CategorySerializer(ModelSerializer):
    """
    A serializer for ``Category``.
    """
    class Meta(object):
        model = Category


class ArticlesSerializer(ModelSerializer):
    """
    A serializer for ``Articlees
    """
    author = AuthorSerializer()
    category = CategorySerializer()

    class Meta(object):
        model = Articles


