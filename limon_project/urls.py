from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import urls
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('pages/', include('pages.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('', include('articles.urls')),

]

# urlpatterns += i18n_patterns(path('', include('articles.urls')), prefix_default_language=False,)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

