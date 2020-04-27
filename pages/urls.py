from django.urls import path
from .views import ContactPageView


urlpatterns = [
    #страница контактов
    path('contacts/', ContactPageView.as_view(), name='contacts'),
]
#http://localhost:8000/