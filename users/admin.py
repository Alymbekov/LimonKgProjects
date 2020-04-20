from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdminPanel(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff',]

@admin.register(Profile)
class ProfileUserAdminPanel(admin.ModelAdmin):
    model = Profile
    list_display = ['first_name', 'last_name', 'user']
    list_display_links = ('user',)

admin.site.register(CustomUser, CustomUserAdminPanel)

