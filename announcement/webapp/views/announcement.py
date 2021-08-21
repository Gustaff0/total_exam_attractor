from django.shortcuts import redirect, render
from django.views.generic import ListView, CreateView, DetailView, UpdateView

from webapp.forms import AnnouncementFormForUser
from webapp.models import Announcement


class AnnouncementListView(ListView):
    template_name = 'announcement/list.html'
    model = Announcement
    context_object_name = 'announcements'
    ordering = ('-created_at',)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(moderate=True)
        return queryset


class AnnouncementCreateView(CreateView):
    template_name = 'announcement/create.html'
    form_class = AnnouncementFormForUser
    model = Announcement

    def form_valid(self, form):
        user = self.request.user
        announcement = form.save(commit=False)
        announcement.user = user
        announcement.save()
        return redirect('webapp:detail_announcement', announcement.id)

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class AnnouncementUpdateView(UpdateView):
    model = Announcement
    template_name = 'announcement/update.html'
    form_class = AnnouncementFormForUser
    context_object_name = 'announcement'


class AnnouncementDetailView(DetailView):
    template_name = 'announcement/view.html'
    context_object_name = 'announcement'
    model = Announcement

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


def announcement_delete_view(request, *args, **kwargs):
    announcement = Announcement.objects.get(id=kwargs.get('pk'))
    if request.user.is_authenticated and request.user == announcement.user:
        announcement.delete()
        return render(request, 'announcement/delete.html')
    else:
        return render(request, 'announcement/delete_error.html')


