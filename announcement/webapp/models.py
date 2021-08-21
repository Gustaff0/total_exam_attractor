from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.

CHOICES = [('electronic', 'Electronic'), ('to_home', 'To Home'), ('phones', 'Phones'), ('other', 'Other')]

class Announcement(models.Model):
    user = models.ForeignKey(get_user_model(), null=False, blank=False, related_name='announcement', on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False, validators=[MinLengthValidator(5)])
    descriptions = models.CharField(max_length=300, blank=False, null=False, validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    edited_at = models.DateTimeField(auto_now=True, blank=False, null=False)
    moderated_at = models.DateTimeField(blank=True, null=True)
    moderate = models.BooleanField(default=False)
    category = models.CharField(max_length=100, null=False, blank=False, choices=CHOICES, default='other')
    photo = models.ImageField(null=True, blank=True, upload_to='announcement_pics')
    price = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    delete = models.BooleanField(default=False)

    class Meta:
        permissions = [('moderator', 'Модератор')]
        db_table = 'Announcements'
        verbose_name = 'Обьявление'
        verbose_name_plural = 'Обьявления'


