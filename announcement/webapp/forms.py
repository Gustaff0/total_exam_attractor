from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe

from webapp.models import Announcement


class AnnouncementFormForUser(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'descriptions', 'photo', 'category', 'price')