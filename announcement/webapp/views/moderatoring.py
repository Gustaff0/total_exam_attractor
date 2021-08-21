from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.views.generic import ListView

from webapp.models import Announcement


class ModeratoringListView(ListView):
    template_name = 'moderatoring/list_to_moder.html'
    model = Announcement
    context_object_name = 'announcements'
    ordering = ('-created_at',)

    def get_queryset(self):
        queryset = queryset = super().get_queryset()
        queryset = queryset.filter(moderate=False, delete=False)
        return queryset

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.moderator'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
