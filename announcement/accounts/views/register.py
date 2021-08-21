from django.shortcuts import render, redirect
from django.contrib.auth import login
from accounts.forms import MyUserCreationForm


def register_view(request, *args, **kwargs):
    if request.method == 'POST':
        form = MyUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user.save()
            return redirect('webapp:list_announcement')
    else:
        form = MyUserCreationForm()
    return render(request, 'reg_user.html', context={'form': form})