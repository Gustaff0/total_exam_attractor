import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils import timezone

from webapp.models import Announcement


def success_moderate(request, *args, **kwargs):
    if request.user.has_perm('webapp.moderator') or request.user.is_staff:
        if request.body:
            body = request.body
            parce_json = json.loads(body)
            announcement = Announcement.objects.get(id=int(parce_json['id']))
            announcement.moderate = True
            announcement.moderated_at = timezone.now()
            announcement.save()
            return HttpResponse('Success! This Announcement in publicate!')
        else:
            return HttpResponse('Я жду json вася!')
    else:
        return HttpResponse('PermissionError')


def reject_moderate(request, *args, **kwargs):
    if request.user.has_perm('webapp.moderator') or request.user.is_staff:
        if request.body:
            body = request.body
            parce_json = json.loads(body)
            announcement = Announcement.objects.get(id=int(parce_json['id']))
            announcement.moderate = False
            announcement.delete = True
            announcement.save()
            return HttpResponse('Success! This Announcement in black list!')
        else:
            return HttpResponse('Я жду json вася!')
    else:
        return HttpResponse('PermissionError')
