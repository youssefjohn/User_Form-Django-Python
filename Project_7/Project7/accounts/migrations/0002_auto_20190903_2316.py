# Generated by Django 2.2.4 on 2019-09-03 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='more_user_details',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='more_user_details',
            name='hobby',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
