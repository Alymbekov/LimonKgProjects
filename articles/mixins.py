from django.shortcuts import get_object_or_404
from .models import Article, ArticleViews

class DispatchFuncMixin():
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


