from django import forms
from django.forms import widgets
from django.utils.safestring import mark_safe

from webapp.models import Announcement, Comment


class AnnouncementFormForUser(forms.ModelForm):
    class Meta:
        model = Announcement
        fields = ('title', 'descriptions', 'photo', 'category', 'price')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')