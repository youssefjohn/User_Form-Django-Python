# Generated by Django 2.2.4 on 2019-09-04 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190903_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='more_user_details',
            name='relation',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
