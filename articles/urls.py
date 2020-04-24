from django.urls import path
from .views import (
    ArticlePageView, 
    ArticleUpdateView,
    ArticleDetailView,
    ArticleDeleteView,
    ArticleCreateView,
    CategoryList,
    # AddComment,
    # add_comment_to_article
)


urlpatterns = [
    path('categories/', CategoryList.as_view(), name='categories'),
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
    #add comment to article
]

# http://localhost:8000/articles/comment/1/