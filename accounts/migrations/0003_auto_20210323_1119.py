# Generated by Django 2.2.13 on 2021-03-23 06:49

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210318_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31, null=True),
        ),
    ]
