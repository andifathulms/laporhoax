# Generated by Django 3.2.7 on 2021-09-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='isAnonym',
            field=models.BooleanField(default=False),
        ),
    ]
