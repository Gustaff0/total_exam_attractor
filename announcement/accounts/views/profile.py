from django.views.generic import DetailView
from django.contrib.auth import get_user_model


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'