# Generated by Django 3.2.7 on 2021-09-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_report_isanonym'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='description',
            field=models.CharField(default='Description', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='report',
            name='url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]