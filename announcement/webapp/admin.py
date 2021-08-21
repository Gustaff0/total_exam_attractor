from django.contrib import admin

# Register your models here.
from webapp.models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'descriptions', 'user', 'created_at', 'moderate']
    list_filter = ['created_at']
    search_fields = ['user', 'descriptions']
    fields = ['id', 'user', 'title', 'descriptions', 'photo', 'delete', 'created_at', 'edited_at', 'moderated_at', 'price', 'moderate', 'category']
    readonly_fields = ['id', 'created_at', 'edited_at']


admin.site.register(Announcement, AnnouncementAdmin)