from django.views.generic import View
from django.shortcuts import render
from blog.models import Articles
from django.http import HttpResponse
from .article_utils import article_context_serializer, get_related_randome_article_ids,get_randome_article
from .serializers import ArticlesSerializer
import json

__author__ = 'murthy'


class ArticlesView(View):

    template_name = "dashboard.html"

    def get(self, request):
        req_data = request.GET
        lang = req_data.get("lang","html")
        articles = Articles.objects.all()
        random_article = articles[get_randome_article(articles)]
        related_articles_ids = get_related_randome_article_ids(articles)
        related_articles = articles.filter(id__in= related_articles_ids)
        context = {
                "blogs": articles,
                "random_article" : random_article,
                "related_articles" : related_articles
            }
        if lang == "html":
            response = render(request, self.template_name, context)
            return response
        else:
            response = dict()
            articles_serilized_data = ArticlesSerializer(articles, many=True).data
            random_article_serilized_data = ArticlesSerializer(random_article).data
            related_article_serilized_data = ArticlesSerializer(related_articles,many=True).data
            response.update({"articles":articles_serilized_data})
            response.update({"related_articles":related_article_serilized_data})
            response.update({"random_article":random_article_serilized_data})
            return HttpResponse(json.dumps(response), content_type="application/json")



