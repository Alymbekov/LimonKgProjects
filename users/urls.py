from django.urls import path
from .views import SignUpView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
]
#http://localhost:8000/signup/