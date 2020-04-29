from .models import Article, Category, Comment, ArticleViews
from .forms import CommentForm
from users.models import CustomUser
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView
from .mixins import DispatchFuncMixin
from django.db.models import Q


class CategoryList(ListView):
    template_name = 'category.html'
    model = Category
    context_object_name = 'categories'


class ArticlePageView(ListView):
    """Вывод всех объектов """
    # template_name = 'articles/article_list.html'
    template_name = 'index1.html'
    paginate_by = 2
    context_object_name = 'posts'
    def get_queryset(self):
        query_result = self.request.GET.get('search_title')
        filter_category = self.request.GET.getlist('category')
        if query_result:
            queryset = Article.objects.filter(
                Q(title__icontains=query_result) |
                Q(description__icontains=query_result)
                 
            )
        if filter_category:
            queryset = Article.objects.filter(
                Q(category__in=filter_category)
            )
        
        else:
            queryset = Article.objects.all()
        return queryset
    




class ArticleDetailView(FormView, DetailView):
    """Детализация объекта """
    model = Article
    form_class = CommentForm
    template_name = 'articles/article_detail.html'
    context_object_name = 'post'

    def dispatch(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=self.kwargs['pk'])
        context = {}
        obj, created = ArticleViews.objects.get_or_create(
            defaults={
                  'article': article,
              },
            article=article 
        )
        if created:
            obj.views += 1
            obj.save(update_fields=['views'])
        else:
            obj.views += 1
            obj.save(update_fields=['views'])
        return super(ArticleDetailView, self).dispatch(request, *args, **kwargs)
        

    def get_context_data(self, **kwargs):
        context = super(ArticleDetailView,self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(article=self.get_object(), reply=None).order_by('-date')
        return context

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('article_detail', kwargs={'pk': self.get_object().pk})
    
    def form_valid(self, form):
        form = form.save(commit=False)
        reply = self.request.POST.get('comment_id', None)
        comment_qs = None
        if reply:
            comment_qs = Comment.objects.get(id=reply)
        form.reply = comment_qs        
        form.article = self.get_object()
        form.author = self.request.user
        form.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, DispatchFuncMixin, UpdateView):
    """Обновление объекта """
    model = Article
    fields = ('title', 'description', 'image', 'category')
    template_name = 'articles/article_edit.html'
    login_url = 'login'


    def get_context_data(self, *args, **kwargs):
        some_list = ["john", "raychel"]
        context = super().get_context_data() #{"object": "object_detail"}
        context['some_lists'] = some_list
        return context


class ArticleDeleteView(LoginRequiredMixin, DispatchFuncMixin, DeleteView):
    """Удаление объекта """
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Создание объекта """
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title', 'description', 'category', 'image')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    

