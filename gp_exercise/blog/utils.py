import os
from django.conf import settings
__author__ = 'murthy'


def get_hero_image_path(instance, file_name):
    return "%s%s-%s"%(settings.BLOG_STATIC_URL, "hero_image",os.path.splitext(file_name)[1])


def get_blog_image_path(instance, file_name):
    return "%s%s%s"%(settings.BLOG_STATIC_URL, "blog_image", str(instance.id) + os.path.splitext(file_name)[1])
