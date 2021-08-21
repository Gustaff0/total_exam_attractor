from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import redirect, render
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.views.generic.edit import FormMixin

from webapp.forms import AnnouncementFormForUser, SearchForm, CommentForm
from webapp.models import Announcement


class AnnouncementListView(ListView):
    template_name = 'announcement/list.html'
    model = Announcement
    context_object_name = 'announcements'
    ordering = ('-created_at',)

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(AnnouncementListView, self).get(request, **kwargs)

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset()
        queryset = queryset.filter(moderate=True, delete=False)

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data) |
                Q(descriptions__icontains=self.search_data), moderate=True, delete=False
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context

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

    def form_valid(self, form):
        announcement = form.save(commit=False)
        announcement.moderate = False
        announcement.moderated_at = None
        if self.request.user.has_perm('webapp.moderator') or self.request.user == announcement.user or self.request.user.is_staff:
            announcement.save()
            return redirect('webapp:detail_announcement', announcement.id)
        else:
            raise PermissionDenied

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class AnnouncementDetailView(DetailView):
    template_name = 'announcement/view.html'
    context_object_name = 'announcement'
    model = Announcement



def announcement_delete_view(request, *args, **kwargs):
    announcement = Announcement.objects.get(id=kwargs.get('pk'))
    user = request.user
    if not user.is_authenticated:
        return redirect('accounts:login')
    if user.is_authenticated and request.user == announcement.user or user.has_perm('webapp.moderator') or user.is_staff:
        announcement.delete = True
        announcement.moderate = True
        announcement.save()
        return render(request, 'announcement/delete.html')
    else:
        return render(request, 'announcement/delete_error.html')



