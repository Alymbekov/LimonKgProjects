from django import template
from django.utils import timezone
from django.db.models import Sum
from articles.models import Article, ArticleViews


register = template.Library()


@register.simple_tag()
def get_latest_posts(n=4):
    return Article.objects.all().order_by('-date')[0:n]

@register.simple_tag()
def get_popular_posts(n=5):
    popular = ArticleViews.objects.filter(
            date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]
        ).values(
            'article__id', 'article__title', 'article__date', 'article__image'
        ).annotate(
            views=Sum('views')
        ).order_by(
            '-views')[:5]
    return popular