__author__ = 'murthy'
import random
from random import randint
import json
from django.http import HttpResponse
from django.core import serializers
from blog.models import Articles


def get_randome_article(articles):
    randome_article_number = randint(1,articles.count())
    return randome_article_number-1


def get_related_randome_article_ids(articles=None):
    articles = Articles.objects.all()
    article_ids = set(articles.values_list("id",flat=True))
    if len(article_ids) >= 4:
        return random.sample(article_ids, 4)
    else:
        return article_ids


def article_context_serializer(context):
    serializer_objects = list()
    JSONSerializer = serializers.get_serializer("json")
    json_serializer = JSONSerializer()
    if context.has_key("blogs"):
        serializer_objects.append(context['blogs'])
    if context.has_key("related_articles"):
        serializer_objects.append(context['related_articles'])
    data = json_serializer.serialize(context['article'])
    return data