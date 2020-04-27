from django.shortcuts import render
from django.views.generic import TemplateView
# from articles.models import Article

# class IndexPageView(ListView):
#     template_name = 'index1.html'
#     model = Article


class ContactPageView(TemplateView):
    """Страница для информации (контакты)"""
    template_name = 'contact.html'