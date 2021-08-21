from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

class PhoneNumber(models.Model):
    phone = models.CharField(max_length=13, null=False, blank=False)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, null=False, blank=False, related_name='phone_number')

    class Meta:
        db_table = 'PhoneNumbers'
        verbose_name = 'Телефоный номер'
        verbose_name_plural = 'Телефонные номера'