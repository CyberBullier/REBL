# Generated by Django 2.1.1 on 2018-09-13 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20180911_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apparel_products',
            name='season',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Season'),
        ),
    ]
