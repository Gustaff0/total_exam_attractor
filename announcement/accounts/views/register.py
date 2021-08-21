from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic import CreateView

from accounts.forms import MyUserCreationForm, PhoneNumberForm
from accounts.models import PhoneNumber


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()
            return redirect('accounts:reg_phone')
    else:
        form = MyUserCreationForm()
    return render(request, 'reg_user.html', context={'form': form})


class PhoneCreateView(CreateView):
    template_name = 'create_phone.html'
    model = PhoneNumber
    form_class = PhoneNumberForm

    def form_valid(self, form):
        user = self.request.user
        phone = form.save(commit=False)
        phone.user = user
        phone.save()
        return redirect('webapp:list_announcement')