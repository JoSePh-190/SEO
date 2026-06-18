from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Blog


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'weekly'

    def items(self):
        return [
            'home',
            'about',
            'projects',
            'blogs',
        ]

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    changefreq = "weekly"

    def items(self):
        return Blog.objects.all()

    def location(self, obj):
        return reverse(
            'blog_detail',
            kwargs={'slug': obj.slug}
        )