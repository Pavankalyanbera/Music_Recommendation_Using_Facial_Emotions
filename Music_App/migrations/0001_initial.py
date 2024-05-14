# Generated by Django 4.1 on 2022-08-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=100)),
                ('apass', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'admin_details',
            },
        ),
        migrations.CreateModel(
            name='userDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Username', models.CharField(max_length=100)),
                ('Passsword', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'userDetails',
            },
        ),
    ]