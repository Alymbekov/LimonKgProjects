from django.urls import path
from .views import (
    ArticlePageView, 
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
)


urlpatterns = [
    #list of posts 
    path('', ArticlePageView.as_view(), name='article_list'),
    #update posts
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_edit'),
    #detail posts
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    #delete post
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
    #create post
    path('article/create/', ArticleCreateView.as_view(), name='article_new'),
]
