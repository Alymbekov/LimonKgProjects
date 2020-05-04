from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

class DispatchFuncMixin():
    def dispatch(self, request, field=None,  *args, **kwargs):
        obj = self.get_object()
        author = "author"
        user = field
        if user is None:
            if obj.author != self.request.user:
                raise PermissionDenied
        else:
            if obj.user != self.request.user:
                raise PermissionDenied


        return super().dispatch(request, *args, **kwargs)


