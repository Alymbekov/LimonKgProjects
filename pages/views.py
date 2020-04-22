from django.shortcuts import render
from django.views.generic import ListView
from articles.models import Article

class IndexPageView(ListView):
    template_name = 'index1.html'
    model = Article