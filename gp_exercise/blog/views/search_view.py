__author__ = 'murthy'

from django.views.generic import View
from django.shortcuts import render
from blog.models import Articles
from django.http import HttpResponse
from .article_utils import article_context_serializer, get_related_randome_article_ids,get_randome_article
from .serializers import ArticlesSerializer
import json


class SearchView(View):

    def get(self, request):
        req_data = request.GET
        query_string = req_data.get("query"," ")
        # case insensitive search "icontains"
        articles = Articles.objects.filter(title__icontains=query_string)
        response = dict()
        articles_serilized_data = ArticlesSerializer(articles, many=True).data
        response.update({"articles":articles_serilized_data})
        return HttpResponse(json.dumps(response), content_type="application/json")



