from django.urls import path
from .views import IndexPageView


urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
]
#http://localhost:8000/