from django import template
from articles.models import Article


register = template.Library()


@register.simple_tag()
def get_latest_posts(n=4):
    return Article.objects.all().order_by('-date')[0:n]

