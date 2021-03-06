# Generated by Django 2.2.13 on 2021-04-12 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_auto_20210411_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sell',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='total_favourite',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='category',
            name='sub_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='home.Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='cat_product', to='home.Category'),
        ),
    ]
