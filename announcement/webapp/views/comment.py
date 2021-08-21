from django.shortcuts import redirect
from django.views.generic import CreateView

from webapp.forms import CommentForm
from webapp.models import Comment, Announcement


class CommentCreateView(CreateView):
    template_name = 'comment/create.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        announcement = Announcement.objects.get(id=self.kwargs.get('pk'))
        user = self.request.user
        comment = form.save(commit=False)
        comment.announcement = announcement
        comment.user = user
        comment.save()
        return redirect('webapp:detail_announcement', announcement.id)

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)
