from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from datetime import datetime
from django.urls import reverse
from tinymce.models import HTMLField




class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

class Article(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=255)
    description = HTMLField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article-photos/', default='media/default.jpg')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
    )
    # updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
    @property
    def get_absolute_image_url(self):
        return f'{self.image.url}'

    class Meta:
        ordering =('-date', )


class Comment(models.Model):
    """Комментарии"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=datetime.now())
    reply = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, related_name='replies')    
    def __str__(self):
        return self.comment[:50]
    
    def get_absolute_url(self):
        return reverse('article_list')
     
    class Meta:
        ordering = ('author', )


class ArticleViews(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_statistic')
    date = models.DateTimeField(auto_now_add=datetime.now())
    views = models.IntegerField('Views', default=0)

    def __str__(self):
        return self.article.title

    