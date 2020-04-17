from .models import Article
from .forms import CommentForm
from users.models import CustomUser
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView, FormView




class ArticlePageView(ListView):
    """Вывод всех объектов """
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(FormView, DetailView):
    """Детализация объекта """
    model = Article
    form_class = CommentForm
    template_name = 'articles/article_detail.html'
    def get_success_url(self, *args, **kwargs):
        return reverse_lazy('article_detail', kwargs={'pk': self.get_object().pk})
    
    def form_valid(self, form):
        form = form.save(commit=False)
        form.article = self.get_object()
        form.author = self.request.user
        form.save()
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    """Обновление объекта """
    model = Article
    fields = ('title', 'description')
    template_name = 'articles/article_edit.html'
    login_url = 'login'


    def get_context_data(self, *args, **kwargs):
        some_list = ["john", "raychel"]
        context = super().get_context_data() #{"object": "object_detail"}
        context['some_lists'] = some_list
        return context
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление объекта """
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Создание объекта """
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title', 'description')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    
# class AddComment(View):
#     """Комментарии"""
    
#     def post(self, request, pk):
#         form = CommentForm(request.POST)
#         article = Article.objects.get(id=pk)
#         if form.is_valid():
#             form = form.save(commit=False)
#             form.author = request.user
#             form.article = article
#             form.save()
#         else:
#             return redirect(reverse_lazy('article_detail', kwargs={'pk': article.pk}))


# def add_comment_to_article(request, pk):
#     article = Article.objects.get(id=pk)
#     if request.method == "POST":
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.article = article
#             comment.author = CustomUser.objects.get(pk=1)
#             comment.save()
#             return redirect(reverse_lazy('article_detail', kwargs={'pk': article.pk}))
#     else:
#         form = CommentForm()
#     return render(request, 'articles/article_comment.html', {'form': form})


  