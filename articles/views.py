from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article


class ArticlePageView(ListView):
    """Вывод всех объектов """
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(DetailView):
    """Детализация объекта """
    model = Article
    template_name = 'articles/article_detail.html'


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


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    """Удаление объекта """
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """Создание объекта """
    model = Article
    template_name = 'articles/article_create.html'
    fields = ('title', 'description')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

