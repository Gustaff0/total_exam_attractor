from django.urls import path
from api_v1.views import success_moderate, reject_moderate

app_name = 'api_v1'

urlpatterns = [
    path('success/moderate/', success_moderate, name='success_moderate'),
    path('reject/moderate/', reject_moderate, name='reject_moderate')
]
