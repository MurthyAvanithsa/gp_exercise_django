__author__ = 'murthy'

__author__ = 'murthy'
from django.views.generic import View
from django.shortcuts import render
from blog.models import Articles
import json
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404,get_list_or_404
from article_utils import get_related_randome_article_ids, article_context_serializer
from .serializers import ArticlesSerializer

class ArticleDetailsView(View):

    template_name = "article.html"

    def get(self, request, article_id):
        req_data = request.GET
        lang = req_data.get("lang", "html")
        article = get_list_or_404(Articles, pk=article_id)
        print "Articles",article
        related_articles_ids = get_related_randome_article_ids()
        related_articles = Articles.objects.filter(id__in=related_articles_ids)
        context = {
                "article": article[0],
                "related_articles": related_articles
            }
        if lang == "html":
            response = render(request, self.template_name, context)
            return response
        if lang == "json":
            response = dict()
            articles_serilized_data = ArticlesSerializer(article, many=True).data
            related_articles_serilized_data = ArticlesSerializer(related_articles, many=True).data
            response.update({"articles":articles_serilized_data})
            response.update({"related_articles":related_articles_serilized_data})
            return HttpResponse(json.dumps(response),content_type="application/json")

