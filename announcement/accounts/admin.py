from django.contrib import admin

# Register your models here.
from accounts.models import PhoneNumber


class PhoneAdmin(admin.ModelAdmin):
    list_display = ['id', 'phone', 'user']
    list_filter = ['user']
    search_fields = ['user']
    fields = ['id', 'phone', 'user']
    readonly_fields = ['id']


admin.site.register(PhoneNumber, PhoneAdmin)