# Generated by Django 2.0.5 on 2018-05-16 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('about', models.CharField(blank=True, max_length=1000)),
                ('comments', models.CharField(blank=True, max_length=1000)),
                ('youtube', models.CharField(max_length=1000)),
            ],
        ),
    ]
