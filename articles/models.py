from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse



class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='article-photos/', default='media/default.jpg')
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])
    
    class Meta:
        ordering =('-date', )


class Comment(models.Model):
    """Комментарии"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    
    def __str__(self):
        return self.comment[:50]
    
    def get_absolute_url(self):
        return reverse('article_list')
    
    class Meta:
        ordering = ('author', )

    