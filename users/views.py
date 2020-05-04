from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView
from limon_project.mixins import DispatchFuncMixin

from .forms import CustomUserCreationForm

from .models import Profile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class UserProfileDetailView(DispatchFuncMixin, DetailView):
    template_name = 'users/user_profile.html'
    model = Profile

    def dispatch(self, request, *args, **kwargs):
        user = 'user'
        return super().dispatch(request, user, *args, **kwargs)
        

    
