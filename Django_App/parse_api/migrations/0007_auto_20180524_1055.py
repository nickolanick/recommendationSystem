# Generated by Django 2.0.5 on 2018-05-24 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_api', '0006_auto_20180524_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='first_video',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
