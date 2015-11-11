from django.db import models
from .utils import get_blog_image_path, get_hero_image_path
# Create your models here.


class ArticleAuthor(models.Model):
    author_name = models.CharField(max_length=256, null=False)

    def __unicode__(self):
        return "%s-%s"%(self.pk, self.author_name)


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return "%s-%s"%(self.pk, self.name)


# Todo check for perfect sizes before submitting to Gale
class Articles(models.Model):
    title = models.CharField(max_length=256)
    author = models.ForeignKey(ArticleAuthor)
    published_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category)
    hero_image = models.ImageField(upload_to="hero_image/", blank=True)
    blog_image = models.ImageField(upload_to="blog_image/", blank=True)
    article_text = models.TextField(max_length=1000)

    def hero_image_link(self):
        if self.hero_image:
            return '<a href="' + str(self.hero_image.url) + '">' + self.hero_image.name + '</a>'
        else:
            return '<a href="''"></a>'
    hero_image_link.allow_tags = True


    def blog_image_link(self):
        if self.blog_image:
            return '<a href="' + str(self.blog_image.url) + '">' + self.hero_image.name + '</a>'
        else:
            return '<a href="''"></a>'
    blog_image_link.allow_tags = True

    def __unicode__(self):
        return "%s-%s-%s-%s"%(self.pk, self.title, self.author, self.published_date)



