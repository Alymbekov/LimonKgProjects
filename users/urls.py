from django.urls import path
from .views import SignUpView, UserProfileDetailView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('myprofile/<int:pk>/', UserProfileDetailView.as_view(), name='profile'),
]
#http://localhost:8000/signup/