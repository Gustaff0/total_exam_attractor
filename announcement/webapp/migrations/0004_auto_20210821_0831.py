# Generated by Django 3.2.6 on 2021-08-21 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_announcement_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcement',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcement',
            name='moderate_rejected',
            field=models.BooleanField(default=False),
        ),
    ]