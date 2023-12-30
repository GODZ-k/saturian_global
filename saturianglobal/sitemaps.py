from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from core.models import product,Category


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'about', 'contact','services','service_detail','popular_service','details']

    def location(self, items):
        return reverse(items)


# class PostViewSitemap(Sitemap):
#     def items(self):
#         return product.objects.all()


class CategoryViewSitemap(Sitemap):
    def items(self):
        return Category.objects.all()