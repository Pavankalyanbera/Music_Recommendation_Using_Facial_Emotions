# Generated by Django 4.1.1 on 2022-09-23 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Music_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='emotion',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
