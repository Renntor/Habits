# Generated by Django 4.2.6 on 2023-10-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='telegram',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='статус'),
        ),
    ]
