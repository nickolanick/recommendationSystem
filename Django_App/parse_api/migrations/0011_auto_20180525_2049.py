# Generated by Django 2.0.5 on 2018-05-25 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parse_api', '0010_data_first_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
