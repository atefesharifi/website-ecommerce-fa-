# Generated by Django 2.2.13 on 2021-04-10 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210323_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='1.jpg', null=True, upload_to='profile'),
        ),
    ]