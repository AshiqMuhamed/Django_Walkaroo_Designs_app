# Generated by Django 3.2.11 on 2022-06-07 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartlist',
            name='remarks',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
